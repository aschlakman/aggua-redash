from typing import List

from sql_to_tables import get_connected_tables

from redash_collector.models import QueryModel, DashboardModel
from connector.connected_models import ConnectedQueryModel, ConnectedDashboardModel


def get_connected_queries(query: QueryModel) -> ConnectedQueryModel:
    connected_tables = get_connected_tables(query)
    return ConnectedQueryModel(query=query, tables=connected_tables)


def get_connected_dashboards(dashboard: DashboardModel) -> ConnectedDashboardModel:
    all_connected_queries: List[ConnectedQueryModel] = []
    if dashboard.widgets:
        for widget in dashboard.widgets:
            all_connected_queries.append(get_connected_queries(widget.query))
    return ConnectedDashboardModel(dashboard=dashboard, queries=all_connected_queries)
