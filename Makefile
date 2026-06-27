.PHONY: push lint

lint:
	uv run black -C .
	uv run pylint location.py
	uv run ty check location.py
	uv run mypy .

push: lint
	git push github
