from rest_framework import serializers

from Frontend.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User;
        fields=('U_PH',)
