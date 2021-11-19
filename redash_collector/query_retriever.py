from typing import List

from redash_toolbelt import Redash

from redash_collector.models import QueryModel


def get_queries(client: 'Redash') -> List[QueryModel]:
    queries = client.paginate(client.queries)
    return [QueryModel.from_json(query) for query in queries]
