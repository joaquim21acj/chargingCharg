# chargingCharg
The project to implement a unified system to charg eletric vehicles when using charging points in Europe.

## HOW TO RUN
First thing you need to do is to install the requirements, you can do it inside or out of the virtualenv:

```sh
pip install -r requirements.txt
```

After, you can run the project by using this commands:

```sh
python ./src/main.py
```

## Json information
In this project, there are a few jsons that the API returns, which are:

### Raw Json from server Supplier charges
```json
 "charges": [
        {
          "Charging end": "2019-05-22T21:18:56",
          "Charging start": "2019-05-22T08:47:45",
          "CountryCode": "MZ",
          "EVSEID": "CE*LMQ*L463*05",
          "Meter value end": "1856,633",
          "Meter value start": "1702,899",
          "Metering signature": "",
          "Partner product ID": false,
          "Proveider ID": "TV-PKI",
          "Session ID": "ac83107c-b41f-49a4-bf66-971b591fa41a",
          "Session end": "2019-05-23T01:26:52",
          "Session start": "2019-05-21T09:33:21",
          "UID": "c73f87fba7b482c5f5f2cf36686164d0"
        }
    ],
    "supplier_prices": [
        {
          "Company name": "Grundig mobile",
          "Currency": [
            "EUR",
            "€"
          ],
          "EVSE ID": "CE*LMQ*L463*05",
          "Identifier": "25368133-fd17-4e7b-a08e-1fee3b508ca3",
          "Product ID": false,
          "has complex minute price": false,
          "has max session Fee": false,
          "has minimum billing threshold": true,
          "has session fee": false,
          "max_session fee": "False",
          "min billing amount": "2,6657",
          "min_duration": "0.0533",
          "session Fee": "False",
          "simple minute price": "0.6206"
        }
    ]
```

### Charges after been casted
```json
"charges": [
        {
          "charging_end": "Fri, 23 Mar 2018 03:31:54 GMT",
          "charging_start": "Thu, 22 Mar 2018 13:25:17 GMT",
          "country_code": "SA",
          "evseid": "TB*UQT*Z888*57",
          "meter_value_end": "1724.537",
          "meter_value_start": "1234.6",
          "metering_signature": "",
          "partner_product_id": "LQ*VOW",
          "proveider_id": "OI-SKG",
          "session_end": "Fri, 23 Mar 2018 14:49:23 GMT",
          "session_id": "a4451497-aff2-4a41-8d29-dbd4ad128d7f",
          "session_start": "Thu, 22 Mar 2018 13:25:17 GMT",
          "uid": "0541f9a53d86dbf2a89f8d69ed182b98"
        }
    ]
```

