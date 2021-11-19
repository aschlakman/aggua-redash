from typing import Optional, Dict, List
from pydantic import BaseModel


class TableModel(BaseModel):
    id: Optional[int]
    data_source_id: int
    table_schema: str
    name: str
    columns: List[str]
