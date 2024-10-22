import sqlite3
import hashlib
from django.contrib.auth.hashers import make_password
from .models import SecureData, Message

# Utilities

# Gets all users with clients from the database
def getUsersWithClients():
    results = []
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    response = cursor.execute("SELECT name FROM Clients").fetchall()
    results = response
    return results

# Gets the client of a searched user
def getClientOfUser(request):
    # Input value
    query = request.POST.get('query', '')
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
        response = cursor.execute(f"SELECT client FROM Clients WHERE name LIKE '{query}' COLLATE NOCASE").fetchall()
        # FIX:
        # Using parameterized queries removes the potential of any SQL injection, sanitizing inputs?
        #response = cursor.execute("SELECT client FROM Clients WHERE name LIKE ? COLLATE NOCASE", [query]).fetchall()
        results = response
    return results

# Hashes the input with MD5 and returns the result
def hash_md5(request):
    query = request.POST.get('query', '')
    md5 = None
    if query:
        # FLAW: Cryptographic failures
        # Hashing with MD5 is insecure! There are many tools on the internet
        # specifically made to encrypt many hashers t. ex. https://crackstation.net/
        # These hashes are shown in the admin only page
        md5 = hashlib.md5(query.encode()).hexdigest()
        # FIX:
        # Using more secure hashing methods such as Django's built-in PBKDF2 algorithm
        # This is recommended by Django
        #md5 = make_password(query)
        createSecureData(request.user.username, md5)
    return md5

# Creates and stores a SecureData object to the Django's db.sqlite3 (inside src folder)
def createSecureData(name, hash):
    secure_data = SecureData(user_name=name, md5_hash=hash)
    secure_data.save()

# Returns all the currently saved hashes
def getHashes():
    hashes = SecureData.objects.all()
    return hashes

def createMessage(data):
    # FLAW: Insecure design?
    # Depending on the fact that the user has to input something in the field (other than empty)
    # Or just forgetting that the user can manually modify the url to make it .../?message=
    empty = Message.objects.filter(message='')
    if empty.count() > 0:
        # Destroy all if there are empty messages (now considered an invalid database)
        messages = getMessages()
        messages.delete()
    message = Message(message=data)
    message.save()

def getMessages():
    messages = Message.objects.all()
    print(messages)
    return messages