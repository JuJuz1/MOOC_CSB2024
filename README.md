# MOOC_CSB2024
Project containing flaws from the OWASP 2021 top ten list for a web application. Made for the MOOC course Cyber Security Base 2024.
Top ten list: https://owasp.org/www-project-top-ten/

Made using Python + Django
 
Currently implemented flaws:
1. Broken access control
2. Cryptographic failures
3. Injection
4. Insecure design
5. Security misconfiguration
6. Software and data integrity failures
7. CSRF (not on the list, but accepted by the course)

See [REPORT.md](./REPORT.md) for a full explanation of the flaws

## Installation instructions:
Ensure you have python 3.7+ installed
- python3 –version (or python –version)

Clone the project from the repository. In a terminal (such as git bash), head over to the root folder of the project (where manage.py is).

- python manage.py migrate -> initialize the Django SQLite database
- python create_db.py -> Create the dummy database
- python manage.py createsuperuser -> create an admin user
- python manage.py runserver -> start the server (most likely at http://localhost:8000)

To test CSRF (Firefox and Chrome at least):
1. Login as any user on the first server
2. Leave some messages to the page
3. Start a second server -> python -m http.server 9000
4. Go to the csrf.html on the second server -> 
http://localhost:9000/project/src/vulnerabilities/templates/pages/csrf.html
(or navigate to it from http://localhost:9000)
5. Reload messages page on the first server -> only the latest message should be left

If you want to test non-admin functionality: 
Head over to the top right corner of the page (header) and click the admin panel. Login with the superuser account you created earlier. Under authentication and authorization, click Add on users. Login as the newly created non-admin account.
