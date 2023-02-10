from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):

    name_max_length=128
    
    name = models.CharField(max_length=name_max_length, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name


class Page(models.Model):

    title_max_length=128
    url_max_length=200
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=title_max_length)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

