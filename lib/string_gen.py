__author__ = 'Aaron'
import re
import random


class Generator:
    """
    Base class for several simple text generators. Words proceeded by @ in format_string will be populated by random
    values in the keys dict. If the key isn't found in the dict, the Generator will leave it in place.
    """

    def __init__(self, format_string, keys):
        self.string = format_string
        for key in re.finditer('@(\w*)', self.string):
            if key.group(1) in keys:
                attr = key.group(1)
                value = random.choice(keys[attr])
                self.string = re.sub('@(\w*)', value, self.string, count=1)
                setattr(self, attr, value)
        self.keys = keys
        self.format_string = format_string

    def output(self):
        print self.string
