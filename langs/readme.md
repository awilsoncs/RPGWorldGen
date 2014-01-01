#langs
Langs is a library for quickly creating randomized, realistic languages on the fly. When created, a language's syllables are defined and new words are built from them. The translate function will result in words being stored in the languages.

However, languages currently have no permanence and will be different if called again. Often, the difference is very minor, but in some cases might be noticable. Translated dictionaries, however, will be lost and have to be recreated.

### Required parameters-
* **vowels:** List, string, or unicode of vowels that appear in the language. Vowels that appear near the front appear exponentially more often.
* **consonants:** As vowels, but should be a list of consonants.
* **constraint:** This pattern is used to build syllables.
    * **(C)** - random consonant
    * **(V)** - random vowel
    * **(abc...)** - one or more lowercase letters may be selected. Ex: (avcsi), (kenqp).
    * **(_?)** - optional, 50% chance of occurring. Can be appended to any other token.

Examples:
* Rough Japanese: (C?)(V)(V?)(n?)
* Very Rough English: (s?)(C?)(rlwy?)(V?)(V)(C?)(C?)(C?)

(Note: these are just meant to display how to write the patterns. Langs isn't sophisticated enough yet to generate real-looking Japanese or English.)

### Options parameters-
* **phoneme_count:** Integer number of basic syllables. Higher numbers will result in more diverse language. By default, this value is 50.
* **punctuation:** String or list of strings Ex: apostrophes or dashes. 
* **word_length:** On average, words will have about this many syllables. Can be set to any positive floating point number.
* **punct_rarity:** An integer that determines how often punctuation appears in words in the language. By default, punct_rarity is set to 10. Lower values will result in more common punctuation.
* **clean_doubles:** If set to true, the language will have many double vowels replaced by a single vowel. clean_doubles is set to true by default.
* **name_suffix:** If set to a string or list of strings, names in this language will occasionally have a name suffix appended to them.
