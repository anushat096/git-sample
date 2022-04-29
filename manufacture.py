import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy_utils import JSONType

from base import Base

class ManufacturingAssumption(Base):
    __tablename__ = 'manufacturing_assumptions'
    manufacturing_assumption_id = Column(Integer, primary_key = True, nullable = False)
    product_name = Column(Integer, nullable=False)
    production_step = Column(String, nullable=False)
    uom = Column(String, nullable=False)
    unit_name = Column(String, nullable=False)
    process = Column(String, nullable=False)
    assumption = Column(String, nullable=False)
    year_based_projection = Column(JSONType, nullable=False)
    baseline_id = Column(Boolean, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )
    created_by = Column(String, nullable=False)
    modified_by = Column(String, nullable=False)

