import os
from typing import List, Dict, Any, Tuple
import json
from datetime import datetime

from ScryfallService import ScryfallService
from TTSClasses.ContainedObject import ContainedObject
from TTSClasses.CustomDeck import CustomDeck
from TTSClasses.ObjectState import ObjectState
from TTSClasses.TTSObject import TTSObject
from Helper.TxtCard import TxtCard


def load_from_txt(file_path: str):
    f = open(file_path, 'r')
    txt_cards: List[TxtCard] = []
    sf = ScryfallService()
    for r in f:
        r = r.strip('\n')
        if len(r) > 0:
            txt_cards.append(TxtCard.from_string(row=r))
    sf_cards: List[Tuple[int, Any]] = []
    for c in txt_cards:
        sf_card = sf.get_card_by_fuzzy(fuzzy=c.name)
        if sf_card.status_code == 200:
            sf_tuple = (c.count, sf_card.json())
            sf_cards.append(sf_tuple)
    return sf_cards


def sf_cards_to_tts_object(sf_cards: List[Tuple[int, Any]]):
    obj_states: List[ObjectState] = []
    contained_objs: List[ContainedObject] = []
    deck_ids: List[int] = []
    current_card: int = 0
    custom_deck: Dict[str, CustomDeck] = {}
    for (count, card) in sf_cards:
        current_card += 1

        contained_objs.append(ContainedObject(card_id=current_card * 100, nickname=card["name"]))
        custom_deck_obj: CustomDeck = CustomDeck(face_url=card["image_uris"][
            "normal"])  # ToDo: double faces (check if key "card_faces" in  response and get 2. items url)
        custom_deck[str(current_card)] = custom_deck_obj
        for x in range(count):
            deck_ids.append(current_card * 100)

    obj_state: ObjectState = ObjectState(contained_objects=contained_objs,
                                         deck_ids=deck_ids, custom_deck=custom_deck)
    obj_states.append(obj_state)

    return TTSObject(object_states=obj_states)


if __name__ == '__main__':
    sf_cards = load_from_txt("data/input/deck_file.txt")
    print(f"{len(sf_cards)} cards loaded from file")

    tts_obj = sf_cards_to_tts_object(sf_cards=sf_cards)

    json_obj = json.dumps(tts_obj.to_dict(), indent=4)

    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    dest_file = f"data/output/tts_deck_{dt}.json"
    os.makedirs(os.path.dirname(dest_file), exist_ok=True)
    with open(dest_file, 'w') as dest_file:
        dest_file.write(json_obj)
