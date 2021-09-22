from rest_framework import serializers
from .models import Interestrate

class InterestrateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interestrate
        fields = ('pk','rate_date', 'rate_value')