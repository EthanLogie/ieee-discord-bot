# 🤖 IEEE Discord Role Application Bot

This bot allows Concordia IEEE members to apply for different teams by reacting to a message in Discord. When a user reacts with an emoji, the bot DMs them team information, prompts them to submit a short application, and forwards it to the correct exec channel while tagging the respective VP.

> 🔄 Fully automated. No forms. No manual tracking.  
> 📍 Hosted on a dedicated desktop in the IEEE lab (24/7 uptime).

---

## 🚀 Features

- Emoji-based team application system
- Custom team info messages
- Collects short applications via DM
- Sends responses to private exec channels
- Tags team leads (VPs) automatically
- Easy to add new teams, emojis, or execs

---

## ⚙️ Setup Instructions (Lab Computer)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ieee-discord-bot.git
cd ieee-discord-bot
2. Install Dependencies
Make sure Python 3 is installed, then run:

bash
Copy
Edit
pip install -r requirements.txt
3. Create a .env File
Inside the project folder, create a file named .env and add:

ini
Copy
Edit
DISCORD_TOKEN=your_bot_token_here
Never share this token publicly.

▶️ Running the Bot
To start the bot manually:
bash
Copy
Edit
python3 ieee_bot.py
To keep it running in the background (Mac/Linux):
bash
Copy
Edit
tmux
python3 ieee_bot.py
# Then press Ctrl+B, then D to detach
🔁 Updating the Bot
This project is linked to a GitHub repository. To update the bot:

bash
Copy
Edit
git pull origin main
Then restart the bot process if needed.

🛡️ Security Notes
Token is stored securely in .env

.env is excluded from version control via .gitignore

Only trusted exec members should have access to the hosting machine

📦 Project Structure
bash
Copy
Edit
ieee-discord-bot/
├── ieee_bot.py           # Main bot code
├── .env                  # (hidden) Token file, not tracked by Git
├── .gitignore            # Ignores .env and compiled Python files
├── requirements.txt      # Required Python packages
├── start.sh              # (Optional) For Render/cloud hosting
└── README.md             # This file
📬 Support & Maintenance
Hosted on IEEE Lab Desktop (9th floor)

Maintained by VP of IT (or whoever inherits the bot 😎)

For issues or suggestions, ping in the IT Discord thread or open a GitHub issue

python
Copy
Edit

---

You're good to paste that straight into a `README.md` file in your project folder. Let me know when you're ready for `.bat` auto-start help (if Windows), or if you'd like to write contributor notes for future devs!







```
