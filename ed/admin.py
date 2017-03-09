from django.contrib import admin

# Register your models here.
from ed.models import Contractor, Contract, Item, Disclosure

admin.site.register(Contractor)
admin.site.register(Contract)
admin.site.register(Item)
admin.site.register(Disclosure)

#admin.site.register(Choice)