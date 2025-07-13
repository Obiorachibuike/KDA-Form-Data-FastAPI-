from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
from . import crud, schemas
from .database import SessionLocal
from .models import WheelSpecification

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/api/forms/wheel-specifications", response_model=schemas.WheelCreateResponse, status_code=201)
def create_wheel_spec(spec: schemas.WheelSpecificationCreate, db: Session = Depends(get_db)):
    existing = db.query(WheelSpecification).filter_by(form_number=spec.formNumber).first()
    if existing:
        raise HTTPException(status_code=400, detail="Form number already exists.")
    wheel = crud.create_wheel_specification(db, spec)
    return {
        "data": {
            "formNumber": wheel.form_number,
            "status": "Saved",
            "submittedBy": wheel.submitted_by,
            "submittedDate": wheel.submitted_date,
        },
        "message": "Wheel specification submitted successfully.",
        "success": True
    }

@router.get("/api/forms/wheel-specifications", response_model=schemas.WheelResponse)
def get_wheel_specs(
    formNumber: Optional[str] = Query(None),
    submittedBy: Optional[str] = Query(None),
    submittedDate: Optional[date] = Query(None),
    db: Session = Depends(get_db)
):
    results = crud.get_filtered_wheel_specs(db, formNumber, submittedBy, submittedDate)
    formatted = []
    for r in results:
        formatted.append({
            "formNumber": r.form_number,
            "submittedBy": r.submitted_by,
            "submittedDate": r.submitted_date,
            "fields": {
                "axleBoxHousingBoreDia": r.axle_box_housing_bore_dia,
                "bearingSeatDiameter": r.bearing_seat_diameter,
                "condemningDia": r.condemning_dia,
                "intermediateWWP": r.intermediate_wwp,
                "lastShopIssueSize": r.last_shop_issue_size,
                "rollerBearingBoreDia": r.roller_bearing_bore_dia,
                "rollerBearingOuterDia": r.roller_bearing_outer_dia,
                "rollerBearingWidth": r.roller_bearing_width,
                "treadDiameterNew": r.tread_diameter_new,
                "variationSameAxle": r.variation_same_axle,
                "variationSameBogie": r.variation_same_bogie,
                "variationSameCoach": r.variation_same_coach,
                "wheelDiscWidth": r.wheel_disc_width,
                "wheelGauge": r.wheel_gauge,
                "wheelProfile": r.wheel_profile
            }
        })
    
    return {
        "data": formatted,
        "message": "Filtered wheel specification forms fetched successfully.",
        "success": True
    }