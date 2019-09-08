setup:
	pip install pipenv
	pipenv install

run:
	python app.py

test:
	py.test