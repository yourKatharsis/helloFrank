class Transform:
    posX: int
    posY: int
    posZ: int
    rotX: int
    rotY: int
    rotZ: int
    scaleX: int
    scaleY: int
    scaleZ: int

    # noinspection PyPep8Naming
    def __init__(self, posX: int = 0, posY: int = 1, posZ: int = 0,
                 rotX: int = 0, rotY: int = 180, rotZ: int = 180,
                 scaleX: int = 1, scaleY: int = 1, scaleZ: int = 1):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.rotX = rotX
        self.rotY = rotY
        self.rotZ = rotZ
        self.scaleX = scaleX
        self.scaleY = scaleY
        self.scaleZ = scaleZ

    def to_dict(self) -> dict:
        return {
            "posX": self.posX,
            "posY": self.posY,
            "posZ": self.posZ,
            "rotX": self.rotX,
            "rotY": self.rotY,
            "rotZ": self.rotZ,
            "scaleX": self.scaleX,
            "scaleY": self.scaleY,
            "scaleZ": self.scaleZ
        }
