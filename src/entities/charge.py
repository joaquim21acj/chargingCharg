from dataclasses import dataclass
from datetime import datetime
from uuid import UUID
from typing import Any
import dateutil.parser


def validate_json_charges(obj) -> str:
    msg = ""
    if "transactions" not in obj:
        msg += "* 'transactions' not in the json from remote server"
    if "supplier_prices" not in obj:
        msg += "\n* 'supplier_prices' not in the json from remote server"


def from_datetime(x) -> datetime:
    return dateutil.parser.parse(x)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class Charge:
    charging_end: datetime
    charging_start: datetime
    country_code: str
    evseid: str
    meter_value_end: str
    meter_value_start: str
    metering_signature: str
    partner_product_id: bool
    proveider_id: str
    session_id: UUID
    session_end: datetime
    session_start: datetime
    uid: str

    @staticmethod
    def from_dict(obj) -> 'Charge':
        """
            This function casts the obj coming from remote server
                into Charge class.
            The "Partner product ID" sometimes comes with false
                so it's filed with ""
        """
        assert isinstance(obj, dict)
        charging_end = from_datetime(obj.get("Charging end"))
        charging_start = from_datetime(obj.get("Charging start"))
        country_code = from_str(obj.get("CountryCode"))
        evseid = from_str(obj.get("EVSEID"))
        meter_value_end = from_str(obj.get("Meter value end"))
        meter_value_start = from_str(obj.get("Meter value start"))
        metering_signature = from_str(obj.get("Metering signature"))
        partner_product_id = "" if isinstance(obj.get("Partner product ID"), bool) else obj.get("Partner product ID")
        proveider_id = from_str(obj.get("Proveider ID"))
        session_id = UUID(obj.get("Session ID"))
        session_end = from_datetime(obj.get("Session end"))
        session_start = from_datetime(obj.get("Session start"))
        uid = from_str(obj.get("UID"))
        return Charge(charging_end, charging_start, country_code, evseid,
                      meter_value_end, meter_value_start, metering_signature,
                      partner_product_id, proveider_id, session_id,
                      session_end, session_start, uid)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Charging end"] = self.charging_end.isoformat()
        result["Charging start"] = self.charging_start.isoformat()
        result["CountryCode"] = from_str(self.country_code)
        result["EVSEID"] = from_str(self.evseid)
        result["Meter value end"] = from_str(self.meter_value_end)
        result["Meter value start"] = from_str(self.meter_value_start)
        result["Metering signature"] = from_str(self.metering_signature)
        result["Partner product ID"] = from_bool(self.partner_product_id)
        result["Proveider ID"] = from_str(self.proveider_id)
        result["Session ID"] = str(self.session_id)
        result["Session end"] = self.session_end.isoformat()
        result["Session start"] = self.session_start.isoformat()
        result["UID"] = from_str(self.uid)
        return result


def charge_from_dict(obj) -> Charge:
    return Charge.from_dict(obj)
