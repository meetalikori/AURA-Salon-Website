from django.contrib import admin
from .models import Appointment, Service, Gallery, Team, Contact, Testimonial

admin.site.register(Appointment)
admin.site.register(Gallery)
admin.site.register(Service)
admin.site.register(Team)
admin.site.register(Contact)
admin.site.register(Testimonial)