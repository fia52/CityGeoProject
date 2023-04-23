from rest_framework import serializers

from .models import City


class CitySerializer(serializers.ModelSerializer):
    distance = serializers.DecimalField(
        source="distance.km",
        max_digits=10,
        decimal_places=2,
        required=False,
        read_only=True,
    )

    class Meta:
        model = City
        fields = ("name", "location", "distance")
        read_only_fields = ("location",)
