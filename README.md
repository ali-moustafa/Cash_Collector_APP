# Cash Collector APP

## About

Made using **Python 3.11** + **Django** and database is **SQLite**.
Testing is done using **untitest** module.

## Important Instructions

From Admin page `http://localhost:8000/admin` login using info at the end of this file:
- Add employees (after loading users as described below) as cash collector or Manager and they are already mapped to auth_user table.
- Add tasks in tasks table.

Using Postman (recommended) for example:
- Run: `http://localhost:8000/login` ['POST']
- Enter username: 'xxx' & password: 'xxx' in [body] tab [x-www-form-urlencoded]
- This will create sessionID which will be used to authenticate user to execute other APIs.
- To see the status of Cash Collector, use `localhost:8000/myapp/tasks/status?cash_collector={employee_id}`
- To collect/deliver, use `localhost:8000/myapp/tasks/{task_id}/[collect or deliver]` and in the request body {"collected/delivered": "True"}
- If collect/deliver endpoit didn't work, add 'X-CSRFToken' in the headers and use the 'csrftoken' in Cookies.

## Prerequisites

\[Optional\] Install virtual environment:

```bash
$ python -m virtualenv env
```

\[Optional\] Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

Run migrations:
```bash
$ python manage.py migrate
```

Initialize data:
```bash
$ python manage.py loaddata users
```

Run server on port 8000:
```bash
$ python manage.py runserver 8000
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$ chmod +x scripts/run.sh
$ scripts/run.sh
```

### Docker

It is also possible to run the myapp app using docker:

Build the Docker image:
```bash
$ docker build -t django-CC -f docker/Dockerfile .
```

Run the Docker container:
```bash
$ docker run --rm -i -p 8000:8000 django-CC
```

#### Helper script

It is possible to run all of the above with helper script:

```bash
$ chmod +x scripts/run_docker.sh
$ scripts/run_docker.sh
```

## Post Installation

Go to the web browser and visit `http://localhost:8000/admin`

Admin username: **admin**

Admin password: **adminpassword**

## Helper Tools

### Django Admin

It is possible to add additional admin user who can login to the admin site. Run the following command:
```bash
$ python manage.py createsuperuser
```
Enter your desired username and press enter.
```bash
Username: admin_username
```
You will then be prompted for your desired email address:
```bash
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```
Password: **********
Password (again): *********
Superuser created successfully.
```

Go to the web browser and visit `http://localhost:8000/admin`

### Tests

Running tests:
```bash
$ python manage.py test myapp
```
