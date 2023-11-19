from TTSClasses.Transform import Transform


class ContainedObject:
    card_id: int
    name: str
    nickname: str
    transform: Transform

    def __init__(self, card_id: int, nickname: str,
                 transform: Transform = Transform(), name: str = "Card"):
        self.card_id = card_id
        self.name = name
        self.nickname = nickname
        self.transform = transform

    def to_dict(self) -> dict:
        return {
            "CardID": self.card_id,
            "Name": self.name,
            "Nickname": self.nickname,
            "Transform": self.transform.to_dict()
        }
