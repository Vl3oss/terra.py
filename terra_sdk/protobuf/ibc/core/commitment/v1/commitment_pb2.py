# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/commitment/v1/commitment.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from confio import proofs_pb2 as confio_dot_proofs__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="ibc/core/commitment/v1/commitment.proto",
    package="ibc.core.commitment.v1",
    syntax="proto3",
    serialized_options=b"Z9github.com/cosmos/ibc-go/modules/core/23-commitment/types",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\'ibc/core/commitment/v1/commitment.proto\x12\x16ibc.core.commitment.v1\x1a\x14gogoproto/gogo.proto\x1a\x13\x63onfio/proofs.proto" \n\nMerkleRoot\x12\x0c\n\x04hash\x18\x01 \x01(\x0c:\x04\x88\xa0\x1f\x00"9\n\x0cMerklePrefix\x12)\n\nkey_prefix\x18\x01 \x01(\x0c\x42\x15\xf2\xde\x1f\x11yaml:"key_prefix""9\n\nMerklePath\x12%\n\x08key_path\x18\x01 \x03(\tB\x13\xf2\xde\x1f\x0fyaml:"key_path":\x04\x98\xa0\x1f\x00"5\n\x0bMerkleProof\x12&\n\x06proofs\x18\x01 \x03(\x0b\x32\x16.ics23.CommitmentProofB;Z9github.com/cosmos/ibc-go/modules/core/23-commitment/typesb\x06proto3',
    dependencies=[
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        confio_dot_proofs__pb2.DESCRIPTOR,
    ],
)


_MERKLEROOT = _descriptor.Descriptor(
    name="MerkleRoot",
    full_name="ibc.core.commitment.v1.MerkleRoot",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="hash",
            full_name="ibc.core.commitment.v1.MerkleRoot.hash",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
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
    serialized_options=b"\210\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=110,
    serialized_end=142,
)


_MERKLEPREFIX = _descriptor.Descriptor(
    name="MerklePrefix",
    full_name="ibc.core.commitment.v1.MerklePrefix",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key_prefix",
            full_name="ibc.core.commitment.v1.MerklePrefix.key_prefix",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\021yaml:"key_prefix"',
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
    serialized_start=144,
    serialized_end=201,
)


_MERKLEPATH = _descriptor.Descriptor(
    name="MerklePath",
    full_name="ibc.core.commitment.v1.MerklePath",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key_path",
            full_name="ibc.core.commitment.v1.MerklePath.key_path",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\017yaml:"key_path"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\230\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=203,
    serialized_end=260,
)


_MERKLEPROOF = _descriptor.Descriptor(
    name="MerkleProof",
    full_name="ibc.core.commitment.v1.MerkleProof",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="proofs",
            full_name="ibc.core.commitment.v1.MerkleProof.proofs",
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
    serialized_start=262,
    serialized_end=315,
)

_MERKLEPROOF.fields_by_name[
    "proofs"
].message_type = confio_dot_proofs__pb2._COMMITMENTPROOF
DESCRIPTOR.message_types_by_name["MerkleRoot"] = _MERKLEROOT
DESCRIPTOR.message_types_by_name["MerklePrefix"] = _MERKLEPREFIX
DESCRIPTOR.message_types_by_name["MerklePath"] = _MERKLEPATH
DESCRIPTOR.message_types_by_name["MerkleProof"] = _MERKLEPROOF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MerkleRoot = _reflection.GeneratedProtocolMessageType(
    "MerkleRoot",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERKLEROOT,
        "__module__": "ibc.core.commitment.v1.commitment_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerkleRoot)
    },
)
_sym_db.RegisterMessage(MerkleRoot)

MerklePrefix = _reflection.GeneratedProtocolMessageType(
    "MerklePrefix",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERKLEPREFIX,
        "__module__": "ibc.core.commitment.v1.commitment_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerklePrefix)
    },
)
_sym_db.RegisterMessage(MerklePrefix)

MerklePath = _reflection.GeneratedProtocolMessageType(
    "MerklePath",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERKLEPATH,
        "__module__": "ibc.core.commitment.v1.commitment_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerklePath)
    },
)
_sym_db.RegisterMessage(MerklePath)

MerkleProof = _reflection.GeneratedProtocolMessageType(
    "MerkleProof",
    (_message.Message,),
    {
        "DESCRIPTOR": _MERKLEPROOF,
        "__module__": "ibc.core.commitment.v1.commitment_pb2"
        # @@protoc_insertion_point(class_scope:ibc.core.commitment.v1.MerkleProof)
    },
)
_sym_db.RegisterMessage(MerkleProof)


DESCRIPTOR._options = None
_MERKLEROOT._options = None
_MERKLEPREFIX.fields_by_name["key_prefix"]._options = None
_MERKLEPATH.fields_by_name["key_path"]._options = None
_MERKLEPATH._options = None
# @@protoc_insertion_point(module_scope)
