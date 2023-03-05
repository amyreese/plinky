# Copyright Amethyst Reese
# Licensed under the MIT license

import logging
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib

from .types import Config, Link, Page

LOG = logging.getLogger(__name__)


def load_config(root: Path) -> Config:
    config_path = root / "site.toml"
    document = tomllib.loads(config_path.read_text())

    def linkify(tables: list[dict[str, str]]) -> list[Link]:
        if not isinstance(tables, list):
            raise ValueError
        return [
            Link(
                url=tbl.pop("url", Link.url),
                text=tbl.pop("text", Link.text),
                brand=tbl.pop("brand", Link.brand),
                icon=tbl.pop("icon", Link.icon),
                image=tbl.pop("image", Link.image),
                extra=tbl,
            )
            for tbl in tables
        ]

    socials = linkify(document.pop("social", []))
    links = linkify(document.pop("link", []))

    tbl = document.pop("page", {})
    page = Page(
        title=tbl.pop("title", Page.title),
        image=tbl.pop("image", Page.image),
        tagline=tbl.pop("tagline", Page.tagline),
        body=tbl.pop("body", Page.body),
        footer=tbl.pop("footer", Page.footer),
        socials=socials,
        links=links,
        extra=tbl,
    )

    if document:
        keys = list(document.keys())
        LOG.warning("unsupported elements in site.toml: %r", keys)

    return Config(root=root, page=page)
