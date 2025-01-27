# coding: utf-8

"""
    JobSet SDK

    Python SDK for the JobSet API

    The version of the OpenAPI document: v0.1.4
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jobset.models.jobset_v1alpha2_depends_on import JobsetV1alpha2DependsOn

class TestJobsetV1alpha2DependsOn(unittest.TestCase):
    """JobsetV1alpha2DependsOn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JobsetV1alpha2DependsOn:
        """Test JobsetV1alpha2DependsOn
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JobsetV1alpha2DependsOn`
        """
        model = JobsetV1alpha2DependsOn()
        if include_optional:
            return JobsetV1alpha2DependsOn(
                name = '',
                status = ''
            )
        else:
            return JobsetV1alpha2DependsOn(
                name = '',
                status = '',
        )
        """

    def testJobsetV1alpha2DependsOn(self):
        """Test JobsetV1alpha2DependsOn"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
