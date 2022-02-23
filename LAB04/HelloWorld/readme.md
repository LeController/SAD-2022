COMMANDS USED 
https://docs.docker.com/samples/django/ - THIS TUTORIAL WAS FOLLOWED

- Dockerfile created
- requirements.txt created
- docker-compose.yml created

In Ubuntu WSL:

$ docker-compose run web django-admin startproject composeexample .

$ sudo chown -R fatcontroller:fatcontroller .

settings.py was edited for postgres

$ docker-compose up

The site was up and running at localhost:8000

At this point, the tutorial from LAB03 was followed to link and HTML template to display HelloWorld! on the website.

DONE
