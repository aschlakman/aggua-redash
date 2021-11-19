import os

from redash_toolbelt import Redash
from redash_collector.table_retriever import get_tables
from redash_collector.dashboard_retriever import get_dashboards
from redash_collector.query_retriever import get_queries

key = os.getenv('TOKEN')
url = 'https://app.redash.io/hasadna'
client = Redash(url, key)


if __name__ == '__main__':
    qs = get_queries(client)
    print(qs)

    ds = get_dashboards(client)
    print(ds)

    ts = get_tables(client)
    print(ts)
