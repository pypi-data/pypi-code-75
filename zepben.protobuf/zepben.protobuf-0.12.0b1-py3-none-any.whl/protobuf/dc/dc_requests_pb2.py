# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zepben/protobuf/dc/dc-requests.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zepben/protobuf/dc/dc-requests.proto',
  package='zepben.protobuf.dc',
  syntax='proto3',
  serialized_options=b'\n\026com.zepben.protobuf.dcP\001\252\002\022Zepben.Protobuf.DC',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$zepben/protobuf/dc/dc-requests.proto\x12\x12zepben.protobuf.dc\"?\n\x1bGetIdentifiedObjectsRequest\x12\x11\n\tmessageId\x18\x01 \x01(\x03\x12\r\n\x05mrids\x18\x02 \x03(\tB/\n\x16\x63om.zepben.protobuf.dcP\x01\xaa\x02\x12Zepben.Protobuf.DCb\x06proto3'
)




_GETIDENTIFIEDOBJECTSREQUEST = _descriptor.Descriptor(
  name='GetIdentifiedObjectsRequest',
  full_name='zepben.protobuf.dc.GetIdentifiedObjectsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='messageId', full_name='zepben.protobuf.dc.GetIdentifiedObjectsRequest.messageId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mrids', full_name='zepben.protobuf.dc.GetIdentifiedObjectsRequest.mrids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=123,
)

DESCRIPTOR.message_types_by_name['GetIdentifiedObjectsRequest'] = _GETIDENTIFIEDOBJECTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetIdentifiedObjectsRequest = _reflection.GeneratedProtocolMessageType('GetIdentifiedObjectsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETIDENTIFIEDOBJECTSREQUEST,
  '__module__' : 'zepben.protobuf.dc.dc_requests_pb2'
  # @@protoc_insertion_point(class_scope:zepben.protobuf.dc.GetIdentifiedObjectsRequest)
  })
_sym_db.RegisterMessage(GetIdentifiedObjectsRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
