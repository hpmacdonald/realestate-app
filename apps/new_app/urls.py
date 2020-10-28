from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'real_estate'

urlpatterns = [
    path('', views.houseindex, name='houseindex'),
    path('houselistings', views.houselistings, name='houselistings'),
    path('<slug:location_slug>/', views.houselistings, name='houses_by_category'),
    path('<slug:location_slug>/<slug:house_slug>/', views.housedetails, name='housedetails'),
    
]