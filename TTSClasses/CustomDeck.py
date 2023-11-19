class CustomDeck:
    face_url: str
    back_url: str
    num_height: int
    num_width: int
    back_is_hidden: bool
    unique_back: bool

    def __init__(self, face_url: str, back_url: str,
                 num_height: int = 1, num_width: int = 1,
                 back_is_hidden: bool = True, unique_back: bool = False):
        self.face_url = face_url
        self.back_url = back_url
        self.num_height = num_height
        self.num_width = num_width
        self.back_is_hidden = back_is_hidden
        self.unique_back = unique_back

    def to_dict(self) -> dict:
        return {
            "face_url": self.face_url,
            "back_url": self.back_url,
            "num_height": self.num_height,
            "num_width": self.num_width,
            "back_is_hidden": self.back_is_hidden
        }
