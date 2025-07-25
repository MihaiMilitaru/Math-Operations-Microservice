
from pydantic import BaseModel

class PowRequest(BaseModel):
    base: float
    exponent: float

class FibRequest(BaseModel):
    n: int

class FactRequest(BaseModel):
    n: int
