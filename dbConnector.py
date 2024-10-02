def init_sqlite_db():
  conn = sqlite3.connect('sqlite.db')# If name does not exist it will create one. 
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        message TEXT NOT NULL)''')
  conn.commit()
  conn.close() # Always make sure to close your database connection when finishing a query
