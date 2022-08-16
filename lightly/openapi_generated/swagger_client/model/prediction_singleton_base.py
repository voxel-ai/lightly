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


class PredictionSingletonBase(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    _required_property_names = set((
        'type',
        'taskName',
        'categoryId',
        'score',
    ))
    type = StrSchema

    @classmethod
    @property
    def taskName(cls) -> typing.Type['PathSafeName']:
        return PathSafeName

    @classmethod
    @property
    def cropDatasetId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def cropSampleId(cls) -> typing.Type['MongoObjectID']:
        return MongoObjectID

    @classmethod
    @property
    def categoryId(cls) -> typing.Type['CategoryId']:
        return CategoryId

    @classmethod
    @property
    def score(cls) -> typing.Type['Score']:
        return Score

    @classmethod
    @property
    def _discriminator(cls):
        return {
            'type': {
                'PredictionSingletonClassification': PredictionSingletonClassification,
                'PredictionSingletonInstanceSegmentation': PredictionSingletonInstanceSegmentation,
                'PredictionSingletonKeypointDetection': PredictionSingletonKeypointDetection,
                'PredictionSingletonObjectDetection': PredictionSingletonObjectDetection,
            }
        }


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        type: type,
        taskName: taskName,
        categoryId: categoryId,
        score: score,
        cropDatasetId: typing.Union['MongoObjectID', Unset] = unset,
        cropSampleId: typing.Union['MongoObjectID', Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'PredictionSingletonBase':
        return super().__new__(
            cls,
            *args,
            type=type,
            taskName=taskName,
            categoryId=categoryId,
            score=score,
            cropDatasetId=cropDatasetId,
            cropSampleId=cropSampleId,
            _configuration=_configuration,
            **kwargs,
        )

from lightly.openapi_generated.swagger_client.model.category_id import CategoryId
from lightly.openapi_generated.swagger_client.model.mongo_object_id import MongoObjectID
from lightly.openapi_generated.swagger_client.model.path_safe_name import PathSafeName
from lightly.openapi_generated.swagger_client.model.prediction_singleton_classification import PredictionSingletonClassification
from lightly.openapi_generated.swagger_client.model.prediction_singleton_instance_segmentation import PredictionSingletonInstanceSegmentation
from lightly.openapi_generated.swagger_client.model.prediction_singleton_keypoint_detection import PredictionSingletonKeypointDetection
from lightly.openapi_generated.swagger_client.model.prediction_singleton_object_detection import PredictionSingletonObjectDetection
from lightly.openapi_generated.swagger_client.model.score import Score
