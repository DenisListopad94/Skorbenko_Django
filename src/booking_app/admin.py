from django.contrib import admin
from .models import Person, Profile, Hotels, HotelsComment, HotelOwner, Hobby, BookInfo, User, PersonComment
from django.utils.safestring import mark_safe


class HotelsCommentInline(admin.TabularInline):
    model = HotelsComment


class HotelsInline(admin.TabularInline):
    model = BookInfo


class PersonCommentInline(admin.TabularInline):
    model = PersonComment.persons.through


class HobbyInline(admin.TabularInline):
    model = Hobby.owners.through


@admin.display(description='photo')
def get_html_photo(objects):
    if objects.photo:
        return mark_safe(f'<img src={objects.photo.url} width=50>')


class UserAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "age", "get_html_photo"]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "age", "sex"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["city", "email"],
            },
        ),
    ]
    search_fields = ["first_name", "last_name"]
    search_help_text = "Поиск осуществлятся по имени и фамилии, а также email"
    list_editable = ["age"]
    list_filter = ["last_name", "age"]
    inlines = [
        HobbyInline,
    ]


class PersonAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "age"]
    fieldsets = [
        (
            None,
            {
                "fields": ["first_name", "last_name", "age", "sex"],
            },
        ),
        (
            "Advanced options",
            {
                "classes": ["collapse"],
                "fields": ["city", "email"],
            },
        ),
    ]
    search_fields = ["first_name", "last_name"]
    search_help_text = "Поиск осуществлятся по имени и фамилии, а также email"
    list_editable = ["age"]
    list_filter = ["last_name", "age"]
    inlines = [
        HotelsCommentInline,
        PersonCommentInline,
    ]


class HobbyAdmin(admin.ModelAdmin):
    list_display = ["name", "experience"]
    inlines = [
        HobbyInline,
    ]


class HotelsAdmin(admin.ModelAdmin):
    list_display = ["name", "stars", "rating"]
    inlines = [
        HotelsInline,
    ]


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
