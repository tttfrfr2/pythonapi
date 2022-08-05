"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from openapi_client.exceptions import ApiAttributeError


def lazy_import():
    from openapi_client.model.cwe_response_body import CweResponseBody
    globals()['CweResponseBody'] = CweResponseBody


class CveListResponseBody(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'all_task_count': (int,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'cve_id': (str,),  # noqa: E501
            'cwes': ([CweResponseBody],),  # noqa: E501
            'is_not_active': (bool,),  # noqa: E501
            'is_owasp_top_ten2017': (bool,),  # noqa: E501
            'max_v2': (float,),  # noqa: E501
            'max_v3': (float,),  # noqa: E501
            'new_task_count': (int,),  # noqa: E501
            'score_v2s': ({str: (float,)},),  # noqa: E501
            'score_v3s': ({str: (float,)},),  # noqa: E501
            'title': (str,),  # noqa: E501
            'topic_count': (int,),  # noqa: E501
            'topic_last_updated_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'vector_v2s': ({str: (str,)},),  # noqa: E501
            'vector_v3s': ({str: (str,)},),  # noqa: E501
            'advisory_ids': ([str],),  # noqa: E501
            'has_exploit': (bool,),  # noqa: E501
            'has_mitigation': (bool,),  # noqa: E501
            'has_workaround': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'all_task_count': 'allTaskCount',  # noqa: E501
        'created_at': 'createdAt',  # noqa: E501
        'cve_id': 'cveID',  # noqa: E501
        'cwes': 'cwes',  # noqa: E501
        'is_not_active': 'isNotActive',  # noqa: E501
        'is_owasp_top_ten2017': 'isOwaspTopTen2017',  # noqa: E501
        'max_v2': 'maxV2',  # noqa: E501
        'max_v3': 'maxV3',  # noqa: E501
        'new_task_count': 'newTaskCount',  # noqa: E501
        'score_v2s': 'scoreV2s',  # noqa: E501
        'score_v3s': 'scoreV3s',  # noqa: E501
        'title': 'title',  # noqa: E501
        'topic_count': 'topicCount',  # noqa: E501
        'topic_last_updated_at': 'topicLastUpdatedAt',  # noqa: E501
        'updated_at': 'updatedAt',  # noqa: E501
        'vector_v2s': 'vectorV2s',  # noqa: E501
        'vector_v3s': 'vectorV3s',  # noqa: E501
        'advisory_ids': 'advisoryIDs',  # noqa: E501
        'has_exploit': 'hasExploit',  # noqa: E501
        'has_mitigation': 'hasMitigation',  # noqa: E501
        'has_workaround': 'hasWorkaround',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, all_task_count, created_at, cve_id, cwes, is_not_active, is_owasp_top_ten2017, max_v2, max_v3, new_task_count, score_v2s, score_v3s, title, topic_count, topic_last_updated_at, updated_at, vector_v2s, vector_v3s, *args, **kwargs):  # noqa: E501
        """CveListResponseBody - a model defined in OpenAPI

        Args:
            all_task_count (int): AllTaskCount of cve
            created_at (datetime): created time
            cve_id (str): Cve ID string of cve
            cwes ([CweResponseBody]): cwes of cve
            is_not_active (bool): Flag of active cve
            is_owasp_top_ten2017 (bool): isOwaspTopTen2017 of cve
            max_v2 (float): maxV2 of cve
            max_v3 (float): maxV3 of cve
            new_task_count (int): NewTaskCount of cve
            score_v2s ({str: (float,)}): cvss v2 scores of cve
            score_v3s ({str: (float,)}): cvss v3 scores of cve
            title (str): Title of cve
            topic_count (int): topicCount of cve
            topic_last_updated_at (datetime): topicLastUpdatedAt of cve
            updated_at (datetime): updated time
            vector_v2s ({str: (str,)}): cvss v2 vectors of cve
            vector_v3s ({str: (str,)}): cvss v3 vectors of cve

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            advisory_ids ([str]): advisoryIDs of cve. [optional]  # noqa: E501
            has_exploit (bool): hasExploit of cve. [optional]  # noqa: E501
            has_mitigation (bool): hasMitigation of cve. [optional]  # noqa: E501
            has_workaround (bool): hasWorkaroundof cve. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.all_task_count = all_task_count
        self.created_at = created_at
        self.cve_id = cve_id
        self.cwes = cwes
        self.is_not_active = is_not_active
        self.is_owasp_top_ten2017 = is_owasp_top_ten2017
        self.max_v2 = max_v2
        self.max_v3 = max_v3
        self.new_task_count = new_task_count
        self.score_v2s = score_v2s
        self.score_v3s = score_v3s
        self.title = title
        self.topic_count = topic_count
        self.topic_last_updated_at = topic_last_updated_at
        self.updated_at = updated_at
        self.vector_v2s = vector_v2s
        self.vector_v3s = vector_v3s
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, all_task_count, created_at, cve_id, cwes, is_not_active, is_owasp_top_ten2017, max_v2, max_v3, new_task_count, score_v2s, score_v3s, title, topic_count, topic_last_updated_at, updated_at, vector_v2s, vector_v3s, *args, **kwargs):  # noqa: E501
        """CveListResponseBody - a model defined in OpenAPI

        Args:
            all_task_count (int): AllTaskCount of cve
            created_at (datetime): created time
            cve_id (str): Cve ID string of cve
            cwes ([CweResponseBody]): cwes of cve
            is_not_active (bool): Flag of active cve
            is_owasp_top_ten2017 (bool): isOwaspTopTen2017 of cve
            max_v2 (float): maxV2 of cve
            max_v3 (float): maxV3 of cve
            new_task_count (int): NewTaskCount of cve
            score_v2s ({str: (float,)}): cvss v2 scores of cve
            score_v3s ({str: (float,)}): cvss v3 scores of cve
            title (str): Title of cve
            topic_count (int): topicCount of cve
            topic_last_updated_at (datetime): topicLastUpdatedAt of cve
            updated_at (datetime): updated time
            vector_v2s ({str: (str,)}): cvss v2 vectors of cve
            vector_v3s ({str: (str,)}): cvss v3 vectors of cve

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            advisory_ids ([str]): advisoryIDs of cve. [optional]  # noqa: E501
            has_exploit (bool): hasExploit of cve. [optional]  # noqa: E501
            has_mitigation (bool): hasMitigation of cve. [optional]  # noqa: E501
            has_workaround (bool): hasWorkaroundof cve. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.all_task_count = all_task_count
        self.created_at = created_at
        self.cve_id = cve_id
        self.cwes = cwes
        self.is_not_active = is_not_active
        self.is_owasp_top_ten2017 = is_owasp_top_ten2017
        self.max_v2 = max_v2
        self.max_v3 = max_v3
        self.new_task_count = new_task_count
        self.score_v2s = score_v2s
        self.score_v3s = score_v3s
        self.title = title
        self.topic_count = topic_count
        self.topic_last_updated_at = topic_last_updated_at
        self.updated_at = updated_at
        self.vector_v2s = vector_v2s
        self.vector_v3s = vector_v3s
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
