from typing import Optional, Dict
from pydantic import BaseModel


class Query(BaseModel):
    id: int
    data_source_id: int
    name: str
    description: Optional[str]
    sql: str
    owner_name: str
    last_update_time: str

    @staticmethod
    def from_json(data: Dict):
        return Query(id=data['id'],
                     data_source_id=data['data_source_id'],
                     name=data['name'],
                     description=data['description'],
                     sql=data['query'],
                     owner_name=data['user'].get('name'),
                     last_update_time=data['retrieved_at'])
