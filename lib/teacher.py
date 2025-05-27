#!/usr/bin/env python

from user import User

import random

from random import randint
from user import User

class Teacher(User):
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = self.knowledge.copy()

    def teach(self):
        random_index = randint(0, len(self.knowledge) - 1)  
        return self.knowledge[random_index]