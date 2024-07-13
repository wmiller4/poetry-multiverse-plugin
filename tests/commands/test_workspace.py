import pytest
from poetry_multiverse_plugin.commands.workspace import WorkspaceCommand
from tests.conftest import ProjectFactory
from tests.utils import command


def test_workspace_not_found(project: ProjectFactory):
    root = project()
    cmd = command(root, WorkspaceCommand)
    assert cmd.execute() == 1


def test_workspace_base_class(project: ProjectFactory):
    root = project(workspace_root=True)
    cmd = command(root, WorkspaceCommand)
    with pytest.raises(NotImplementedError):
        cmd.execute()