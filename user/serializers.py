from .models import Location, Author
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = Author
        fields = "__all__"

    def create(self, validated_data):
        user = Author.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()

        return user
