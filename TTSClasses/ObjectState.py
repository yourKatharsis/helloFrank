from typing import Dict, Optional, List

from TTSClasses.AltLookAngle import AltLookAngle
from TTSClasses.ColorDiffuse import ColorDiffuse
from TTSClasses.ContainedObject import ContainedObject
from TTSClasses.CustomDeck import CustomDeck


class ObjectState:
    guid: str
    name: str
    transform: Dict[str, float]
    nickname: str
    description: str
    gm_notes: str
    alt_look_angle: AltLookAngle
    color_diffuse: ColorDiffuse
    layout_group_sort_index: int
    value: int
    locked: bool
    grid: bool
    snap: bool
    ignore_fo_w: bool
    measure_movement: bool
    drag_selectable: bool
    autoraise: bool
    sticky: bool
    tooltip: bool
    grid_projection: bool
    hide_when_face_down: bool
    hands: bool
    sideways_card: bool
    deck_i_ds: Optional[List[int]]
    custom_deck: Dict[str, CustomDeck]
    lua_script: str
    lua_script_state: str
    xml_ui: str
    contained_objects: Optional[List[ContainedObject]]
    card_id: Optional[int]

    def __init__(self, guid: str, name: str, transform: Dict[str, float], nickname: str, description: str,
                 gm_notes: str, alt_look_angle: AltLookAngle, color_diffuse: ColorDiffuse, layout_group_sort_index: int,
                 value: int, locked: bool, grid: bool, snap: bool, ignore_fo_w: bool, measure_movement: bool,
                 drag_selectable: bool, autoraise: bool, sticky: bool, tooltip: bool, grid_projection: bool,
                 hide_when_face_down: bool, hands: bool, sideways_card: bool, deck_i_ds: Optional[List[int]],
                 custom_deck: Dict[str, CustomDeck], lua_script: str, lua_script_state: str, xml_ui: str,
                 contained_objects: Optional[List[ContainedObject]], card_id: Optional[int]) -> None:
        self.guid = guid
        self.name = name
        self.transform = transform
        self.nickname = nickname
        self.description = description
        self.gm_notes = gm_notes
        self.alt_look_angle = alt_look_angle
        self.color_diffuse = color_diffuse
        self.layout_group_sort_index = layout_group_sort_index
        self.value = value
        self.locked = locked
        self.grid = grid
        self.snap = snap
        self.ignore_fo_w = ignore_fo_w
        self.measure_movement = measure_movement
        self.drag_selectable = drag_selectable
        self.autoraise = autoraise
        self.sticky = sticky
        self.tooltip = tooltip
        self.grid_projection = grid_projection
        self.hide_when_face_down = hide_when_face_down
        self.hands = hands
        self.sideways_card = sideways_card
        self.deck_i_ds = deck_i_ds
        self.custom_deck = custom_deck
        self.lua_script = lua_script
        self.lua_script_state = lua_script_state
        self.xml_ui = xml_ui
        self.contained_objects = contained_objects
        self.card_id = card_id
