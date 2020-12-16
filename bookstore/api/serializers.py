from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from api.models import Author, Book, Customer, Order


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(CustomerSerializer, self).create(validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"