from sqlalchemy.orm import Session
from .models import WheelSpecification
from .schemas import WheelSpecificationCreate
from typing import Optional
from datetime import date

def create_wheel_specification(db: Session, spec: WheelSpecificationCreate) -> WheelSpecification:
    wheel = WheelSpecification(
        form_number=spec.formNumber,
        submitted_by=spec.submittedBy,
        submitted_date=spec.submittedDate,
        axle_box_housing_bore_dia=spec.fields.axleBoxHousingBoreDia,
        bearing_seat_diameter=spec.fields.bearingSeatDiameter,
        condemning_dia=spec.fields.condemningDia,
        intermediate_wwp=spec.fields.intermediateWWP,
        last_shop_issue_size=spec.fields.lastShopIssueSize,
        roller_bearing_bore_dia=spec.fields.rollerBearingBoreDia,
        roller_bearing_outer_dia=spec.fields.rollerBearingOuterDia,
        roller_bearing_width=spec.fields.rollerBearingWidth,
        tread_diameter_new=spec.fields.treadDiameterNew,
        variation_same_axle=spec.fields.variationSameAxle,
        variation_same_bogie=spec.fields.variationSameBogie,
        variation_same_coach=spec.fields.variationSameCoach,
        wheel_disc_width=spec.fields.wheelDiscWidth,
        wheel_gauge=spec.fields.wheelGauge,
        wheel_profile=spec.fields.wheelProfile
    )
    db.add(wheel)
    db.commit()
    db.refresh(wheel)
    return wheel

def get_filtered_wheel_specs(
    db: Session,
    form_number: Optional[str],
    submitted_by: Optional[str],
    submitted_date: Optional[date]
):
    query = db.query(WheelSpecification)
    
    if form_number:
        query = query.filter(WheelSpecification.form_number == form_number)
    if submitted_by:
        query = query.filter(WheelSpecification.submitted_by == submitted_by)
    if submitted_date:
        query = query.filter(WheelSpecification.submitted_date == submitted_date)
    
    return query.all()