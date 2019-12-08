from django.db import models
from django.db import models
from django.template.defaultfilters import slugify

# Register your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    content = models.TextField()
    blog_image = models.FileField(upload_to='uploads')
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('published date')
    slug = models.SlugField(max_length=200)

    def __str__(self):
      return self.title

    def slug(self):
        return slugify(self.title)

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    body = models.TextField()
    course_image = models.FileField(upload_to='uploads')

    def __str__(self):
      return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    description = models.CharField(max_length=250, default=None, blank=True, null=True)
    event_image = models.FileField(upload_to='uploads')
    event_date = models.DateTimeField('Event Date')
    created_at = models.DateTimeField('published date')

    def __str__(self):
      return self.title