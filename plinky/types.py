# Copyright Amethyst Reese
# Licensed under the MIT license

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Link:
    url: str = ""
    text: str = ""
    brand: str = ""
    icon: str = ""
    image: str = ""
    extra: dict[str, str] = field(default_factory=dict)


@dataclass
class Page:
    title: str = "Plinky"
    author: str = "Anonymous Penguin"
    image: str = "images/avatar.png"
    tagline: str = "A neat set of links"
    body: str = ""
    footer: str = ""
    socials: list[Link] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)
    extra: dict[str, str] = field(default_factory=dict)


@dataclass
class Config:
    root: Path
    page: Page
