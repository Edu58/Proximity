# Proximity
Proximity ia a neighborhood watch web app built with Django 4, Cloudinary, PostgreSQL and deployed on Heroku. With proximity, a user can create an acount, login, and see what other users have posted on the platform. Posts are categorised into 3, Events, Announcements and Alerts. They are also color coded to allow easier spotting.
A user can also create their own post, add their neighbourhood or even a business.They can also search for a specifi business or neighbourhood which will also show the extra info such as the total occupants, location and emergency contacts eg. police, hospital, fire department.

![Home](static/images/proximity-home.png)

## Getting Started

- Type the following command in your terminal to clone this repository

```
git clone https://github.com/Edu58/Proximity.git
```

If you are using SSH, use the following command

```
git clone git@github.com:Edu58/Proximity.git
```

When you run the commands successfully, you should have a local version of this repository.

### Prerequisites

- A computer with Python 3 install. Check [here](https://realpython.com/installing-python/) for
  further [instructions](https://realpython.com/installing-python/)
- Access to the Internet
- An IDE of your choice e.g. Pycharm, VS Code, Sublime Text

### Installing

Before starting the application, run ```pip install -r requirements.txt``` to install the project dependencies.

create .env file in the project root directory and populate it with:
```
SECRET_KEY= '<your django project secret key>'
DEBUG= '<True or False>'
DB_NAME= <your db name>
DB_USER= <your db username>
DB_PASSWORD= <your db password>
CLOUD_NAME= <your cloudinary name>
CLOUD_API_KEY= <your cloudinary api key>
CLOUD_API_SECRET= <your cloudinary api secret>
```

To run the app, unzip the cloned folder if it is zipped. Otherwise, navigate inside the folder and
run ```python manage.py runserver``` or ```python manage.py server``` in your terminal. Any of these 2 should start the
server at
localhost:8000. Once the server is running, open your browser and enter localhost:8000 in your url bar of your
preferred browser, and you should be able to use the app now. This will only work on the computer running the server. It
is not available to anyone else.

When you signup, login and submit a project successfully, you should be able to see posts from other users if there are any.

## Deployment

This project can be deployed for free on Heroku. Follow
these [instructions](https://realpython.com/django-hosting-on-heroku/) to deploy.

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Cloudinary](https://cloudinary.com/) - For storing images
* [Django-Bootstrap-V5](https://pypi.org/project/django-bootstrap-v5/) - CSS Framework
* [JQuery](https://jquery.com/) - Javascript Library used for fade effects
* [PostgreSQL](https://www.postgresql.org/) - Database used

## Known Bugs
My List feature is not working

Feel free to submit a pull request or reach out at edumuriithi58@gmail.com.

## Contributing

Feel free to submit a pull request or reach out at edumuriithi58@gmail.com.

## Authors

* **Edwin Karimi** - *Initial work* - [Proximity](https://github.com/Edu58/Proximity)

- Twitter - [@GISDevEd](https://twitter.com/GISDevEd)
- Linkedin - [edwin-karimi](https://www.linkedin.com/in/edwin-karimi/)
  <br>
  <br>
- No contributors yet

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details