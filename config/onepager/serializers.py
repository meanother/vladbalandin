from rest_framework import serializers

from .models import *


class ShortQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortQuestions
        fields = '__all__'


class PollQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollQuestions
        fields = '__all__'


class QuizQuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestions
        fields = '__all__'