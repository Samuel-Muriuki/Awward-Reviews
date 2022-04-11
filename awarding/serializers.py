from rest_framework import serializers
from .models import Profile, Post, Rating

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title', 'photo','description', 'url', 'technologies_used', 'upload_date', 'user']
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','name', 'profile_pic', 'bio', 'phone_number']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','user', 'post', 'rating']