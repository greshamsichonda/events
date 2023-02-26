from django.contrib import admin
from . models import Funs, Venues, Events

# Register your models here.
admin.site.register(Funs)
admin.site.register(Venues)
#admin.site.register(Events)
@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display=('name', 'venue', 'manager', 'event_date')
    search_fields=('name',)
    list_filter=('event_date',)

