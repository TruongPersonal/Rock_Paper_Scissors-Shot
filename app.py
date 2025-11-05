# app.py
from flask import Flask, render_template, request, jsonify, session
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

CHOICES = ["🪨 Rock", "📄 Paper", "✂️ Scissors"]

def determine_winner(player, computer):
    """Determine the winner and return status and message"""
    if player == computer:
        return "tie", "🤝 It's a Tie!"
    elif (player == "🪨 Rock" and computer == "✂️ Scissors") or \
         (player == "📄 Paper" and computer == "🪨 Rock") or \
         (player == "✂️ Scissors" and computer == "📄 Paper"):
        return "win", "🎉 You Win!"
    else:
        return "lose", "💻 Computer Wins!"

def init_scores():
    """Initialize scores in session if not exists"""
    if 'scores' not in session:
        session['scores'] = {'wins': 0, 'losses': 0, 'ties': 0}

@app.route("/")
def index():
    """Render main page"""
    init_scores()
    return render_template("index.html", 
                         choices=CHOICES, 
                         scores=session['scores'])

@app.route("/play", methods=["POST"])
def play():
    """Handle game play logic"""
    init_scores()
    
    data = request.get_json()
    player_choice = data.get("choice")
    
    # Validate player choice
    if player_choice not in CHOICES:
        return jsonify({"error": "Invalid choice"}), 400
    
    # Computer makes random choice
    computer_choice = random.choice(CHOICES)
    
    # Determine winner
    status, message = determine_winner(player_choice, computer_choice)
    
    # Update scores
    if status == 'win':
        session['scores']['wins'] += 1
    elif status == 'lose':
        session['scores']['losses'] += 1
    else:
        session['scores']['ties'] += 1
    
    session.modified = True
    
    return jsonify({
        "player_choice": player_choice,
        "computer_choice": computer_choice,
        "status": status,
        "message": message,
        "scores": session['scores']
    })

@app.route("/reset-scores", methods=["POST"])
def reset_scores():
    """Reset all scores to zero"""
    session['scores'] = {'wins': 0, 'losses': 0, 'ties': 0}
    session.modified = True
    return jsonify({"scores": session['scores']})

@app.route("/get-scores", methods=["GET"])
def get_scores():
    """Get current scores"""
    init_scores()
    return jsonify({"scores": session['scores']})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)