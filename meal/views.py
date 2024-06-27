from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Meal,Country,Region
from fruit.models import Fruit
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from .countries import ramining,countries_by_region
import os
from iFood.settings import BASE_DIR

def meal_details(request,region,country,year,month,day,post):
    meal = Meal.objects.get(country__region__name = region, country__name = country,slug = post)

    if f'post_views_{meal.id}' not in request.session:
        meal.seen += 1
        meal.save()
        request.session[f'post_views_{meal.id}'] = True

    most_liked_meals = Meal.filter.get_most_liked_10()
    most_viewed_meals = Meal.filter.get_most_viewed_10()
    related = Meal.objects.filter(country__name = country)[:10]

    content_type = ContentType.objects.get_for_model(meal)
    commnets = Comment.objects.filter(content_type = content_type,object_id = meal.id,reply__isnull = True)

    context = {
        'meal':meal,
        'most_liked_meals':most_liked_meals,
        'most_viewed_meals':most_viewed_meals,
        'related':related,
        'comments':commnets,
    }

    return render(request,'meal_details.html',context)

def create_meal(request):
    Meal.objects.all().delete()
    
    food_names = [
        {"name": "Pizza", "country": "Italy"},
        {"name": "Sushi", "country": "Japan"},
        {"name": "Hamburger", "country": "United States"},
        {"name": "Pasta", "country": "Italy"},
        {"name": "Curry", "country": "India"},
        {"name": "Tacos", "country": "Mexico"},
        {"name": "Steak", "country": "United States"},
        {"name": "Fried Rice", "country": "China"},
        {"name": "Kebab", "country": "Uzbekistan"},
        {"name": "Chicken Tikka Masala", "country": "United Kingdom"},
        {"name": "Pho", "country": "Vietnam"},
        {"name": "Paella", "country": "Spain"},
        {"name": "Goulash", "country": "Hungary"},
        {"name": "Moussaka", "country": "Greece"},
        {"name": "Bibimbap", "country": "South Korea"},
        {"name": "Biryani", "country": "India"},
        {"name": "Shepherd's Pie", "country": "United Kingdom"},
        {"name": "Schnitzel", "country": "Austria"},
        {"name": "Chili Con Carne", "country": "United States"},
        {"name": "Lasagna", "country": "Italy"},
        {"name": "Jambalaya", "country": "United States"},
        {"name": "Pad Thai", "country": "Thailand"},
        {"name": "Ravioli", "country": "Italy"},
        {"name": "Ratatouille", "country": "France"},
        {"name": "Fish and Chips", "country": "United Kingdom"},
        {"name": "Tandoori Chicken", "country": "India"},
        {"name": "Ramen", "country": "Japan"},
        {"name": "Gyoza", "country": "Japan"},
        {"name": "Kofta", "country": "Saudi Arabia"},
        {"name": "Beef Stroganoff", "country": "Russia"},
        {"name": "Fajitas", "country": "Mexico"},
        {"name": "Shawarma", "country": "Saudi Arabia"},
        {"name": "Risotto", "country": "Italy"},
        {"name": "Pad See Ew", "country": "Thailand"},
        {"name": "Stuffed Peppers", "country": "Thailand"},
        {"name": "Tamales", "country": "Mexico"},
        {"name": "Currywurst", "country": "Germany"},
        {"name": "Falafel", "country": "Saudi Arabia"},
        {"name": "Pierogi", "country": "Poland"},
        {"name": "Gumbo", "country": "United States"},
        {"name": "Miso Soup", "country": "Japan"},
        {"name": "Ceviche", "country": "Peru"},
        {"name": "Katsu Curry", "country": "Japan"},
        {"name": "Coq au Vin", "country": "France"},
        {"name": "Beef Bourguignon", "country": "France"},
        {"name": "Hainanese Chicken Rice", "country": "Singapore"},
        {"name": "Peking Duck", "country": "China"},
        {"name": "Beef Rendang", "country": "Indonesia"},
        {"name": "Corned Beef and Cabbage", "country": "Ireland"},
        {"name": "Bibimbap", "country": "South Korea"},
        {"name": "Rösti", "country": "Switzerland"},
        {"name": "Croque Monsieur", "country": "France"},
        {"name": "Cannelloni", "country": "Italy"},
        {"name": "Empanadas", "country": "Argentina"},
        {"name": "Beef Bulgogi", "country": "South Korea"},
        {"name": "Quiche Lorraine", "country": "France"},
        {"name": "Chicken Adobo", "country": "Philippines"},
        {"name": "Kung Pao Chicken", "country": "China"},
        {"name": "Croquettes", "country": "Spain"},
        {"name": "Beef Empanadas", "country": "Argentina"},
        {"name": "Chicken Parmesan", "country": "Italy"},
        {"name": "Beef Tacos", "country": "Mexico"},
        {"name": "Mole Poblano", "country": "Mexico"},
        {"name": "Huevos Rancheros", "country": "Mexico"},
        {"name": "Beef Pot Roast", "country": "United States"},
        {"name": "Chicken Satay", "country": "Thailand"},
        {"name": "Chicken Shawarma", "country": "Saudi Arabia"},
        {"name": "Chicken Quesadilla", "country": "Mexico"},
        {"name": "Chicken Marsala", "country": "Italy"},
        {"name": "Shrimp Scampi", "country": "Italy"},
        {"name": "Shrimp Fried Rice", "country": "China"},
        {"name": "Lobster Roll", "country": "United States"},
    ]


    blogs = os.path.join(BASE_DIR,"meal","food_blogs",'bogs.txt')
    iamges = os.path.join(BASE_DIR,"meal","food_blogs",'images.txt')
    keys = os.path.join(BASE_DIR,"meal","food_blogs",'keywords.txt')
    prices = os.path.join(BASE_DIR,"meal","food_blogs",'new_price.txt')

    def get_blogs(blogs):
        with open(blogs,'r',encoding='utf-8') as file:
            blogs = file.read().split("#####")
            blogs = [x.split("```")[1].replace('html','') for x in blogs if x.strip()]
            titles = [x[x.find('<h1>')+4:x.find("</h1>")] for x in blogs]
            return blogs,titles
        
    def get_images(iamges):
        with open(iamges,'r',encoding='utf-8') as file:
            images = file.readlines()
            images = [x.split('##')[1].strip() for x in images]
            
            return images
    def get_keys(keys):
        with open(keys,'r',encoding='utf-8') as file:
            keys = file.readlines()
            keys = [x.strip() for x in keys if not "#####" in x]
            return keys
    
    def get_price(prices):
        with open(prices,'r',encoding='utf-8') as file:
            prices = file.read().split('#####')
            prices = [x.split(":**")[1].strip() for x in prices if x.strip()]
            return prices

    blogs,titles = get_blogs(blogs)
    images = get_images(iamges)
    keys = get_keys(keys)
    prices = get_price(prices)

    for index,c in enumerate(food_names):
        try:
            country = Country.objects.get(name = c['country'])
            Meal.objects.create(country = country,name = c['name'],title = titles[index],description = blogs[index],image = images[index],author = 'Admin',avarage_cost = prices[index])
        except:
            print(c)


    return HttpResponse('good game')

def create_countries(request):
    food_names = [
        {"name": "Pizza", "country": "Italy"},
        {"name": "Sushi", "country": "Japan"},
        {"name": "Hamburger", "country": "United States"},
        {"name": "Pasta", "country": "Italy"},
        {"name": "Curry", "country": "India"},
        {"name": "Tacos", "country": "Mexico"},
        {"name": "Steak", "country": "United States"},
        {"name": "Fried Rice", "country": "China"},
        {"name": "Kebab", "country": "Uzbekistan"},
        {"name": "Chicken Tikka Masala", "country": "United Kingdom"},
        {"name": "Pho", "country": "Vietnam"},
        {"name": "Paella", "country": "Spain"},
        {"name": "Goulash", "country": "Hungary"},
        {"name": "Moussaka", "country": "Greece"},
        {"name": "Bibimbap", "country": "South Korea"},
        {"name": "Biryani", "country": "India"},
        {"name": "Shepherd's Pie", "country": "United Kingdom"},
        {"name": "Schnitzel", "country": "Austria"},
        {"name": "Chili Con Carne", "country": "United States"},
        {"name": "Lasagna", "country": "Italy"},
        {"name": "Jambalaya", "country": "United States"},
        {"name": "Pad Thai", "country": "Thailand"},
        {"name": "Ravioli", "country": "Italy"},
        {"name": "Ratatouille", "country": "France"},
        {"name": "Fish and Chips", "country": "United Kingdom"},
        {"name": "Tandoori Chicken", "country": "India"},
        {"name": "Ramen", "country": "Japan"},
        {"name": "Gyoza", "country": "Japan"},
        {"name": "Kofta", "country": "Saudi Arabia"},
        {"name": "Beef Stroganoff", "country": "Russia"},
        {"name": "Fajitas", "country": "Mexico"},
        {"name": "Shawarma", "country": "Saudi Arabia"},
        {"name": "Risotto", "country": "Italy"},
        {"name": "Pad See Ew", "country": "Thailand"},
        {"name": "Stuffed Peppers", "country": "Thailand"},
        {"name": "Tamales", "country": "Mexico"},
        {"name": "Currywurst", "country": "Germany"},
        {"name": "Falafel", "country": "Saudi Arabia"},
        {"name": "Pierogi", "country": "Poland"},
        {"name": "Gumbo", "country": "United States"},
        {"name": "Miso Soup", "country": "Japan"},
        {"name": "Ceviche", "country": "Peru"},
        {"name": "Katsu Curry", "country": "Japan"},
        {"name": "Coq au Vin", "country": "France"},
        {"name": "Beef Bourguignon", "country": "France"},
        {"name": "Hainanese Chicken Rice", "country": "Singapore"},
        {"name": "Peking Duck", "country": "China"},
        {"name": "Beef Rendang", "country": "Indonesia"},
        {"name": "Corned Beef and Cabbage", "country": "Ireland"},
        {"name": "Bibimbap", "country": "South Korea"},
        {"name": "Rösti", "country": "Switzerland"},
        {"name": "Croque Monsieur", "country": "France"},
        {"name": "Cannelloni", "country": "Italy"},
        {"name": "Empanadas", "country": "Argentina"},
        {"name": "Beef Bulgogi", "country": "South Korea"},
        {"name": "Quiche Lorraine", "country": "France"},
        {"name": "Chicken Adobo", "country": "Philippines"},
        {"name": "Kung Pao Chicken", "country": "China"},
        {"name": "Croquettes", "country": "Spain"},
        {"name": "Beef Empanadas", "country": "Argentina"},
        {"name": "Chicken Parmesan", "country": "Italy"},
        {"name": "Beef Tacos", "country": "Mexico"},
        {"name": "Mole Poblano", "country": "Mexico"},
        {"name": "Huevos Rancheros", "country": "Mexico"},
        {"name": "Beef Pot Roast", "country": "United States"},
        {"name": "Chicken Satay", "country": "Thailand"},
        {"name": "Chicken Shawarma", "country": "Saudi Arabia"},
        {"name": "Chicken Quesadilla", "country": "Mexico"},
        {"name": "Chicken Marsala", "country": "Italy"},
        {"name": "Shrimp Scampi", "country": "Italy"},
        {"name": "Shrimp Fried Rice", "country": "China"},
        {"name": "Lobster Roll", "country": "United States"},
    ]

    for c in food_names:
        for key,value in countries_by_region.items():
            if c['country'] in countries_by_region[key]:
                region,created = Region.objects.get_or_create(name = key)
                Country.objects.get_or_create(region = region,name = c['country'])
                break
    
    return HttpResponse('fffff')

def meals(request,region = None):
    if request.method == "POST":
        filter_params = {}
        for key,value in request.POST.items():
            if not key == 'csrfmiddlewaretoken' and value:
                filter_params[key] = value
        if filter_params:
            meals = Meal.objects.filter(**filter_params)
        else:
            meals = Meal.objects.all()
    else:
        if region:
            meals = Meal.objects.filter(country__region__slug = region)
        else:
            meals = Meal.objects.all()
    
    paginator = Paginator(meals, 21)
    page_number = request.GET.get('page', 1)
    vegs = paginator.page(page_number)
    
    most_viwed_fruits = Fruit.filter.get_most_viewed_10()
    country_id = request.POST.get('country',None)
    context = {
        'meals':vegs,
        'most_viwed_fruits':most_viwed_fruits,
        'country':Country.objects.get(id = country_id) if country_id else None,
        'region':Region.objects.get(slug = region) if region else None,
    }
    return render(request,'meal.html',context)

def like_post(request, post_id):
    # Retrieve the post object from the database
    
    post = get_object_or_404(Meal, pk=post_id)
    if f'meal_like_{post.id}' not in request.session:
        post.like += 1
        post.save()
        request.session[f'meal_like_{post.id}'] = True
        return JsonResponse({'status': 1,'like':post.like})
    
    return JsonResponse({'status': 0})
