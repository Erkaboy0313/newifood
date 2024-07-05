from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from .managers import VegManger
# Create your models here.
from django_ckeditor_5.fields import CKEditor5Field

class Vegetable(models.Model):

    class SeasonalityChoices(models.TextChoices):
        SPRING = 'spring' 
        SUMMER = 'summer' 
        FALL = 'fall' 
        WINTER = 'winter' 
    
    class Status(models.TextChoices):
        DRAFT = "draft"
        PUBLISHED = 'published'

    country = models.ForeignKey('meal.Country',on_delete = models.SET_NULL, blank=True, null=True)
    season = models.CharField(max_length = 30,blank=True, null=True,choices = SeasonalityChoices.choices)
    slug = models.SlugField(max_length = 50, unique_for_date='created_time', blank=True)
    name = models.CharField(max_length = 50, blank=True, null=True)
    title = models.CharField(max_length = 200, blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True,config_name='extends')
    image = models.URLField(blank=True,null=True)
    avarage_cost = models.CharField(max_length = 30, blank=True, null=True)
    like = models.PositiveIntegerField(default = 0)
    seen = models.PositiveIntegerField(default = 0)
    author = models.CharField(max_length = 50,blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    key_words = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=100,blank=True,default=Status.PUBLISHED,choices=Status.choices)
    confirmed = models.BooleanField(default=False,blank=True,null=True)

    objects = models.Manager()
    filter = VegManger()

    class Meta:
        ordering = ['-created_time']
        indexes = [
            models.Index(fields=['-created_time']),
        ]

    def imageURL(self):
        if self.image:
            return self.image
        else:
            return ''

    def save(self, *args, **kwargs):
        if not self.slug:  # If slug is not set
            self.slug = slugify(self.name)  # Generate slug from title
        return super().save(*args, **kwargs) 
    
    def get_absolute_url(self):
        return reverse("vegetable:vegetable_details", args=[self.country.region.name,self.country.name,self.created_time.year,self.created_time.month,self.created_time.day,self.slug])
    
class Section(models.Model):
    meal = models.ForeignKey(Vegetable,on_delete= models.CASCADE)
    image = models.ImageField(upload_to='Meals/',blank=True,null=True)
    text = models.TextField(blank=True, null=True)

    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''