#!/usr/bin/env python3

import argparse
from  markov_generator import MarkovGenerator

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")
parser.add_argument("source_text_location", help="source text file")
parser.add_argument("output_length", help="length of sentence to generate", type=int)

args = parser.parse_args()

if args.verbose: print("starting markov generator")

if args.verbose:
	print("source file: {}".format(args.source_text_location))
	print("output length: {}".format(args.output_length))

if args.verbose: print("building model")

generator = MarkovGenerator()

with open(args.source_text_location, 'r') as source_file:
	source_text = source_file.read()
	generator.ingest_text(source_text)

if args.verbose: print ("generating string")
chain_sentence = generator.generate_string(args.output_length, True)

print(chain_sentence)