from django.contrib import admin
from booking.models import indexdb, nonsubscribdb, primedb, subscribdb

# Register your models here.
class indexAdmin(admin.ModelAdmin):
      admin.site.register(indexdb),
      admin.site.register(primedb),
      admin.site.register(subscribdb),
      admin.site.register(nonsubscribdb),