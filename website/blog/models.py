from django.db import models
#this you need to defin like column_name=datatype, here title is column name and charfield is data type
class Post(models.Model):
    title = models.CharField(max_length = 140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
