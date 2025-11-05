      const cards = document.querySelectorAll(".choice-card");
      const battleArena = document.getElementById("battleArena");
      const resultDisplay = document.getElementById("resultDisplay");
      const playAgainBtn = document.getElementById("playAgain");
      const choicesSection = document.getElementById("choicesSection");

      const playerBattleChoice = document.getElementById("playerBattleChoice");
      const computerBattleChoice = document.getElementById(
        "computerBattleChoice"
      );
      const resultBadge = document.getElementById("resultBadge");
      const playerResult = document.getElementById("playerResult");
      const computerResult = document.getElementById("computerResult");
      const resetScoresBtn = document.getElementById("resetScores");

      // Sidebar toggle
      const sidebar = document.getElementById("sidebar");
      const toggleSidebarBtn = document.getElementById("toggleSidebar");
      const closeSidebarBtn = document.getElementById("closeSidebar");

      toggleSidebarBtn.addEventListener("click", () => {
        sidebar.classList.toggle("sidebar-open");
        document.body.classList.toggle("sidebar-active");
      });

      closeSidebarBtn.addEventListener("click", () => {
        sidebar.classList.remove("sidebar-open");
        document.body.classList.remove("sidebar-active");
      });

      // Close sidebar when clicking outside on mobile
      document.addEventListener("click", (e) => {
        if (
          window.innerWidth < 1024 &&
          !sidebar.contains(e.target) &&
          !toggleSidebarBtn.contains(e.target) &&
          sidebar.classList.contains("sidebar-open")
        ) {
          sidebar.classList.remove("sidebar-open");
          document.body.classList.remove("sidebar-active");
        }
      });

      // Theme toggle
      const themeToggle = document.getElementById("themeToggle");
      const themeIcon = themeToggle.querySelector(".theme-icon");
      let isDarkMode = true;

      themeToggle.addEventListener("click", () => {
        isDarkMode = !isDarkMode;
        document.body.classList.toggle("light-mode", !isDarkMode);
        themeIcon.textContent = isDarkMode ? "🌙" : "☀️";
      });

      function updateScores(scores) {
        document.getElementById("winsScore").textContent = scores.wins;
        document.getElementById("lossesScore").textContent = scores.losses;
        document.getElementById("tiesScore").textContent = scores.ties;

        const total = scores.wins + scores.losses + scores.ties;
        document.getElementById("totalGames").textContent = total;

        const winRate = total > 0 ? Math.round((scores.wins / total) * 100) : 0;
        document.getElementById("winRate").textContent = winRate + "%";
      }

      resetScoresBtn.addEventListener("click", async () => {
        try {
          const res = await fetch("/reset-scores", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
          });
          const data = await res.json();
          updateScores(data.scores);
        } catch (error) {
          console.error("Error resetting scores:", error);
        }
      });

      cards.forEach((card) => {
        card.addEventListener("click", async () => {
          const choice = card.getAttribute("data-choice");
          const emoji = choice.split(" ")[0];

          // Add click animation
          card.style.transform = "scale(0.95)";
          setTimeout(() => (card.style.transform = ""), 150);

          choicesSection.classList.add("hidden");
          battleArena.classList.remove("hidden");

          playerBattleChoice.querySelector(".battle-emoji").textContent = emoji;
          playerBattleChoice.classList.add("revealed");

          const thinkEmojis = ["🪨", "📄", "✂️"];
          let thinkCount = 0;
          const thinkInterval = setInterval(() => {
            computerBattleChoice.querySelector(".battle-emoji").textContent =
              thinkEmojis[Math.floor(Math.random() * 3)];
            thinkCount++;
            if (thinkCount > 8) clearInterval(thinkInterval);
          }, 150);

          await new Promise((r) => setTimeout(r, 1500));

          try {
            const res = await fetch("/play", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ choice }),
            });
            const data = await res.json();

            const computerEmoji = data.computer_choice.split(" ")[0];
            computerBattleChoice.querySelector(".battle-emoji").textContent =
              computerEmoji;
            computerBattleChoice.classList.add("revealed");

            await new Promise((r) => setTimeout(r, 500));

            updateScores(data.scores);

            resultBadge.textContent = data.message;
            resultBadge.className = "result-badge " + data.status;
            playerResult.textContent = data.player_choice;
            computerResult.textContent = data.computer_choice;

            resultDisplay.classList.remove("hidden");
            playAgainBtn.classList.remove("hidden");
          } catch (error) {
            console.error("Error playing game:", error);
          }
        });
      });

      playAgainBtn.addEventListener("click", () => {
        battleArena.classList.add("hidden");
        resultDisplay.classList.add("hidden");
        playAgainBtn.classList.add("hidden");
        choicesSection.classList.remove("hidden");

        playerBattleChoice.classList.remove("revealed");
        computerBattleChoice.classList.remove("revealed");
        playerBattleChoice.querySelector(".battle-emoji").textContent = "❓";
        computerBattleChoice.querySelector(".battle-emoji").textContent = "❓";
      });

      // Initialize stats
      updateScores(JSON.parse("{{ scores|tojson | safe }}"));