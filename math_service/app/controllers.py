
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import PowRequest, FibRequest, FactRequest
from app.services import compute_pow, compute_fibonacci, compute_factorial
from app.database import get_db, OperationLog

router = APIRouter()

@router.post("/math/pow")
def pow_route(req: PowRequest, db: Session = Depends(get_db)):
    result = compute_pow(req.base, req.exponent)
    db_log = OperationLog(operation="pow", input=str(req.dict()), output=str(result))
    db.add(db_log)
    db.commit()
    return {"result": result}

@router.post("/math/fibonacci")
def fib_route(req: FibRequest, db: Session = Depends(get_db)):
    result = compute_fibonacci(req.n)
    db_log = OperationLog(operation="fibonacci", input=str(req.dict()), output=str(result))
    db.add(db_log)
    db.commit()
    return {"result": result}

@router.post("/math/factorial")
def fact_route(req: FactRequest, db: Session = Depends(get_db)):
    result = compute_factorial(req.n)
    db_log = OperationLog(operation="factorial", input=str(req.dict()), output=str(result))
    db.add(db_log)
    db.commit()
    return {"result": result}
