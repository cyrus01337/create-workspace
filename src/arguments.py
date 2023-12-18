import argparse
import pathlib


class Arguments:
    __slots__ = ("directories", "cli", "fork", "third_party", "work")
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


_CWD = pathlib.Path.cwd()
_PARSER = argparse.ArgumentParser(
    prog="create-workspace",
    description="CLI tool for creating workspaces using my personal environment",
    add_help=True,
    allow_abbrev=True,
)
_PARSER.add_argument("directories", nargs="*", type=pathlib.Path, default=[_CWD], help="Generate in CLI sub-directory")
# TODO: Assign sub-directory name as default value for all sub-directory flags
# and reflect in get_target_directory
#
# https://docs.python.org/3/library/argparse.html#action
_PARSER.add_argument("--cli", action="store_true", required=False, help="Generate in CLI sub-directory")
_PARSER.add_argument("--fork", action="store_true", required=False, help="Generate in forks sub-directory")
_PARSER.add_argument(
    "--third-party", action="store_true", dest="third_party", required=False, help="Generate in third-party sub-directory"
)
_PARSER.add_argument("--work", action="store_true", required=False, help="Generate in work sub-directory")


def parse():
    return _PARSER.parse_args(namespace=Arguments())
