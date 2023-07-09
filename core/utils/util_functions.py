import re

from core.utils.vars import get_schema, build_schema_ref_path


def get_python_data_type(fhir_data):
    if fhir_data:
        if fhir_data == 'array':
            return list
        elif fhir_data == 'string':
            return str
        elif fhir_data == 'boolean':
            return bool
        elif fhir_data == 'number':
            return int
        elif fhir_data == 'object':
            return dict



def property_and_datatype_checker(fhir_schema, resource, errors):
    backlog_data = []

    if isinstance(resource, dict):

        actual_resource_elements = ['id', 'meta', 'implicitRules', '_implicitRules', 'language', 'text', 'contained',
                                    'extension',
                                    'modifierExtension', 'resourceType']
        print(resource)
        print(fhir_schema)
        for key in actual_resource_elements:
            if fhir_schema.get(key):
                del fhir_schema[key]
            if resource.get(key):
                del resource[key]

        for patient_key in fhir_schema.keys():
            if not patient_key.startswith("_") and patient_key not in resource:
                errors['patient'].append({"type": "key missing",
                                          "value": patient_key})

            elif not patient_key.startswith("_") and patient_key in resource:
                patient_property = fhir_schema[patient_key]

                if 'type' in patient_property:
                    python_data_type = get_python_data_type(patient_property.type)

                    if not isinstance(resource.get(patient_key), python_data_type):
                        errors['patient'].append({"type": "incorrect data type",
                                                  "value": patient_key})

                if '$ref' in patient_property:
                    validation_pattern = get_schema().get(build_schema_ref_path(patient_property['$ref'])+'.pattern')
                    if validation_pattern:
                        pat = re.compile(validation_pattern)
                        if not re.match(pat, str(resource.get(patient_key))):
                            errors['patient'].append({"type": "incorrect data type",
                                                      "value": resource.get(patient_key)})

                if 'items' in patient_property:
                    items = patient_property['items']
                    backlog_data.append({"path": build_schema_ref_path(items['$ref'] + '.properties'), "patient_key": patient_key})

        return backlog_data

