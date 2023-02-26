from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, Venues
from . forms import VenuesForm, EventForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.
def venue_text(request):
    response= HttpResponse(content_type='text/plain')
    response['Content-disposition']='attachment; filename=venues.txt'
#get all from the venue model
    venues= Venues.objects.all()  
    lines=[]
    for venue in venues:
        lines.append(f'{venue}\n')
    response.writelines(lines)
    return response


#generate text files

#add event
def add_event(request):
    submitted=False
    if request.method=="POST":
        form= EventForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form= EventForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'events/add_event.html',{
            'form': form,
            'submitted': submitted
            })
#updating events view function
def update_event(request, event_id): 
    event= Events.objects.get(pk=event_id)
    form= EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events-list')
        
    return render(request, 'events/update_event.html',{
            'event': event,
            'form': form,
         })  
#delete event
def delete_event(request, event_id):
    event = Events.objects.get(pk=event_id)   
    event.delete()
    return redirect('events-list')            
#add venue view
def add_venue(request):
    submitted=False
    if request.method=="POST":
        form= VenuesForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form= VenuesForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'events/add_venue.html',{
            'form': form,
            'submitted': submitted
            })
#venue data
def venues(request):
    venues= Venues.objects.all()
    return render(request, 'events/venue_list.html',{
        'venues': venues
    })
#display event data in the web browser
def event_list(request):
    event_list=Events.objects.all()
    return render(request, 'events/event_list.html',{
       'event_list': event_list
    })
#venue details
def show_venues(request, venue_id):
    show_venues=Venues.objects.get(pk=venue_id)  
    return render(request, 'events/show_venue.html',{
       'show_venues': show_venues
    })
#update venue data    
def update_venue(request, venue_id): 
    venues= Venues.objects.get(pk=venue_id)
    form= VenuesForm(request.POST or None, instance=venues)
    if form.is_valid():
      form.save()
      return redirect('venue-list')
    return render(request, 'events/update_venue.html',{
        'venues': venues,
        'form': form
    })  
#search venue view function    
def search_venue(request):
    if request.method == "POST":
        searched=request.POST['searched']
        venues=Venues.objects.filter(name__contains=searched)
        return render(request, 'events/search_venue.html',{
            'searched': searched,
            'venues': venues
        }) 
    else:
        return render(request, 'events/search_venue.html',{
        
     })
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name="john"  
    #converting month name to numbber
    month=month.title()
    month_number = list(calendar.month_name).index(month)
    month_number=int(month_number)
    #create an html calender
    cal= HTMLCalendar().formatmonth(year, month_number)
    #get current time
    now= datetime.now()
    current_year= now.year
    return render(request, 'events/home.html',{
    })