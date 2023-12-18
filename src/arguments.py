import argparse
import pathlib


class Arguments(argparse.Namespace):
    __slots__ = ("_cached_repr", "_flags", "directories", "cli", "fork", "third_party", "work")

    def __init__(self):
        self._cached_repr = ""
        self._flags = ("cli", "fork", "third_party", "work")
        self.cli = False
        self.fork = False
        self.third_party = False
        self.work = False

    def __str__(self):
        return self._cached_repr or self._generate_and_cache_repr()

    def _generate_and_cache_repr(self):
        if enabled_flags := [name for name in self._flags if getattr(self, name)]:
            formatted_flags = " ".join(enabled_flags)
            self._cached_repr = f"<Namespace directories={self.directories} {formatted_flags}>"
        else:
            self._cached_repr = f"<Namespace directories={self.directories}>"

        return self._cached_repr


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
