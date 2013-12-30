# coding=utf-8
from random import *
import re
#@TODO Language class should read from XML files.


class Language:
    def __init__(self, vowels, consonants, constraint, **kwargs):
        if "phoneme_count" in kwargs:
            self.phoneme_count = kwargs["phoneme_count"]
        else:
            self.phoneme_count = 50
        if "punctuation" in kwargs:
            self.punctuation = kwargs["punctuation"]
        else:
            self.punctuation = ""
        if "word_length" in kwargs:
            self.word_length = kwargs["word_length"]
        else:
            self.word_length = 1.5
        if "punctuation_rarity" in kwargs:
            self.punctuation_rarity = kwargs["punctuation_rarity"]
        else:
            self.punctuation_rarity = 10
        if "clean_doubles" in kwargs:
            self.clean_doubles = kwargs["clean_doubles"]
        else:
            self.clean_doubles = True
        if "name_suffix" in kwargs:
            self.name_suffix = kwargs["name_suffix"]
        else:
            self.name_suffix = ""
        if "name_patterns" in kwargs:
            self.name_patterns = kwargs["name_patterns"]
        else:
            self.name_patterns = ["(U) (U)(w)"]
        self.vowels = vowels
        self.consonants = consonants
        self.constraint = constraint
        self.syllables = []
        self.dictionary = ()
        self._build_syllables()

    def _build_syllables(self):
        def build_syllable():
            pattern = self.constraint
            output = ""
            for match in re.finditer('\((.+?)\)', pattern):
                if re.match('([a-z]+)\?', match.group(1)):
                    possible = choice(re.match('([a-z]+)\?', match.group(1)).group(1))
                    output += choice([possible, ""])
                elif re.match('([a-z]+)', match.group(1)):
                    output += choice(re.match('([a-z]+)', match.group(1)).group(1))
                elif match.group(1) == "C":
                    output += self._random_consonant()
                elif match.group(1) == "V":
                    output += self._random_vowel()
                elif match.group(1) == "C?":
                    output += choice([self._random_consonant(), ""])
                elif match.group(1) == "V?":
                    output += choice([self._random_vowel(), ""])
            return output

        for _ in range(0, self.phoneme_count):
            syllable = build_syllable()
            self.syllables.append(syllable)

    def _random_vowel(self):
        return self.vowels[int(betavariate(1, 3) * len(self.vowels))]

    def _random_consonant(self):
        return self.consonants[int(betavariate(1, 3) * len(self.consonants))]

    def _random_syllable(self):
        return self.syllables[int(betavariate(1, 3) * len(self.syllables))]

    def sample(self):
        """
        Provide a string of phrases in the random language.
        """
        output = ""
        for x in range(5):
            output += self.phrase()
        return output

    def phrase(self):
        """
        Provide a string of words in the random language.
        """
        output = ""
        output += self.word().capitalize()
        for x in range(int(expovariate(1) * 3) + 1):
            output += " " + self.word()
        output += " " + self.word() + choice([". ", ", ", "! ", "? "])
        return output

    def word(self):
        """
        Provide a string, consisting of a single word in the random language.
        """
        output = []
        word_length = int(expovariate(2) * self.word_length) + 1
        for x in range(word_length):
            output.append(choice(self.syllables))
            #Insert Punctuation
        if word_length > 1 and len(self.punctuation) > 0:
            if randint(1, self.punctuation_rarity) is self.punctuation_rarity:
                punct = randint(1, word_length - 1)
                output.insert(punct, choice(self.punctuation))
        output = ''.join(output)
        #Clean out ugly doubles by default.
        if self.clean_doubles:
            for double in ["aa", "ee", "ii", "oo", "uu", "yy"]:
                output = output.replace(double, double[0])
        return output

    #TODO clean_repetitions needs implementation
    def clean_repetitions(self, string):
        """
        Take a generated language string and cleans out any words that appear twice in a row.
        """
        pass

    def name(self):
        output = ""
        while len(output) < 3 or len(output) > 10:
            output = self.word()
        if len(self.name_suffix) > 0 and randint(0, 1) is 0:
            output += choice(self.name_suffix)
        return output

    def pattern_name(self):
        """
        Return a name, stylized with an arbitrary pattern, where (U) gives a capital syllable and () gives a lower 
        case syllable. (w) gives a standard word.
        """
        pattern = choice(self.name_patterns)
        for symbol in ["(U)", "()", "(w)", "(w)"]:
            while symbol in pattern:
                if symbol == "(U)":
                    new_syllable = self.name().capitalize()
                elif symbol == "(w)":
                    new_syllable = self.word()
                elif symbol == "(w)":
                    new_syllable = self.word().capitalize()
                else:
                    new_syllable = self.name()
                pattern = pattern.replace(symbol, new_syllable, 1)
        return pattern

# Predefined languages
# The northern language is designed to sound fairly familiar, as if it might be
# an undiscovered germanic cousin.
northern = Language(u"eaoiuy",
                 "tnshrdlcmwfgypbvkjxqz",
                 "(C?)(rlwy?)(V?)(V)(C?)(C?)",
                 name_suffix=["wyn", "mer", "son", "ron", "iam"],
                 word_length=1,
                 name_patterns=["(U)", "(U) of (U)", "(U) of House (U)", "(U), son of (U)",
                                "(U)a, daughter of (U)", "(U)i, daughter of (U)",
                                "(U) of the (U)", "(U)ol, son of (U)",
                                "(U) (U)son", "(U) of (U)ton"])

dwarvish = Language(u"aouiôeá",
                    "rbldmfhjngtkvs",
                    "(C)(V)(V?)(C)",
                    name_suffix="io",
                    punctuation="-",
                    name_patterns=["(U) (U)(w)", "(U) of (U)()", "(U) of House (U)", "(U), son of (U)",
                                   "(U), daughter of (U)", "(U) of the (U)()"])

# Elves prefer longer words, some punctuation
elvish = Language(["a", "i", "e", "o", "u", "ai", "ae", u"ê", "ui", "au", u"í", u"â", u"ú", "ue", u"ô", "y", u"ý"],
                  ["n", "r", "l", "h", "t", "d", "m", "ch", "v", "ll", "g", "s", "c", "p", "f", "b", "w"],
                  "(C?)(V)(C)",
                  word_length=2,
                  punctuation="'-",
                  phoneme_count=150,
                  name_suffix=["a", "ia", "as", "el", "is", "lon", "iel", "ra", "al"],
                  punctuation_rarity=2,
                  name_patterns=["(U) of (U)()", "(U) of House (U)", "(U), son of (U)",
                                 "(U), daughter of (U)", "(U) of the (U)()"])

old_elvish = Language(["a", "i", "e", u"ë", "u", "o", "y", u"á", u"í", u"ó", u"ú", u"é"],
                      ["n", "r", "l", "m", "t", "v", "s", "d", "c", "h", "p", "b", "f", "w", "q"],
                      "(C?)(V)(C)",
                      word_length=2.25,
                      punctuation="'-",
                      phoneme_count=150,
                      name_suffix=["el", "iss", "lon", "iel", "ra", "al"],
                      punctuation_rarity=2,
                      name_patterns=["(w)()"])

# Goblins like ugly doubles and have fewer syllables.
# This language displays how to use sounds that take multiple letters in english.
goblin = Language("ouaei",
                  ["b", "r", "g", "ch", "m",
                   "t", "z", "l", "k", "h", "s"],
                  "(C)(V)(V?)(C)",
                  word_length=1,
                  clean_doubles=False,
                  phoneme_count=30,
                  name_patterns=["(U)"])

orcish = Language(u"aoâue",
                  ["k", "r", "j", "ch", "m",
                   "t", "z", "l", "p", "b", "h", "s"],
                  "(C)(V?)(V?)(C)",
                  word_length=1.2,
                  phoneme_count=40,
                  name_patterns=["(U)()", "(U)() of Clan (U)(w)", "(U)(), slayer of (U)()", "(U)",
                                 "(U)-()", "(U)-() of Clan (U)(w)", "(U)-(), slayer of (U)()"])