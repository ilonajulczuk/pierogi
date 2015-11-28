from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models import EmailField


class Company(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.name


class FoodUserManager(BaseUserManager):
    def create_user(self, email, password, company, **kwargs):
        if not email:
            raise ValueError('Email address must be specified')

        user = self.model(email=self.normalize_email(email), company=company, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(email, password, company=Company.objects.first(), **kwargs)
        user.is_admin = True
        user.save(using=self._db)
        return user

    def __str__(self):
        return self.name


class FoodUser(AbstractBaseUser):
    email = EmailField(verbose_name='Email address', max_length=255, unique=True)
    name = models.CharField(max_length=255, null=True, blank=True, default=None)
    company = models.ForeignKey(Company)
    should_be_notified = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = FoodUserManager()


class Food(models.Model):
    name = models.CharField(max_length=128)
    place = models.ForeignKey(Place, null=True, blank=True)
    # only for test null=True
    giver = models.ForeignKey(FoodUser, related_name='food_given', null=True, blank=True)
    taker = models.ForeignKey(FoodUser, null=True, related_name='food_taken', blank=True)
    image = models.ImageField(upload_to='', max_length=254, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from notifications import notify
        notify.food_available(self)
