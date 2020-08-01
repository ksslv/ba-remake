# BA-remake
> An (in-progress) attempt to remake the Bon Appetit website using Python and Django. This is a project that I'm currently working on in order to understand Django better. 


### Technologies used
- Python 3.7
- Django 2.2.5
- Tailwind CSS 1.4


### Demo
https://youtu.be/cDlhAxioP_w


### Usage
To activate the project environment, navigate inside the project directory in Terminal and run `pipenv shell`. 

Once in the project env, run `python manage.py runserver` from the project's directory to start the it locally. 

### Structure 
This Django project has several apps: 
- `users`
- `recipes`
- `reviews`
- `lists` 
- `core` 
- `api`


Additionally, it has: 
- A `templates` folder for all HTML templates. 
- An `uploads` folder for all all user uploads.
- A `static` folder for CSS and some image assets.
- A few other CSS-related files.

### Testing 
Inside of your project environment, run `python manage.py test`. 

Note: I haven't added many test yet. 

### TODO
1. Adding recipes functionality
2. Error handling + error pages
3. Edit profile functionality
4. Improved home page
5. Upgrade Djnago
6. CSS/HTML best practices


### Other
If you've somehow stumbled upon this repo while trying to learn Django, here are some resources that I've personally used to get started and can recommend: 
- *Two Scoops of Django* by  D. and A. Feldroy
- *Django for Professionals* by  William S. Vincent
