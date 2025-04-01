#python3 ieee_bot.py

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

TARGET_MESSAGE_ID = 1354999419795144875 # Message ID of the sign-up message
CHANNEL_ID = 1354999619096150097  # Default application review channel

# Emoji to team info map
TEAM_INFO = {
    "🖥️": {
        "name": "IT Team",
        "description": "💻 The IT Team is responsible for maintaining the technical systems in the IEEE lab. This includes managing lab infrastructure such as the cameras, Wi-Fi, shared computers, and access systems. Members may help troubleshoot issues, set up new equipment, and ensure everything runs smoothly for events or daily use. While some tasks are hands-on, others involve scripting or automating internal workflows. It’s a great team for anyone interested in networking, hardware, or system administration. No matter your experience level, there’s always an opportunity to learn and make a real impact.",
        "vp_id": 248230862657683457,
        "channel_id": CHANNEL_ID
    },
    "📢": {
        "name": "Marketing Team",
        "description": "📣 The Marketing Team is responsible for how IEEE shows up online and in person. You'll work on promoting events, managing our social media platforms, and designing visual content like posters and reels. This team thrives on creativity and consistency, making sure members and partners stay informed and engaged. If you have skills in graphic design, content writing, or video editing — or want to learn — this is your place. You’ll also have the chance to analyze engagement data and optimize campaigns. Expect a fun, fast-paced vibe with plenty of room for fresh ideas.",
        "vp_id": 702958543879536671,
        "channel_id": CHANNEL_ID
    },
    "📚": {
        "name": "Academics Team",
        "description": "📚 The Academics Team focuses on organizing hands-on workshops for IEEE members throughout the year. These workshops cover a wide range of topics — from soldering, GitHub, circuit design, basic programming, and many more. The goal is to help members gain practical skills outside the classroom. You'll help plan and host these workshops, and possibly lead or assist during sessions. It's a great team if you enjoy teaching, explaining technical topics, or just want to support your peers' learning. No tutoring or exam prep — just engaging, skill-based events.",
        "vp_id": 297399831050190848,
        "channel_id": CHANNEL_ID
    },
    "🛠️": {
        "name": "Projects Team",
        "description": "🛠️ The Projects Team works on large, hands-on engineering builds that span multiple weeks or even months. These include IEEE’s flagship team projects like the Robotic Arm, Drone, Sumobot, and the Lab IoT System. Members collaborate to design, prototype, and test hardware and software in a team-based environment. You'll get experience with electronics, 3D printing, microcontrollers, CAD, and more — depending on the project. This team is perfect for builders, tinkerers, and anyone excited about turning complex ideas into working systems. Whether you’re a beginner or experienced, there’s always something to learn and contribute.",
        "vp_id": 995708835111120927,
        "channel_id": CHANNEL_ID
    },
    "🌐": {
        "name": "Community Team",
        "description": "🌐 The Community Team is all about making IEEE feel like a family. You'll plan and host social events, themed nights, game sessions, and wellness activities to keep members connected and engaged. The focus here is on creating a supportive, inclusive, and fun environment for everyone. If you're outgoing, organized, and love making people feel welcome, this is a great fit. The team often partners with other Concordia groups for larger events. You’ll also gather feedback from members to make sure we’re always improving.",
        "vp_id": 1156934653412913234,
        "channel_id": CHANNEL_ID
    },
    "🗂️": {
        "name": "Internal Team",
        "description": "🗂️ The Internal Team handles the logistical side of IEEE’s events and operations. This includes booking rooms, ordering food and supplies, and making sure everything is in place behind the scenes. Their work keeps events running smoothly and ensures all other teams can focus on their own responsibilities. It’s a great fit for organized, dependable people who enjoy planning and coordination. While it may not be the flashiest role, it's absolutely essential to how IEEE functions. You’ll often work closely with VPs and other teams to support events across the board.",
        "vp_id": 772593955908747284,
        "channel_id": CHANNEL_ID
    },
    "💰": {
        "name": "Finance Team",
        "description": "💰 The Finance Team handles all things money — budgeting, reimbursements, sponsorship tracking, and financial planning. You’ll work closely with the VPs and the External team to keep IEEE financially healthy and transparent. Expect to use spreadsheets, manage receipts, and help create funding proposals for big projects or competitions. It’s perfect for people interested in business, accounting, or operations. There’s also opportunity to help build budgeting tools or streamline financial workflows. No need to be a math genius — just be responsible, organized, and curious about how money flows.",
        "vp_id": 874842014456356874,
        "channel_id": CHANNEL_ID
    },
    "🏆": {
        "name": "Competitions Team",
        "description": "🏆 The Competitions Team is in charge of organizing IEEE’s flagship competitions, including Robowars (our annual sumobot tournament) and Botquest, a beginner-friendly engineering challenge for CEGEP students. You’ll plan event rules, design challenges, manage logistics, and help create a fun and fair competitive environment. The team also hosts smaller events throughout the year — often collaborating with other student societies — giving you the chance to get creative with new formats. Members may also be involved in recruiting volunteers, running demo days, and preparing test platforms or arenas for participants. Whether you’re technical or not, this team offers a dynamic space to build big events that bring the engineering community together. If you love the thrill of competition and want to help make it happen, this is the team for you.",
        "vp_id": 290894293042987009,
        "channel_id": CHANNEL_ID
    },
    "🔬": {
        "name": "Lab Supervisor",
        "description": "🔬 Lab Supervisors are responsible for maintaining a safe, functional, and accessible workspace in the IEEE lab. Each supervisor is assigned mandatory lab hours during which they monitor the space and assist members using it. They’re expected to have a solid understanding of the lab’s tools and equipment — including soldering stations, oscilloscopes, 3D printers, and more — in order to help others safely and effectively. This role is perfect for someone who’s dependable, hands-on, and enjoys helping people with technical tasks. You'll also play a key role in keeping the lab organized and ready for events or projects.",
        "vp_id": 332262168806555649,
        "channel_id": CHANNEL_ID
    },
    "🌍": {
        "name": "External Team",
        "description": "🌍 The External Team focuses on building and maintaining relationships with sponsors, industry partners, and other student groups. You’ll help with outreach emails, pitch decks, and sponsor packages — working to secure funding and partnerships for our events and operations. It's a great place to sharpen your communication and business development skills. You’ll also assist in coordinating sponsored events, networking nights, and company visits. If you like talking to people, making deals, or working on polished presentations, this team is for you.",
        "vp_id": 1212048971380559965,
        "channel_id": CHANNEL_ID
    },
    "💻": {
        "name": "Development Team",
        "description": "💻 The Development Team is responsible for building and maintaining IEEE’s digital platforms — including the main website and any custom apps needed for events or internal use. This could include things like project dashboards, registration systems, or mobile tools for competitions. Members typically work with web frameworks and version control tools like GitHub, and there are opportunities to get involved with both frontend and backend development. It's a great team for anyone looking to gain experience in software development while making a real impact. Whether you're a beginner or experienced coder, there's always something meaningful to build.",
        "vp_id": 349671812512219136,  
        "channel_id": CHANNEL_ID
    }
}
#When bot is online, display in terminal
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

#When a reaction is added to the message, send a DM to the user with the team info and prompt them to apply
@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id != TARGET_MESSAGE_ID or payload.user_id == bot.user.id:
        return

    emoji = str(payload.emoji.name)
    user = await bot.fetch_user(payload.user_id)

    if emoji in TEAM_INFO:
        info = TEAM_INFO[emoji]

        try:
            # DM user with team info
            await user.send(
                # Team Name
                f"📌 __**{info['name']} Info**__\n\n" 
                # Team Description
                f"{info['description']}\n\n"
                # Application prompt
                "Please reply to this message with a short application:\n"
                "- Why do you want to join?\n"
                "- What can you contribute?\n"
                "Your application will be sent to the team lead."
            )
            # Wait for user reply
            def check(m):
                return m.author.id == user.id and isinstance(m.channel, discord.DMChannel)

            reply = await bot.wait_for("message", check=check, timeout=300)

            # Forward to exec application review channel
            channel = bot.get_channel(info["channel_id"])
            await channel.send(
                f"📬 __**New application for {info['name']}**__\n"
                f"<@{info['vp_id']}>, you've got a new applicant!\n\n"
                f"**From:** <@{user.id}>\n"
                f"**Application:**\n{reply.content}"
            )
            await user.send("✅ Your application has been submitted successfully!")

        except discord.Forbidden:
            print(f"Couldn't DM user {user.name}.")
        except Exception as e:
            print(f"Error: {e}")

# Run the bot (bot token)
load_dotenv()
bot.run(os.getenv("DISCORD_TOKEN"))
