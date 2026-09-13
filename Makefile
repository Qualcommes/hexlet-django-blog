dev:
	uv run manage.py runserver

tree:
	tree -I __pycache__ -I conspect.txt

migrations:
	uv run manage.py makemigrations