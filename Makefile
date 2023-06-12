precommit:
	poetry run pre-commit run --all-files

pylint:
	@pylint my_library/**/**.py
