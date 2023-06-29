# python-library
a python library example with well-know tools and best practices of software engineer

## features and tools
- `poetry` for requirements management

## setup

```sh
$ poetry new my-library
$ poetry add numpy Pillow "typer[all]"
$ poetry add --group dev black isort pytest pylint flake8 ruff mypy interrogate pre-commit "bandit[toml]" types-Pillow
$ pre-commmit install --install-hooks
```

## build

```sh
$ poetry build
$ pip install dist/my_library-0.1.0-py3-none-any.whl
```

library will be in `dist` folder

## CLI

```sh
$ my-library bright ~/Documents/image.jpg 100 --output-path ~/Documents/bright.jpg
$ my-library crop ~/Documents/image.jpg 150 150 500 500 ~/Documents/crop.jpg
```
