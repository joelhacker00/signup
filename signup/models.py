from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import gettext_lazy as _


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    class GENDER_(models.TextChoices):
        MALE = 'MA', _('Male')
        FEMALE = 'FA', _('Female')
        OTHER = 'OT', _('Other')
    
    class LOCATION_(models.TextChoices):
        STOCKHOLM = 'ST', _('STOCKHOLM')
        GOTHENBURG = 'GO', _('GOTHENBURG')
        UPPSALA = 'UP', _('UPPSALA')
        MALMÖ = 'MA', _('MALMÖ')
    
    gender = models.CharField(
        max_length=2,
        choices=GENDER_.choices,
        default='Choose Gender',
        )
    location = models.CharField(
        max_length=2,
        choices=LOCATION_.choices,
        default='Choose Location',
        )
    profilepic = models.ImageField(blank=True)
    bio = models.CharField(
        max_length=500,
        blank=True
        )

    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin



































# from django.db import models
# from django.utils import timezone
# from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# class CustomAccountManager(BaseUserManager):

#     def create_superuser(self, email, first_name, last_name, password, **other_fields):

#         other_fields.setdefault('is_staff', True)
#         other_fields.setdefault('is_superuser', True)
#         other_fields.setdefault('is_active', True)

#         if other_fields.get('is_staff') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_staff=True.')
#         if other_fields.get('is_superuser') is not True:
#             raise ValueError(
#                 'Superuser must be assigned to is_superuser=True.')

#         return self.create_user(email, first_name, last_name, password, **other_fields)

#     def create_user(self, email, first_name, last_name, password, **other_fields):

#         if not email:
#             raise ValueError(_('You must provide an email address'))

#         email = self.normalize_email(email)
#         user = self.model(email=email,
#                           first_name=first_name, 
#                           last_name=last_name, 
#                           **other_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


# class NewUser(AbstractBaseUser, PermissionsMixin):

#     class GENDER_(models.TextChoices):
#         MALE = 'MA', _('Male')
#         FEMALE = 'FA', _('Female')
#         OTHER = 'OT', _('Other')
    
#     class LOCATION_(models.TextChoices):
#         STOCKHOLM = 'ST', _('STOCKHOLM')
#         GOTHENBURG = 'GO', _('GOTHENBURG')
#         UPPSALA = 'UP', _('UPPSALA')
#         MALMÖ = 'MA', _('MALMÖ')



#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=50,
#         unique=True)

    
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
    
    
#     gender = models.CharField(
#         max_length=2,
#         choices=GENDER_.choices,
#         default='Choose Gender',
#         )
#     location = models.CharField(
#         max_length=2,
#         choices=LOCATION_.choices,
#         default='Choose Location',
#         )
#     profilepic = models.ImageField(blank=True)
#     bio = models.CharField(
#         max_length=500,
#         blank=True
#         )
#     start_date = models.DateTimeField(default=timezone.now)

#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=False)

#     objects = CustomAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['email', 'first_name','last_name','gender','location']

#     def __str__(self):
#         return self.email