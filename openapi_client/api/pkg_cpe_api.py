"""
    Future Vuls Public API

    Future Vuls Public API  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.pkg_cpe_add_cpe_request_body import PkgCpeAddCpeRequestBody
from openapi_client.model.pkg_cpe_add_cpe_response_body import PkgCpeAddCpeResponseBody
from openapi_client.model.pkg_cpe_delete_cpe_deprecated_request_body import PkgCpeDeleteCpeDeprecatedRequestBody
from openapi_client.model.pkg_cpe_get_cpe_detail_response_body import PkgCpeGetCpeDetailResponseBody
from openapi_client.model.pkg_cpe_get_pkg_cpe_list_response_body import PkgCpeGetPkgCpeListResponseBody
from openapi_client.model.pkg_cpe_get_pkg_detail_response_body import PkgCpeGetPkgDetailResponseBody


class PkgCpeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.pkg_cpe_add_cpe_endpoint = _Endpoint(
            settings={
                'response_type': (PkgCpeAddCpeResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/pkgCpe/cpe',
                'operation_id': 'pkg_cpe_add_cpe',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'add_cpe_request_body',
                    'authorization',
                ],
                'required': [
                    'add_cpe_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'add_cpe_request_body':
                        (PkgCpeAddCpeRequestBody,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'add_cpe_request_body': 'body',
                    'authorization': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/gob'
                ],
                'content_type': [
                    'application/json',
                    'application/xml',
                    'application/gob'
                ]
            },
            api_client=api_client
        )
        self.pkg_cpe_delete_cpe_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/pkgCpe/cpe/{cpeID}',
                'operation_id': 'pkg_cpe_delete_cpe',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'cpe_id',
                    'authorization',
                ],
                'required': [
                    'cpe_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'cpe_id':
                        (int,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'cpe_id': 'cpeID',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'cpe_id': 'path',
                    'authorization': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.pkg_cpe_delete_cpe_deprecated_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/pkgCpe/cpe',
                'operation_id': 'pkg_cpe_delete_cpe_deprecated',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'delete_cpe_deprecated_request_body',
                    'authorization',
                ],
                'required': [
                    'delete_cpe_deprecated_request_body',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'delete_cpe_deprecated_request_body':
                        (PkgCpeDeleteCpeDeprecatedRequestBody,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'delete_cpe_deprecated_request_body': 'body',
                    'authorization': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json',
                    'application/xml',
                    'application/gob'
                ]
            },
            api_client=api_client
        )
        self.pkg_cpe_get_cpe_detail_endpoint = _Endpoint(
            settings={
                'response_type': (PkgCpeGetCpeDetailResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/pkgCpe/cpe/{cpeID}',
                'operation_id': 'pkg_cpe_get_cpe_detail',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'cpe_id',
                    'authorization',
                ],
                'required': [
                    'cpe_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'cpe_id':
                        (int,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'cpe_id': 'cpeID',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'cpe_id': 'path',
                    'authorization': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/gob'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.pkg_cpe_get_pkg_cpe_list_endpoint = _Endpoint(
            settings={
                'response_type': (PkgCpeGetPkgCpeListResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/pkgCpes',
                'operation_id': 'pkg_cpe_get_pkg_cpe_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'limit',
                    'offset',
                    'filter_cve_id',
                    'filter_task_id',
                    'filter_server_id',
                    'filter_role_id',
                    'authorization',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'limit',
                    'offset',
                    'filter_task_id',
                    'filter_server_id',
                    'filter_role_id',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 1,
                    },
                    ('limit',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                    ('offset',): {

                        'inclusive_minimum': 0,
                    },
                    ('filter_task_id',): {

                        'inclusive_minimum': 1,
                    },
                    ('filter_server_id',): {

                        'inclusive_minimum': 1,
                    },
                    ('filter_role_id',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'filter_cve_id':
                        (str,),
                    'filter_task_id':
                        (int,),
                    'filter_server_id':
                        (int,),
                    'filter_role_id':
                        (int,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'limit': 'limit',
                    'offset': 'offset',
                    'filter_cve_id': 'filterCveID',
                    'filter_task_id': 'filterTaskID',
                    'filter_server_id': 'filterServerID',
                    'filter_role_id': 'filterRoleID',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'page': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'filter_cve_id': 'query',
                    'filter_task_id': 'query',
                    'filter_server_id': 'query',
                    'filter_role_id': 'query',
                    'authorization': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/gob'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.pkg_cpe_get_pkg_detail_endpoint = _Endpoint(
            settings={
                'response_type': (PkgCpeGetPkgDetailResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/pkgCpe/pkg/{pkgID}',
                'operation_id': 'pkg_cpe_get_pkg_detail',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'pkg_id',
                    'authorization',
                ],
                'required': [
                    'pkg_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'pkg_id':
                        (int,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'pkg_id': 'pkgID',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'pkg_id': 'path',
                    'authorization': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml',
                    'application/gob'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def pkg_cpe_add_cpe(
        self,
        add_cpe_request_body,
        **kwargs
    ):
        """addCpe pkgCpe  # noqa: E501

        add cpe  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pkg_cpe_add_cpe(add_cpe_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            add_cpe_request_body (PkgCpeAddCpeRequestBody):

        Keyword Args:
            authorization (str): api key auth. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PkgCpeAddCpeResponseBody
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['add_cpe_request_body'] = \
            add_cpe_request_body
        return self.pkg_cpe_add_cpe_endpoint.call_with_http_info(**kwargs)

    def pkg_cpe_delete_cpe(
        self,
        cpe_id,
        **kwargs
    ):
        """deleteCpe pkgCpe  # noqa: E501

        delete cpe (urlにcpeIDを指定してください。cpeIDの指定のないアクセス方法は今後削除されます。)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pkg_cpe_delete_cpe(cpe_id, async_req=True)
        >>> result = thread.get()

        Args:
            cpe_id (int): cpe ID

        Keyword Args:
            authorization (str): api key auth. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['cpe_id'] = \
            cpe_id
        return self.pkg_cpe_delete_cpe_endpoint.call_with_http_info(**kwargs)

    def pkg_cpe_delete_cpe_deprecated(
        self,
        delete_cpe_deprecated_request_body,
        **kwargs
    ):
        """deleteCpe_deprecated pkgCpe  # noqa: E501

        [deprecated] urlにcpeIDを指定して利用してください。cpeIDの指定のないこちらのアクセス方法は今後削除されます。  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pkg_cpe_delete_cpe_deprecated(delete_cpe_deprecated_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            delete_cpe_deprecated_request_body (PkgCpeDeleteCpeDeprecatedRequestBody):

        Keyword Args:
            authorization (str): api key auth. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['delete_cpe_deprecated_request_body'] = \
            delete_cpe_deprecated_request_body
        return self.pkg_cpe_delete_cpe_deprecated_endpoint.call_with_http_info(**kwargs)

    def pkg_cpe_get_cpe_detail(
        self,
        cpe_id,
        **kwargs
    ):
        """getCpeDetail pkgCpe  # noqa: E501

        cpe detail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pkg_cpe_get_cpe_detail(cpe_id, async_req=True)
        >>> result = thread.get()

        Args:
            cpe_id (int): cpe ID

        Keyword Args:
            authorization (str): api key auth. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PkgCpeGetCpeDetailResponseBody
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['cpe_id'] = \
            cpe_id
        return self.pkg_cpe_get_cpe_detail_endpoint.call_with_http_info(**kwargs)

    def pkg_cpe_get_pkg_cpe_list(
        self,
        **kwargs
    ):
        """getPkgCpeList pkgCpe  # noqa: E501

        pkgCpe list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pkg_cpe_get_pkg_cpe_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page Number. [optional] if omitted the server will use the default value of 1
            limit (int): Limit. [optional] if omitted the server will use the default value of 20
            offset (int): Offset. [optional] if omitted the server will use the default value of 0
            filter_cve_id (str): CveID filter. [optional]
            filter_task_id (int): TaskID filter. [optional]
            filter_server_id (int): ServerID filter. [optional]
            filter_role_id (int): ServerRoleID filter. [optional]
            authorization (str): api key auth. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PkgCpeGetPkgCpeListResponseBody
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        return self.pkg_cpe_get_pkg_cpe_list_endpoint.call_with_http_info(**kwargs)

    def pkg_cpe_get_pkg_detail(
        self,
        pkg_id,
        **kwargs
    ):
        """getPkgDetail pkgCpe  # noqa: E501

        pkg detail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.pkg_cpe_get_pkg_detail(pkg_id, async_req=True)
        >>> result = thread.get()

        Args:
            pkg_id (int): PackageID

        Keyword Args:
            authorization (str): api key auth. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            PkgCpeGetPkgDetailResponseBody
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['pkg_id'] = \
            pkg_id
        return self.pkg_cpe_get_pkg_detail_endpoint.call_with_http_info(**kwargs)

