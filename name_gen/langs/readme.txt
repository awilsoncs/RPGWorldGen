Language Construction:

Required parameters-
    vowels: List or string of vowels that appear in the language. Vowels that appear near the front appear exponentially
        more often.
    consonants: As vowels, but should be a list of consonants.
    constraint: This pattern is used to build syllables.
        (C) - random consonant
        (V) - random vowel
        (abc...) - one or more lowercase letters may be selected. Ex: (avcsi), (kenqp).
        (_?) - optional, 50% chance of occurring. Can be appended to any other token.
        Examples:
            Rough Japanese: (C?)(V)(V?)(n?)
            Very Rough English: (s?)(C?)(rlwy?)(V?)(V)(C?)(C?)(C?)
            (Note: these are just meant to display how to write the patterns. Langs isn't sophisticated enough yet to
            generate real-looking Japanese or English.)

Options parameters-
    phoneme_count: Number of basic syllables.
    punctuation: Occasional punctuation within words. Ex: apostrophes or dashes.
    word_length: On average, words will have about this many syllables.
    punct_rarity: How often punctuation occurs within words. No effect is punctuation list is empty.
    clean_doubles: By default, most double vowels are removed from words. Some can still occur.
    name_suffix: By default, no languages have common suffixes for names. If yours should, list them here.

Other-
