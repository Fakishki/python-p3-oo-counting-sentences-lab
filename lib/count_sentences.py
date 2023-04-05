#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self.value = value

    def get_value(self):
        return self._value
        
    def set_value(self, value):
        if type(value) == str:
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
        if self.value[-1] == ".":
            return True
        else:
            return False
        
    def is_question(self):
        if self.value[-1] == "?":
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value[-1] == "!":
            return True
        else:
            return False
    
    def count_sentences(self):
        value = self.value.replace("!", ".")
        value = value.replace("?", ".")
        sentences = value.split(".")
        count = 0
        for sentence in sentences:
            trimmed_sentence = sentence.strip()
            if len(trimmed_sentence) > 0:
              count += 1
              if sentence.endswith("!!") or sentence.endswith("??") or sentence.endswith("..."):
                  count += 1
        return count