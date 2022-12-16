from django.db import models


# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    tags = models.ManyToManyField('tag', blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
