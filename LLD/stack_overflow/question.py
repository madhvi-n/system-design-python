from users import Member
from answer import Answer
from constants import QuestionStatus, QuestionClosingRemark
from question import Tag

from typing import List
import datetime


# todo: Abstract vote and comment class
# todo: flag question
class Question:
    def __init__(self, title: str, content: str, author: Member, question_status=QuestionStatus.OPEN) -> None:
        self.title = title
        self.content = content
        self.tags: List[Tag] = []
        self.answers: List[Answer] = []
        self.author = author
        self.date = datetime.datetime.now()
        self.question_status = question_status
        self.closing_remark = None
        self.bounty = None

    def add_bounty(self, bounty: Bounty):
        self.bounty = bounty

    def add_tags(self, tag: Tag) -> None:
        self.tags.append(tag)

    def update_status(self, question_status: QuestionStatus) -> None:
        self.question_status = question_status

    def update_closing_remark(self, question_closing_remark: QuestionClosingRemark) -> None:
        self.closing_remark = question_closing_remark

    def close_question(self) -> None:
        ...

    def delete_question(self) -> None:
        ...


class Tag:
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description


class Bounty:
    def __init__(self, points=10, expires_in_days: int = 1):
        self.points = points
        self.start_date = datetime.datetime.today()
        self.end_date = self.start_date + datetime.timedelta(days=expires_in_days)
