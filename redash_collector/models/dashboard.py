from typing import Optional, Dict, List
from pydantic import BaseModel

from redash_collector.models.query import QueryModel


class WidgetModel(BaseModel):
    id: int
    query: QueryModel

    @staticmethod
    def from_json(data: Dict):
        widget_id = data['id']
        query = QueryModel.from_json(data['visualization']['query'])
        return WidgetModel(id=widget_id, query=query)


class DashboardModel(BaseModel):
    id: int
    name: str
    slug: str
    owner_name: str
    last_update_time: Optional[str]
    widgets: Optional[List[WidgetModel]]

    @staticmethod
    def from_json(data: Dict):
        raw_widgets = data.get('widgets')
        if raw_widgets:
            widgets = [WidgetModel.from_json(widget_data) for widget_data in data['widgets']]
            w = widgets[0]
            last_update_time = max([widget.query.last_update_time for widget in widgets])
        else:
            widgets = None
            last_update_time = None

        return DashboardModel(id=data['id'],
                              name=data['name'],
                              slug=data['slug'],
                              owner_name=data['user'].get('name'),
                              last_update_time=last_update_time,
                              widgets=widgets,
                              )
