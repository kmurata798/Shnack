from rest_framework.serializers import ModelSerializer

from meals.models import Meals

class MealsSerializer(ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'