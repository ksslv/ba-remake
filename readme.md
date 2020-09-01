# BA-remake

> An (in-progress) attempt to remake the Bon Appetit website using Python and Django. This is a project that I'm currently working on in order to understand Django better.

### Technologies used

- Python 3.7
- Django 2.2.5
- Tailwind CSS 1.4

### Demo

[![YouTube Demo](https://img.youtube.com/vi/cDlhAxioP_w/0.jpg)](https://www.youtube.com/watch?v=cDlhAxioP_w)

### How to run

In order to run the project locally, you need to have Python3 and pip installed.

```
# To check whether Python3 and pip are installed, run:
python --version
pip --version

# If you don't have pip, one of the ways to install it is using brew, as below. Other ways are available too.
brew install pipenv
```

After making sure that both Python3 and pip are installed, navigate inside the project root directory in Terminal and run `pipenv shell` to activate the project environment:

```
pipenv shell
```

You will also need to generate a secret key for the local copy of the project:

```
# In Terminal, run from within the project folder:
python -c 'from django.core.management.utils import get_random_secret_key; print(f"SECRET_KEY = \"{get_random_secret_key()}\"")' >> secret.py
```

To start the Django project locally:

```
# Once in the project env and inside the project's directory, run:
python manage.py runserver
```

Create a superuser:

```
python manage.py createsuperuser
```

In the browser, go to the admin panel `http://localhost:8000/admin/` to log in. Feel free to add some test users and recipes from the admin panel.

Once there has been at least one recipe added, visit `http://localhost:8000/` to view the home page.

NOTE: I've seeded my local Django database with fake data. Will add the scripts I used once I improve them :)

### Structure

This Django project has several apps:

- `users`
- `recipes`
- `reviews`
- `lists` [not started]
- `core`
- `api`

Additionally, it has:

- A `templates` folder for all HTML templates.
- An `uploads` folder for all all user uploads.
- A `static` folder for CSS and some image assets.
- A few other CSS-related files.

### Testing

Inside of your project environment, run `python manage.py test`.

NOTE: I've added a limited number of unit tests so far, primarily in the `recipes` and `users` apps. More will be added in the next few weeks.

### TODO

1. Adding recipes functionality
2. Error handling + error pages
3. Edit profile functionality
4. Improved home page / Switch `recipes` app from FBV to CBV
5. Upgrade Django
6. CSS/HTML best practices

### Other

If you've somehow stumbled upon this repo while trying to learn Django, here are some resources that I've personally used to get started and can recommend:

- _Two Scoops of Django_ by D. and A. Feldroy
- _Django for Professionals_ by William S. Vincent
