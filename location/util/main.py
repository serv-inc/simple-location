#! /usr/bin/env python3
"""show the current config"""

from .. import config

if __name__ == "__main__":
    print(config.Config.load())
