#!/usr/bin/env python3

import argparse
from  markov_generator import MarkovGenerator

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("--ngram-size", help="set the size of n-grams", type=int, default=2)
parser.add_argument("--use-weighted-transitions", help="use weighted transitions", action="store_true", default=False)
parser.add_argument("source_text_location", metavar="SOURCE_TEXT_LOCATION", help="source text file")
parser.add_argument("output_length", metavar="OUTPUT_LENGTH", help="word length of sentence to generate", type=int)

args = parser.parse_args()

if args.verbose: print("starting markov generator")

if args.verbose:
    print("ngram size: {}".format(args.ngram_size))
    print("use weighted transitions: {}".format(args.use_weighted_transitions))
    print("source file: {}".format(args.source_text_location))
    print("output length: {}".format(args.output_length))

if args.verbose: print("building model")

generator = MarkovGenerator(ngram_size=args.ngram_size)

with open(args.source_text_location, 'r') as source_file:
    source_text = source_file.read()
    generator.ingest_text(source_text)

if args.verbose: print ("generating string")
chain_sentence = generator.generate_string(args.output_length, args.use_weighted_transitions)

print(chain_sentence)
