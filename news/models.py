from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.models import TimeStampedModel


class Author(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, default=None)
    name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'author'

    def __unicode__(self):
        return "{}".format(self.name)


class Article(TimeStampedModel):
    author = models.ForeignKey(Author, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    publish = models.BooleanField(default=False)

    class Meta:
        db_table = 'article'

    def __unicode__(self):
        return "{}".format(self.title)
