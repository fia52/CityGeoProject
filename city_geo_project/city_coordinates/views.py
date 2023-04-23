from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from .get_city_coords import get_city_coords
from .models import City
from .serializers import CitySerializer


class CityApiView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def perform_create(self, serializer):
        try:
            location = get_city_coords(serializer.initial_data["name"])
        except:
            raise ValidationError()

        serializer.save(location=location)

    def get_queryset(self):
        queryset = super().get_queryset()
        latitude = self.request.query_params.get("lat")
        longitude = self.request.query_params.get("lng")

        if latitude and longitude:
            point = Point(x=float(latitude), y=float(longitude), srid=4326)
            queryset = queryset.annotate(distance=Distance("location", point)).order_by("distance")[:2]

        return queryset


class RetrieveDestroyCityApiView(generics.RetrieveDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "name"
