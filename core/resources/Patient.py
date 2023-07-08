import this

from core.DomainResource import DomainResource
from core.utils.resource_validator import is_common_resource_validation


class Patient(DomainResource):
    resource = None


def do_patient_specific_validation():
    pass


def __init__(self, resource):
    print("From ===> class Patient")
    super().__init__(resource)
    self.resource = resource
    if is_common_resource_validation(resource):
        self.do_patient_specific_validation()
