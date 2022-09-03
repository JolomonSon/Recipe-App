# Recipe-App

### Cloning the repository

--> Clone the repository using the command below :
```bash
git clone https://github.com/JolomonSon/Recipe-App.git

```
--> Move into the directory where you have the cloned application : 
```bash
cd recipe
```

--> Create a virtual environment :
```bash
# Create our virtual environment
python -m venv venv

```

--> Activate the virtual environment : <br><br>
Mac OS
```bash
source venv/bin/activate
```

Windows OS
```bash
venv\scripts\activate

```
Linux OS
```bash
source venv/bin/activate
```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Migrate Database
```bash
python manage.py migrate

```

--> Create Super User
```bash
python manage.py createsuperuser

```

#

### Run the Development Server

--> To run the App :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

#

## Documentation
Check up [Django Docs](https://docs.djangoproject.com/en/4.0/) for further information.
