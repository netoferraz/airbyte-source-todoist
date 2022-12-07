# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from connector_builder.generated.models.any_of_cartesian_product_stream_slicer_datetime_stream_slicer_list_stream_slicer_single_slice_substream_slicer import AnyOfCartesianProductStreamSlicerDatetimeStreamSlicerListStreamSlicerSingleSliceSubstreamSlicer
from connector_builder.generated.models.any_of_default_paginator_no_pagination import AnyOfDefaultPaginatorNoPagination
from connector_builder.generated.models.any_of_interpolated_stringstring import AnyOfInterpolatedStringstring
from connector_builder.generated.models.any_ofarrayarraystring import AnyOfarrayarraystring
from connector_builder.generated.models.http_requester import HttpRequester
from connector_builder.generated.models.record_selector import RecordSelector
from connector_builder.generated.models.simple_retriever_all_of import SimpleRetrieverAllOf


class SimpleRetriever(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SimpleRetriever - a model defined in OpenAPI

        requester: The requester of this SimpleRetriever.
        record_selector: The record_selector of this SimpleRetriever.
        config: The config of this SimpleRetriever.
        name: The name of this SimpleRetriever [Optional].
        name: The name of this SimpleRetriever [Optional].
        primary_key: The primary_key of this SimpleRetriever [Optional].
        primary_key: The primary_key of this SimpleRetriever [Optional].
        paginator: The paginator of this SimpleRetriever [Optional].
        stream_slicer: The stream_slicer of this SimpleRetriever [Optional].
    """

    requester: HttpRequester
    record_selector: RecordSelector
    config: Dict[str, Any]
    name: Optional[str] = None
    name: Optional[AnyOfInterpolatedStringstring] = None
    primary_key: Optional[AnyOfarrayarraystring] = None
    primary_key: Optional[str] = None
    paginator: Optional[AnyOfDefaultPaginatorNoPagination] = None
    stream_slicer: Optional[AnyOfCartesianProductStreamSlicerDatetimeStreamSlicerListStreamSlicerSingleSliceSubstreamSlicer] = None

SimpleRetriever.update_forward_refs()
