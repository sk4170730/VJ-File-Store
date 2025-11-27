# Bot Information
API_ID = int(environ.get("API_ID", "34254284")) or 0
API_HASH = environ.get("API_HASH", "746da987fd34ef8d8363c55f42d00aef")
BOT_TOKEN = environ.get("BOT_TOKEN", "7985190165:AAHr4aHlPmJFOZSTr3xxYMzPgby88ke8W9E")

# ADMINS safe banao
ADMIN_LIST = environ.get("ADMINS", "7009144658").split()
ADMINS = [7009144658]
for admin in ADMIN_LIST:
    if admin.isdigit():
        ADMINS.append(int(admin))
    elif id_pattern.search(admin):
        ADMINS.append(int(admin))

# Database
DB_URI = environ.get("DB_URI", "mongodb+srv://sk4170730:Sumit@2003@cluster0.d0w1y7n.mongodb.net/?appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "filesharebot")   # ← YEH SABSE BADI GALTI THI

# Log Channel
try:
    LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002721017177"))
except ValueError:
    LOG_CHANNEL = -1002721017177

# Auto Delete Time (seconds ko minutes se match karo
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))  # minutes
AUTO_DELETE_TIME = AUTO_DELETE * 60  # seconds mein convert (agar tum 30 min chahte ho)
