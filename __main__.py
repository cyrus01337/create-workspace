#!/usr/bin/env python3
import argparse
import pathlib


# TODO: Use __slots__
class Namespace:
    directories: list[pathlib.Path]
    cli: bool
    fork: bool
    third_party: bool
    work: bool

    # TODO: Refactor?
    def __str__(self):
        return (
            "<Namespace "
            f"directories={self.directories}"
            f"{' cli' if self.cli else ''}"
            f"{' fork' if self.fork else ''}"
            f"{' third_party' if self.third_party else ''}"
            f"{' work' if self.work else ''}"
            ">"
        )


CWD = pathlib.Path.cwd()
PARSER = argparse.ArgumentParser(
    prog="create-workspace",
    description="CLI tool for creating workspaces using my personal environment",
    add_help=True,
    allow_abbrev=True,
)
PARSER.add_argument("directories", nargs="*", type=pathlib.Path, default=[CWD], help="Generate in CLI sub-directory")
PARSER.add_argument("--cli", action="store_true", required=False, help="Generate in CLI sub-directory")
PARSER.add_argument("--fork", action="store_true", required=False, help="Generate in forks sub-directory")
PARSER.add_argument(
    "--third-party", action="store_true", dest="third_party", required=False, help="Generate in third-party sub-directory"
)
PARSER.add_argument("--work", action="store_true", required=False, help="Generate in work sub-directory")


def main():
    args = PARSER.parse_args(namespace=Namespace())

    print(args)


if __name__ == "__main__":
    main()
