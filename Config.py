import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "7703556"))
    API_HASH = os.environ.get("API_HASH", "8341f9e3bfcf89d521685b1dd041555d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5636613817:AAEs8wVDwyhOpPzg3Z-gXT97HrenrY1JutU")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLcBuwMMQCgYy7ysDNFIjS-UVvOP7xgoFh5TLhGiYrk1Whc0Zp5Ew1FGYhupquCqmyfz3qcrtOXRsOfgOxxallF08OdBllaMlROjSNLk8IGwtZa6vCCBI41oo30mN_wSgE05AY6hS19swBa56V6_dwFJjUvgpnl6ru-FRmgblICTap5zWKN0zklH_f2qPjt3j519L5f9zibWnxjiGPEZ7pRdKiyhguCN7X0FOA50FfB6xMi7H8a42q6yfprjUQh4XYHjAMPuirQADeVVsz1S4UTl5DtLoj1vm9QrwMGEppDQwL2E6pSgyG-qYxOyn5C_P8e3GCOVFpv0UKs1ha8Rc2fHUMc=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "yunusmusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1069593275")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
