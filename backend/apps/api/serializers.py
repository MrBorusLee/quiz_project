from rest_framework import serializers


class AnswerSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    answer = serializers.CharField()
    next_question = serializers.IntegerField()


class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    question = serializers.CharField()
    answers = AnswerSerializer(many=True)


class QuestionAnswerSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()
