# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zepben/protobuf/cim/iec61970/base/meas/AccumulatorValue.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from zepben.protobuf.cim.iec61970.base.meas import MeasurementValue_pb2 as zepben_dot_protobuf_dot_cim_dot_iec61970_dot_base_dot_meas_dot_MeasurementValue__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='zepben/protobuf/cim/iec61970/base/meas/AccumulatorValue.proto',
  package='zepben.protobuf.cim.iec61970.base.meas',
  syntax='proto3',
  serialized_options=b'\n*com.zepben.protobuf.cim.iec61970.base.measP\001\252\002&Zepben.Protobuf.CIM.IEC61970.Base.Meas',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n=zepben/protobuf/cim/iec61970/base/meas/AccumulatorValue.proto\x12&zepben.protobuf.cim.iec61970.base.meas\x1a=zepben/protobuf/cim/iec61970/base/meas/MeasurementValue.proto\"\x80\x01\n\x10\x41\x63\x63umulatorValue\x12\x44\n\x02mv\x18\x01 \x01(\x0b\x32\x38.zepben.protobuf.cim.iec61970.base.meas.MeasurementValue\x12\x17\n\x0f\x61\x63\x63umulatorMRID\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\rBW\n*com.zepben.protobuf.cim.iec61970.base.measP\x01\xaa\x02&Zepben.Protobuf.CIM.IEC61970.Base.Measb\x06proto3'
  ,
  dependencies=[zepben_dot_protobuf_dot_cim_dot_iec61970_dot_base_dot_meas_dot_MeasurementValue__pb2.DESCRIPTOR,])




_ACCUMULATORVALUE = _descriptor.Descriptor(
  name='AccumulatorValue',
  full_name='zepben.protobuf.cim.iec61970.base.meas.AccumulatorValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='mv', full_name='zepben.protobuf.cim.iec61970.base.meas.AccumulatorValue.mv', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accumulatorMRID', full_name='zepben.protobuf.cim.iec61970.base.meas.AccumulatorValue.accumulatorMRID', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='zepben.protobuf.cim.iec61970.base.meas.AccumulatorValue.value', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=169,
  serialized_end=297,
)

_ACCUMULATORVALUE.fields_by_name['mv'].message_type = zepben_dot_protobuf_dot_cim_dot_iec61970_dot_base_dot_meas_dot_MeasurementValue__pb2._MEASUREMENTVALUE
DESCRIPTOR.message_types_by_name['AccumulatorValue'] = _ACCUMULATORVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccumulatorValue = _reflection.GeneratedProtocolMessageType('AccumulatorValue', (_message.Message,), {
  'DESCRIPTOR' : _ACCUMULATORVALUE,
  '__module__' : 'zepben.protobuf.cim.iec61970.base.meas.AccumulatorValue_pb2'
  # @@protoc_insertion_point(class_scope:zepben.protobuf.cim.iec61970.base.meas.AccumulatorValue)
  })
_sym_db.RegisterMessage(AccumulatorValue)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
