# coding=utf-8
from name_gen.langs.langs import *

dwarvish = Language("aouie",
                    "rbldmfhjngtkvs",
                    "(C)(V)(V?)(C)",
                    name_suffix="io",
                    name_patterns=["{U} {U}{w}", "{U} of {U}{}", "{U} of House {U}", "{U}, son of {U}",
                                   "{U}, daughter of {U}", "{U} of the {U}{}"])

# Elves prefer longer words, some punctuation
elvish = Language(u"iueaóëáéôîûú",
                  "lncrshtbdz",
                  "(C?)(V)(C)",
                  word_length=3,
                  punctuation="'",
                  name_suffix=["i", "ia", "ue"],
                  punctuation_rarity=2,
                  name_patterns=["{U} {U}{w}", "{U} of {U}{}", "{U} of House {U}", "{U}, son of {U}",
                                 "{U}, daughter of {U}", "{U} of the {U}{}"])

# Goblins like ugly doubles and have fewer syllables.
# This language displays how to use sounds that take multiple letters in english.
goblin = Language("ouae",
                  ["b", "r", "g", "ch", "m",
                   "t", "z", "l", "k", "h", "s"],
                  "(C)(V)(V?)(C)",
                  clean_doubles=False,
                  phoneme_count=20)

print "\nDwarvish Names\n"
for _ in range(5):
    print dwarvish.pattern_name()
print "\nDwarvish Phrases\n"
for _ in range(5):
    print dwarvish.phrase()
print "\nElvish Names\n"
for _ in range(5):
    print elvish.pattern_name()
print "\nElvish Phrases\n"
for _ in range(5):
    print elvish.phrase()
print "\nGoblin Names\n"
for _ in range(5):
    print goblin.pattern_name()
print "\nGoblin Phrases\n"
for _ in range(5):
    print goblin.phrase()