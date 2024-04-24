from django.db import models
from django.forms import ImageField


# Create your models here.


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)
    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    name = models.CharField(max_length=212)
    def __str__(self):
        return self.name

class Author(TimeStampedModel):
    name = models.CharField(max_length=212)
    description = models.TextField()
    image = models.ImageField(upload_to='author_images')
    def __str__(self):
        return self.name

class Post(TimeStampedModel):
    title = models.CharField(max_length=212)
    body = models.TextField()
    image = models.ImageField(upload_to='post_images')
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title