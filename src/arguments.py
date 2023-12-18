import argparse
import pathlib


class Arguments:
    __slots__ = ("directories", "cli", "fork", "third_party", "work")

    directories: list[pathlib.Path]
    cli: bool
    fork: bool
    third_party: bool
    work: bool

    # TODO: Convert to cached property
    @property
    def _str_attrs(self):
        return {
            "cli": self.cli,
            "fork": self.fork,
            "third_party": self.third_party,
            "work": self.work,
        }

    # TODO: Check if results of dunder methods can be cached
    def __str__(self):
        enabled_flags: list[str] = []

        for name in self.__slots__[1:]:
            flag_enabled = self._str_attrs[name]

            if not flag_enabled:
                continue

            enabled_flags.append(name)

        formatted_flags = " ".join(enabled_flags)

        return f"<Namespace directories={self.directories} {formatted_flags}>"


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
