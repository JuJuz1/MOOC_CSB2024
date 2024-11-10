# Report of the flaws

LINK: https://github.com/JuJuz1/MOOC_CSB2024 
Installation instructions -> see README

FLAW 1: Broken access control
Link: 
https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/views.py#L22 
Broken access control is a serious vulnerability that can occur when an application fails to do the appropriate authorization checks for the user. This can lead to a situation where the unauthorized user can access information and resources they have no permission to. In this current implementation, the flaw could be exploited by any logged in user as the @login_required decorator ensures. The user could access the page, which should be reserved to admins only, by manually navigating to the url or by clicking the link in the header. Data to the page comes from the secure data page where any logged in user can save data in a MD5-hashed form.

As commented out in the code, the fix is very simple. Checking if the user is an admin and rendering a HttpResponseForbidden page if a non-admin tries to access the page. Only rendering the page with the hashed data if the user is an admin.

FLAW 2: Cryptographic failures
Link: https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/utils.py#L48 
Cryptographic failures are failures in software where sensitive data is stored using weak or insecure cryptographic algorithms. In this example, MD5 (Message Digest Algorithm 5) which generates a 128-bit hash value, is used to store secure data. MD5 is nowadays considered outdated as it is vulnerable to collision attacks. This means that different inputs can produce the same output. There are many lookup tables and decryption tools available on the internet that can decrypt weak hashing algorithms.

Fixing this issue is straightforward: Use a more robust algorithm such as Django’s built-in PBKDF2 (Password-Based Key Derivation Function 2). This algorithm uses a SHA-256 hash which leads to a substantially better protection against brute-force attacks. The algorithm has two major improvements. It uses salting which adds random data to the hash preventing any possibility of a precomputed table. On top of this, it uses hash iterations which means hashing the data repeatedly possibly hundreds of thousands of times. This adds significant computational costs for the attacker.

FLAW 3: Injection
Link: https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/utils.py#L32 
Injection is a vulnerability in which a user can manipulate the input to a query in a way that lets them execute arbitrary code against a database. For this project, SQL injection is used to demonstrate the point. On the website, there is a page where a user can access the database created through create_db.py. The intended use is to access the Clients table to see the client of a specific user. However the query is constructed in a way that can be seriously exploited. The input is directly inserted into the query which causes the vulnerability. This causes the database to interpret the query as executable SQL. The commented code shows the ways the attacker could access any part of the database.

Parameterizing the query would eliminate the possibility of an injection. This way the database wouldn’t consider the user input as SQL code but rather as data. Now the database also removes any special characters from the input automatically preventing the ability to modify the intended query.

FLAW 4: Insecure design
Link: 
https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/views.py#L37 
https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/utils.py#L70 
Insecure design is a broad term for the design failures in software which occur due to insufficient security considerations. The potential risks or attacks a malicious actor could exploit are not fully covered by the system’s security measures. In this example, the user could leave a message to the site using the messages page. The flaw arises from the fact that the server assumes the input is validated properly and that there are no other ways to input data to the server. The latter which could be done by manually constructing the url to input an empty string. Ultimately, the design choice of invalidating the database and clearing it when there exists an empty message leads to the root of the flaw.

Fixing this issue would require multiple steps. First, the database should not be cleared if there exists an empty message (i.e. empty string). And secondly, the server should get the input using POST, not GET. This way the url couldn’t be manually constructed to send invalid considered data.

FLAW 5: Security misconfiguration
Link: https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/utils.py#L78 
Security misconfiguration is a security-related flaw in applications that arises when the application or its components are not securely configured. In this example, the user input is not restricted by length which could lead to errors at the database level and exhaust server resources. The latter could lead to DoS (Denial of Service) attacks.

Limiting the length of the input directly in the html document and at the server level would fix this issue correctly.

FLAW 6: Software and data integrity failures
Link: https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/models.py#L10 
Software and data integrity failures is a term that refers to failures in handling data in software. This includes processing, storing, moving, displaying or any other use of data. In this project the flaw is presented by the fact that two database entries could have the same primary key leading to data integrity issues and errors in the database. This happens if two users input the same secure data they wish to save due to MD5 hashing (see cryptographic failures).

Using Django’s built-in UUID (Universally Unique Identifier) generator ensures that every database entry has a unique primary key. The generated keys are designed to be collision-resistant meaning they should always be unique.

FLAW 7: CSRF (Cross-site request forgery)
Link: https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/templates/pages/csrf.html#L6 
https://github.com/JuJuz1/MOOC_CSB2024/blob/35646f178f73f130094bbb76f2c8a079317ba3c0/project/src/vulnerabilities/templates/pages/messages.html#L13 
CSRF is an attack where a user or a website can mislead a logged-in user to perform actions without their consent. For this project, the attacker has created a malicious web page called csrf.html which, when loaded, sends a get request to the messages page with an empty input. This works because the server doesn’t have proper CSRF protections and the GET request includes the session cookie.

Fixing the flaw involves two simple steps. The messages form should include a CSRF token and the form should use POST instead of GET for requests. Having the CSRF token check would tie the user’s session to the authenticated user. Using POST would prevent using image tags or other methods to trigger unwanted actions.
