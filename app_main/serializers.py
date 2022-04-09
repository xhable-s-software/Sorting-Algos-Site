from django.contrib.auth.models import User, Group
from .models import Algorithm
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AlgorithmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Algorithm
        fields = ['url', 'name', 'type', 'complexity', 'sort_percentage',
                  'item_count', 'time', 'iter_count', 'replacements_count',
                  'code_lines_count', 'code', 'description']
