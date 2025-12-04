
from typing import List

from periods.phase import Phase


class Activity:
    def __init__(self, name: str, type: str, description: str, phase: List[Phase], emoji: str, article: str):
        self.name = name
        self.description = description
        self.type = type
        self.phase = phase
        self.emoji = emoji
        self.article = article
