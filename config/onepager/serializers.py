from rest_framework import serializers

from .models import *


class ShortQuestionsSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ShortQuestions
        # lookup_field = 'slug'
        fields = '__all__'


class PollQuestionsSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = PollQuestions
        # lookup_field = 'slug'
        fields = '__all__'

# class PromiseListSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Promise
#         fields = '__all__'
