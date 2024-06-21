from collections import defaultdict
from dataclasses import dataclass
from typing import Iterator
from poetry.core.packages.package import Package
from poetry.poetry import Poetry
from poetry.repositories.repository_pool import RepositoryPool

from poetry_multiverse_plugin.dependencies import Record


@dataclass
class Packages:
    records: dict[str, list[Record[Package]]]

    @staticmethod
    def from_projects(*projects: Poetry) -> 'Packages':
        deps: dict[str, list[Record[Package]]] = defaultdict(list)
        for project in projects:
            for dep in project.locker.locked_repository().packages:
                deps[dep.complete_name].append(Record(project, dep))
        return Packages(deps)
    
    def __iter__(self) -> Iterator[Package]:
        for record in self.records.values():
            for package in record:
                yield package.value
    
    @property
    def repository_pool(self) -> RepositoryPool:
        return RepositoryPool.from_packages(list(self), None)
