from rest_framework import serializers
from .models import (
    Location, Address, Company, User, Todo,
    Post, Comment,
    Album, Photo
)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('lat', 'lng')


class AddressSerializer(serializers.ModelSerializer):
    geo = LocationSerializer()

    class Meta:
        model = Address
        fields = ('street', 'suite', 'city', 'zipcode', 'geo')


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'catchPhrase', 'bs')


class UserSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    company = CompanySerializer()

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email', 'address', 'phone', 'website', 'company')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('userId', 'id', 'title', 'completed')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('userId', 'id', 'title', 'body')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('postId', 'id', 'name', 'email', 'body')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('userId', 'id', 'title')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('albumId', 'id', 'title', 'url', 'thumbnailUrl')