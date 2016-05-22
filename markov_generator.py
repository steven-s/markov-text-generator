from nltk import ngrams
from collections import defaultdict, Counter
from random import choice
import string, unicodedata, sys

class MarkovGenerator(object):
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
            if gram not in self._transition_map:
                self._transition_map[gram] = Counter()

    def generate_string(self, length=14, use_weighted_transition=False):
        sentence = []
        start_point = choice(list(self._transition_map.items()))
        while len(sentence) < length:
            (gram, transitions) = start_point
            for word in gram:
                sentence.append(word)
            if (len(transitions) > 0):
                if use_weighted_transition:
                    weighted_transitions = [gram for gram, count in transitions for i in range(count)]
                    start_point = choice(weighted_transitions)
                else:
                    start_point = choice([gram for gram, count in transitions])
            else:
                start_point = choice(list(self._transition_map.items()))
        return ' '.join(sentence[:length])


            
        
