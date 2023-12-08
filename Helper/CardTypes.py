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
from enum import Enum
from pprint import pprint
from typing import Tuple, List

"""
2023-152-06, Frank
Schon bei dem winzigen Layout der Split-Karten fällt auf das die Daten mehrfach abgespeichert werden und mehrfach Platz brauchen
"""

"""
2023-12-06, Frank
Noch schlimmer wird diese mehrfache Abspeicherung beim Flip-Layout (Creature-Type mit allen Unter-Typen + Enchantments.
Im Moment gibt es nur 21 Flip-Layout + 6 Flip-Token ... Aber das kann ja noch mehr werden. Also müssten hier auch alle möglichen Werte nochmal abgespeichert werden.

Am Ende habe ich versucht ne Lösung zu "Skizieren"
"""

"""
Lösung für das o.g. Dilema V0.1 :-)
"""
# Klasse in der ALLE CardTypes aufgelistet sind << z.B. so wie ich das NORMAL-Layout ausgearbeitet habe>>
if __name__ == '__main__':
    mitarbeiter: dict = { "vorname": "Frank", "nachname": "Daske"}
    #print(mitarbeiter)
    #print(mitarbeiter["nachname"])

    mitarbeiter["personummer"] = 12345

    aufgaben_frank: List[str] = ["kochen", "putzen", "zocken"]
    mitarbeiter["aufgaben"] = aufgaben_frank
    pprint(mitarbeiter)

    print(f"Aufgaben: {mitarbeiter['aufgaben']}")
    print(f"letzte Aufgabe: {mitarbeiter['aufgaben'][2]}")





# class CardTypes(Enum):
#     SUPER = ["Basic", "Elite", "Legendary", "Ongoing", "Snow", "Token", "World"]
#     "Spells" ("Adventure", "Arcane", "Lesson", "Instant", "Sorcery", "Trap"),
#     "Enchantments" ("Aura", "Background", "Cartouche", "Class", "Curse", "Role", "Rune", "Saga", "Shard", "Shrine"),
#     "Artifacts" ("Attraction", "Blood", "Clue", "Contraption", "Equipment", "Food", "Fortification", "Gold",
#                  "Powerstone", "Treasure", "Vehicle"),
#     "Creatures" ("Advisor", "Aetherborn", "Alien", "Ally", "Angel", "Antelope", "Ape", "Archer", "Archon", "Army",
#                  "Artificer", "Assassin", "Assembly-Worker", "Astartes", "Atog", "Aurochs", "Automaton", "Avatar",
#                  "Azra", "Badger", "Balloon", "Barbarian", "Bard", "Basilisk", "Bat", "Bear", "Beast", "Beeble",
#                  "Beholder", "Berserker", "Bird", "Blinkmoth", "Boar", "Brainiac", "Bringer", "Brushwagg", "C'tan",
#                  "Camarid", "Camel", "Capybara", "Caribou", "Carrier", "Cat", "Centaur", "Cephalid", "Chicken",
#                  "Child", "Chimera", "Citizen", "Cleric", "Clown", "Cockatrice", "Construct", "Coward", "Crab",
#                  "Crocodile", "Custodes", "Cyberman", "Cyclops", "Dalek", "Dauthi", "Demigod", "Demon", "Deserter",
#                  "Detective", "Devil", "Dinosaur", "Djinn", "Doctor", "Dog", "Dragon", "Drake", "Dreadnought",
#                  "Drone", "Druid", "Dryad", "Dwarf", "Efreet", "Egg", "Elder", "Eldrazi", "Elemental", "Elephant",
#                  "Elf", "Elk", "Employee", "Eye", "Faerie", "Ferret", "Fish", "Flagbearer", "Fox", "Fractal",
#                  "Frog", "Fungus", "Gamer", "Gargoyle", "Germ", "Giant", "Gith", "Gnoll", "Gnome", "Goat", "Goblin",
#                  "God", "Golem", "Gorgon", "Graveborn", "Gremlin", "Griffin", "Guest", "Hag", "Halfling", "Hamster",
#                  "Harpy", "Head", "Hellion", "Hippo", "Hippogriff", "Homarid", "Homunculus", "Hornet", "Horror",
#                  "Horse", "Human", "Hydra", "Hyena", "Illusion", "Imp", "Incarnation", "Inkling", "Inquisitor",
#                  "Insect", "Jackal", "Jellyfish", "Juggernaut", "Kavu", "Kirin", "Kithkin", "Knight", "Kobold",
#                  "Kor", "Kraken", "Lamia", "Lammasu", "Leech", "Leviathan", "Lhurgoyf", "Licid", "Lizard",
#                  "Manticore", "Masticore", "Mercenary", "Merfolk", "Metathran", "Minion", "Minotaur", "Mite",
#                  "Mole", "Monger", "Mongoose", "Monk", "Monkey", "Moonfolk", "Mouse", "Mutant", "Myr", "Mystic",
#                  "Naga", "Nautilus", "Necron", "Nephilim", "Nightmare", "Nightstalker", "Ninja", "Noble", "Noggle",
#                  "Nomad", "Nymph", "Octopus", "Ogre", "Ooze", "Orb", "Orc", "Orgg", "Otter", "Ouphe", "Ox",
#                  "Oyster", "Pangolin", "Peasant", "Pegasus", "Pentavite", "Performer", "Pest", "Phelddagrif",
#                  "Phoenix", "Phyrexian", "Pilot", "Pincher", "Pirate", "Plant", "Praetor", "Primarch", "Prism",
#                  "Processor", "Rabbit", "Raccoon", "Ranger", "Rat", "Rebel", "Reflection", "Reveler", "Rhino",
#                  "Rigger", "Robot", "Rogue", "Sable", "Salamander", "Samurai", "Sand", "Saproling", "Satyr",
#                  "Scarecrow", "Scientist", "Scion", "Scorpion", "Scout", "Sculpture", "Serf", "Serpent", "Servo",
#                  "Shade", "Shaman", "Shapeshifter", "Shark", "Sheep", "Siren", "Skeleton", "Slith", "Sliver",
#                  "Slug", "Snail", "Snake", "Soldier", "Soltari", "Spawn", "Specter", "Spellshaper", "Sphinx",
#                  "Spider", "Spike", "Spirit", "Splinter", "Sponge", "Spy", "Squid", "Squirrel", "Starfish",
#                  "Surrakar", "Survivor", "Teddy", "Tentacle", "Tetravite", "Thalakos", "Thopter", "Thrull",
#                  "Tiefling", "Time Lord", "Treefolk", "Trilobite", "Triskelavite", "Troll", "Turtle", "Tyranid",
#                  "Unicorn", "Urzan", "Vampire", "Vedalken", "Viashino", "Volver", "Wall", "Walrus", "Warlock",
#                  "Warrior", "Wasp", "Weird", "Werewolf", "Whale", "Wizard", "Wolf", "Wolverine", "Wombat", "Worm",
#                  "Wraith", "Wurm", "Yeti", "Zombie", "Zubera"),
#     "Lands" ("Cloud", "Desert", "Forest", "Gate", "Island", "Lair", "Locus", "Mine", "Mountain", "Sphere", "Plains",
#              "Power-Plant", "Swamp", "Tower", "Urza's")
#
# und plötzlich ist mein Kopf leer und ich weiß nicht weiter, Sorry ist mal wieder das Große Loch das Frank da hinterlassen hat.
# Muss mir dafür in meinem Geist ert noch nen Deckel basteln. Sorry mach hier an der Stelle den Push
# """
