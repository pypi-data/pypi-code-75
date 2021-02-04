from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class NeptuneClusterLogging(BaseResourceCheck):
    def __init__(self):
        name = "Ensure Neptune logging is enabled"
        id = "CKV_AWS_101"
        supported_resources = ['aws_neptune_cluster']
        categories = [CheckCategories.LOGGING]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        log_types = ["audit"]
        if 'enable_cloudwatch_logs_exports' in conf.keys():
            if all(elem in conf['enable_cloudwatch_logs_exports'] for elem in log_types):
                return CheckResult.PASSED
        return CheckResult.FAILED

check = NeptuneClusterLogging()
