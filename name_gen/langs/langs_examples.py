from name_gen.langs.langs import *

dwarvish = Language("aouie",
                    "rbldmfhjngtkvs",
                    "(C)(V)(C)",
                    name_suffix="io")

# Elves prefer longer words, some punctuation
elvish = Language("aiueo",
                  "lncrshtbdz",
                  "(C?)(V)(C)",
                  word_length=3,
                  punctuation="'",
                  name_suffix=["i", "ia", "ue"],
                  punctuation_rarity=2)

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
    print dwarvish.name().capitalize() + " " + dwarvish.word().capitalize() + dwarvish.word()
print "\nDwarvish Phrases\n"
for _ in range(5):
    print dwarvish.phrase()
print "\nElvish Names\n"
for _ in range(5):
    print elvish.name().capitalize() + " " + elvish.word().capitalize() + elvish.word()
print "\nElvish Phrases\n"
for _ in range(5):
    print elvish.phrase()
print "\nGoblin Names\n"
for _ in range(5):
    print goblin.name().capitalize()
print "\nGoblin Phrases\n"
for _ in range(5):
    print goblin.phrase()