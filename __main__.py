#!/usr/bin/env python3
import pathlib

from src import arguments, workspaces

HOME = pathlib.Path.home()


# TODO: Determine using TOML config
def get_target_directory(args: arguments.Arguments):
    target_directory = HOME / "Workspaces"
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
    args = arguments.parse()
    target_directory = get_target_directory(args)

    for directory in map(pathlib.Path.resolve, args.directories):
        workspaces.generate(source=directory, destination=target_directory)


if __name__ == "__main__":
    main()
