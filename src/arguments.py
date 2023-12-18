import argparse
import pathlib


class Arguments(argparse.Namespace):
    __slots__ = ("_cached_str_attrs", "directories", "cli", "fork", "third_party", "work")

    def __init__(self):
        self._cached_str_attrs: dict[str, bool] = {}

    @property
    def _str_attrs(self):
        if not self._cached_str_attrs:
            self._cached_str_attrs = {
                "cli": self.cli,
                "fork": self.fork,
                "third_party": self.third_party,
                "work": self.work,
            }

        return self._cached_str_attrs

    # TODO: Check if results of dunder methods can be cached
    def __str__(self):
        enabled_flags: list[str] = []

        for name in self.__slots__[2:]:
            flag_enabled = self._str_attrs[name]

            if not flag_enabled:
                continue

            enabled_flags.append(name)

        if formatted_flags := " ".join(enabled_flags):
            return f"<Namespace directories={self.directories} {formatted_flags}>"

        return f"<Namespace directories={self.directories}>"


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
