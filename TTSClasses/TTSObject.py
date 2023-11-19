from typing import List

from TTSClasses.ObjectState import ObjectState


class TTSObject:
    object_states: List[ObjectState]

    def __init__(self, object_states: List[ObjectState]) -> None:
        self.object_states = object_states

    def to_dict(self) -> dict:
        return {
            "ObjectStates": [x.to_dict() for x in self.object_states]
        }
