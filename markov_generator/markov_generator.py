from nltk import ngrams
from collections import defaultdict, Counter
from random import choice
import string, unicodedata, sys

class MarkovGenerator:
    def __init__(self, ngram_size=2):
        self._ngram_size = ngram_size
        self._transition_map = defaultdict(Counter)
        self._punctuation_table = dict.fromkeys(i for i in range(sys.maxunicode) 
                if unicodedata.category(chr(i)).startswith(u'P'))

    def ingest_text(self, text):
        clean_text = text.translate(self._punctuation_table).lower()
        text_ngrams = ngrams(clean_text.split(), self._ngram_size)
        previous_gram = None
        for gram in text_ngrams:
            if previous_gram:
                self._transition_map[previous_gram][gram] += 1
            previous_gram = gram

    def generate_string(self, length=14, use_weighted_transition=False):
        sentence = []
        start_point = choice(list(self._transition_map.keys()))
        while len(sentence) < length:
            for word in list(start_point)[(self._ngram_size - 1):]:
                sentence.append(word)
            transitions = self._transition_map[start_point]
            if (len(transitions) > 0):
                if use_weighted_transition:
                    weighted_transitions = [gram for gram, count in transitions.items() for _ in range(count)]
                    start_point = choice(weighted_transitions)
                else:
                    start_point = choice(list(transitions.keys()))
            else:
                start_point = choice(list(self._transition_map.keys()))
        return ' '.join(sentence[:length])

