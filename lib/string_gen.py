__author__ = 'Aaron'
import random
import re


class Generator:
    """
    Base class for several simple text generators.

    In order to use a Generator, you must subclass it and define two attributes:
    format_string: This is the string that will be printed when you call output(). The generator will attempt to
    replace @-prefixed words (ex: @race, @weapons, etc) with a random value from the possible values.
    keys: This is a dict of keys that the generator will replace. The generator selects a value at random from the
    dict's values. (ex: {"weapons": ["knife", "sword"], "race": ["human", "elf"]}.

    See regions.regions for a full example.
    """

    #@TODO- The Generator should attempt to replace keys until it cannot, allowing recursive generation.
    def __init__(self, format_string, keys):
        self.string = format_string
        for key in re.finditer('@(\w*)', self.string):
            if key.group(1) in keys:
                attr = key.group(1)
                value = random.choice(keys[attr])
                self.string = re.sub('@%s' % (key.group(1)), value, self.string, count=1)
                setattr(self, attr, value)
        self.keys = keys
        self.format_string = format_string

    def output(self):
        print self.string