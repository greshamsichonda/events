from django import forms
from django.forms import ModelForm
from .models import Venues, Events

#venue form
class VenuesForm(forms.ModelForm):
    
    class Meta:
        model = Venues
        fields = ("name","address", "phone")
        #labels for venue form

        labels={
            'name': '',
            'address': '',
            'phone': '',

        }
        #widgets for venue form
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Name Of Venue'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Address'}),
            'phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Mobile Number'}),

        }
#event form
class EventForm(forms.ModelForm):
    
    class Meta:
        model = Events
        fields = ("name","event_date", "venue","manager","funs", "description", )
        #labels for venue form

        labels={
            'name': '',
            'event_date': '',
            'venue': 'Select Venue',
            'manager': 'Select Manager',
            'funs': '',
            'description': '',
           

        }
        #widgets for venue form
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter Event Name '}),
            'event_date': forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter Date '}),
            'venue': forms.Select(attrs={'class':'form-select', 'placeholder': 'Enter Venue'}),
            'manager': forms.Select(attrs={'class':'form-select', 'placeholder': 'Enter Manager Of The Event'}),
            'funs': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter funs'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Enter Decription'}),
        }        

