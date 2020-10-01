from django.contrib import admin
from APPtest.models import Item , CharityRegistration \
    ,UserRegistration,OrderedItem
# Register your models here.
admin.site.register(Item,)
admin.site.register(CharityRegistration,)
admin.site.register(UserRegistration,)
admin.site.register(OrderedItem,)