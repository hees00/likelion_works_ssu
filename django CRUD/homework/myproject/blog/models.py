from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Food(models.Model):
    title= models.CharField(max_length=200)
    locate= models.CharField(max_length=30)
    score= models.CharField(max_length=2)
    pub_date=models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]