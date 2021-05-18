from rest_framwork import serializers
from .models import quiz
class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields=('title','body','answer')