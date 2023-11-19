from typing import List

from ScryfallService import ScryfallService
from TTSClasses.Transform import Transform
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

    for card in scryfall_cards:
        print(f"{card['name']}")
        print(f"{card['uri']}")


if __name__ == '__main__':
    main()
