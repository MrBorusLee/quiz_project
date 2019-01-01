from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import pytest

from apps.api.quiz import Quiz


def test_quiz():
    normal_path = Quiz.FILE_PATH
    Quiz.FILE_PATH = '/fake/path/'
    q = Quiz()
    assert not q._data
    Quiz.FILE_PATH = normal_path


def test_get_first_question():
    client = APIClient()
    response = client.get(reverse('question-first'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.parametrize('question_id, status_code', [
    (1, status.HTTP_200_OK),
    (2, status.HTTP_200_OK),
    (0, status.HTTP_404_NOT_FOUND),
])
def test_get_question(question_id, status_code):
    client = APIClient()
    response = client.get(reverse('question-detail', kwargs={'pk': question_id}))
    assert response.status_code == status_code


@pytest.mark.parametrize('data, status_code', [
    ([{'question_id': 1, 'answer_id': 2}], status.HTTP_200_OK),
    ([{'answer_id': 2}], status.HTTP_400_BAD_REQUEST),
])
def test_finish_quiz(data, status_code):
    client = APIClient()
    response = client.post(reverse('question-finish-quiz'), data=data, format='json')
    assert response.status_code == status_code
