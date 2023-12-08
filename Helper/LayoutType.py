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
    """
    2023-12-06, Frank
    Tupel aller Cardtypes mit Normalem Leyout - Sind ne ganze menge
    Unterteile die ganzen Typen mal in Tupels in Tupels.
    Der Grund: Auf https://scryfall.com/docs/api/catalogs kann man die ganzen Layouts und Typen sich anzeigen lassen.
        Wenn die alle in ein einzelnes Tupel gespeichert werden verliert man schnell den Überblick.
        - SuperTypes
        - SpellTypes
        - LandTypes
        - CreatureTypes
        - ArtifactTypes
        - EnchantmentTypes
    """
    NORMAL = ("SuperTypes" ("Basic", "Elite", "Legendary", "Ongoing", "Snow", "Token", "World"),
              "SpellTypes" ("Adventure", "Arcane", "Lesson", "Instant", "Sorcery", "Trap"),
              "EnchantmentTypes" ("Aura","Background","Cartouche","Class","Curse","Role","Rune","Saga","Shard","Shrine"),
              "ArtifactTypes" ("Attraction","Blood","Clue","Contraption","Equipment","Food","Fortification","Gold","Powerstone","Treasure","Vehicle"),
              "CreatureTypes" ("Advisor","Aetherborn","Alien","Ally","Angel","Antelope","Ape","Archer","Archon","Army","Artificer","Assassin","Assembly-Worker","Astartes","Atog","Aurochs","Automaton","Avatar","Azra","Badger","Balloon","Barbarian","Bard","Basilisk","Bat","Bear","Beast","Beeble","Beholder","Berserker","Bird","Blinkmoth","Boar","Brainiac","Bringer","Brushwagg","C'tan","Camarid","Camel","Capybara","Caribou","Carrier","Cat","Centaur","Cephalid","Chicken","Child","Chimera","Citizen","Cleric","Clown","Cockatrice","Construct","Coward","Crab","Crocodile","Custodes","Cyberman","Cyclops","Dalek","Dauthi","Demigod","Demon","Deserter","Detective","Devil","Dinosaur","Djinn","Doctor","Dog","Dragon","Drake","Dreadnought","Drone","Druid","Dryad","Dwarf","Efreet","Egg","Elder","Eldrazi","Elemental","Elephant","Elf","Elk","Employee","Eye","Faerie","Ferret","Fish","Flagbearer","Fox","Fractal","Frog","Fungus","Gamer","Gargoyle","Germ","Giant","Gith","Gnoll","Gnome","Goat","Goblin","God","Golem","Gorgon","Graveborn","Gremlin","Griffin","Guest","Hag","Halfling","Hamster","Harpy","Head","Hellion","Hippo","Hippogriff","Homarid","Homunculus","Hornet","Horror","Horse","Human","Hydra","Hyena","Illusion","Imp","Incarnation","Inkling","Inquisitor","Insect","Jackal","Jellyfish","Juggernaut","Kavu","Kirin","Kithkin","Knight","Kobold","Kor","Kraken","Lamia","Lammasu","Leech","Leviathan","Lhurgoyf","Licid","Lizard","Manticore","Masticore","Mercenary","Merfolk","Metathran","Minion","Minotaur","Mite","Mole","Monger","Mongoose","Monk","Monkey","Moonfolk","Mouse","Mutant","Myr","Mystic","Naga","Nautilus","Necron","Nephilim","Nightmare","Nightstalker","Ninja","Noble","Noggle","Nomad","Nymph","Octopus","Ogre","Ooze","Orb","Orc","Orgg","Otter","Ouphe","Ox","Oyster","Pangolin","Peasant","Pegasus","Pentavite","Performer","Pest","Phelddagrif","Phoenix","Phyrexian","Pilot","Pincher","Pirate","Plant","Praetor","Primarch","Prism","Processor","Rabbit","Raccoon","Ranger","Rat","Rebel","Reflection","Reveler","Rhino","Rigger","Robot","Rogue","Sable","Salamander","Samurai","Sand","Saproling","Satyr","Scarecrow","Scientist","Scion","Scorpion","Scout","Sculpture","Serf","Serpent","Servo","Shade","Shaman","Shapeshifter","Shark","Sheep","Siren","Skeleton","Slith","Sliver","Slug","Snail","Snake","Soldier","Soltari","Spawn","Specter","Spellshaper","Sphinx","Spider","Spike","Spirit","Splinter","Sponge","Spy","Squid","Squirrel","Starfish","Surrakar","Survivor","Teddy","Tentacle","Tetravite","Thalakos","Thopter","Thrull","Tiefling","Time Lord","Treefolk","Trilobite","Triskelavite","Troll","Turtle","Tyranid","Unicorn","Urzan","Vampire","Vedalken","Viashino","Volver","Wall","Walrus","Warlock","Warrior","Wasp","Weird","Werewolf","Whale","Wizard","Wolf","Wolverine","Wombat","Worm","Wraith","Wurm","Yeti","Zombie","Zubera"),
              "LandTypes" ("Cloud","Desert","Forest","Gate","Island","Lair","Locus","Mine","Mountain","Sphere","Plains","Power-Plant","Swamp","Tower","Urza's")
              )
    """
    2023-152-06, Frank
    Schon bei dem winzigen Layout der Split-Karten fällt auf das die Daten mehrfach abgespeichert werden und mehrfach Platz brauchen
    """
    SPLIT = ("Instant", "Sorcery")

    """
    2023-12-06, Frank
    Noch schlimmer wird diese mehrfache Abspeicherung beim Flip-Layout (Creature-Type mit allen Unter-Typen + Enchantments.
    Im Moment gibt es nur 21 Flip-Layout + 6 Flip-Token ... Aber das kann ja noch mehr werden. Also müssten hier auch alle möglichen Werte nochmal abgespeichert werden.

    Am Ende habe ich versucht ne Lösung zu "Skizieren"
    """
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

"""
Lösung für das o.g. Dilema V0.1 :-)
"""
class card(Enum): # Klasse in der ALLE CardTypes aufgelistet sind << z.B. so wie ich das NORMAL-Layout ausgearbeitet habe>>
    CardTypes = [
        "Super" ("Basic", "Elite", "Legendary", "Ongoing", "Snow", "Token", "World"),
        "Spells" ("Adventure", "Arcane", "Lesson", "Instant", "Sorcery", "Trap"),
        "Enchantments" ("Aura", "Background", "Cartouche", "Class", "Curse", "Role", "Rune", "Saga", "Shard", "Shrine"),
        "Artifacts" ("Attraction", "Blood", "Clue", "Contraption", "Equipment", "Food", "Fortification", "Gold",
                     "Powerstone", "Treasure", "Vehicle"),
        "Creatures" ("Advisor", "Aetherborn", "Alien", "Ally", "Angel", "Antelope", "Ape", "Archer", "Archon", "Army",
                     "Artificer", "Assassin", "Assembly-Worker", "Astartes", "Atog", "Aurochs", "Automaton", "Avatar",
                     "Azra", "Badger", "Balloon", "Barbarian", "Bard", "Basilisk", "Bat", "Bear", "Beast", "Beeble",
                     "Beholder", "Berserker", "Bird", "Blinkmoth", "Boar", "Brainiac", "Bringer", "Brushwagg", "C'tan",
                     "Camarid", "Camel", "Capybara", "Caribou", "Carrier", "Cat", "Centaur", "Cephalid", "Chicken",
                     "Child", "Chimera", "Citizen", "Cleric", "Clown", "Cockatrice", "Construct", "Coward", "Crab",
                     "Crocodile", "Custodes", "Cyberman", "Cyclops", "Dalek", "Dauthi", "Demigod", "Demon", "Deserter",
                     "Detective", "Devil", "Dinosaur", "Djinn", "Doctor", "Dog", "Dragon", "Drake", "Dreadnought",
                     "Drone", "Druid", "Dryad", "Dwarf", "Efreet", "Egg", "Elder", "Eldrazi", "Elemental", "Elephant",
                     "Elf", "Elk", "Employee", "Eye", "Faerie", "Ferret", "Fish", "Flagbearer", "Fox", "Fractal",
                     "Frog", "Fungus", "Gamer", "Gargoyle", "Germ", "Giant", "Gith", "Gnoll", "Gnome", "Goat", "Goblin",
                     "God", "Golem", "Gorgon", "Graveborn", "Gremlin", "Griffin", "Guest", "Hag", "Halfling", "Hamster",
                     "Harpy", "Head", "Hellion", "Hippo", "Hippogriff", "Homarid", "Homunculus", "Hornet", "Horror",
                     "Horse", "Human", "Hydra", "Hyena", "Illusion", "Imp", "Incarnation", "Inkling", "Inquisitor",
                     "Insect", "Jackal", "Jellyfish", "Juggernaut", "Kavu", "Kirin", "Kithkin", "Knight", "Kobold",
                     "Kor", "Kraken", "Lamia", "Lammasu", "Leech", "Leviathan", "Lhurgoyf", "Licid", "Lizard",
                     "Manticore", "Masticore", "Mercenary", "Merfolk", "Metathran", "Minion", "Minotaur", "Mite",
                     "Mole", "Monger", "Mongoose", "Monk", "Monkey", "Moonfolk", "Mouse", "Mutant", "Myr", "Mystic",
                     "Naga", "Nautilus", "Necron", "Nephilim", "Nightmare", "Nightstalker", "Ninja", "Noble", "Noggle",
                     "Nomad", "Nymph", "Octopus", "Ogre", "Ooze", "Orb", "Orc", "Orgg", "Otter", "Ouphe", "Ox",
                     "Oyster", "Pangolin", "Peasant", "Pegasus", "Pentavite", "Performer", "Pest", "Phelddagrif",
                     "Phoenix", "Phyrexian", "Pilot", "Pincher", "Pirate", "Plant", "Praetor", "Primarch", "Prism",
                     "Processor", "Rabbit", "Raccoon", "Ranger", "Rat", "Rebel", "Reflection", "Reveler", "Rhino",
                     "Rigger", "Robot", "Rogue", "Sable", "Salamander", "Samurai", "Sand", "Saproling", "Satyr",
                     "Scarecrow", "Scientist", "Scion", "Scorpion", "Scout", "Sculpture", "Serf", "Serpent", "Servo",
                     "Shade", "Shaman", "Shapeshifter", "Shark", "Sheep", "Siren", "Skeleton", "Slith", "Sliver",
                     "Slug", "Snail", "Snake", "Soldier", "Soltari", "Spawn", "Specter", "Spellshaper", "Sphinx",
                     "Spider", "Spike", "Spirit", "Splinter", "Sponge", "Spy", "Squid", "Squirrel", "Starfish",
                     "Surrakar", "Survivor", "Teddy", "Tentacle", "Tetravite", "Thalakos", "Thopter", "Thrull",
                     "Tiefling", "Time Lord", "Treefolk", "Trilobite", "Triskelavite", "Troll", "Turtle", "Tyranid",
                     "Unicorn", "Urzan", "Vampire", "Vedalken", "Viashino", "Volver", "Wall", "Walrus", "Warlock",
                     "Warrior", "Wasp", "Weird", "Werewolf", "Whale", "Wizard", "Wolf", "Wolverine", "Wombat", "Worm",
                     "Wraith", "Wurm", "Yeti", "Zombie", "Zubera"),
        "Lands" ("Cloud", "Desert", "Forest", "Gate", "Island", "Lair", "Locus", "Mine", "Mountain", "Sphere", "Plains",
                 "Power-Plant", "Swamp", "Tower", "Urza's")
    ]

""" und plötzlich ist mein Kopf leer und ich weiß nicht weiter, Sorry ist mal wieder das Große Loch das Frank da hinterlassen hat.
    Muss mir dafür in meinem Geist ert noch nen Deckel basteln. Sorry mach hier an der Stelle den Push
"""
