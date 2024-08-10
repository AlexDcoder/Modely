'''
    Defining questions for the context
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from unittest import result


class Item:
    def __init__(self, text: str, score: int = 0) -> None:
        self.text: str = text
        self.score: int = score

    def __repr__(self) -> str:
        return f'Item=(text: {self.text}; score: {self.score})'


class Question(ABC):
    '''
        Creating an abstract class for question
    '''

    def __init__(self, text: str, answer: Item | None = None) -> None:
        self.text: str = text
        self.items: list[Item] = []
        self.answer = answer

    @abstractmethod
    def add_item(self, text: str):
        pass


class MultipleChoiceQuestion(Question):
    def add_item(self, text: str):
        if self.answer is not None:
            if text is self.answer.text:
                self.items.append(Item(text, 10))
            else:
                self.items.append(Item(text))


class TrueOrFalseQuestion(Question):
    def add_item(self, text: str):
        if self.answer is not None:
            if text is self.answer.text:
                self.items.append(Item(text, 1))
            else:
                self.items.append(Item(text))


class Questionnaire:
    def __init__(
            self,
            multiple_choice_qtd: int = 5,
            true_false_qtd: int = 5) -> None:

        self.multiple_choice_qtd = multiple_choice_qtd
        self.true_false_qtd = true_false_qtd
        self.questions: list[Question] = []
        self.result: int = 0

    def generate_multiple_choice_questions(self, question_data):
        for _ in range(self.multiple_choice_qtd):
            ...
        return

    def generate_true_or_false_questions(self, question_data):
        for _ in range(self.true_false_qtd):
            ...
        return

    def choose_option(self, option: str):
        ...

    def total_points(self):
        return result
