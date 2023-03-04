# Copyright Amethyst Reese
# Licensed under the MIT license

import logging
import sys
from pathlib import Path

import click

try:
    from rich import print
except ImportError:
    from pprint import pprint as print

from .config import load_config
from .render import render_site


@click.group()
@click.option("--verbose / --quiet", "-v / -q", is_flag=True, default=None)
def main(verbose: bool | None):
    match verbose:
        case True:
            level = logging.DEBUG
        case False:
            level = logging.ERROR
        case _:
            level = logging.WARNING

    logging.basicConfig(level=level, stream=sys.stderr)


@main.command("debug")
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    default=Path.cwd(),
)
def debug(path: Path) -> None:
    """
    Dump debug info about site configuration
    """
    config = load_config(path)
    print(config)


@main.command("render")
@click.option(
    "--out",
    "-o",
    type=click.Path(
        exists=False,
        file_okay=True,
        dir_okay=False,
        writable=True,
        resolve_path=True,
        allow_dash=True,
        path_type=Path,
    ),
    default=None,
)
@click.argument(
    "path",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, resolve_path=True, path_type=Path
    ),
    default=Path.cwd(),
)
def render(path: Path, out: Path | None) -> None:
    config = load_config(path)
    content = render_site(config)
    if out == Path("-"):
        sys.stdout.write(content)
        sys.stdout.flush()
    else:
        if out is None:
            out = config.root / "index.html"
        out.write_text(content)


@main.command("serve")
@click.argument(
    "path",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, resolve_path=True, path_type=Path
    ),
    default=Path.cwd(),
)
def serve(path: Path) -> None:
    raise NotImplementedError
