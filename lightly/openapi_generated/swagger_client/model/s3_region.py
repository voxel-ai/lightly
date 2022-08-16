# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from lightly.openapi_generated.swagger_client.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class S3Region(
    _SchemaEnumMaker(
        enum_value_to_name={
            "af-south-1": "AFSOUTH1",
            "ap-east-1": "APEAST1",
            "ap-northeast-1": "APNORTHEAST1",
            "ap-northeast-2": "APNORTHEAST2",
            "ap-northeast-3": "APNORTHEAST3",
            "ap-south-1": "APSOUTH1",
            "ap-southeast-1": "APSOUTHEAST1",
            "ap-southeast-2": "APSOUTHEAST2",
            "ap-southeast-3": "APSOUTHEAST3",
            "ca-central-1": "CACENTRAL1",
            "cn-northwest-1": "CNNORTHWEST1",
            "eu-central-1": "EUCENTRAL1",
            "eu-north-1": "EUNORTH1",
            "eu-south-1": "EUSOUTH1",
            "eu-west-1": "EUWEST1",
            "eu-west-2": "EUWEST2",
            "eu-west-3": "EUWEST3",
            "me-south-1": "MESOUTH1",
            "sa-east-1": "SAEAST1",
            "us-east-1": "USEAST1",
            "us-east-2": "USEAST2",
            "us-gov-east-1": "USGOVEAST1",
            "us-west-1": "USWEST1",
            "us-west-2": "USWEST2",
            "us-gov-west-1": "USGOVWEST1",
        }
    ),
    StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    The region where your bucket is located (see https://docs.aws.amazon.com/general/latest/gr/s3.html for further information)
    """
    
    @classmethod
    @property
    def AFSOUTH1(cls):
        return cls._enum_by_value["af-south-1"]("af-south-1")
    
    @classmethod
    @property
    def APEAST1(cls):
        return cls._enum_by_value["ap-east-1"]("ap-east-1")
    
    @classmethod
    @property
    def APNORTHEAST1(cls):
        return cls._enum_by_value["ap-northeast-1"]("ap-northeast-1")
    
    @classmethod
    @property
    def APNORTHEAST2(cls):
        return cls._enum_by_value["ap-northeast-2"]("ap-northeast-2")
    
    @classmethod
    @property
    def APNORTHEAST3(cls):
        return cls._enum_by_value["ap-northeast-3"]("ap-northeast-3")
    
    @classmethod
    @property
    def APSOUTH1(cls):
        return cls._enum_by_value["ap-south-1"]("ap-south-1")
    
    @classmethod
    @property
    def APSOUTHEAST1(cls):
        return cls._enum_by_value["ap-southeast-1"]("ap-southeast-1")
    
    @classmethod
    @property
    def APSOUTHEAST2(cls):
        return cls._enum_by_value["ap-southeast-2"]("ap-southeast-2")
    
    @classmethod
    @property
    def APSOUTHEAST3(cls):
        return cls._enum_by_value["ap-southeast-3"]("ap-southeast-3")
    
    @classmethod
    @property
    def CACENTRAL1(cls):
        return cls._enum_by_value["ca-central-1"]("ca-central-1")
    
    @classmethod
    @property
    def CNNORTHWEST1(cls):
        return cls._enum_by_value["cn-northwest-1"]("cn-northwest-1")
    
    @classmethod
    @property
    def EUCENTRAL1(cls):
        return cls._enum_by_value["eu-central-1"]("eu-central-1")
    
    @classmethod
    @property
    def EUNORTH1(cls):
        return cls._enum_by_value["eu-north-1"]("eu-north-1")
    
    @classmethod
    @property
    def EUSOUTH1(cls):
        return cls._enum_by_value["eu-south-1"]("eu-south-1")
    
    @classmethod
    @property
    def EUWEST1(cls):
        return cls._enum_by_value["eu-west-1"]("eu-west-1")
    
    @classmethod
    @property
    def EUWEST2(cls):
        return cls._enum_by_value["eu-west-2"]("eu-west-2")
    
    @classmethod
    @property
    def EUWEST3(cls):
        return cls._enum_by_value["eu-west-3"]("eu-west-3")
    
    @classmethod
    @property
    def MESOUTH1(cls):
        return cls._enum_by_value["me-south-1"]("me-south-1")
    
    @classmethod
    @property
    def SAEAST1(cls):
        return cls._enum_by_value["sa-east-1"]("sa-east-1")
    
    @classmethod
    @property
    def USEAST1(cls):
        return cls._enum_by_value["us-east-1"]("us-east-1")
    
    @classmethod
    @property
    def USEAST2(cls):
        return cls._enum_by_value["us-east-2"]("us-east-2")
    
    @classmethod
    @property
    def USGOVEAST1(cls):
        return cls._enum_by_value["us-gov-east-1"]("us-gov-east-1")
    
    @classmethod
    @property
    def USWEST1(cls):
        return cls._enum_by_value["us-west-1"]("us-west-1")
    
    @classmethod
    @property
    def USWEST2(cls):
        return cls._enum_by_value["us-west-2"]("us-west-2")
    
    @classmethod
    @property
    def USGOVWEST1(cls):
        return cls._enum_by_value["us-gov-west-1"]("us-gov-west-1")
