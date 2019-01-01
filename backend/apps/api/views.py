import logging
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from apps.api.serializers import QuestionSerializer, QuestionAnswerSerializer
from .quiz import Quiz, QuestionDoesNotExists

logger = logging.getLogger(__name__)


class QuestionsViewSet(ViewSet):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.objects = Quiz()

    def retrieve(self, request, **kwargs):
        try:
            question = self.objects.get_question(int(kwargs['pk']))
        except QuestionDoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(data=QuestionSerializer(instance=question).data)

    @action(detail=False)
    def first(self, request):
        question = self.objects.get_initial_question()
        return Response(data=QuestionSerializer(instance=question).data)

    @action(detail=False, methods=['post'])
    def finish_quiz(self, request: Request):
        serializer = QuestionAnswerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            q_a_list = [(item['question_id'], item['answer_id']) for item in serializer.data]
            history = self.objects.construct_history(q_a_list)
            logger.info(history)
            return Response()
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
