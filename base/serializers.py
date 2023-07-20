from rest_framework import serializers
from base.models import *


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class WeightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weighting
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=('animal', 'date'),
                message="Can't record more than one weighting per day"
            )
        ]
