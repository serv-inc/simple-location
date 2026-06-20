#! /usr/bin/env python
"""location set and retrieve"""

import pathlib
from dataclasses import dataclass
from typing import Optional


def user_dir() -> pathlib.Path:
    """user location storage"""
    return pathlib.Path.home() / ".config" / "location"


def system_dir() -> pathlib.Path:
    """system location storage"""
    return pathlib.Path("/etc/location")


@dataclass
class Config:
    """one location"""

    lat: float
    lon: float
    alt: float = 0.0
    path: Optional[pathlib.Path] = None

    @property
    def latitude(self) -> float:
        return self.lat

    @property
    def longitude(self) -> float:
        return self.lon

    @property
    def altitude(self) -> float:
        return self.alt

    @staticmethod
    def from_dir(d: pathlib.Path) -> "Config":
        lat = float((d / "latitude").open().read())
        lon = float((d / "longitude").open().read())
        try:
            alt = float((d / "altitude").open().read())
        except FileNotFoundError:
            alt = 0.0
        return Config(lat, lon, alt, path=d)

    @staticmethod
    def load() -> "Config":
        if system_dir().exists():
            return Config.from_dir(system_dir())
        if user_dir().exists():
            return Config.from_dir(user_dir())
        return Config(51.48, 0, 0, None)  # 'Greenwich'

    def save(self):
        assert self.path
        if not self.path.exists():
            self.path.mkdir()
        (self.path / "latitude").open("w").write(str(self.lat))
        (self.path / "longitude").open("w").write(str(self.lon))
        (self.path / "altitude").open("w").write(str(self.alt))


def get():
    return Config.load()


if __name__ == "__main__":
    print(Config.load())
