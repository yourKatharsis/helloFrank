class CustomDeck:
    face_url: str
    back_url: str
    num_width: int
    num_height: int
    back_is_hidden: bool
    unique_back: bool
    type: int

    def __init__(self, face_url: str, back_url: str, num_width: int, num_height: int, back_is_hidden: bool,
                 unique_back: bool, type: int) -> None:
        self.face_url = face_url
        self.back_url = back_url
        self.num_width = num_width
        self.num_height = num_height
        self.back_is_hidden = back_is_hidden
        self.unique_back = unique_back
        self.type = type
