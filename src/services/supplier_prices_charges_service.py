from constants.supplier_prices_charges import URL, USER, PASSWORD
from requests.auth import HTTPBasicAuth
import requests


def get_supplier_charges():
    res = requests.get(URL, auth=HTTPBasicAuth(USER, PASSWORD))
    return res.json(), res.status_code
