from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    #this you need to defin like column_name=datatype, here title is column name and charfield is data type
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __unicode__(self):
        #if you are using python3 then use __str__ instead of unicode
        return self.title
