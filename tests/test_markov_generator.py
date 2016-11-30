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
    @classmethod
    def setUpClass(self):
        self.generator = MarkovGenerator()
        self.generator.ingest_text(test_text)

    def test_generating_transition_map(self):
        self.assertNotEqual(0, len(self.generator._transition_map))
        (gram, transitions) = list(self.generator._transition_map.items())[0]
        for (following_gram, count) in list(transitions.items()):
            self.assertEqual(gram[-1], following_gram[0])
            self.assertTrue(count > 0)

    def test_generating_string(self):
        test_string = self.generator.generate_string(20)
        self.assertIsNotNone(test_string)
        self.assertEqual(20, len(test_string.split()))

if __name__ == '__main__':
    unittest.main()
