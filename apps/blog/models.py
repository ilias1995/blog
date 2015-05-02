from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class BlogType(models.Model):
    type_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.type_name

class Blog(models.Model):
    blog_type = models.ForeignKey(BlogType)
    blog_name = models.CharField(max_length=200)
    add_date = models.DateTimeField(default=datetime.now())
    user = models.ForeignKey(User)
    blog_text = models.TextField()

    def __unicode__(self):
        return self.blog_name

class Comments(models.Model):
    user = models.ForeignKey(User)
    blog = models.ForeignKey(Blog)
    add_date = models.DateTimeField(default=datetime.now())
    comment = models.TextField()
    def __unicode__(self):
        return self.comment
