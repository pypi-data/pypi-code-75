# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: voltha_protos/logical_device.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from voltha_protos import meta_pb2 as voltha__protos_dot_meta__pb2
from voltha_protos import openflow_13_pb2 as voltha__protos_dot_openflow__13__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='voltha_protos/logical_device.proto',
  package='voltha',
  syntax='proto3',
  serialized_options=b'\n\023org.opencord.volthaB\017OFLogicalDeviceZ.github.com/opencord/voltha-protos/v4/go/voltha',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"voltha_protos/logical_device.proto\x12\x06voltha\x1a\x1cgoogle/api/annotations.proto\x1a\x18voltha_protos/meta.proto\x1a\x1fvoltha_protos/openflow_13.proto\",\n\rLogicalPortId\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07port_id\x18\x02 \x01(\t\"\xb5\x01\n\x0bLogicalPort\x12\n\n\x02id\x18\x01 \x01(\t\x12\'\n\x08ofp_port\x18\x02 \x01(\x0b\x32\x15.openflow_13.ofp_port\x12\x11\n\tdevice_id\x18\x03 \x01(\t\x12\x16\n\x0e\x64\x65vice_port_no\x18\x04 \x01(\r\x12\x11\n\troot_port\x18\x05 \x01(\x08\x12\x33\n\x0eofp_port_stats\x18\x06 \x01(\x0b\x32\x1b.openflow_13.ofp_port_stats\"2\n\x0cLogicalPorts\x12\"\n\x05items\x18\x01 \x03(\x0b\x32\x13.voltha.LogicalPort\"\xa8\x01\n\rLogicalDevice\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x61tapath_id\x18\x02 \x01(\x04\x12#\n\x04\x64\x65sc\x18\x03 \x01(\x0b\x32\x15.openflow_13.ofp_desc\x12\x39\n\x0fswitch_features\x18\x04 \x01(\x0b\x32 .openflow_13.ofp_switch_features\x12\x16\n\x0eroot_device_id\x18\x05 \x01(\t\"6\n\x0eLogicalDevices\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x15.voltha.LogicalDeviceBV\n\x13org.opencord.volthaB\x0fOFLogicalDeviceZ.github.com/opencord/voltha-protos/v4/go/volthab\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,voltha__protos_dot_meta__pb2.DESCRIPTOR,voltha__protos_dot_openflow__13__pb2.DESCRIPTOR,])




_LOGICALPORTID = _descriptor.Descriptor(
  name='LogicalPortId',
  full_name='voltha.LogicalPortId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='voltha.LogicalPortId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_id', full_name='voltha.LogicalPortId.port_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=135,
  serialized_end=179,
)


_LOGICALPORT = _descriptor.Descriptor(
  name='LogicalPort',
  full_name='voltha.LogicalPort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='voltha.LogicalPort.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ofp_port', full_name='voltha.LogicalPort.ofp_port', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='voltha.LogicalPort.device_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='device_port_no', full_name='voltha.LogicalPort.device_port_no', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root_port', full_name='voltha.LogicalPort.root_port', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ofp_port_stats', full_name='voltha.LogicalPort.ofp_port_stats', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=182,
  serialized_end=363,
)


_LOGICALPORTS = _descriptor.Descriptor(
  name='LogicalPorts',
  full_name='voltha.LogicalPorts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='voltha.LogicalPorts.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=365,
  serialized_end=415,
)


_LOGICALDEVICE = _descriptor.Descriptor(
  name='LogicalDevice',
  full_name='voltha.LogicalDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='voltha.LogicalDevice.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datapath_id', full_name='voltha.LogicalDevice.datapath_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='desc', full_name='voltha.LogicalDevice.desc', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='switch_features', full_name='voltha.LogicalDevice.switch_features', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='root_device_id', full_name='voltha.LogicalDevice.root_device_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=418,
  serialized_end=586,
)


_LOGICALDEVICES = _descriptor.Descriptor(
  name='LogicalDevices',
  full_name='voltha.LogicalDevices',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='voltha.LogicalDevices.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=588,
  serialized_end=642,
)

_LOGICALPORT.fields_by_name['ofp_port'].message_type = voltha__protos_dot_openflow__13__pb2._OFP_PORT
_LOGICALPORT.fields_by_name['ofp_port_stats'].message_type = voltha__protos_dot_openflow__13__pb2._OFP_PORT_STATS
_LOGICALPORTS.fields_by_name['items'].message_type = _LOGICALPORT
_LOGICALDEVICE.fields_by_name['desc'].message_type = voltha__protos_dot_openflow__13__pb2._OFP_DESC
_LOGICALDEVICE.fields_by_name['switch_features'].message_type = voltha__protos_dot_openflow__13__pb2._OFP_SWITCH_FEATURES
_LOGICALDEVICES.fields_by_name['items'].message_type = _LOGICALDEVICE
DESCRIPTOR.message_types_by_name['LogicalPortId'] = _LOGICALPORTID
DESCRIPTOR.message_types_by_name['LogicalPort'] = _LOGICALPORT
DESCRIPTOR.message_types_by_name['LogicalPorts'] = _LOGICALPORTS
DESCRIPTOR.message_types_by_name['LogicalDevice'] = _LOGICALDEVICE
DESCRIPTOR.message_types_by_name['LogicalDevices'] = _LOGICALDEVICES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LogicalPortId = _reflection.GeneratedProtocolMessageType('LogicalPortId', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALPORTID,
  '__module__' : 'voltha_protos.logical_device_pb2'
  # @@protoc_insertion_point(class_scope:voltha.LogicalPortId)
  })
_sym_db.RegisterMessage(LogicalPortId)

LogicalPort = _reflection.GeneratedProtocolMessageType('LogicalPort', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALPORT,
  '__module__' : 'voltha_protos.logical_device_pb2'
  # @@protoc_insertion_point(class_scope:voltha.LogicalPort)
  })
_sym_db.RegisterMessage(LogicalPort)

LogicalPorts = _reflection.GeneratedProtocolMessageType('LogicalPorts', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALPORTS,
  '__module__' : 'voltha_protos.logical_device_pb2'
  # @@protoc_insertion_point(class_scope:voltha.LogicalPorts)
  })
_sym_db.RegisterMessage(LogicalPorts)

LogicalDevice = _reflection.GeneratedProtocolMessageType('LogicalDevice', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALDEVICE,
  '__module__' : 'voltha_protos.logical_device_pb2'
  # @@protoc_insertion_point(class_scope:voltha.LogicalDevice)
  })
_sym_db.RegisterMessage(LogicalDevice)

LogicalDevices = _reflection.GeneratedProtocolMessageType('LogicalDevices', (_message.Message,), {
  'DESCRIPTOR' : _LOGICALDEVICES,
  '__module__' : 'voltha_protos.logical_device_pb2'
  # @@protoc_insertion_point(class_scope:voltha.LogicalDevices)
  })
_sym_db.RegisterMessage(LogicalDevices)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
