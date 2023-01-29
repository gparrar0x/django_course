import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProject.settings')

import django
django.setup()


## FAKE POP SCRIPT
import random
from MyApp.models import AccessRecord, Webpage, Topic, User
from faker import Faker

faker = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    return t

def populate(N=5):
    for entry in range(N):

        # get the topic for the entry
        # top = add_topic()
        # fake_url = faker.url()
        # fake_date = faker.date()
        # fake_name = faker.company()

        # # Create the new webpage entry
        # webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # # Create a fake access record for that webpage
        # acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        # Create fake users
        fake_first_name = faker.first_name()
        fake_last_name = faker.last_name()
        fake_email = faker.ascii_safe_email()

        user = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
    print("Populating script!")
    populate(20)
    print("Population complete!")