import psycopg2

class Database:
    def __init__(self, info):
        self.con = psycopg2.connect(database=info[0], user=info[1], password=info[2], host=info[3], port=info[4])
        self.con.autocommit = True
        self.cursor = self.con.cursor()
    
    def close(self):
        self.con.close()

def get_from_file(file="db.txt"):
    with open(file) as dbinfo:
        info = []
        for line in dbinfo.readline().split(","):
            info.append(line.strip())
        return info
