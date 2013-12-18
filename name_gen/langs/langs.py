from random import *


class Language:

    def __init__(self, vowels,
                 consonants, constraint,
                 phoneme_count=50, punctuation="",
                 word_length=1.5, punctuation_rarity=10,
                 clean_doubles=True, name_suffix=""):
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
        self._stock_syllables()

    # TODO Replace this method with regex method
    def _stock_syllables(self):
        for x in range(0, self.phoneme_count):
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
        wordlen = int(expovariate(2) * self.word_length) + 1
        for x in range(wordlen):
            output.append(choice(self.syllables))
            #Insert Punctuation
        if wordlen > 1 and len(self.punctuation) > 0:
            if randint(1, self.punctuation_rarity) is self.punctuation_rarity:
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