DB_PATH = './db.json'

try:
    db = open('./db.json', 'r')
    db.close()
    
except:
    db = open('./db.json', 'w')
    db.close