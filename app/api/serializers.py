import datetime
from rest_framework import serializers
from .models import Photo
from .geolocation_services import get_geolocation


class StringListField(serializers.ListField):
    child = serializers.CharField()


class RetrievePhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ('id', 'picture', 'description',
                  'people_list', 'geolocation', 'upload_date')


class ListPhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = ("id", "picture")


class CreatePhotoSerializer(serializers.ModelSerializer):

    latitude = serializers.CharField(write_only=True, required=False)
    longitude = serializers.CharField(write_only=True, required=False)
    geolocation = serializers.CharField(read_only=True)
    upload_date = serializers.DateTimeField(default=datetime.datetime.now())
    people_list = serializers.ListField()

    class Meta:
        model = Photo
        fields = ('picture', 'latitude',
                  'longitude', 'description',
                  'people_list', 'upload_date', 'geolocation')

    def validate(self, attrs):
        try:
            float(attrs['latitude'])
        except ValueError:
            raise serializers.ValidationError({"latitude": "Incorrect value."})
        try:
            float(attrs['longitude'])
        except ValueError:
            raise serializers.ValidationError({"longitude": "Incorrect value."})
        return attrs

    def create(self, validated_data):
        photo = Photo.objects.create(
            user=self.context['request'].user,
            picture=validated_data['picture'],
            description=validated_data['description'],
            upload_date=validated_data['upload_date'],
            people_list=validated_data['people_list'][0].replace(" ", "").split(","),
            geolocation=get_geolocation(latitude=validated_data['latitude'],
                                        longitude=validated_data['longitude']),
        )
        return photo

