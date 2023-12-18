#!/usr/bin/env python3
import pathlib
import typing

from src import arguments, workspaces

HOME = pathlib.Path.home()


# TODO: Determine using TOML config
def resolve_target_directory(args: arguments.Arguments):
    target_directory = HOME / "Workspaces"
    sub_directory: str = ""

    for name in arguments.FLAGS:
        if typing.cast(bool, getattr(args, name, False)):
            sub_directory = name

    return target_directory / sub_directory if sub_directory else target_directory


def main():
    args = arguments.parse()
    target_directory = resolve_target_directory(args)

    for directory in map(pathlib.Path.resolve, args.directories):
        workspaces.generate(source=directory, destination=target_directory)


if __name__ == "__main__":
    main()
