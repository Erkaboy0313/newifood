from meal.models import Country,Region

def custom_context(request):

    custom_data = {
        'countries': Country.objects.all(),
        'regions': Region.objects.all()
    }
    return custom_data