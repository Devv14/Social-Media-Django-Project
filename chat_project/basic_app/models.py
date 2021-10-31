from django.db import models
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse
from django.utils import timezone
# Create your models here.

# to override save method in model

# auth.models.user comes with attributes like first name, last name, email, username etc 
class User(auth.models.User,LoginRequiredMixin):

    def __str__(self):
        return "@{}".format(self.username)

    

class MyGroup(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length=256)
    member_count = models.PositiveIntegerField(default=0)
    post_count = models.PositiveIntegerField(default=0)
    join_click = models.BooleanField(default=False)
    add_string = models.CharField(max_length=1024,default=".")
    remove_string = models.CharField(max_length=1024,default=".")

    def __str__(self):
        return self.name

    # ASSOCIATED WITH CREATE VIEW
    def get_absolute_url(self):
        return reverse("basic_app:join",kwargs={"pk": self.pk})
    
    def on_click(self):
        self.join_click = True
        self.save()

    def return_click(self):
        self.join_click = False
        self.save()

class MyPost(models.Model):
    mssg = models.CharField(max_length=512)
    group = models.ForeignKey(MyGroup,related_name='posts',on_delete=models.CASCADE)
    curr_user = models.CharField(max_length=256)
    published_date = models.DateTimeField(default=timezone.now,blank=True)
    created_by = models.CharField(max_length=100,default=",")

    # for descending order of date time
    class Meta:
        ordering = ('-published_date',)

    def __str__(self):
        return self.mssg

# ONLY WORKS FOR CREATE VIEW
    def get_absolute_url(self):
        return reverse('basic_app:nondisplaysetup',kwargs={"pk": self.pk})



