from django.db import models
from cloudinary.models import CloudinaryField
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

 
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):     
        return self.email

    @property
    def get_full_name(self):       
        return self.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Post(models.Model):
    #specifying post choices
    ITEM_CHOICES = (
        ("1", "Men's causual apparell"), 
        ("2", "Men's official apparell"), 
        ("3", "Men's sports apparell"), 
        ("4", "Men's casual shoes"), 
        ("5", "Men's official shoes"), 
        ("6", "Men's sports shoes"), 
        ("7", "Women's causual apparell"), 
        ("8", "Women's official apparell"), 
        ("9", "Women's sports apparell"), 
        ("10", "Women's casual shoes"), 
        ("11", "women's official shoes"), 
        ("12", "women's sports shoes"),
        ("13", "Kid's causual apparell"), 
        ("14", "Kid's official apparell"), 
        ("15", "Kid's sports apparell"), 
        ("16", "Kid's shoes"), 
        )
    Account = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    post_image =CloudinaryField('image',  null=True) 
    category = models.CharField( 
        max_length = 20, 
        choices = ITEM_CHOICES, 
        default = '1'
        )
    contact = models.IntegerField()
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return f' {self.name} Post'


    def create_post(self):
        self.save()

    def delete_post(self):
        self.delete()
                   
    @classmethod
    def find_post_by_id(cls,id):
        post_result = cls.objects.get(id=id)
        return post_result
 
    @classmethod
    def update_post(cls,current_value,new_value):
        fetched_object = cls.objects.filter(count=current_value).update(count=new_value)
        return fetched_object


    @classmethod
    def retrieve_all(cls):
        all_objects = Post.objects.all()
        for item in all_objects:
            return item
        




