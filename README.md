# MOOC_CSB2024
Project containing flaws from the OWASP 2021 top ten list for a web application. Made for the MOOC course Cyber Security Base 2024.

Top ten list: https://owasp.org/www-project-top-ten/
 
Currently implemented flaws:
1. Broken access control
2. Cryptographic failures
3. Injection
4. Insecure design
5. Security misconfiguration
6. Software and data integrity failures
7. CSRF (not on the list, but accepted by the course)

# Installation instructions:
Ensure you have python 3.7+ installed
python3 –version (or python –version)

Clone the project from the repository. In a terminal (such as git bash), head over to the root folder of the project (where manage.py is).

python manage.py migrate -> initialize the Django SQLite database
python create_db.py -> Create the dummy database
python manage.py createsuperuser -> create an admin user
python manage.py runserver -> start the server (most likely at http://127.0.0.1:8000)

If you want to test non-admin functionality: Head over to the top right corner of the page (header) and click the admin panel. Login with the superuser account you created earlier. Under authentication and authorization, click Add on users. Login as the newly created non-admin account.
