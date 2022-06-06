from .models import Location, Author
from rest_framework import serializers
from .validators import no_children_on_site, no_rambler_on_my_site


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True)
    birth_date = serializers.DateField(validators=[no_children_on_site])
    email = serializers.EmailField(validators=[no_rambler_on_my_site()])

    class Meta:
        model = Author
        fields = "__all__"

    def create(self, validated_data):
        user = Author.objects.create(**validated_data)

        user.set_password(validated_data["password"])
        user.save()

        return user
