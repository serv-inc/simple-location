.PHONY: push lint

lint:
	uv run black -C location
	uv run pylint location
	uv run ty check location
	uv run mypy location

push: lint
	git push github

run:
	python -m location.util.main

