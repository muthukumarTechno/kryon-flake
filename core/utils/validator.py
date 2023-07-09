from core.resources.Patient import Patient
from core.utils.vars import get_schema, build_schema_ref_path


def validate_resource_type(resource_type, json):
    resource_ref = get_schema().get('discriminator.mapping' + '.' + resource_type)

    if resource_type is not None:
        resource_path = build_schema_ref_path(resource_ref)
        if resource_type == 'Patient':
            patient = Patient(json, resource_path)

    return None

