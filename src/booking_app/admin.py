from django.contrib import admin
from .models import Person, Profile, Hotels, HotelsComment, HotelOwner, Hobby, BookInfo, User, PersonComment

# Register your models here.
admin.site.register(Person)
admin.site.register(Profile)
admin.site.register(Hotels)
admin.site.register(HotelsComment)
admin.site.register(HotelOwner)
admin.site.register(Hobby)
admin.site.register(BookInfo)
admin.site.register(User)
admin.site.register(PersonComment)
