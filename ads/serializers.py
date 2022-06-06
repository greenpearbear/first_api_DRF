from .models import Announcement, Categories, Selection
from rest_framework import serializers
from .validators import no_true_in_published


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = "__all__"


class AnnouncementSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    is_published = serializers.CharField(validators=[no_true_in_published])

    class Meta:
        model = Announcement
        fields = "__all__"


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"