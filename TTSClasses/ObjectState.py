from typing import Dict, List

from TTSClasses.ContainedObject import ContainedObject
from TTSClasses.CustomDeck import CustomDeck
from TTSClasses.Transform import Transform


class ObjectState:
    name: str
    contained_objects: List[ContainedObject]
    deck_ids: List[int]
    custom_deck: Dict[str, CustomDeck]
    transform:  Transform

    def __init__(self, name: str, contained_objects: List[ContainedObject], deck_ids: List[int],
                 custom_deck: Dict[str, CustomDeck], transform: Transform) -> None:
        self.name = name
        self.contained_objects = contained_objects
        self.deck_ids = deck_ids
        self.custom_deck = custom_deck
        self.transform = transform

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "contained_objects": self.contained_objects,
            "deck_ids": self.deck_ids,
            "custom_deck": self.custom_deck,
            "transform": self.transform
        }
