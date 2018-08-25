setup:
	pip install pipenv
	pipenv install --dev

run:
	python app/bot.py

test:
	pytest