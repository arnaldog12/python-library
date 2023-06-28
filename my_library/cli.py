"""CLI commands"""

import typer
from typing_extensions import Annotated

from my_library.cv.operations import bright, crop
from my_library.io.image import load_image, save_image

app = typer.Typer()


@app.command(name="bright")
def bright_cli(image_path: str, value: int, output_path: Annotated[str, typer.Option()]) -> None:
    """CLI command for bright operation"""
    image = load_image(image_path)
    res = bright(image, value)
    save_image(res, output_path)


@app.command(name="crop")
def crop_cli(image_path: str, top: int, left: int, bottom: int, right: int, output_path: str) -> None:
    """CLI command for crop operation"""
    image = load_image(image_path)
    res = crop(image, top, left, bottom, right)
    save_image(res, output_path)
