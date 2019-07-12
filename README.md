# Towi Portal Backend

Towi was born as a platform to evaluate and develop cognitive abilities in children between 6 and 12 years old.

Now, thanks to the support of the UNICEF INNOVATION FUND, it is also a research tool that incorporates elements of big data and artificial intelligence to obtain information about children´s cognitive abilities and the learning difficulties that they can present, among other topics of scientific, psychological and educative interest.

Towi platform and its data base are available for research for free. To start using it you just follow the next instructions.

## Getting Started

These instructions will get you a copy of Towi up and running on your local machine for development and testing purposes.

### Prerequisites

This are the prerequisites to install Towi on your local machine.

```
Python 3.5 >= 3.7
MySQL
Virtual Environment
Sendgrid Account
Openpay Account
```

## Installing

Please clone this repository
```
git clone https://github.com/pixframe/towi_portal
```

Create a new python environment and install the requirements

```
virtualenv -p python3.5 YOUR-ENVIRONMENT-NAME

workon YOUR-ENVIRONMENT-NAME/bin/activate

pip install -r requirements/develop.txt
```

Install the test dump for MySQL DB

```
mysqldump -u YOUR-USER -p YOUR_DATABASE < towi_portal/db/towi_test_dump.sql
```
After set the dump db please configure your config/settings/local.py file:
```
from .base import *

DEBUG = False or True

ALLOWED_HOSTS = ["ALLOWED_HOSTS"]

DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "DATABASE-NAME",
        'USER': "DB-USERNAME",
        'PASSWORD': "DB-USERNAME-PASSWORD",
        'HOST': "HOST",
        'PORT': "PORT"
       }
   }

STATIC_URL = "/NAME-FOR-THE-STATIC-ROOT/"

STATIC_ROOT = "PROJECT-ROOT"


```
After configuring your config/settings/local.py
```
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
```

You will receive this in the console:
```
System check identified no issues (0 silenced).
--DATE OF RUNSERVER--
Django version 1.11.7, using settings "config.settings.local"
Starting development server at http://localhost/
Quit the server with CONTROL-C.
```

Please read the system documentation in:

```
http://localhost/docs/
```

## Running the tests

Go to:

```
http://localhost/inicio/
```

Register or login with a test account to see the game reports and more.


## Built With

* [Django](https://www.djangoproject.com/) - The web framework used.
* [Django Rest Framework](www.django-rest-framework.org/) - Used to generate the web API's.
* [Celery](www.celeryproject.org) - Used to manage tasks.
* [drf-yasg](https://rometools.github.io/rome/) - Used to generate project documentation.

## Contributing

Please read [CONTRIBUTING.md](https://github.com/pixframe/towi/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.


## Authors

* **Pixframe Studios SAPI de CV**  - [Pixframe Studios](https://www.pixframestudios.com)

See also the list of [contributors](https://github.com/pixframe/towi/blob/master/CONTRIBUTORS.md) who participated in this project.

## License

This project is licensed under the GNU License - see the [LICENSE.md](https://github.com/pixframe/towi/blob/master/LICENSE) file for details

## Acknowledgments

* Unicef
* Publimetro
* Nyx Technologies
