from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from .manager import MealManger

class Region(models.Model):
    slug = models.SlugField(max_length = 50, unique=True, blank=True)
    name = models.CharField(max_length = 50, blank=True, null=True)
    meal_key_words = models.TextField(blank=True, null=True)
    fruit_key_words = models.TextField(blank=True, null=True)
    veg_key_words = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  # If slug is not set
            self.slug = slugify(self.name)  # Generate slug from title
        return super().save(*args, **kwargs)

class Country(models.Model):
    slug = models.SlugField(max_length = 50, unique=True, blank=True)
    region = models.ForeignKey(Region,on_delete = models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length = 50, blank=True, null=True)
    meal_key_words = models.TextField(blank=True, null=True)
    fruit_key_words = models.TextField(blank=True, null=True)
    veg_key_words = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:  # If slug is not set
            self.slug = slugify(self.name)  # Generate slug from title
        return super().save(*args, **kwargs)

class Meal(models.Model):
    
    country = models.ForeignKey(Country,on_delete = models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(max_length = 50, unique_for_date='created_time', blank=True)
    name = models.CharField(max_length = 50, blank=True, null=True)
    title = models.CharField(max_length = 200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True,null=True)
    like = models.PositiveIntegerField(default = 0)
    seen = models.PositiveIntegerField(default = 0)
    avarage_cost = models.CharField(max_length = 30, blank=True, null=True)
    author = models.CharField(max_length = 50,blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    key_words = models.TextField(blank=True, null=True)

    objects = models.Manager()
    filter = MealManger()

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
    
    def __str__(self):
        return self.slug
    

    def get_absolute_url(self):
        return reverse("meal:meal_details", args=[self.country.region.name,self.country.name,self.created_time.year,self.created_time.month,self.created_time.day,self.slug])

class Section(models.Model):
    meal = models.ForeignKey(Meal,on_delete= models.CASCADE)
    image = models.ImageField(upload_to='Meals/',blank=True,null=True)
    text = models.TextField(blank=True, null=True)
    
    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''

class Locations(models.Model):
    meal = models.ForeignKey(Meal,on_delete= models.CASCADE)
    latitude = models.CharField(max_length=50,blank=True, null=True)
    longitude = models.CharField(max_length=50,blank=True, null=True)
    address = models.CharField(max_length=50,blank=True, null=True)

