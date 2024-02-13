<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Setup Instructions</title>
</head>
<body>

<h1>Project Setup Instructions</h1>

<ol>
    <li><a href="#" onclick="executeCommand('git clone https://github.com/VladKrit-commits/newspaper-agency')">Clone a repository</a></li>
    <li><a href="#" onclick="executeCommand('cd agency-project')">Create a directory</a></li>
    <li><a href="#" onclick="executeCommand('python3 -m venv venv')">Create a venv</a></li>
    <li><a href="#" onclick="executeCommand('source venv/bin/activate')">Activate a venv</a></li>
    <li><a href="#" onclick="executeCommand('pip install -r requirements.txt')">Install requirements</a></li>
    <li><a href="#" onclick="executeCommand('python manage.py makemigrations')">Make migrations</a></li>
    <li><a href="#" onclick="executeCommand('python manage.py migrate')">Apply migrations</a></li>
    <li><a href="#" onclick="executeCommand('python manage.py runserver')">Start the project</a></li>
</ol>

<h2>How it looks</h2>

<h3>Data base structure schema</h3>
<img src="agency/static/ScreenshotsNewspapaersAgency/db structure.jpg" alt="DB Structure">

<h3>Interface</h3>

<h4>Login page</h4>
<img src="agency/static/ScreenshotsNewspapaersAgency/login.jpg" alt="Login Page">

<h4>Home page</h4>
<img src="agency/static/ScreenshotsNewspapaersAgency/homepage.jpg" alt="Home Page">

<h4>Newspapers main page</h4>
<img src="agency/static/ScreenshotsNewspapaersAgency/newspapers main.jpg" alt="Newspapers Main Page">

<h4>Newspapers create page</h4>
<img src="agency/static/ScreenshotsNewspapaersAgency/newspapers create.jpg" alt="Newspapers Create Page">

<h4>Newspapers detail page</h4>
<img src="agency/static/ScreenshotsNewspapaersAgency/newspapers detail.jpg" alt="Newspapers Detail Page">

<h4>Newspapers update page</h4>
<img src="agency/static/ScreenshotsNewspapaersAgency/newspapers update.jpg" alt="Newspapers Update Page">

<h4>Logged out page</h4>
<img src="agency/static/ScreenshotsNewspapaersAgency/logged out.jpg" alt="Logged Out Page">

</body>
</html>