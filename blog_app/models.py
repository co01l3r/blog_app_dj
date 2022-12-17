from django.db import models


class Topic(models.Model):
    """A model representing a topic, with a title, subtitle, description, creation date,
    featured image, and tags.

    Attributes:
        title (models.CharField): The title of the topic.
        subtitle (models.CharField): The subtitle of the topic, can be blank.
        description (models.TextField): The description of the topic.
        created (models.DateTimeField): The date and time when the topic was created,
            set automatically when the object is created.
        featured_image (models.ImageField): The featured image for the topic, can be blank
            or null. If not provided, a default image will be used.
        tags (models.ManyToManyField): A many-to-many field representing the tags associated
            with the topic.
    """
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    tags = models.ManyToManyField('tag', blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Tag(models.Model):
    """A model representing a tag, with a name.

    Attributes:
        name (models.CharField): The name of the tag.
    """
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
