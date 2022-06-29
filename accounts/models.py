from operator import truediv
from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.core.validators import validate_email
from painless.models.validations import validate_phone_number
from painless.models.mixins import TimeStampedMixin



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
            

        return self._create_user(email, password, **extra_fields)


class City(TimeStampedMixin):
   
    title = models.CharField(max_length = 64, unique = True, verbose_name = _('title'), null = True, blank = True)
    province = models.ForeignKey('Province', on_delete = models.CASCADE, related_name='provice')

    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.title


class Province(TimeStampedMixin):

    title = models.CharField(max_length = 64, null = True, blank = True)

    class Meta:
        verbose_name = _('Province')
        verbose_name_plural = _('Provinces')

    def __str__(self):
        return self.title


class User(AbstractUser, PermissionsMixin,TimeStampedMixin):
    date_joined = None
    published_at = None
    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_TRANS = 3
    GENDER_CHOICES = [
        (GENDER_MALE, _("Male")),
        (GENDER_FEMALE, _("Female")),
        (GENDER_TRANS, _("Trans")),
    ]


    VALIDATION_TYPE_MOBILE = 1
    VALIDATION_TYPE_EMAIL = 2
    VALIDATION_TYPE_CHOICES = [
        (VALIDATION_TYPE_MOBILE, _("Mobile")),
        (VALIDATION_TYPE_EMAIL, _("Email")),
    ]


    email = models.EmailField(unique=True, validators = [validate_email])
    mobile_number = models.CharField(max_length = 12, validators=[
           validate_phone_number
        ])
  
    profile_image_url = models.ImageField(upload_to="avatar/%Y/%m/%d", null=True, blank=True)
    varification_type = models.PositiveSmallIntegerField(choices=VALIDATION_TYPE_CHOICES, null=True, blank=True, default=1)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True, blank=True, default=1)
    job = models.CharField(max_length=128, blank = True, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE,null = True, blank = True)
    address = models.CharField(max_length=228, blank = True, null = True)
    birth_date = models.DateField(null=True, blank=True)
    level = models.IntegerField(blank = True, null = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


