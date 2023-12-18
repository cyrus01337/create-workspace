#!/usr/bin/env python3
import argparse
import pathlib

from src import workspaces


# TODO: Move to module
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
# TODO: Assign sub-directory name as default value for all sub-directory flags
# and reflect in get_target_directory
#
# https://docs.python.org/3/library/argparse.html#action
PARSER.add_argument("--cli", action="store_true", required=False, help="Generate in CLI sub-directory")
PARSER.add_argument("--fork", action="store_true", required=False, help="Generate in forks sub-directory")
PARSER.add_argument(
    "--third-party", action="store_true", dest="third_party", required=False, help="Generate in third-party sub-directory"
)
PARSER.add_argument("--work", action="store_true", required=False, help="Generate in work sub-directory")


# TODO: Determine using TOML config
def get_target_directory(args: Namespace):
    target_directory = pathlib.Path.home() / "Workspaces"
    sub_directory: str = ""

    if args.cli:
        sub_directory = "cli"
    elif args.fork:
        sub_directory = "fork"
    elif args.third_party:
        sub_directory = "third-party"
    elif args.work:
        sub_directory = "work"

    return target_directory / sub_directory if sub_directory else target_directory


def main():
    args: Namespace = PARSER.parse_args(namespace=Namespace())
    target_directory = get_target_directory(args)

    for directory in map(pathlib.Path.resolve, args.directories):
        workspaces.generate(source=directory, destination=target_directory)


if __name__ == "__main__":
    main()
