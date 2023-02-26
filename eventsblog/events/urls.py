
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('<int:year>/<str:month>', views.home, name='home-page'),
    path('events/', views.event_list, name='events-list'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('venues/', views.venues, name='venue-list'),
    path('show_venues/<venue_id>', views.show_venues, name='show-venue'),
    path('search_venue/', views.search_venue, name='search-venue'),
    path('update_venue/<venue_id>', views.update_venue, name='update-venue'),
    path('update_event/<event_id>', views.update_event, name='update-event'),
    path('delete_event/<event_id>', views.delete_event, name='delete-event'),
    path('add_event/', views.add_event, name='add-event'),
    path('venue_text/', views.venue_text, name='venue_text'),
]