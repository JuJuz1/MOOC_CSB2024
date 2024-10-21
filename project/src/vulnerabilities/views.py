from django.shortcuts import render
import sqlite3

# Create your views here.

def homePageView(request):
    return render(request, 'pages/home.html')


def injectionPageView(request):
    # Input value
    query = request.GET.get('query', '')
    results = []
    if query:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        # How the attacker could get the name of the tables:
        # ' UNION SELECT name FROM sqlite_master WHERE type='table' --
        # Example injection to get the passwords of all admins: 
        # ' UNION SELECT password FROM Users WHERE admin=1 --
        response = cursor.execute(f"SELECT id FROM Users WHERE name LIKE '{query}'").fetchall()
        results = response
    return render(request, 'pages/injection.html', {'results': results})