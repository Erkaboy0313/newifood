from django.shortcuts import render
from meal.models import Meal,Country
from .models import Fruit
from vegetable.models import Vegetable
from django.core.paginator import Paginator
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q

def home(request):
    most_viwed_fruits = Fruit.filter.get_most_viewed_10()
    most_viwed_meals = Meal.filter.get_most_viewed_10()
    most_liked_meals = Meal.filter.get_most_viewed_10()
    most_viwed_veg = Vegetable.filter.get_most_viewed_10()

    context = {
        'most_viwed_fruits':most_viwed_fruits,
        'most_viwed_meals':most_viwed_meals,
        'most_viwed_veg':most_viwed_veg,
        'most_liked_meals':most_liked_meals,
    }

    return render(request,'index.html',context)

def contact_us(request):
    return render(request,'contact.html')

def fruitdetails(request,region,country,year,month,day,post):
    fruit = Fruit.objects.get(slug = post)

    if f'post_views_{fruit.id}' not in request.session:
        fruit.seen += 1
        fruit.save()
        request.session[f'post_views_{fruit.id}'] = True


    most_liked_fruits = Fruit.filter.get_most_liked_10()
    most_viewed_fruits = Fruit.filter.get_most_viewed_10()
    related = Fruit.objects.filter(type = fruit.type)[:10]

    content_type = ContentType.objects.get_for_model(fruit)
    commnets = Comment.objects.filter(content_type = content_type,object_id = fruit.id,reply__isnull = True)

    context = {
        'fruit':fruit,
        'most_liked_fruits':most_liked_fruits,
        'most_viewed_fruits':most_viewed_fruits,
        'related':related,
        'comments':commnets,
    }

    return render(request,'fruit_details.html',context)

def search_result(request):
    keyword = request.GET.get('search',None)
    if keyword:
        meals = Meal.objects.filter(Q(name__icontains = keyword) | Q(description__icontains = keyword))
        fruits = Fruit.objects.filter(Q(name__icontains = keyword) | Q(description__icontains = keyword))
        vegetables = Vegetable.objects.filter(Q(name__icontains = keyword) | Q(description__icontains = keyword))
        context = {
            'meals':meals,
            'fruits':fruits,
            'vegetables':vegetables,
            'empty':meals.exists() or fruits.exists() or vegetables.exists(),
            'keyword':keyword
        }
    return render(request,'search.html',context)

def fruits(request):
    if request.method == "POST":
        filter_params = {}
        for key,value in request.POST.items():
            if not key == 'csrfmiddlewaretoken' and value:
                filter_params[key] = value
        if filter_params:
            fruits = Fruit.objects.filter(**filter_params)
        else:
            fruits = Fruit.objects.all()
    else:
        fruits = Fruit.objects.all()
    
    paginator = Paginator(fruits, 5)
    page_number = request.GET.get('page', 1)
    vegs = paginator.page(page_number)
    most_viwed_veg = Vegetable.filter.get_most_viewed_10()
    country_id = request.POST.get('country',None)
    context = {
        'fruits':vegs,
        'most_viwed_veg':most_viwed_veg,
        'country':Country.objects.get(id = country_id) if country_id else None,
        'type':request.POST.get('type',None)
    }
    return render(request,'fruit.html',context)

def like_post(request, post_id):
    # Retrieve the post object from the database
    
    post = get_object_or_404(Fruit, pk=post_id)
    if f'fruit_like_{post.id}' not in request.session:
        post.like += 1
        post.save()
        request.session[f'fruit_like_{post.id}'] = True
        return JsonResponse({'status': 1,'like':post.like})
    
    return JsonResponse({'status': 0})



# Create your views here.


