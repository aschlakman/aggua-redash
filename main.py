import os

from redash_toolbelt import Redash
from redash_collector import get_tables, get_dashboards, get_queries

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
