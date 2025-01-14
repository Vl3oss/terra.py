# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: terra/tx/v1beta1/service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.tx.v1beta1 import tx_pb2 as cosmos_dot_tx_dot_v1beta1_dot_tx__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="terra/tx/v1beta1/service.proto",
    package="terra.tx.v1beta1",
    syntax="proto3",
    serialized_options=b"Z*github.com/terra-money/core/custom/auth/tx\300\343\036\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\x1eterra/tx/v1beta1/service.proto\x12\x10terra.tx.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a\x1a\x63osmos/tx/v1beta1/tx.proto"6\n\x11\x43omputeTaxRequest\x12!\n\x02tx\x18\x01 \x01(\x0b\x32\x15.cosmos.tx.v1beta1.Tx"u\n\x12\x43omputeTaxResponse\x12_\n\ntax_amount\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins2\x8d\x01\n\x07Service\x12\x81\x01\n\nComputeTax\x12#.terra.tx.v1beta1.ComputeTaxRequest\x1a$.terra.tx.v1beta1.ComputeTaxResponse"(\x82\xd3\xe4\x93\x02""\x1d/terra/tx/v1beta1/compute_tax:\x01*B0Z*github.com/terra-money/core/custom/auth/tx\xc0\xe3\x1e\x01\x62\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        cosmos_dot_base_dot_v1beta1_dot_coin__pb2.DESCRIPTOR,
        cosmos_dot_tx_dot_v1beta1_dot_tx__pb2.DESCRIPTOR,
    ],
)


_COMPUTETAXREQUEST = _descriptor.Descriptor(
    name="ComputeTaxRequest",
    full_name="terra.tx.v1beta1.ComputeTaxRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="tx",
            full_name="terra.tx.v1beta1.ComputeTaxRequest.tx",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=164,
    serialized_end=218,
)


_COMPUTETAXRESPONSE = _descriptor.Descriptor(
    name="ComputeTaxResponse",
    full_name="terra.tx.v1beta1.ComputeTaxResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="tax_amount",
            full_name="terra.tx.v1beta1.ComputeTaxResponse.tax_amount",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=220,
    serialized_end=337,
)

_COMPUTETAXREQUEST.fields_by_name[
    "tx"
].message_type = cosmos_dot_tx_dot_v1beta1_dot_tx__pb2._TX
_COMPUTETAXRESPONSE.fields_by_name[
    "tax_amount"
].message_type = cosmos_dot_base_dot_v1beta1_dot_coin__pb2._COIN
DESCRIPTOR.message_types_by_name["ComputeTaxRequest"] = _COMPUTETAXREQUEST
DESCRIPTOR.message_types_by_name["ComputeTaxResponse"] = _COMPUTETAXRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComputeTaxRequest = _reflection.GeneratedProtocolMessageType(
    "ComputeTaxRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMPUTETAXREQUEST,
        "__module__": "terra.tx.v1beta1.service_pb2"
        # @@protoc_insertion_point(class_scope:terra.tx.v1beta1.ComputeTaxRequest)
    },
)
_sym_db.RegisterMessage(ComputeTaxRequest)

ComputeTaxResponse = _reflection.GeneratedProtocolMessageType(
    "ComputeTaxResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMPUTETAXRESPONSE,
        "__module__": "terra.tx.v1beta1.service_pb2"
        # @@protoc_insertion_point(class_scope:terra.tx.v1beta1.ComputeTaxResponse)
    },
)
_sym_db.RegisterMessage(ComputeTaxResponse)


DESCRIPTOR._options = None
_COMPUTETAXRESPONSE.fields_by_name["tax_amount"]._options = None

_SERVICE = _descriptor.ServiceDescriptor(
    name="Service",
    full_name="terra.tx.v1beta1.Service",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_start=340,
    serialized_end=481,
    methods=[
        _descriptor.MethodDescriptor(
            name="ComputeTax",
            full_name="terra.tx.v1beta1.Service.ComputeTax",
            index=0,
            containing_service=None,
            input_type=_COMPUTETAXREQUEST,
            output_type=_COMPUTETAXRESPONSE,
            serialized_options=b'\202\323\344\223\002""\035/terra/tx/v1beta1/compute_tax:\001*',
            create_key=_descriptor._internal_create_key,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name["Service"] = _SERVICE

# @@protoc_insertion_point(module_scope)
