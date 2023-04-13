from csv import DictReader

from django.core.management import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title, User


class Command(BaseCommand):
    help = "Loads data"

    def handle(self, *args, **options):

        print("Loading data")

        for row in DictReader(open('static/data/genre.csv')):
            genre = Genre(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            genre.save()

        for row in DictReader(open('static/data/genre_title.csv')):
            title = Title(id=row['id'], pk=row['title_id'])
            title.save()

            genre = Genre.objects.filter(id=row['genre_id'])
            for g in genre:
                title.genre.add(g)

        for row in DictReader(open('static/data/category.csv')):
            category = Category(
                id=row['id'],
                name=row['name'],
                slug=row['slug']
            )
            category.save()

        for row in DictReader(open('static/data/titles.csv')):
            title = Title(
                id=row['id'],
                name=row['name'],
                year=row['year'],
                category=Category.objects.get(id=row['category'])
            )
            title.save()

        for row in DictReader(open('static/data/review.csv')):
            review = Review(
                id=row['id'],
                title=Title.objects.get(id=row['title_id']),
                text=row['text'],
                author=User.objects.get(id=row['author']),
                score=row['score'],
                pub_date=row['pub_date'])
            review.save()

        for row in DictReader(open('static/data/comments.csv')):
            comment = Comment(
                review=Review.objects.get(id=row['review_id']),
                text=row['text'],
                author=User.objects.get(id=row['author']),
                pub_date=row['pub_date']
            )
            comment.save()
