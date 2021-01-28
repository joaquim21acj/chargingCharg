from services import supplier_prices_charges_service as service


def get_supplier_prices_charges_pretty():
    """
        Function that receaves the request to return supplier prices
        and charges, make a requisition to the server, than convert
        the result from supplier prices and transactions into
        supplier prices and charges
    """
    res, cod = service.get_supplier_charges()
    if cod == 200:
        res["charges"] = res["transactions"]
        del res["transactions"]
        return res, cod
    else:
        return "Not able to recieve information from server", cod
