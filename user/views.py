from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm,MealForm,FruitForm,VegetableForm,Meal,Vegetable,Fruit
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django_ckeditor_5.forms import UploadFileForm
from django.conf import settings
from django_ckeditor_5.views import image_verify,handle_uploaded_file
from django.http import JsonResponse,Http404

class NoImageException(Exception):
    pass

def log_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,username= username,password=password)
            if user:
                login(request,user=user)
                return redirect('/profile')
            else:
                messages.add_message(request,messages.WARNING,'User not found')
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    return render(request,'login.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user=user)
            return redirect('/profile')
        else:
            print(form.errors)
            messages.add_message(request,messages.WARNING,form.errors)    
    return render(request,'register.html')

@login_required(login_url='user:login')
def log_out(request):
    logout(request)
    return redirect('/home')

def profile(request,cat = None):

    cat = 'meal' if not cat else cat

    blogs = []
    if cat == 'meal':
        blogs = Meal.objects.filter(author = request.user.username)
    elif cat == 'fruit':
        blogs = Fruit.objects.filter(author = request.user.username)
    elif cat == 'vegetable':
        blogs = Vegetable.objects.filter(author = request.user.username)



    context = {
        'category':cat,
        'blogs':blogs
    }

    return render(request,'profile.html',context)

def create_meal(request):
    form = MealForm()
    if request.method == "POST":
        form = MealForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  
            image_file = form.cleaned_data['image_file']
            file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
            image_url = default_storage.url(file_name)
            instance.image = image_url
            instance.author = request.user.username
            instance.save()   
            return redirect('/profile')
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    context = {
        'form':form,
        'category':'meal'
    }
    return render(request,"create_blog.html",context)

def create_fruit(request):
    form = FruitForm()
    if request.method == "POST":
        form = FruitForm(request.POST,request.FILES)
        if form.is_valid():            
            instance = form.save(commit=False)  
            image_file = form.cleaned_data['image_file']
            file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
            image_url = default_storage.url(file_name)
            instance.image = image_url
            instance.author = request.user.username
            instance.save()   
            return redirect('/profile')
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    context = {
        'form':form,
        'category':'fruit'
    }
    return render(request,"create_blog.html",context)

def create_vegetable(request):
    form = VegetableForm()
    if request.method == "POST":
        form = VegetableForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)  
            image_file = form.cleaned_data['image_file']
            file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
            image_url = default_storage.url(file_name)
            instance.image = image_url
            instance.author = request.user.username
            instance.save()   
            return redirect('/profile')
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    context = {
        'form':form,
        'category':'vegetable'
    }
    return render(request,"create_blog.html",context)

def edit_meal(request,slug):
    meal = get_object_or_404(Meal,slug = slug)
    form = MealForm(instance = meal)
    if request.method == "POST":
        form = MealForm(request.POST,request.FILES,instance = meal)
        if form.is_valid():
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                instance = form.save(commit=False)
                file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
                image_url = default_storage.url(file_name)
                instance.image = image_url
                instance.save()
            else:
                form.save()
            return redirect("/profile")
        else:
            messages.add_message(request,messages.WARNING,form.errors)
    context = {
        'form':form,
        "edit":True,
        'current_image': meal.image
    }

    return render(request,"create_blog.html",context)

def edit_fruit(request,slug):
    fruit = get_object_or_404(Fruit,slug = slug)
    form = FruitForm(instance = fruit)

    if request.method == "POST":
        form = FruitForm(request.POST,request.FILES,instance = fruit)
        if form.is_valid():
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                instance = form.save(commit=False)
                file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
                image_url = default_storage.url(file_name)
                instance.image = image_url
                instance.save()
            else:
                form.save()
            return redirect("/profile")
        else:
            messages.add_message(request,messages.WARNING,form.errors)

    context = {
        'form':form,
        "edit":True,
        'current_image': fruit.image
    }

    return render(request,"create_blog.html",context)

def edit_vegetable(request,slug):
    vegetable = get_object_or_404(Vegetable,slug = slug)
    form = VegetableForm(instance = vegetable)

    if request.method == "POST":
        form = VegetableForm(request.POST,request.FILES,instance = vegetable)
        if form.is_valid():
            image_file = form.cleaned_data.get('image_file')
            if image_file:
                instance = form.save(commit=False)
                file_name = default_storage.save(image_file.name, ContentFile(image_file.read()))
                image_url = default_storage.url(file_name)
                instance.image = image_url
                instance.save()
            else:
                form.save()
            return redirect("/profile")
        else:
            messages.add_message(request,messages.WARNING,form.errors)

    context = {
        'form':form,
        "edit":True,
        'current_image': vegetable.image
    }

    return render(request,"create_blog.html",context)

def upload_file(request):
    if request.method == "POST":
        print('hiii hitler')
        form = UploadFileForm(request.POST, request.FILES)
        allow_all_file_types = getattr(settings, "CKEDITOR_5_ALLOW_ALL_FILE_TYPES", False)

        if not allow_all_file_types:
            try:
                image_verify(request.FILES['upload'])
            except NoImageException as ex:
                return JsonResponse({"error": {"message": f"{ex}"}}, status=400)
        if form.is_valid():
            url = handle_uploaded_file(request.FILES["upload"])
            return JsonResponse({"url": url})
    raise Http404(("Page not found."))

def delete_meal(request,slug):
    url = request.META.get('HTTP_REFERER')
    meal = get_object_or_404(Meal,slug = slug)
    meal.delete()
    return redirect(url)

def delete_fruit(request,slug):
    url = request.META.get('HTTP_REFERER')
    meal = get_object_or_404(Fruit,slug = slug)
    meal.delete()
    return redirect(url)

def delete_vegetable(request,slug):
    url = request.META.get('HTTP_REFERER')
    meal = get_object_or_404(Vegetable,slug = slug)
    meal.delete()
    return redirect(url)

def change_meal_status(request,slug):
    url = request.META.get('HTTP_REFERER')
    meal = get_object_or_404(Meal,slug = slug)
    if meal.status == Meal.Status.PUBLISHED:
        meal.status = Meal.Status.DRAFT
    else:
        meal.status = Meal.Status.PUBLISHED
    messages.add_message(request,messages.SUCCESS,"Status updated")
    meal.save()
    return redirect(url)

def change_vegetable_status(request,slug):
    url = request.META.get('HTTP_REFERER')
    vegetable = get_object_or_404(Vegetable,slug = slug)
    if vegetable.status == Vegetable.Status.PUBLISHED:
        vegetable.status = Vegetable.Status.DRAFT
    else:
        vegetable.status = Vegetable.Status.PUBLISHED
    messages.add_message(request,messages.SUCCESS,"Status updated")
    vegetable.save()
    return redirect(url)

def change_fruit_status(request,slug):
    url = request.META.get('HTTP_REFERER')
    fruit = get_object_or_404(Fruit,slug = slug)
    if fruit.status == Fruit.Status.PUBLISHED:
        fruit.status = Fruit.Status.DRAFT
    else:
        fruit.status = Fruit.Status.PUBLISHED
    messages.add_message(request,messages.SUCCESS,"Status updated")
    fruit.save()
    return redirect(url)

