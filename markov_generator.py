from nltk import bigrams
from collections import defaultdict, Counter
from random import choice

class MarkovGenerator(object):
	def __init__(self):
		self.transition_map = defaultdict(Counter)
		self.bigram_counts = Counter()

	def ingest_text(self, text):
		text_bigrams = bigrams(text.split())

		previous_gram = None
		for gram in text_bigrams:
			if previous_gram:
				self.transition_map[previous_gram][gram] += 1
			if gram not in self.transition_map:
				self.transition_map[gram] = Counter()
			self.bigram_counts[gram] += 1

	def generate_string(self, length=14):
		sentence = []
		start_point = choice(list(self.transition_map.items()))
		while len(sentence) < length:
			((word1, word2), transitions) = start_point
			sentence.append(word1)
			sentence.append(word2)
			if (len(transitions) > 0):
				weighted_transitions = [gram for gram, count in transitions for i in range(count)]
				start_point = choice(weighted_transitions)
			else:
				start_point = choice(list(self.transition_map.items()))
		return ' '.join(sentence[:length])


			
		