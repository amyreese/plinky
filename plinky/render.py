# Copyright Amethyst Reese
# Licensed under the MIT license

from dataclasses import replace
from textwrap import dedent

from jinja2 import Environment, FileSystemLoader
from markdown import Markdown

from .types import Config


def render_site(config: Config) -> str:
    markdown = Markdown(extensions=["extra", "smarty"])
    env = Environment(
        loader=FileSystemLoader([config.root]),
        lstrip_blocks=True,
        trim_blocks=True,
    )
    tpl = env.get_template("page.html")

    page = config.page
    page = replace(
        page,
        tagline=markdown.convert(dedent(page.tagline)),
        body=markdown.convert(dedent(page.body)),
        footer=markdown.convert(dedent(page.footer)),
    )

    result = tpl.render(
        page=page,
        socials=page.socials,
        links=page.links,
    )
    return result
