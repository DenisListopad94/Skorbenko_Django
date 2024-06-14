from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator

from .validators import age_validator

from django.db import models


# Create your models here.
class User(models.Model):
    SEX_PERSON = {
        "m": "male",
        "f": "female",
    }
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    age = models.PositiveIntegerField(validators=[age_validator])
    city = models.CharField(max_length=30, null=False)
    sex = models.CharField(max_length=1, choices=SEX_PERSON)
    email = models.EmailField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_hobbies = models.ManyToManyField(to="Hobby")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Person(User):
    guest_rating = models.PositiveIntegerField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=["guest_rating"], name="guest_rating_idx"),
        ]


class HotelOwner(User):
    owner_exp_status = models.PositiveIntegerField(null=True)


class Hobby(models.Model):
    name = models.CharField(max_length=100)
    experience = models.IntegerField(null=True)
    owners = models.ManyToManyField(
        to="User",
        related_name="hobbies"
    )

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    photo = models.ImageField(null=True, blank=True)
    id_card_number = models.IntegerField(null=True)
    serial = models.CharField(max_length=30, null=True)
    persons = models.OneToOneField(to="User", on_delete=models.CASCADE, related_name="profile", null=True)

    def __str__(self):
        return f'{self.persons} - {self.serial} - {self.id_card_number}'


class BookInfo(models.Model):
    book_time = models.DateTimeField(auto_now_add=True)
    detail = models.CharField(max_length=200, null=True)
    persons = models.ForeignKey(to="Person", on_delete=models.SET_NULL, null=True)
    hotels = models.ForeignKey(to="Hotels", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.detail}, Person - {self.persons}, {self.book_time}//{self.hotels}'


class Hotels(models.Model):
    name = models.CharField(max_length=50)
    stars = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    rating = models.FloatField(null=True)
    owners = models.ForeignKey(to="HotelOwner", on_delete=models.SET_NULL, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["name"], name="name_idx"),
        ]

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    comment = models.CharField(max_length=100)
    time_comment = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class HotelsComment(Comment):
    hotel_rating = models.PositiveIntegerField(null=True)
    persons = models.ForeignKey(to="Person", on_delete=models.CASCADE, null=True, related_name="hotel_comments")
    hotels = models.ForeignKey(to="Hotels", on_delete=models.SET_NULL, null=True, related_name="hotel_comments")

    def __str__(self):
        return f'{self.comment}'


class PersonComment(Comment):
    person_rating = models.PositiveIntegerField(null=True)
    persons = models.ManyToManyField(to="Person")
    hotels = models.ForeignKey(to="Hotels", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.comment}'


class Room(models.Model):
    hotel = models.ForeignKey(Hotels, related_name='rooms', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(validators=[
        MaxValueValidator(1000),
        MinValueValidator(1)
    ])
    is_booked = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='booked_rooms', on_delete=models.SET_NULL, null=True, blank=True)


class Booking(models.Model):
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    customer_full_name = models.CharField(max_length=255)


class Feedback(models.Model):
    user = models.ForeignKey(User, related_name='users_feedback', on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=100)
