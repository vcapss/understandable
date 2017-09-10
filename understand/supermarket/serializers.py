from rest_framework import serializers

from supermarket.models import Supermarket


class SupermarketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Supermarket
        fields = '__all__'
