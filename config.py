# Bot Information
API_ID = int(environ.get("API_ID", "34254284")) or 0
API_HASH = environ.get("API_HASH", "746da987fd34ef8d8363c55f42d00aef")
BOT_TOKEN = environ.get("BOT_TOKEN", "7985190165:AAHr4aHlPmJFOZSTr3xxYMzPgby88ke8W9E")

# ADMINS - 100% working
ADMIN = environ.get("ADMINS", "7009144658")
ADMINS = []
for x in ADMIN.split():
    try:
        ADMINS.append(int(x))
    except:
        pass
if not ADMINS:
    ADMINS = [7009144658]

# Database - password real daal do ya env se
DB_URI = environ.get("DB_URI", "mongodb+srv://sk4170730:Sumit@2003@cluster0.d0w1y7n.mongodb.net/?appName=Cluster0")
DB_NAME = environ.get("DB_NAME", "filesharebot")

# Log Channel
try:
    LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002721017177"))
except:
    LOG_CHANNEL = -1002721017177

# Auto Delete
AUTO_DELETE = int(environ.get("AUTO_DELETE", "30"))
AUTO_DELETE_TIME = AUTO_DELETE * 60
