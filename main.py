from typing import List, Dict
import json

from ScryfallService import ScryfallService
from TTSClasses.ContainedObject import ContainedObject
from TTSClasses.CustomDeck import CustomDeck
from TTSClasses.ObjectState import ObjectState
from TTSClasses.TTSObject import TTSObject
from TxtCard import TxtCard


def main():
    f = open('data/examples/deck_file.txt', 'r')
    cards: List[TxtCard] = []
    scryfall_cards = []
    sf = ScryfallService()
    for r in f:
        r = r.strip('\n')
        if len(r) > 0:
            cards.append(TxtCard.from_string(row=r))
    for c in cards:
        sf_card = sf.get_card_by_fuzzy(fuzzy=c.name)
        if sf_card.status_code == 200:
            scryfall_cards.append(sf_card.json())
    print(f"{len(scryfall_cards)} cards loaded from file")

    """
    custom_deck: CustomDeck = CustomDeck(face_url="", back_url="")
    contained_obj: ContainedObject = ContainedObject(card_id=1, nickname="")
    contained_objs: List[ContainedObject] = [contained_obj]
    deck_ids: List[int] = [100]
    obj_state: ObjectState = ObjectState(name="", contained_objects=contained_objs, deck_ids=deck_ids,
                                         custom_deck={"0": custom_deck})
    obj_states: List[ObjectState] = [obj_state]
    tts_obj: TTSObject = TTSObject(object_states=obj_states)
    """
    obj_states: List[ObjectState] = []
    contained_objs: List[ContainedObject] = []
    deck_ids: List[int] = []
    current_card: int = 0
    custom_deck: Dict[str, CustomDeck] = {}
    for card in scryfall_cards:
        current_card += 1

        contained_objs.append(ContainedObject(card_id=current_card*100, nickname=card["name"]))
        custom_deck_obj: CustomDeck = CustomDeck(face_url=card["image_uris"]["normal"])  # karte ToDo: Auswahl img größe
        custom_deck[str(current_card)] = custom_deck_obj
        deck_ids.append(current_card * 100)  # ToDo: mehrfach hinzufügen wenn count > 1


    obj_state: ObjectState = ObjectState(contained_objects=contained_objs,
                                         deck_ids=deck_ids, custom_deck=custom_deck)
    obj_states.append(obj_state)

    tts_obj: TTSObject = TTSObject(object_states=obj_states)

    tts_obj_dict = tts_obj.to_dict()
    # pprint(tts_obj_dict)
    json_obj = json.dumps(tts_obj_dict)
    print(json_obj)


if __name__ == '__main__':
    main()
