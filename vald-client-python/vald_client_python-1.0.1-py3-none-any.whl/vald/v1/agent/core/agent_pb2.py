# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vald/v1/agent/core/agent.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2
from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vald/v1/agent/core/agent.proto',
  package='core.v1',
  syntax='proto3',
  serialized_options=b'\n org.vdaas.vald.api.v1.agent.coreB\tValdAgentP\001Z-github.com/vdaas/vald/apis/grpc/v1/agent/core\310\342\036\001\320\342\036\001\340\342\036\001\300\343\036\001\310\343\036\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1evald/v1/agent/core/agent.proto\x12\x07\x63ore.v1\x1a\x1dvald/v1/payload/payload.proto\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto2\xf2\x02\n\x05\x41gent\x12_\n\x0b\x43reateIndex\x12&.payload.v1.Control.CreateIndexRequest\x1a\x11.payload.v1.Empty\"\x15\x82\xd3\xe4\x93\x02\x0f\x12\r/index/create\x12\x46\n\tSaveIndex\x12\x11.payload.v1.Empty\x1a\x11.payload.v1.Empty\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/index/save\x12m\n\x12\x43reateAndSaveIndex\x12&.payload.v1.Control.CreateIndexRequest\x1a\x11.payload.v1.Empty\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/index/createandsave\x12Q\n\tIndexInfo\x12\x11.payload.v1.Empty\x1a\x1c.payload.v1.Info.Index.Count\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/index/infoBr\n org.vdaas.vald.api.v1.agent.coreB\tValdAgentP\x01Z-github.com/vdaas/vald/apis/grpc/v1/agent/core\xc8\xe2\x1e\x01\xd0\xe2\x1e\x01\xe0\xe2\x1e\x01\xc0\xe3\x1e\x01\xc8\xe3\x1e\x01\x62\x06proto3'
  ,
  dependencies=[vald_dot_v1_dot_payload_dot_payload__pb2.DESCRIPTOR,gogoproto_dot_gogo__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None

_AGENT = _descriptor.ServiceDescriptor(
  name='Agent',
  full_name='core.v1.Agent',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=127,
  serialized_end=497,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateIndex',
    full_name='core.v1.Agent.CreateIndex',
    index=0,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._CONTROL_CREATEINDEXREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\017\022\r/index/create',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SaveIndex',
    full_name='core.v1.Agent.SaveIndex',
    index=1,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._EMPTY,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\r\022\013/index/save',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateAndSaveIndex',
    full_name='core.v1.Agent.CreateAndSaveIndex',
    index=2,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._CONTROL_CREATEINDEXREQUEST,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._EMPTY,
    serialized_options=b'\202\323\344\223\002\026\022\024/index/createandsave',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='IndexInfo',
    full_name='core.v1.Agent.IndexInfo',
    index=3,
    containing_service=None,
    input_type=vald_dot_v1_dot_payload_dot_payload__pb2._EMPTY,
    output_type=vald_dot_v1_dot_payload_dot_payload__pb2._INFO_INDEX_COUNT,
    serialized_options=b'\202\323\344\223\002\r\022\013/index/info',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_AGENT)

DESCRIPTOR.services_by_name['Agent'] = _AGENT

# @@protoc_insertion_point(module_scope)
