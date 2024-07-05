from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from .managers import FruitManger
from django_ckeditor_5.fields import CKEditor5Field
# Create your models here.

class Fruit(models.Model):

    class Status(models.TextChoices):
        DRAFT = "draft"
        PUBLISHED = 'published'
    
    class TypeChoices(models.TextChoices):
        CITRUS = 'citrus'
        TROPICAL = 'tropical'
        BERRIES= 'berries'
        STONE = 'stone'
        MELONS= 'melons'
        DRUPES= 'drupes'
        POME = 'pome'
        EXOTIC = 'exotic'
        DRIED = 'dried'
        CLIMACTERIC = 'climacteric'
        NONCLIMACTERIC = 'nonclimacteric'
        SUBTROPICAL = 'subtropical'
        TEMPERATE = 'temperate'
        HARDY = 'hardy'
        SOFT = 'soft'
        HARD = 'hard'
        JUICY = 'juicy'
        AROMATIC = 'aromatic'
        TART = 'tart'
        SWEET = 'sweet'
    
    country = models.ForeignKey('meal.Country',on_delete = models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length = 30,blank=True, null=True,choices = TypeChoices.choices)
    title = models.CharField(max_length = 200, blank=True, null=True)
    slug = models.SlugField(max_length = 50, unique_for_date='created_time', blank=True,)
    name = models.CharField(max_length = 50, blank=True, null=True)
    description = CKEditor5Field(blank=True, null=True,config_name='extends')
    image = models.URLField(blank=True,null=True)
    like = models.PositiveIntegerField(default = 0)
    seen = models.PositiveIntegerField(default = 0)
    avarage_cost = models.CharField(max_length = 30, blank=True, null=True)
    author = models.CharField(max_length = 50,blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    key_words = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=100,blank=True,default=Status.PUBLISHED,choices=Status.choices)
    confirmed = models.BooleanField(default=False,blank=True,null=True)

    objects = models.Manager()
    filter = FruitManger()

    def imageURL(self):
        if self.image:
            return self.image
        else:
            return ''

    class Meta:
        ordering = ['-created_time','-confirmed']
        indexes = [
            models.Index(fields=['-created_time']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:  # If slug is not set
            self.slug = slugify(self.name)  # Generate slug from name
        return super().save(*args, **kwargs) 

    def get_absolute_url(self):
        return reverse("fruit:fruit_details", args=[self.country.region.name,self.country.name,self.created_time.year,self.created_time.month,self.created_time.day,self.slug])
    
class Section(models.Model):
    meal = models.ForeignKey(Fruit,on_delete= models.CASCADE)
    image = models.ImageField(upload_to='Meals/',blank=True,null=True)
    text = models.TextField(blank=True, null=True)

    def imageURL(self):
        if self.image:
            return self.image.url
        else:
            return ''