from __future__ import annotations

import uuid

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/data",
    tags=["data"],
    responses={404: {"description": "not found"}},
)


class FritzDeviceModel(BaseModel):
    model: str
    os_version: str
    services: dict[str, list[str]]
    detected_capabilities: list[str]
    action_results: dict[str, dict[str, dict[str, str]]]


class Donation(BaseModel):
    exporter_version: str
    fritzdevice: FritzDeviceModel


@router.post("/donate")
async def post_data(donation: Donation):
    donation_id = uuid.uuid4()

    with open(f"/donations/{donation_id}.json", "w") as donation_file:
        donation_file.write(donation.json())

    return {"donation_id": donation_id}
