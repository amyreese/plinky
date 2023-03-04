# Copyright Amethyst Reese
# Licensed under the MIT license

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Link:
    url: str
    text: str
    brand: str = ""
    icon: str = ""
    extra: dict[str, str] = field(default_factory=dict)


@dataclass
class Page:
    title: str = "Plinky"
    image: str = "avatar.png"
    tagline: str = ""
    body: str = ""
    footer: str = ""
    links: list[Link] = field(default_factory=list)
    extra: dict[str, str] = field(default_factory=dict)


@dataclass
class Config:
    root: Path
    page: Page
