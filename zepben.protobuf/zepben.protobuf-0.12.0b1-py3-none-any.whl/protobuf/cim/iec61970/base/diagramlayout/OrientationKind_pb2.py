# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zepben/protobuf/cim/iec61970/base/diagramlayout/OrientationKind.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zepben/protobuf/cim/iec61970/base/diagramlayout/OrientationKind.proto',
  package='zepben.protobuf.cim.iec61970.base.diagramlayout',
  syntax='proto3',
  serialized_options=b'\n3com.zepben.protobuf.cim.iec61970.base.diagramlayoutP\001\252\002/Zepben.Protobuf.CIM.IEC61970.Base.DiagramLayout',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nEzepben/protobuf/cim/iec61970/base/diagramlayout/OrientationKind.proto\x12/zepben.protobuf.cim.iec61970.base.diagramlayout*-\n\x0fOrientationKind\x12\x0c\n\x08POSITIVE\x10\x00\x12\x0c\n\x08NEGATIVE\x10\x01\x42i\n3com.zepben.protobuf.cim.iec61970.base.diagramlayoutP\x01\xaa\x02/Zepben.Protobuf.CIM.IEC61970.Base.DiagramLayoutb\x06proto3'
)

_ORIENTATIONKIND = _descriptor.EnumDescriptor(
  name='OrientationKind',
  full_name='zepben.protobuf.cim.iec61970.base.diagramlayout.OrientationKind',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POSITIVE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NEGATIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=122,
  serialized_end=167,
)
_sym_db.RegisterEnumDescriptor(_ORIENTATIONKIND)

OrientationKind = enum_type_wrapper.EnumTypeWrapper(_ORIENTATIONKIND)
POSITIVE = 0
NEGATIVE = 1


DESCRIPTOR.enum_types_by_name['OrientationKind'] = _ORIENTATIONKIND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
