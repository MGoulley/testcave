TODO: UTILISER https://django-simple-history.readthedocs.io/en/latest/quick_start.html

mgoulley : 1234
pgoulley : )nAP-E#RnS+sY5R
mbeurk : J68s9s.3FeBWDYX


## Deployer en prod :
Update model in you dev environment

python manage.py makemigrations

python manage.py migrate

If there were no errors in your development environment doing 1-3, commit all files (including new migrations)

Deploy changes to production server

From production server run `python3 manage.py migrate`

If you have a staging server you can test it as step 5&6 and then run on production after. As people have said, database is locked during migrations.

## How to use it

```bash
$ # Get the code
$ git clone https://github.com/app-generator/django-dashboard-coreui.git
$ cd django-dashboard-coreui
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv --no-site-packages env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv --no-site-packages env
$ # .\env\Scripts\activate
$
$ # Install modules
$ # SQLIte version
$ pip3 install -r requirements.txt
$
$ # Create tables
$ python manage.py makemigrations
$ python manage.py migrate
$
$ # Start the application (development mode)
$ python manage.py runserver # default port 8000
$
$ # Start the app - custom port
$ # python manage.py runserver 0.0.0.0:<your_port>
$
$ # Access the web app in browser: http://127.0.0.1:8000/
```

<br />


## License

@MIT
