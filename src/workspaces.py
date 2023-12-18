import copy
import json
import pathlib
import typing


class _WorkspacePath(typing.TypedDict):
    path: str


class _WorkspaceTemplate(typing.TypedDict):
    folders: list[_WorkspacePath]
    settings: dict


_WORKSPACE_TEMPLATE = _WorkspaceTemplate(folders=[_WorkspacePath(path="")], settings={})


def generate(*, source: pathlib.Path, destination: pathlib.Path):
    workspace = copy.deepcopy(_WORKSPACE_TEMPLATE)
    workspace["folders"][0]["path"] = str(source.relative_to(destination, walk_up=True))
    file = destination / f"{source.name}.code-workspace"

    with file.open("w") as fh:
        json.dump(workspace, fh, indent=4, sort_keys=True)
