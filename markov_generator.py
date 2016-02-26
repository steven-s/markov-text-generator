from nltk import bigrams
from collections import defaultdict, Counter

class MarkovGenerator(object):
	def __init__(self):
		self.transition_map = defaultdict(Counter)
		self.bigram_counts = Counter()

	def build_chain(self, text):
		text_bigrams = bigrams(text.split())

		previous_gram = None
		for gram in text_bigrams:
			if previous_gram:
				self.transition_map[previous_gram][gram] += 1
			if gram not in self.transition_map:
				self.transition_map[gram] = Counter()
			self.bigram_counts[gram] += 1






