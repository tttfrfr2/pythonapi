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
from openapi_client.model.lockfile_add_lockfile_request_body import LockfileAddLockfileRequestBody
from openapi_client.model.lockfile_add_lockfile_response_body import LockfileAddLockfileResponseBody
from openapi_client.model.lockfile_get_lockfile_detail_response_body import LockfileGetLockfileDetailResponseBody
from openapi_client.model.lockfile_get_lockfile_list_response_body import LockfileGetLockfileListResponseBody
from openapi_client.model.lockfile_update_lockfile_request_body import LockfileUpdateLockfileRequestBody
from openapi_client.model.lockfile_update_lockfile_response_body import LockfileUpdateLockfileResponseBody


class LockfileApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.lockfile_add_lockfile_endpoint = _Endpoint(
            settings={
                'response_type': (LockfileAddLockfileResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/lockfile',
                'operation_id': 'lockfile_add_lockfile',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'add_lockfile_request_body',
                    'authorization',
                ],
                'required': [
                    'add_lockfile_request_body',
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
                    'add_lockfile_request_body':
                        (LockfileAddLockfileRequestBody,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'add_lockfile_request_body': 'body',
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
        self.lockfile_delete_lockfile_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/lockfile/{lockfileID}',
                'operation_id': 'lockfile_delete_lockfile',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'lockfile_id',
                    'authorization',
                ],
                'required': [
                    'lockfile_id',
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
                    'lockfile_id':
                        (int,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'lockfile_id': 'lockfileID',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'lockfile_id': 'path',
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
        self.lockfile_get_lockfile_detail_endpoint = _Endpoint(
            settings={
                'response_type': (LockfileGetLockfileDetailResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/lockfile/{lockfileID}',
                'operation_id': 'lockfile_get_lockfile_detail',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lockfile_id',
                    'authorization',
                ],
                'required': [
                    'lockfile_id',
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
                    'lockfile_id':
                        (int,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'lockfile_id': 'lockfileID',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'lockfile_id': 'path',
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
        self.lockfile_get_lockfile_list_endpoint = _Endpoint(
            settings={
                'response_type': (LockfileGetLockfileListResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/lockfiles',
                'operation_id': 'lockfile_get_lockfile_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'limit',
                    'offset',
                    'filter_server_id',
                    'filter_path',
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
                    'filter_server_id':
                        (int,),
                    'filter_path':
                        (str,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'page': 'page',
                    'limit': 'limit',
                    'offset': 'offset',
                    'filter_server_id': 'filterServerID',
                    'filter_path': 'filterPath',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'page': 'query',
                    'limit': 'query',
                    'offset': 'query',
                    'filter_server_id': 'query',
                    'filter_path': 'query',
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
        self.lockfile_update_lockfile_endpoint = _Endpoint(
            settings={
                'response_type': (LockfileUpdateLockfileResponseBody,),
                'auth': [
                    'api_key_header_Authorization'
                ],
                'endpoint_path': '/v1/lockfile/{lockfileID}',
                'operation_id': 'lockfile_update_lockfile',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'lockfile_id',
                    'update_lockfile_request_body',
                    'authorization',
                ],
                'required': [
                    'lockfile_id',
                    'update_lockfile_request_body',
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
                    'lockfile_id':
                        (int,),
                    'update_lockfile_request_body':
                        (LockfileUpdateLockfileRequestBody,),
                    'authorization':
                        (str,),
                },
                'attribute_map': {
                    'lockfile_id': 'lockfileID',
                    'authorization': 'Authorization',
                },
                'location_map': {
                    'lockfile_id': 'path',
                    'update_lockfile_request_body': 'body',
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

    def lockfile_add_lockfile(
        self,
        add_lockfile_request_body,
        **kwargs
    ):
        """addLockfile lockfile  # noqa: E501

        add lockfile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_add_lockfile(add_lockfile_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            add_lockfile_request_body (LockfileAddLockfileRequestBody):

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
            LockfileAddLockfileResponseBody
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
        kwargs['add_lockfile_request_body'] = \
            add_lockfile_request_body
        return self.lockfile_add_lockfile_endpoint.call_with_http_info(**kwargs)

    def lockfile_delete_lockfile(
        self,
        lockfile_id,
        **kwargs
    ):
        """deleteLockfile lockfile  # noqa: E501

        lockfile delete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_delete_lockfile(lockfile_id, async_req=True)
        >>> result = thread.get()

        Args:
            lockfile_id (int): Lockfile ID

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
        kwargs['lockfile_id'] = \
            lockfile_id
        return self.lockfile_delete_lockfile_endpoint.call_with_http_info(**kwargs)

    def lockfile_get_lockfile_detail(
        self,
        lockfile_id,
        **kwargs
    ):
        """getLockfileDetail lockfile  # noqa: E501

        lockfile detail  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_get_lockfile_detail(lockfile_id, async_req=True)
        >>> result = thread.get()

        Args:
            lockfile_id (int): Lockfile ID

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
            LockfileGetLockfileDetailResponseBody
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
        kwargs['lockfile_id'] = \
            lockfile_id
        return self.lockfile_get_lockfile_detail_endpoint.call_with_http_info(**kwargs)

    def lockfile_get_lockfile_list(
        self,
        **kwargs
    ):
        """getLockfileList lockfile  # noqa: E501

        lockfile list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_get_lockfile_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page Number. [optional] if omitted the server will use the default value of 1
            limit (int): Limit. [optional] if omitted the server will use the default value of 20
            offset (int): Offset. [optional] if omitted the server will use the default value of 0
            filter_server_id (int): ServerID filter. [optional]
            filter_path (str): Path filter. [optional]
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
            LockfileGetLockfileListResponseBody
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
        return self.lockfile_get_lockfile_list_endpoint.call_with_http_info(**kwargs)

    def lockfile_update_lockfile(
        self,
        lockfile_id,
        update_lockfile_request_body,
        **kwargs
    ):
        """updateLockfile lockfile  # noqa: E501

        update lockfile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lockfile_update_lockfile(lockfile_id, update_lockfile_request_body, async_req=True)
        >>> result = thread.get()

        Args:
            lockfile_id (int): Lockfile ID
            update_lockfile_request_body (LockfileUpdateLockfileRequestBody):

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
            LockfileUpdateLockfileResponseBody
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
        kwargs['lockfile_id'] = \
            lockfile_id
        kwargs['update_lockfile_request_body'] = \
            update_lockfile_request_body
        return self.lockfile_update_lockfile_endpoint.call_with_http_info(**kwargs)

