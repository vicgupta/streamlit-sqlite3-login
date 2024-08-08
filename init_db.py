from aster.db.sqlite3orm import SQLite3ORM
db = SQLite3ORM("test.db")

db.drop_table("users")
db.drop_table("logs")
db.create_table("users", {"userid": "INTEGER PRIMARY KEY", "email": "TEXT", "password": "TEXT"})
db.create_table("logs", {"logid": "INTEGER PRIMARY KEY", "logemail": "TEXT","logvoice": "TEXT", "logtext": "TEXT"})
status = db.signup("users", email="admin@gmail.com", password="admin123")