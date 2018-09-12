"""

Tests
To run django tests in a django environment, first make sure you have the packages from requirement-test.txt installed, then run the following:

$ python runtests.py
or if you have django_seed in INSTALLED_APPS:

$ python manage.py test django_seed

"""

from django_seed import Seed
import random

seeder = Seed.seeder()

from .models import mModel, Question, Choice

glist = ['M', 'F']
surname = ['Roberta', "Alexandria", "Romania", "Hickland", "Hockland"]
firstname = ['Kangaroo', 'Pikachu', "Megaman", 'Goku', 'Vegeta', 'Cell']
email = ['Kangaroo@earth.com', 'Pikachu@earth.com', "Megaman@earth.com", 'Goku@earth.com', 'Vegeta@earth.com', 'Cell@earth.com']

seeder.add_entity(mModel, 10, {
    'name': lambda x: firstname[x] + " " + surname[x],
    'gender': lambda x: glist[random.randint(2)],
    'age': lambda x: random.randint(1000),
    'email': lambda x: email[x],
})

seeder.execute()


