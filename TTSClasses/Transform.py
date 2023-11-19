class Transform:
    pos_x: int
    pos_y: int
    pos_z: int
    rot_x: int
    rot_y: int
    rot_z: int
    scale_x: int
    scale_y: int
    scale_z: int

    def __init__(self, pos_x: int = 0, pos_y: int = 0, pos_z: int = 0,
                 rot_x: int = 0, rot_y: int = 180, rot_z: int = 180,
                 scale_x: int = 1, scale_y: int = 1, scale_z: int = 1):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.rot_x = rot_x
        self.rot_y = rot_y
        self.rot_z = rot_z
        self.scale_x = scale_x
        self.scale_y = scale_y
        self.scale_z = scale_z

    def to_dict(self) -> dict:
        return {
            "posX": self.pos_x,
            "posY": self.pos_y,
            "posZ": self.pos_z,
            "rotX": self.rot_x,
            "rotY": self.rot_y,
            "rotZ": self.rot_z,
            "scaleX": self.scale_x,
            "scaleY": self.scale_y,
            "scaleZ": self.scale_z
        }
