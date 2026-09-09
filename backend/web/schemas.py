from datetime import date

from pydantic import BaseModel, ConfigDict, Field


class IndexInfo(BaseModel):
    index_code: str
    index_name: str


class Valuation(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    index_code: str
    index_name: str
    data: date
    pe_percentile: float = Field(ge=0, le=1)
    pb_percentile: float = Field(ge=0, le=1)