from typing import List

from redash_toolbelt import Redash

from redash_collector.models.table import TableModel


def get_tables(url, key) -> List[TableModel]:
    client = Redash(url, key)
    tables: List[TableModel] = []
    data_sources = client.get_data_sources()
    for data_source in data_sources:
        data_source_id = data_source['id']
        schema_type = data_source['syntax']
        # Copied from redash toolbelt example, a little hacky
        schemas = client._get(f"api/data_sources/{data_source_id}/schema").json().get("schema", [])
        for schema in schemas:
            table_name = schema['name']
            column_names = schema['columns']
            # TODO: add missing id
            table = TableModel(id=0,
                               data_source_id=data_source_id,
                               table_schema=schema_type,
                               name=table_name,
                               columns=column_names,
                               )
            tables.append(table)
    return tables
