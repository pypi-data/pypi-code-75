# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: msg_stock_common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='msg_stock_common.proto',
  package='MsgStockCommon',
  syntax='proto3',
  serialized_options=b'\n#com.kaisaglobal.proto.stock.message\200\001\000\210\001\001\220\001\000',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16msg_stock_common.proto\x12\x0eMsgStockCommon\x1a\x1fgoogle/protobuf/timestamp.proto\"7\n\x07ReqHead\x12\r\n\x05reqId\x18\x01 \x01(\t\x12\x0f\n\x07reqType\x18\x02 \x01(\r\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\"\x87\x01\n\x07ResHead\x12\r\n\x05resId\x18\x01 \x01(\t\x12\"\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x14.MsgStockCommon.Code\x12\x0b\n\x03msg\x18\x03 \x01(\t\x12.\n\x04type\x18\x04 \x01(\x0e\x32 .MsgStockCommon.SubscriptionType\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c*U\n\x04\x43ode\x12\x0c\n\x08\x65nETNone\x10\x00\x12\x10\n\x0c\x65nETSerError\x10\x01\x12\x14\n\x10\x65nETRequestError\x10\x02\x12\x17\n\x13\x65nETInvalidArgument\x10\x03*j\n\x06Market\x12\x08\n\x04NONE\x10\x00\x12\x06\n\x02\x43N\x10\x01\x12\x06\n\x02HK\x10\x02\x12\x06\n\x02US\x10\x03\x12\x06\n\x02QS\x10\x1e\x12\x06\n\x02NS\x10\x1f\x12\x06\n\x02\x41S\x10 \x12\x06\n\x02PS\x10!\x12\x06\n\x02\x42S\x10\"\x12\x06\n\x02VS\x10#\x12\x06\n\x02SH\x10\n\x12\x06\n\x02SZ\x10\x0b*\x8d\x02\n\x10SubscriptionType\x12\x07\n\x03\x41LL\x10\x00\x12\t\n\x05QUOTE\x10\x01\x12\x08\n\x04TICK\x10\x02\x12\n\n\x06\x42ROKER\x10\x03\x12\t\n\x05ORDER\x10\x04\x12\x11\n\rHandicapQuota\x10\x05\x12\x13\n\x0fPopularIndustry\x10\x06\x12\x12\n\x0ePopularConcept\x10\x07\x12\x12\n\x0e\x41llSectorQuota\x10\x08\x12\x11\n\rIndustryQuota\x10\t\x12\x10\n\x0c\x43onceptQuota\x10\n\x12\x12\n\x0e\x42\x61sicAssetInfo\x10\x0b\x12\x16\n\x12\x42\x61sicSubMarketInfo\x10\x0c\x12\x08\n\x04\x45XIT\x10\r\x12\x0c\n\x08TIME_OUT\x10\x0e\x12\x0b\n\x07Warrant\x10\x0f*\"\n\x08Language\x12\x06\n\x02ZH\x10\x00\x12\x06\n\x02TW\x10\x01\x12\x06\n\x02\x45N\x10\x02\x42.\n#com.kaisaglobal.proto.stock.message\x80\x01\x00\x88\x01\x01\x90\x01\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_CODE = _descriptor.EnumDescriptor(
  name='Code',
  full_name='MsgStockCommon.Code',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='enETNone', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='enETSerError', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='enETRequestError', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='enETInvalidArgument', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=270,
  serialized_end=355,
)
_sym_db.RegisterEnumDescriptor(_CODE)

Code = enum_type_wrapper.EnumTypeWrapper(_CODE)
_MARKET = _descriptor.EnumDescriptor(
  name='Market',
  full_name='MsgStockCommon.Market',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CN', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='US', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QS', index=4, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NS', index=5, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AS', index=6, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PS', index=7, number=33,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BS', index=8, number=34,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VS', index=9, number=35,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SH', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SZ', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=357,
  serialized_end=463,
)
_sym_db.RegisterEnumDescriptor(_MARKET)

Market = enum_type_wrapper.EnumTypeWrapper(_MARKET)
_SUBSCRIPTIONTYPE = _descriptor.EnumDescriptor(
  name='SubscriptionType',
  full_name='MsgStockCommon.SubscriptionType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ALL', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QUOTE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TICK', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BROKER', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ORDER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HandicapQuota', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PopularIndustry', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PopularConcept', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AllSectorQuota', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='IndustryQuota', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ConceptQuota', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BasicAssetInfo', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BasicSubMarketInfo', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EXIT', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TIME_OUT', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Warrant', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=466,
  serialized_end=735,
)
_sym_db.RegisterEnumDescriptor(_SUBSCRIPTIONTYPE)

SubscriptionType = enum_type_wrapper.EnumTypeWrapper(_SUBSCRIPTIONTYPE)
_LANGUAGE = _descriptor.EnumDescriptor(
  name='Language',
  full_name='MsgStockCommon.Language',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ZH', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TW', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='EN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=737,
  serialized_end=771,
)
_sym_db.RegisterEnumDescriptor(_LANGUAGE)

Language = enum_type_wrapper.EnumTypeWrapper(_LANGUAGE)
enETNone = 0
enETSerError = 1
enETRequestError = 2
enETInvalidArgument = 3
NONE = 0
CN = 1
HK = 2
US = 3
QS = 30
NS = 31
AS = 32
PS = 33
BS = 34
VS = 35
SH = 10
SZ = 11
ALL = 0
QUOTE = 1
TICK = 2
BROKER = 3
ORDER = 4
HandicapQuota = 5
PopularIndustry = 6
PopularConcept = 7
AllSectorQuota = 8
IndustryQuota = 9
ConceptQuota = 10
BasicAssetInfo = 11
BasicSubMarketInfo = 12
EXIT = 13
TIME_OUT = 14
Warrant = 15
ZH = 0
TW = 1
EN = 2



_REQHEAD = _descriptor.Descriptor(
  name='ReqHead',
  full_name='MsgStockCommon.ReqHead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reqId', full_name='MsgStockCommon.ReqHead.reqId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='reqType', full_name='MsgStockCommon.ReqHead.reqType', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='MsgStockCommon.ReqHead.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=75,
  serialized_end=130,
)


_RESHEAD = _descriptor.Descriptor(
  name='ResHead',
  full_name='MsgStockCommon.ResHead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='resId', full_name='MsgStockCommon.ResHead.resId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='MsgStockCommon.ResHead.code', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='msg', full_name='MsgStockCommon.ResHead.msg', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='MsgStockCommon.ResHead.type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='MsgStockCommon.ResHead.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=133,
  serialized_end=268,
)

_RESHEAD.fields_by_name['code'].enum_type = _CODE
_RESHEAD.fields_by_name['type'].enum_type = _SUBSCRIPTIONTYPE
DESCRIPTOR.message_types_by_name['ReqHead'] = _REQHEAD
DESCRIPTOR.message_types_by_name['ResHead'] = _RESHEAD
DESCRIPTOR.enum_types_by_name['Code'] = _CODE
DESCRIPTOR.enum_types_by_name['Market'] = _MARKET
DESCRIPTOR.enum_types_by_name['SubscriptionType'] = _SUBSCRIPTIONTYPE
DESCRIPTOR.enum_types_by_name['Language'] = _LANGUAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqHead = _reflection.GeneratedProtocolMessageType('ReqHead', (_message.Message,), {
  'DESCRIPTOR' : _REQHEAD,
  '__module__' : 'msg_stock_common_pb2'
  # @@protoc_insertion_point(class_scope:MsgStockCommon.ReqHead)
  })
_sym_db.RegisterMessage(ReqHead)

ResHead = _reflection.GeneratedProtocolMessageType('ResHead', (_message.Message,), {
  'DESCRIPTOR' : _RESHEAD,
  '__module__' : 'msg_stock_common_pb2'
  # @@protoc_insertion_point(class_scope:MsgStockCommon.ResHead)
  })
_sym_db.RegisterMessage(ResHead)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
