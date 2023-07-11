from core.DomainResource import DomainResource
from core.utils.resource_validator import is_common_resource_validation
from core.utils.util_functions import property_and_datatype_checker
from core.utils.vars import get_schema


class Patient(DomainResource):
    resource = None

    def __init__(self, json, resource_path):
        super().__init__(json)
        print("From ===> class Patient")
        self.resource = json
        if is_common_resource_validation(json):
            self.do_patient_specific_validation(resource_path)

    def do_patient_specific_validation(self, resource_path):

        errors = {"patient": []}

        fhir_schema = get_schema().get(resource_path + '.properties')

        backlog_data = property_and_datatype_checker(fhir_schema, self.resource, errors)

        for data in backlog_data:

            for resource_data in self.resource.get(data['patient_key']):

                backlog_data_1 = property_and_datatype_checker(get_schema().get(data['path']), resource_data, errors)
                for data_1 in backlog_data_1:

                    for resource_data_1 in resource_data.get(data_1['patient_key']):

                        if get_schema().get(data_1['path']):

                            backlog_data_2 = property_and_datatype_checker(get_schema().get(data_1['path']), resource_data_1, errors)

                        else:
                            backlog_data_2 = property_and_datatype_checker(get_schema().get(data_1['path'].replace('.properties','')),
                                                                           resource_data_1, errors)

                        print(backlog_data_2)
        print(errors)



