# YBKY 2023
Test project for YBKY 2023.

## How To Use

To clone and run this application, you'll need [Git](https://git-scm.com) installed on your computer. From your command line:


#### Clone this repository

``` bash
git clone https://github.com/sobirjonovme/ybky_2023.git
```


#### Go into the repository

``` bash
cd ybky_2023
```

#### Create virtual environment

``` bash
python -m venv env
```


#### Activate virtual environment

``` bash
source env/bin/activate # for linux
env/scripts/activate # for windows
```


#### Install dependencies

``` bash
pip install -r requirements/develop.txt
```

#### Create `.env` file in root directory and fill it according to `.env.example` file


#### Run migrations to setup database:
``` bash
python manage.py migrate
```

#### Create superuser to get access to admin panel:
``` bash
python manage.py createsuperuser
```

#### Run server:
``` bash
python manage.py runserver
```

### Enjoy!!! 🥂
