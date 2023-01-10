##Config

from os import getenv

from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv('SESSION_NAME', 'BQCzMdThQFFDQH2v2rLmmQjW2PBDAndpmUJwRsXDxPHS51ch0THau0dnoIWb4c2Fh_bW351MDDbmczZd-d8qyiMZdaCdmy1waqCu7nfFuMsTINw8DE9VNwi1sqxScJnoHWCyTUVzbA-mqs9gkUaGDvuDmCoqc7FOrm34PjIqbtxwP1dBq23msTN16A7SDrLTrp9UOgQnlqBx04Vb7ugxhsr84N3VHgPZ2Chi_FmdOv3aHfSxOViU1ihXhErN0UNDqaG-_D0IoF_zDO-HrFTVM-kZf7ixEH1QmKHnfUdWO6NAuNmckW3wjbKWlf6FNEesHhVMb5Xe0UmagaMRr46oBKrkAAAAAVKlSlsA')
BOT_TOKEN = getenv('BOT_TOKEN', '5657806589:AAFU5COS7-Ao98snL_LX68ucdK_oROlT_i4')
API_ID = int(getenv('API_ID', '13861846'))
API_HASH = getenv('API_HASH', '4001710ae09a26c8326db4776b876d01')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '54000'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://2004:2004@cluster0.vugmi1n.mongodb.net/?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '1548904516').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001898472056'))
ASS_ID = int(getenv("ASS_ID", '5681531483'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '1548904516').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "Lover_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheLoverMusic")
GROUP = getenv("GROUP", "Lover_Support")
CHANNEL = getenv("CHANNEL", "TheLoverMusic")
