# Markov Text Generator
This tool generates markov text of specified lengths based on an input document

## MarkovGenerator class

This class does the actual heavy listing of generating the Markov chain from an input document.

The constructor provides an optional arg, `ngram_size` (default of 2) to choose the size of the n-grams that are generated from the source text

`ingest_text` takes a string that represents the source text to generate a chain from

`generate_string` will spit out a string with `length` (optional, default 14) words. It also provides an optional `use_weighted_transition` arg to weight the next random n-gram choice while building the string

## generate.py

`generate.py` is a utility script to easily build random markov text from the command line
