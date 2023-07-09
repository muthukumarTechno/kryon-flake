from core.utils import validator


def add_resource(resource_type, json):
    validator.validate_resource_type(resource_type,json)
    return json
