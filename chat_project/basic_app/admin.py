from django.contrib import admin
from basic_app.models import MyGroup,MyPost
from basic_app import forms
# Register your models here.

admin.site.register(MyGroup)
admin.site.register(MyPost)

