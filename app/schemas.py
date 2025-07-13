from pydantic import BaseModel
from datetime import date
from typing import List

class WheelFields(BaseModel):
    axleBoxHousingBoreDia: str
    bearingSeatDiameter: str
    condemningDia: str
    intermediateWWP: str
    lastShopIssueSize: str
    rollerBearingBoreDia: str
    rollerBearingOuterDia: str
    rollerBearingWidth: str
    treadDiameterNew: str
    variationSameAxle: str
    variationSameBogie: str
    variationSameCoach: str
    wheelDiscWidth: str
    wheelGauge: str
    wheelProfile: str

class WheelSpecificationCreate(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields

class WheelSpecificationOut(BaseModel):
    formNumber: str
    submittedBy: str
    submittedDate: date
    fields: WheelFields

class WheelSpecificationStatus(BaseModel):
    formNumber: str
    status: str
    submittedBy: str
    submittedDate: date

class WheelCreateResponse(BaseModel):
    data: WheelSpecificationStatus
    message: str
    success: bool

class WheelResponse(BaseModel):
    data: List[WheelSpecificationOut]
    message: str
    success: bool