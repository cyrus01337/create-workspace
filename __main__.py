#!/usr/bin/env python3
import argparse
import copy
import json
import pathlib
import typing


# TODO: Move to module
class WorkspacePath(typing.TypedDict):
    path: str


class WorkspaceTemplate(typing.TypedDict):
    folders: list[WorkspacePath]
    settings: dict


WORKSPACE_TEMPLATE = WorkspaceTemplate(folders=[WorkspacePath(path="")], settings={})


# TODO: Move to module
# TODO: Use __slots__
class Namespace:
    directories: list[pathlib.Path]
    cli: bool
    fork: bool
    third_party: bool
    work: bool
    name: str

    # TODO: Refactor?
    def __str__(self):
        return (
            "<Namespace "
            f"name={self.name} "
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
PARSER.add_argument("--name", type=str, required=False, help="Set filename for generated workspace file")


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
        workspace = copy.deepcopy(WORKSPACE_TEMPLATE)
        workspace["folders"][0]["path"] = str(directory.relative_to(target_directory, walk_up=True))
        filename = args.name or directory.name
        workspace_file = target_directory / f"{filename}.code-workspace"

        with workspace_file.open("w") as fh:
            json.dump(workspace, fh, indent=4, sort_keys=True)


if __name__ == "__main__":
    main()
