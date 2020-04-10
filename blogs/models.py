from django.db import models
import datetime
from datetime import datetime
from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from colorful.fields import RGBColorField
from django.urls import reverse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
class notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notify = RichTextUploadingField(null =True)
class blog(models.Model):
    title = RichTextUploadingField(blank=True, null=True, config_name='special')
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField( default=datetime.now())
    content =  RichTextUploadingField(blank=True, null=True)
    back =  RGBColorField(colors=['#003cb3', '#ff1a1a', '#00e600'], default='#003cb3')
    def __str__(self):
    	return str(self.id)
    class meta:
        get_latest_by = "pub_date"
class likes(models.Model):
    blog_id = models.ForeignKey(blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    def validate_unique(self, *args, **kwargs):
        super(likes, self).validate_unique(*args, **kwargs)

        if self.__class__.objects.\
                filter(blog_id=self.blog_id, user=self.user).\
                exists():
            raise ValidationError(
                message='likes with this (blog_id, user) already exists.',
                code='unique_together',
            )
class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null = True)
    description = models.TextField(null = True)
    country = models.CharField(max_length=200,null = True)
    address = models.TextField(null = True)
    phone_number = models.IntegerField(null = True)
    profile_pic = models.FileField(upload_to="profile_pictures",blank=True,null = True)
    def __str__(self):
    	return str(self.user)
def create_profile(sender, **kwargs):
    if kwargs['created']:
        userprofile = user_profile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

