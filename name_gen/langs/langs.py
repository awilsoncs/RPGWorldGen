# coding=utf-8
from random import *
import re


class Language:

    def __init__(self, vowels, consonants, constraint, phoneme_count=50, punctuation="", word_length=1.5,
                 punctuation_rarity=10, clean_doubles=True, name_suffix=""):
        self.vowels = vowels
        self.consonants = consonants
        self.constraint = constraint
        self.phoneme_count = phoneme_count
        self.punctuation = punctuation
        self.word_length = word_length
        self.punctuation_rarity = punctuation_rarity
        self.clean_doubles = clean_doubles
        self.name_suffix = name_suffix
        self.syllables = []
        self.build_syllables()

    def build_syllables(self):
        def build_syllable():
            pattern = self.constraint
            output = ""
            for match in re.finditer('\((.+?)\)', pattern):
                #matches one or more optional predefined characters
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

    def name(self):
        output = ""
        while len(output) < 3 or len(output) > 10:
            output = self.word()
        if len(self.name_suffix) > 0 and randint(0, 1) is 0:
            output += choice(self.name_suffix)
        return output.capitalize()


# TODO
def lang_from_file(syllables):
    """
    Takes a text file of language syllables and returns a language based on it.
    """
    pass