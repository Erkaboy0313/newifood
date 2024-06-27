from .models import Comment
from django.contrib.contenttypes.models import ContentType
from fruit.models import Fruit
from meal.models import Meal
from vegetable.models import Vegetable
from django.shortcuts import redirect
from .forms import ContactUsForm


def create_comment(request):
    if request.method == "POST":
        url = request.META.get('HTTP_REFERER')
        type = request.POST.get('type',None)
        object_id = request.POST.get('object_id',None)
        username = request.POST.get('username',None)
        email = request.POST.get('email',None)
        text = request.POST.get('content',None)
        reply = request.POST.get('reply',None)
    
        if type and type == 'fruit':
            content = Fruit.objects.get(id = object_id)
            content_type = ContentType.objects.get_for_model(content)
        
        elif type and type == 'meal':
            content = Meal.objects.get(id = object_id)
            content_type = ContentType.objects.get_for_model(content)
        
        elif type and type == 'vegetable':
            content = Vegetable.objects.get(id = object_id)
            content_type = ContentType.objects.get_for_model(content)

        comment = Comment.objects.create(
            username = username,
            content= text,
            email = email,
            content_type=content_type,
            object_id=object_id,
        )

        if reply:
            reply = Comment.objects.get(id = int(reply))
            comment.reply = reply
            comment.save()

        return redirect(url)
    
def contact_us(request):
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect(url)