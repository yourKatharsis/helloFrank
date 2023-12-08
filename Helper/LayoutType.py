from enum import Enum

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


class LayoutType(Enum):
    """
        Enumareted Types of Layout as specified in https://scryfall.com/docs/api/layouts.
        Information about size and background are stored in a tuple of bool and int.
    """
    NORMAL = (False, 1)
    """A standard Magic card with one face"""

    SPLIT = (False, 1)
    """A split-faced card"""

    FLIP = (False, 1)
    """Cards that invert vertically with the flip keyword"""

    TRANSFORM = (True, 1)
    MODAL_DFC = (True, 1)
    MELD = (True, 1)
    LEVELER = (False, 1)
    CLASS = (False, 1)
    SAGA = (False, 1)
    ADVENTURE = (False, 1)
    MUTATE = (False, 1)
    PROTOTYPE = (False, 1)
    BATTLE = (False, 1)
    PLANAR = (False, 2)
    SCHEME = (False, 2)
    VANGUARD = (False, 1)
    TOKEN = (False, 1)
    DOUBLE_FACED_TOKEN = (True, 1)
    EMBLEM = (False, 1)
    AUGMENT = (False, 1)
    HOST = (False, 1)
    ART_SERIES = (True, 1)
    REVERSIBLE_CARD = (True, 1)
