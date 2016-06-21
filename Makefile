init:
	pip install -r requirements.txt

test:
	python -m unittest discover -v tests

clean:
	rm -f `find markov_generator -name '*.pyc'`
	rm -f `find markov_generator -name '*.pyo'`
	rm -f `find . -name '*~'`
	rm -rf build iso dist api markov_text_generator-$(VERSION) markov_text_generator.egg-info
