from django.db.models import fields
from rest_framework import serializers
# from django.conf.urls import include, url 
# from  django.contrib.auth.models import User, models

from .models import BlogPost



class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model=BlogPost
        fields ='__all__'
        lookup_field = 'slug' 