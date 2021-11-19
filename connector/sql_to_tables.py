"""
Mock service to retrieve tables mentioned in sql.
(Similar to redash-toolbelt/redash_toolbelt/examples/find_table_names.py)
"""
from typing import List

from redash_collector.models import TableModel, QueryModel


def get_connected_tables(query: QueryModel) -> List[TableModel]:
    pass
