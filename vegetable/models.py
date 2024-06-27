from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from .managers import VegManger
# Create your models here.

class Vegetable(models.Model):

    class TypeChoices(models.TextChoices):
        LEAFYGREENS  = 'leafygreens'
        ROOT = 'root'
        CRUCIFEROUS = 'cruciferous'
        ALLIUMS  = 'alliums '
        NIGHTSHADES  = 'nightshades '
        SQUASHANDGOURDS = 'squashandgourds'
        LEGUMES = 'legumes'
    
    class ColorChoices(models.TextChoices):
        GREEN = 'green' 
        ORANGEANDYELLOW = 'orangeandyellow' 
        REDANDPURPLE = 'redandpurple' 
        WHITEANDTAN = 'whiteandtan' 
    
    class SeasonalityChoices(models.TextChoices):
        SPRING = 'spring' 
        SUMMER = 'summer' 
        FALL = 'fall' 
        WINTER = 'winter' 
    
    class CouisineChoices(models.TextChoices):
        MEDITERRANEAN  = 'mediterranean'
        ASIAN  = 'asian'
        LATINAMERICAN  = 'latinamerican'
        INDIAN = 'indian'
    
    class CookingMethodChoices(models.TextChoices):
        RAW = 'raw'
        STEAMED = 'steamed'
        ROASTED = 'roasted'
        GRILLED = 'grilled'
        STIRFRIED = 'stirfried'
        BOILED = 'boiled'
    
    class UseChoices(models.TextChoices):
        SALAD = 'salad'
        SOUP = 'soup'
        SIDEDISH = 'sidedish'
        MAINCOURSE = 'maincourse'
    
    class NutritionalContentChoices(models.TextChoices):
        HIGHFIBER = 'highfiber' 
        HIGHPROTEIN = 'highprotein' 
        LOWCARB = 'lowcarb'
    
    class PopularityChoices(models.TextChoices):
        MOSTUSED = 'mostused'
        SPECIALTY = 'specialty'
        EXOTIC = 'exotic'

    country = models.ForeignKey('meal.Country',on_delete = models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length = 30,blank=True, null=True,choices = TypeChoices.choices)
    color = models.CharField(max_length = 30,blank=True, null=True,choices = ColorChoices.choices)
    season = models.CharField(max_length = 30,blank=True, null=True,choices = SeasonalityChoices.choices)
    couisine = models.CharField(max_length = 30,blank=True, null=True,choices = CouisineChoices.choices)
    cooking_method = models.CharField(max_length = 30,blank=True, null=True,choices = CookingMethodChoices.choices)
    use_case = models.CharField(max_length = 30,blank=True, null=True,choices = UseChoices.choices)
    nurtitional = models.CharField(max_length = 30,blank=True, null=True,choices = NutritionalContentChoices.choices)
    popularity = models.CharField(max_length = 30,blank=True, null=True,choices = PopularityChoices.choices)
    
    slug = models.SlugField(max_length = 50, unique_for_date='created_time', blank=True)
    name = models.CharField(max_length = 50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Vegetables/',blank=True,null=True)
    avarage_cost = models.CharField(max_length = 30, blank=True, null=True)
    like = models.PositiveIntegerField(default = 0)
    seen = models.PositiveIntegerField(default = 0)
    author = models.CharField(max_length = 50,blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)
    key_words = models.TextField(blank=True, null=True)

    objects = models.Manager()
    filter = VegManger()

    class Meta:
        ordering = ['-created_time']
        indexes = [
            models.Index(fields=['-created_time']),
        ]

    def imageURL(self):
        if self.image:
            return self.image.url
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