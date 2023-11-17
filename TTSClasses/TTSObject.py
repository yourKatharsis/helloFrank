from typing import List, Any

from TTSClasses.ObjectState import ObjectState
from TTSClasses.TabStates import TabStates


class TTSObject:
    save_name: str
    date: str
    version_number: str
    game_mode: str
    game_type: str
    game_complexity: str
    tags: List[Any]
    gravity: float
    play_area: float
    table: str
    sky: str
    note: str
    tab_states: TabStates
    lua_script: str
    lua_script_state: str
    xml_ui: str
    object_states: List[ObjectState]

    def __init__(self, save_name: str, date: str, version_number: str, game_mode: str, game_type: str,
                 game_complexity: str, tags: List[Any], gravity: float, play_area: float, table: str, sky: str,
                 note: str, tab_states: TabStates, lua_script: str, lua_script_state: str, xml_ui: str,
                 object_states: List[ObjectState]) -> None:
        self.save_name = save_name
        self.date = date
        self.version_number = version_number
        self.game_mode = game_mode
        self.game_type = game_type
        self.game_complexity = game_complexity
        self.tags = tags
        self.gravity = gravity
        self.play_area = play_area
        self.table = table
        self.sky = sky
        self.note = note
        self.tab_states = tab_states
        self.lua_script = lua_script
        self.lua_script_state = lua_script_state
        self.xml_ui = xml_ui
        self.object_states = object_states
