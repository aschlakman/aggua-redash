from typing import List

from redash_toolbelt import Redash

from redash_collector.models import DashboardModel


def get_dashboards(client: 'Redash') -> List[DashboardModel]:
    dashboards = client.paginate(client.dashboards)
    return [DashboardModel.from_json(dashboard) for dashboard in dashboards]
