from django.contrib import admin
from .models import advertiser, publiser, contactus, SavLoc, advRequest


@admin.register(advertiser)
class AdvertiserAdmin(admin.ModelAdmin):
    list_display = ('adverid', 'fname', 'lname', 'gender', 'emailid', 'role')
    search_fields = ('fname', 'lname', 'emailid')


@admin.register(publiser)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('pubid', 'fname', 'lname', 'cname', 'emailid', 'role')
    search_fields = ('fname', 'lname', 'cname')


@admin.register(contactus)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'emailid', 'monumber')
    search_fields = ('fname', 'lname', 'emailid')


@admin.register(SavLoc)
class SavLocAdmin(admin.ModelAdmin):
    list_display = ('locid', 'locname', 'city', 'adtype', 'advprice')
    search_fields = ('locname', 'city', 'pcname')
    list_filter = ('adtype', 'city')


@admin.register(advRequest)
class AdvRequestAdmin(admin.ModelAdmin):
    list_display = ('advrequestid', 'locaddress', 'city', 'adtype', 'starttime', 'lastdate')
    search_fields = ('city', 'adtype', 'fname')
    list_filter = ('city', 'adtype')
