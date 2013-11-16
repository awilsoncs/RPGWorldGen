# -*- coding: utf-8 -*-
from random import *

class Language:
    """
    Constraint Guide
    (C) - consonant
    (V) - vowel
    (_?) - optional, 50% chance of occuring    
    """
    
    def __init__(self, vowels,
                 consonants, constraint,
                 phonemes=50, punctuation="",
                 wordlen=1.5, punct_rarity=10,
                 clean_doubles=True, name_suffix=""):
        self.vowels = vowels
        self.consonants = consonants
        self.constraint = constraint
        self.phonemes = phonemes
        self.punctuation = punctuation
        self.wordlen = wordlen
        self.punct_rarity = punct_rarity
        self.clean_doubles = clean_doubles
        self.name_suffix = name_suffix
        self.syllables = []
        self._stock_syllables()

    def _stock_syllables(self):
        for x in range(0, self.phonemes):
            pattern = self.constraint
            while "(C)" in pattern:
                pattern = pattern.replace("(C)", self._random_consonant(), 1)
            while "(V)" in pattern:
                pattern = pattern.replace("(V)", self._random_vowel(), 1)
            while "(C?)" in pattern:
                new_letter = choice([self._random_consonant(), ""])
                pattern = pattern.replace("(C?)", new_letter, 1)
            while "(V?)" in pattern:
                new_letter = choice([self._random_vowel(), ""])
                pattern = pattern.replace("(V?)", new_letter, 1)
            self.syllables.append(pattern)

    def _random_vowel(self):
        return self.vowels[int(betavariate(1,3) * len(self.vowels))]
    
    def _random_consonant(self):
        return self.consonants[int(betavariate(1,3) * len(self.consonants))]
    
    def _random_syllable(self):
        return self.syllables[int(betavariate(1,3) * len(self.syllables))]

    def sample(self):
        """
        Provides a string of phrases in the random language.
        """
        output = ""
        for x in range(5):
            output += self.phrase()
        return output

    def phrase(self):
        """
        Provides a string of words in the random language.
        """
        output = ""
        output += self.word().capitalize()
        for x in range(int(expovariate(1) * 3) + 1):
            output += " " + self.word()
        output += " " + self.word() + choice([". ", ", ", "! ", "? "])
        return output

    def word(self):
        """
        Provides a string, consisting of a single word in the random language.
        """
        output = []
        wordlen = int(expovariate(2) * self.wordlen) + 1
        for x in range(wordlen):
            output.append(choice(self.syllables))
        #Insert Punctuation
        if wordlen > 1 and len(self.punctuation) > 0:
            if randint(1, self.punct_rarity) is self.punct_rarity:
                punct = randint(1, wordlen - 1)
                output.insert(punct, choice(self.punctuation))
        output = ''.join(output)
        #Clean out ugly doubles by default.
        if self.clean_doubles:
            for double in ["aa", "ee", "ii", "oo", "uu", "yy"]:
                output = output.replace(double, double[0])
        return output

    def name(self):
        output = ""
        while len(output) < 3:
            output = self.word()
        if len(self.name_suffix) > 0 and randint(0,1) is 0:
            output += choice(self.name_suffix)
        return output.capitalize()
    
example = Language("aeiou",
                   "bcdfghjklmnpqrstvwxyz",
                   "(C?)(V)",
                   punctuation="'",
                   wordlen=4,
                   punct_rarity=10)
dwarvish = Language("aouie",
                    "rbldmfhjngtkvs",
                    "(C)(V)(C)",
                    punctuation="-",
                    name_suffix="io")
elvish = Language("aiueo",
                  "lncrshtbd",
                  "(C)(V)(V?)(C?)",
                  wordlen=2.5,
                  punctuation="'",
                  name_suffix=["i", "ia", "ue"],
                  punct_rarity=2)
goblin = Language("ouae",
                  ["b", "r", "g", "ch", "m",
                   "t", "z", "l", "k", "h", "s"],
                  "(C)(V)(V?)(C)",
                  wordlen=1.75,
                  clean_doubles=False,
                  phonemes=25)
print "\nDwarvish Names\n"
for _ in range(5):
    print dwarvish.name().capitalize() + " " + dwarvish.word().capitalize() + dwarvish.word()
print "\nElvish Names\n"
for _ in range(5):
    print elvish.name().capitalize() + " " + elvish.word().capitalize() + elvish.word()
print "\nGoblin Names\n"
for _ in range(5):
    print goblin.name().capitalize()
