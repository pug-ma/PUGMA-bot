setup:
	pip install pipenv
	pipenv install
	pipenv install --dev

run:
	python app/bot.py

test:
	python tests/test.py