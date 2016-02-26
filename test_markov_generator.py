import unittest
from markov_generator import MarkovGenerator

test_text = u"""
A Markov chain (discrete-time Markov chain or DTMC[1]), named after Andrey Markov, 
is a random process that undergoes transitions from one state to another on a state space. 
It must possess a property that is usually characterized as "memorylessness": 
the probability distribution of the next state depends only on the current state and not on 
the sequence of events that preceded it. 
This specific kind of "memorylessness" is called the Markov property. 
Markov chains have many applications as statistical models of real-world processes.
"""

class MarkovGeneratorTestCase(unittest.TestCase):
	def test_generating_transition_map(self):
		generator = MarkovGenerator()
		generator.build_chain(test_text)
		self.assertNotEqual(0, len(generator.transition_map))

if __name__ == '__main__':
	unittest.main()