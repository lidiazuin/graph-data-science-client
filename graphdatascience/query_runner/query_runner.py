from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Dict, List, Optional

from pandas import DataFrame

from ..call_parameters import CallParameters
from ..server_version.server_version import ServerVersion
from .graph_constructor import GraphConstructor


class EndpointType(Enum):
    PROCEDURE = "PROCEDURE"
    FUNCTION = "FUNCTION"


class QueryRunner(ABC):
    def call_function(
        self,
        endpoint: str,
        params: Optional[CallParameters] = None,
        yields: Optional[List[str]] = None,
        database: Optional[str] = None,
        custom_error: bool = True,
    ) -> DataFrame:
        return self.call_endpoint(
            type=EndpointType.FUNCTION,
            endpoint=endpoint,
            yields=yields,
            params=params,
            database=database,
            custom_error=custom_error,
        )

    def call_procedure(
        self,
        endpoint: str,
        params: Optional[CallParameters] = None,
        yields: Optional[List[str]] = None,
        database: Optional[str] = None,
        logging: bool = False,
        custom_error: bool = True,
    ) -> DataFrame:
        return self.call_endpoint(
            type=EndpointType.PROCEDURE,
            endpoint=endpoint,
            yields=yields,
            params=params,
            database=database,
            custom_error=custom_error,
        )

    @abstractmethod
    def call_endpoint(
        self,
        type: EndpointType,
        endpoint: str,
        params: Optional[CallParameters],
        yields: Optional[List[str]] = None,
        database: Optional[str] = None,
        logging: bool = False,
        custom_error: bool = True,
    ) -> DataFrame:
        pass

    @abstractmethod
    def run_cypher(
        self,
        query: str,
        params: Optional[Dict[str, Any]] = None,
        database: Optional[str] = None,
        custom_error: bool = True,
    ) -> DataFrame:
        pass

    @abstractmethod
    def set_database(self, database: str) -> None:
        pass

    @abstractmethod
    def set_bookmarks(self, bookmarks: Optional[Any]) -> None:
        pass

    def close(self) -> None:
        pass

    @abstractmethod
    def create_graph_constructor(
        self, graph_name: str, concurrency: int, undirected_relationship_types: Optional[List[str]]
    ) -> GraphConstructor:
        pass

    @abstractmethod
    def database(self) -> Optional[str]:
        pass

    @abstractmethod
    def bookmarks(self) -> Optional[Any]:
        pass

    @abstractmethod
    def last_bookmarks(self) -> Optional[Any]:
        pass

    def set_server_version(self, _: ServerVersion) -> None:
        pass
