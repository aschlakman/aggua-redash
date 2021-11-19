requirements.txt contains project reqs.

redash_collector - methods to query redash objects (PART 1)
connector - represent connections between objects (PART 2)

In part 2, I wanted to keep the types as simple as possible.
Queries are connected to tables through their sql content - so I created a Model containing a query,
and the tables it connects to.

Dashboards can be connected to tables through their queries. To keep things simple,
dashboard widgets are replaced with ConnectedQueryModels - building on the previous objects.

The opposite direction (connecting tables to queries / dashboards) can be achieved by getting all queries / dashboards
and checking which ones contain a given table.
This is pretty inefficient, and a more efficient way would be to query the redash service for queries while filtering by
table name. However, I'm not sure that endpoint exists.
In the interest of saving time, I did it this way.
