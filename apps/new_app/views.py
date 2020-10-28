from django.shortcuts import render, HttpResponse, get_object_or_404	
from .models import Location,House

def houseindex(request):
    return render(request, "new_app/index.html")

def houselistings(request, location_slug=None):
    location_page = None 
    houses_list = None
    if location_slug!= None:
        location_page = get_object_or_404(Location, slug=location_slug)
        houses_list = House.objects.filter(location=location_page, available=True)
    else:
        houses_list = House.objects.all().filter(available=True)

    return render(request, 'new_app/listings.html', {'location':location_page,'houses':houses_list})

def housedetails(request, location_slug, house_slug):
    try:
        house = House.objects.get(location__slug=location_slug, slug=house_slug)
    except Exception as e:
        raise e
    return render(request, 'new_app/house.html', {'house':house})
