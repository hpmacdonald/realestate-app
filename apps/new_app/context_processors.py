from .models import Location

def location_links(request):
    l_links = Location.objects.all()
    return dict(l_links=l_links)