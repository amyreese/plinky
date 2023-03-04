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

    error = False

    links: list[Link] = []
    link_tables = document.pop("link", [])
    for tbl in link_tables:
        url = tbl.pop("url", "")
        text = tbl.pop("text", "")
        brand = tbl.pop("brand", Link.brand)
        icon = tbl.pop("icon", Link.icon)

        if not url or not text:
            LOG.error("url and text are required for links: %r", tbl)

        links.append(Link(url=url, text=text, brand=brand, icon=icon, extra=tbl))

    tbl = document.pop("page", {})
    title = tbl.pop("title", Page.title)
    image = tbl.pop("image", Page.image)
    tagline = tbl.pop("tagline", Page.tagline)
    body = tbl.pop("body", Page.body)
    footer = tbl.pop("footer", Page.footer)

    page = Page(
        title=title,
        image=image,
        tagline=tagline,
        body=body,
        footer=footer,
        links=links,
        extra=tbl,
    )

    if document:
        keys = list(document.keys())
        LOG.warning("unsupported elements in site.toml: %r", keys)

    if error:
        raise RuntimeError("invalid site config")

    return Config(root=root, page=page)
