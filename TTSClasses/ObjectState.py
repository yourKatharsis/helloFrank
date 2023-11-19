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

    def __init__(self, contained_objects: List[ContainedObject], deck_ids: List[int],
                 custom_deck: Dict[str, CustomDeck], transform: Transform = Transform()):
        self.name = "DeckCustom"
        self.contained_objects = contained_objects
        self.deck_ids = deck_ids
        self.custom_deck = custom_deck
        self.transform = transform

    def to_dict(self) -> dict:
        return {
            "Name": self.name,
            "ContainedObjects": [x.to_dict() for x in self.contained_objects],
            "DeckIDs": self.deck_ids,
            "CustomDeck": {key: value.to_dict() for key, value in self.custom_deck.items()},
            "Transform": self.transform.to_dict()
        }
