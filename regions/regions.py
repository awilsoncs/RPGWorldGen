__author__ = 'Aaron'

from lib.string_gen import Generator

class Region(Generator):

    def __init__(self):
        format_string = "Alignment: @alignment\n" \
                        "Government: @government_modifier @government\n" \
                        "Government Agenda: @focus\n" \
                        "Foreign Policy: @foreign\n" \
                        "Military Focus: @military\n" \
                        "\n--People--\n" \
                        "Race: @race\n" \
                        "Skin Tone: @skin\n" \
                        "Worship: deities of @domain and @domain\n" \
                        "\n--Environment--\n" \
                        "Dominant Biome: @biome\n"

        keys = {"alignment": ["lawful good", "neutral good", "chaotic good", "lawful neutral", "true neutral",
                              "chaotic neutral", "lawful evil", "neutral evil", "chaotic evil"],
                "government": ["monarchy", "democracy", "meritocracy", "theocracy", "confederation", "alliance",
                               "republic", "dictatorship", "council", "plutocracy", "oligarchy"],
                "government_modifier": ["sacred", "magocratic", "democratic", "oligarchic", "patriarchal",
                                        "matriarchal", "bureaucratic", "technocratic", "aristocratic", "grand",
                                        "fledgling", "hereditary", "imperial", "mercantile", "loose", "revolutionary",
                                        "undead", "colonial", "anarchic", "military", "constitutional", "secret"],
                "foreign": ["defensive", "aggressive", "seeks alliances", "seeks conquest",
                            "secluded", "cosmopolitan", "watchful", "heedless", "intrusive",
                            "respectful", "greedy", "generous", "dependent", "independent",
                            "provocative", "pleasant"],
                "focus": ["arts and culture", "knowledge", "spirituality", "military might", "trade and economy",
                          "magic", "slaves", "industry", "tourism", "resource gathering", "tradition", "propaganda",
                          "safety and security", "foreign sabotage", "expansion", "diversity"],
                "military": ["land armies", "navy/marine", "magic/divine", "military tech", "spies and special forces",
                             "heavy defenses", "support and resources", "animals and creatures",
                             "mercenaries and contractors", "mass disposable forces"],
                "race": ["human"],
                "skin": ["light, pale white", "white, fair", "medium, white to olive", "olive, moderate brown",
                         "brown, dark brown", "Black, very dark brown to black"],
                "domain": ["air", "animals", "artifice", "chaos", "charm", "community", "darkness", "death",
                           "destruction", "earth", "evil", "fire", "glory", "good", "healing", "knowledge", "law",
                           "liberation", "luck", "madness", "magic", "nobility", "plants", "protection", "repose",
                           "runes", "strength", "the sun", "travel", "trickery", "the void", "war", "water", "weather"],
                "biome": ["pond or lake", "stream or river", "wetlands", "ocean", "coral reef",
                          "estuary", "hot and dry desert", "semiarid desert", "coastal desert", "cold desert",
                          "tropical forest", "temperate forest", "taiga", "arctic tundra", "alpine tundra",
                          "savanna", "temperate grassland", "steppe"]}
        Generator.__init__(self, format_string, keys)