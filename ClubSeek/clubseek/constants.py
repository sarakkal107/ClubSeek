

'''
Schemas and DB Classes for validating API Request Schemas and Communicating with DB Tables
'''

# Request Schema for Adding Bars (/bars POST Request)
barSchema = {
    'type': 'array',
    "minItems": 1,
    'items': {
        'barName': {'type': 'string',  "minLength": 4, "maxLength": 30},
        'wowFactor': {'type': 'integer', "minimum": 1, "maximum": 100},
        'capacity': {'type': 'integer', "minimum": 1, "maximum": 1000},
        'currentTraffic': {'type': 'integer', "minimum": 1, "maximum": 1000},
        'address': {'type': 'string', "minLength": 4, "maxLength": 255},
    },
    'required': ['barName', 'wowFactor', 'capacity', 'currentTraffic']
}

# Request Schema for Deleting Bars (/bars DELETE Request)
barDeleteSchema = {
    'type': 'object',
    'properties': {
        'barName': {'type': 'string',  "minLength": 4, "maxLength": 30},
        'address': {'type': 'string',  "minLength": 4, "maxLength": 255}
    },
    'required': ['barName', 'address']
}

# Request Schema for Updating Bars (/bars PUT Request)
barUpdateSchema = {
    'type': 'object',
    'properties': {
        'barName': {'type': 'string',  "minLength": 4, "maxLength": 30},
        'wowFactorChange': {'type': 'integer', "minimum": 1, "maximum": 100},
        'capacityChange': {'type': 'integer', "minimum": 1, "maximum": 1000},
        'currentTrafficChange': {'type': 'integer', "minimum": 1, "maximum": 1000},
        'address': {'type': 'string', "minLength": 4, "maxLength": 255},
    },
    'required': ['barName', 'address']
}


# Request Schema for Choosing a Bar (/barSelection GET Request)
barAlgorithmSchema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string',  "minLength": 4, "maxLength": 30},
        'phoneNumber': {'type': 'string' , "minLength": 10, "maxLength": 15},
        'minWowFactor': {'type': 'integer', "minimum": 1, "maximum": 100},
        'maxTraffic': {'type': 'integer', "minimum": 1, "maximum": 1000},
        'preference': {'type': 'string'}
    },
    'required': ['name', 'phoneNumber']
}

