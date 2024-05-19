import psycopg2

class Database:
    def __init__(self):
        db_info = get_from_file('.db')
        self.con = psycopg2.connect(database=db_info[0], user=db_info[1], password=db_info[2], host=db_info[3], port=db_info[4])
        self.con.autocommit = True
        self.cursor = self.con.cursor()
    
    def close(self):
        self.con.close()

def get_from_file(file=".db"):
    db_info = []
    with open(file) as db_config:
        db_info = db_config.readline().split()

    return db_info
    
