precommit:
	poetry run pre-commit run --all-files

pylint:
	@pylint my_library/**/**.py
	@pylint tests/**/**.py

mypy:
	@mypy my_library
	@mypy tests

test:
	@pytest --cov=my_library --cov-report=term-missing tests
