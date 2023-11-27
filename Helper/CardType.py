from enum import Enum, auto


class CardType(Enum):
    """
        LAYOUT				DESCRIPTION
        normal				A standard Magic card with one face
        split				A split-faced card
        flip				Cards that invert vertically with the flip keyword
        transform			Double-sided cards that transform
        modal_dfc			Double-sided cards that can be played either-side
        meld				Cards with meld parts printed on the back
        leveler				Cards with Level Up
        class				Class-type enchantment cards
        saga				Saga-type cards
        adventure			Cards with an Adventure spell part
        mutate				Cards with Mutate
        prototype			Cards with Prototype
        battle				Battle-type cards
        planar				Plane and Phenomenon-type cards
        scheme				Scheme-type cards
        vanguard			Vanguard-type cards
        token				Token cards
        double_faced_token	Tokens with another token printed on the back
        emblem				Emblem cards
        augment				Cards with Augment
        host				Host-type cards
        art_series			Art Series collectable double-faced cards
        reversible_card		A Magic card with two sides that are unrelated

        See: https://scryfall.com/docs/api/layouts
    """
    NORMAL = auto()
    SPLIT = auto()
    FLIP = auto()
    TRANSFORM = auto()
    MODAL_DFC = auto()
    MELD = auto()
    LEVELER = auto()
    CLASS = auto()
    SAGA = auto()
    ADVENTURE = auto()
    MUTATE = auto()
    PROTOTYPE = auto()
    BATTLE = auto()
    PLANAR = auto()
    SCHEME = auto()
    VANGUARD = auto()
    TOKEN = auto()
    DOUBLE_FACED_TOKEN = auto()
    EMBLEM = auto()
    AUGMENT = auto()
    HOST = auto()
    ART_SERIES = auto()
    REVERSIBLE_CARD = auto()
