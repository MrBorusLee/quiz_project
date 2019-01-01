from collections import namedtuple
import json
import os
import reprlib
from pathlib import Path

from django.conf import settings


class QuestionDoesNotExists(Exception):
    pass


Question = namedtuple('Question', ('id', 'question', 'answers'))
Answer = namedtuple('Answer', ('id', 'answer', 'next_question'))


class Quiz:
    """Wrapper to work with questions structure which is stored in {data_dir}/quiz.json file"""

    FILE_PATH = os.path.join(settings.DATA_DIR, 'quiz.json')
    _data = None

    def __init__(self):
        self._load_data()

    def __repr__(self):  # pragma: no cover
        return 'Quiz structure: ({})'.format(reprlib.repr(self._data))

    @classmethod
    def _load_data(cls):
        if cls._data:
            return

        if Path(cls.FILE_PATH).is_file():
            with open(cls.FILE_PATH) as f:
                raw_data = json.load(f)
                for q in raw_data:
                    q['answers'] = [Answer(**a) for a in q['answers']]
                data = [Question(**q) for q in raw_data]
        else:
            data = []

        cls._data = data

    def get_question(self, question_id: int=1) -> Question:
        try:
            return next(question for question in self._data if question.id == question_id)
        except StopIteration:
            raise QuestionDoesNotExists

    def get_initial_question(self):
        return self.get_question()

    def construct_history(self, question_answer_list: list):
        question_answer = []
        for qa in question_answer_list:
            q_id, a_id = qa
            question = self.get_question(q_id)
            answer = next(a.answer for a in question.answers if a.id == a_id)
            question_answer.append(f'{question.question}: {answer}')

        return ' -> '.join(question_answer)
