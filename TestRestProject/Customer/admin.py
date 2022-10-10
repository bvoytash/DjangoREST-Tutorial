from django.contrib import admin

from TestRestProject.Customer.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Profession)
admin.site.register(DataSheet)
admin.site.register(Document)