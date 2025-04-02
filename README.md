# 🤖 IEEE Discord Role Application Bot

This bot powers the team application system inside IEEE Concordia’s Discord server. Members can react to a message using an emoji that represents the team they're interested in, and the bot will DM them more info, collect a short application, and forward it to the respective VP or team lead.

> 🔄 Fully automated  
> 🖥️ Hosted on a 24/7 Windows desktop in the IEEE lab  
> 👨‍💻 Maintained by: IEEE IT Team

---

## 🚀 Features

- Emoji-based application system  
- Auto-DMs users with team-specific info  
- Collects short applications via reply  
- Sends to private exec channels  
- Auto-tags the VP/team lead  
- Easy to add new teams & emojis

---

## 📁 Repository

**GitHub:** [https://github.com/EthanLogie/ieee-discord-bot](https://github.com/EthanLogie/ieee-discord-bot)  
**Main bot file:** `ieee_bot.py`  
**Maintainer:** Ethan Logie – Director IT

---

## ⚙️ Setup Instructions (Windows Desktop)

### 1. Install Python 3

Download it from [https://python.org](https://python.org)  
Make sure to check ✅ **"Add Python to PATH"** during installation.

---

### 2. Clone the Repository

git clone https://github.com/EthanLogie/ieee-discord-bot.git
cd ieee-discord-bot

---

### 3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt

---

### 4. Create a .env File
In the root of the folder, create a file named .env and add:

DISCORD_TOKEN=your_token_here
⚠️ Do not share this file or commit it to GitHub.

---

### 5. Run the Bot
To launch manually:
python ieee_bot.py
You should see:

Bot is online as IEEE Carl#XXXX

### 🪄 Run in Background on Windows (Task Scheduler)
Use Task Scheduler to start the bot on boot:

Open Task Scheduler → Action > Create Task

Under General, name it: IEEE Discord Bot

Check: ✅ "Run whether user is logged on or not"

Under Triggers, click New

Begin the task: "At startup"

Under Actions, click New

Program/script: python

Add arguments: ieee_bot.py

Start in: C:\Path\To\ieee-discord-bot

The bot will now launch when the computer boots up 🎉

### 🔁 Updating the Bot
When new changes are pushed to GitHub:

cd ieee-discord-bot
git pull origin main
Then re-run the script or restart the scheduled task.

---

### 🔐 Security & Structure
The .env file stores your bot token securely (never push to GitHub)

---

### Project structure:
ieee-discord-bot/
├── ieee_bot.py         # Main bot script
├── .env                # Token file (hidden)
├── .gitignore          # Ignores .env, pycache, etc.
├── requirements.txt    # Python dependencies
└── README.md           # This file

---

### 🛠 Maintained By
IEEE Concordia IT Team
Contact: Ethan Logie – Director IT
GitHub: @EthanLogie

Built with 🧠 by the IEEE Concordia IT Team to make team onboarding seamless.
