from django.db import migrations
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# news from philly.com
news_list = [{'title': 'Chipotle among Philly eateries closed for health violations',
              'body': 'The city asked — or ordered — nearly two dozen restaurants to close temporarily for health violations between Jan. 16 and Feb. 1. ',
              'published': True},
             {'title': 'Eagles QB Carson Wentz\'s jersey one of most popular in NFL',
              'body': 'The No. 11 Eagles jersey and other Carson Wentz merchandise rank among the most popular in the NFL. Wentz is fifth on the list of  NFL player merchandise sales through November of last season, according to the NFLPA.',
              'published': False},
             {'title': 'Did Budweiser steal artist\'s image for ads during pope',
              'body': 'A Philadelphia photographer says Anheuser-Busch stole his copyright picture of the Philadelphia skyline and used it to create neon Budweiser beer signs that began appearing around the city during Pope Francis’ visit in 2015, according to a lawsuit filed Wednesday in federal court.',
              'published': False},
             {'title': 'Facing a budget crunch, Wolf pays consultants -- to help find savings',
              'body': 'HARRISBURG -- Facing a multibillion-dollar deficit in the state budget, Gov. Wolf took the unusual step late last year of quietly turning to a private consulting firm for advice.',
              'published': True}]


def create_news(apps, schema_editor):
    Author = apps.get_registered_model('news', 'Author')
    news_author = Author.objects.get(name='Test Author')
    Article = apps.get_registered_model('news', 'Article')
    for news in news_list:
        news_article = Article(
            author=news_author,
            title=news['title'],
            body=news['body'],
            publish=news['published']
            )
        news_article.save()


class Migration(migrations.Migration):

     dependencies = [
         ('news', '0002_make_inital_user')
     ]

     operations = [
         migrations.RunPython(create_news),
     ]
