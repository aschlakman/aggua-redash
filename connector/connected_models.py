from typing import List
from pydantic import BaseModel

from redash_collector.models import QueryModel, DashboardModel, TableModel


class ConnectedQueryModel(BaseModel):
    query: QueryModel
    tables: List[TableModel]


class ConnectedDashboardModel(BaseModel):
    dashboard: DashboardModel
    queries: List[ConnectedQueryModel]
