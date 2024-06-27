from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Vegetable
from meal.models import Meal,Country
from comment.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def vegetable_details(request,region,country,year,month,day,post):
    vegetable = Vegetable.objects.get(slug = post)

    if f'post_views_{vegetable.id}' not in request.session:
        vegetable.seen += 1
        vegetable.save()
        request.session[f'post_views_{vegetable.id}'] = True

    most_liked_vegetables = Vegetable.filter.get_most_liked_10()
    most_viewed_vegetables = Vegetable.filter.get_most_viewed_10()
    related = Vegetable.objects.filter(type = vegetable.type)[:10]

    content_type = ContentType.objects.get_for_model(vegetable)
    commnets = Comment.objects.filter(content_type = content_type,object_id = vegetable.id,reply__isnull = True)

    context = {
        'vegtable':vegetable,
        'most_liked_vegetables':most_liked_vegetables,
        'most_viewed_vegetables':most_viewed_vegetables,
        'related':related,
        'comments':commnets,
    }

    return render(request,'veg_details.html',context)

def vegetables(request,type=None):
    if request.method == "POST":
        filter_params = {}
        for key,value in request.POST.items():
            if not key == 'csrfmiddlewaretoken' and value:
                filter_params[key] = value
        if filter_params:
            vegetables = Vegetable.objects.filter(**filter_params)
        else:
            vegetables = Vegetable.objects.all()
    else:
        if type:
            vegetables = Vegetable.objects.filter(type = type)
        else:
            vegetables = Vegetable.objects.all()
    
    paginator = Paginator(vegetables, 5)
    page_number = request.GET.get('page', 1)
    vegs = paginator.page(page_number)
    most_viwed_meals = Meal.filter.get_most_viewed_10()
    country_id = request.POST.get('country',None)
    context = {
        'vegetables':vegs,
        'most_viwed_meals':most_viwed_meals,
        'country':Country.objects.get(id = country_id) if country_id else None,
        'type':type,
    }

    return render(request,'vegetable.html',context)

def like_post(request, post_id):
    # Retrieve the post object from the database
    post = get_object_or_404(Vegetable, pk=post_id)

    if f'veg_like_{post.id}' not in request.session:
        post.like += 1
        post.save()
        request.session[f'veg_like_{post.id}'] = True
        return JsonResponse({'status': 1,'like':post.like})
    
    return JsonResponse({'status': 0})
