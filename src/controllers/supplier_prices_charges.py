from services import supplier_prices_charges_service as service


def get_supplier_prices_charges_pretty():
    res, cod = service.get_supplier_charges()
    if cod == 200:
        res["charges"] = res["transactions"]
        del res["transactions"]
        return res, cod
    else:
        return "Not able to recieve information from server", cod
