from controllers import supplier_prices_charges as controller
from flask import Blueprint
from flask_cors import CORS

supplier_prices_charges_blueprint = Blueprint(
    'additional', __name__, url_prefix='/api')
CORS(supplier_prices_charges_blueprint)


@supplier_prices_charges_blueprint.route('/supplier-charges',
                                         methods=['GET'])
def get_supplier_prices_charges():
    res, cod = controller.get_supplier_prices_charges_pretty()
    return res, cod
