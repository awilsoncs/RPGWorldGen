__author__ = 'Aaron'

from lib.string_gen import Generator

class Region(Generator):

    def __init__(self):
        format_string = "Morality: @morality\n" \
                        "Order: @order\n" \
                        "Government: @government\n" \
                        "Foreign Policy: @foreign\n" \
                        "Focus for Advancement: @focus\n" \
                        "Military Focus: @military\n" \
                        "\n--People--\n" \
                        "Race: @race\n"

        keys = {"morality": ["evil to the core", "pretty bad", "not the nicest",
                             "fairly average", "decent enough", "general good", "virtue incarnate"],
                "order": ["complete chaos", "lawlessness", "low order", "balanced order", "organized", "lawful",
                          "supreme justice"],
                "government": ["monarchy", "democracy", "aristocracy", "meritocracy", "military rule", "theocracy",
                               "republic"],
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
                "race": ["human"]}
        Generator.__init__(self, format_string, keys)