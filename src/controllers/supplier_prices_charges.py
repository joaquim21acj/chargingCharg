from services import supplier_prices_charges_service as service
from entities.charge import validate_json_charges, charge_from_dict
import logging
import os

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(
                        os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def get_supplier_prices_charges_pretty() -> tuple:
    """
        Function that return the supplier prices and charges,
        make a requisition to the server, than convert
        the result from supplier prices and transactions into
        supplier prices and charges
    """
    res, cod = service.get_supplier_charges()
    if cod == 200:
        err = validate_json_charges(res)
        if err:
            logger.error(err)
            return "Problem with the input from remote server", cod
        res["charges"] = res["transactions"]
        del res["transactions"]
        return res, cod
    else:
        return "Not able to recieve information from server", cod


def get_charges_pretty() -> tuple:
    """
        Function that returns the charges from converting it
        to the class
    """
    res, cod = service.get_supplier_charges()
    if cod == 200:
        err = validate_json_charges(res)
        if err:
            logger.error(err)
            return "Problem with the input from remote server", cod

        list_charges = []
        list_errs = []
        for transaction in res["transactions"]:
            try:
                
                charge = charge_from_dict(transaction)
                list_charges.append(charge)
            except Exception as e:
                err = dict()
                err["transaction"] = transaction
                err["error"] = str(e)
                list_errs.append(err)

        if list_errs:
            logger.error("This erros happened after the casting process:")
            for error in list_errs:
                logger.error(f"Dict:\n{error['transaction']}\nError:\n{error['error']}")
        charges = dict()
        charges["charges"] = list_charges
        return charges, cod
    else:
        return "Not able to recieve information from server", cod
