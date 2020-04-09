import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name_surname text, email text, password text, confirm_password text, birth_year text)")
        self.conn.commit()
    
    def fetch(self):
        self.cur.execute("SELECT * FROM users")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name_surname, email, password, confirm_password, birth_year):
        self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?)", (name_surname,email,password,confirm_password,birth_year))
        self.conn.commit()
    
    def remove(self,id):
        self.cur.execute("DELETE FROM users WHERE id=?", (id,))
        self.conn.commit()
    def update(self,id,name_surname,email,password,confirm_password,birth_year):
        self.cur.execute("UPDATE users SET name_surname = ?, email = ?, password = ? , confirm_password = ?, birth_year = ? WHERE id = ?", (name_surname, email, password, confirm_password, birth_year, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

db = Database('store.db')

#db.insert("pencan pencil","pen1@gmail.com","pen123","pen123","1982")