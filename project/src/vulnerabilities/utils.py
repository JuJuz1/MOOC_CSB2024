import sqlite3

# Utilities

def access_database(request):
    # Input value
    query = request.GET.get('query', '')
    results = []
    if query:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        # FLAW: SQL injection
        # How the attacker could get the name of the tables:
        # ' UNION SELECT name FROM sqlite_master WHERE type='table' --
        # The names of the admin accounts:
        # ' UNION SELECT name FROM Users WHERE admin=1 --
        # Example injection to get the passwords of all admins: 
        # ' UNION SELECT password FROM Users WHERE admin=1 --
        response = cursor.execute(f"SELECT client FROM Clients WHERE name LIKE '{query}'").fetchall()
        # FIX:
        # Using parameterized queries removes the potential of any SQL injection, sanitizing inputs?
        #response = cursor.execute("SELECT client FROM Clients WHERE name LIKE ?", [query]).fetchall()
        results = response
    return results