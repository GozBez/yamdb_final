from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import User


class Command(BaseCommand):
    help = "Loads data from users.csv"

    def handle(self, *args, **options):

        if User.objects.exists():
            print('user data already loaded...exiting.')
            return

        print("Loading users data")

        for row in DictReader(open('static/data/users.csv')):
            if row['role'] == 'admin':
                user = User(
                    id=row['id'],
                    username=row['username'],
                    is_staff=True,
                    is_superuser=True,
                    email=row['email'],
                    role=row['role'])
                user.save()
            elif row['role'] == 'moderator':
                user = User(
                    id=row['id'],
                    username=row['username'],
                    is_staff=True,
                    email=row['email'],
                    role=row['role'])
                user.save()
            else:
                user = User(
                    id=row['id'],
                    username=row['username'],
                    email=row['email'],
                    role=row['role'])
                user.save()
