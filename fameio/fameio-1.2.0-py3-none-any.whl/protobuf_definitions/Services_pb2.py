# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Services.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Services.proto',
  package='communication',
  syntax='proto2',
  serialized_options=b'\n\024de.dlr.fame.protobufB\010Services',
  serialized_pb=b'\n\x0eServices.proto\x12\rcommunication\"!\n\rScheduledTime\x12\x10\n\x08timeStep\x18\x01 \x02(\x03\"v\n\nProtoSetup\x12\x12\n\noutputPath\x18\x01 \x02(\t\x12\x19\n\x11\x61gentPackageNames\x18\x02 \x03(\t\x12\x1b\n\x13messagePackageNames\x18\x03 \x03(\t\x12\x1c\n\x14portablePackageNames\x18\x04 \x03(\t\"\x1f\n\rWarmUpMessage\x12\x0e\n\x06needed\x18\x01 \x02(\x08\"\xcc\x03\n\x06Output\x12\x32\n\tagentType\x18\x01 \x03(\x0b\x32\x1f.communication.Output.AgentType\x12,\n\x06series\x18\x02 \x03(\x0b\x32\x1c.communication.Output.Series\x1a\x81\x01\n\tAgentType\x12\x11\n\tclassName\x18\x01 \x02(\t\x12\x34\n\x05\x66ield\x18\x02 \x03(\x0b\x32%.communication.Output.AgentType.Field\x1a+\n\x05\x46ield\x12\x0f\n\x07\x66ieldId\x18\x01 \x02(\x05\x12\x11\n\tfieldName\x18\x02 \x02(\t\x1a\xdb\x01\n\x06Series\x12\x11\n\tclassName\x18\x01 \x02(\t\x12\x0f\n\x07\x61gentId\x18\x02 \x02(\x03\x12/\n\x04line\x18\x03 \x03(\x0b\x32!.communication.Output.Series.Line\x1a|\n\x04Line\x12\x10\n\x08timeStep\x18\x01 \x02(\x03\x12\x38\n\x06\x63olumn\x18\x02 \x03(\x0b\x32(.communication.Output.Series.Line.Column\x1a(\n\x06\x43olumn\x12\x0f\n\x07\x66ieldId\x18\x01 \x02(\x05\x12\r\n\x05value\x18\x02 \x02(\x01\"1\n\x0b\x41\x64\x64ressBook\x12\x11\n\tprocessId\x18\x01 \x02(\x05\x12\x0f\n\x07\x61gentId\x18\x02 \x03(\x03\x42 \n\x14\x64\x65.dlr.fame.protobufB\x08Services'
)




_SCHEDULEDTIME = _descriptor.Descriptor(
  name='ScheduledTime',
  full_name='communication.ScheduledTime',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStep', full_name='communication.ScheduledTime.timeStep', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=33,
  serialized_end=66,
)


_PROTOSETUP = _descriptor.Descriptor(
  name='ProtoSetup',
  full_name='communication.ProtoSetup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputPath', full_name='communication.ProtoSetup.outputPath', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentPackageNames', full_name='communication.ProtoSetup.agentPackageNames', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='messagePackageNames', full_name='communication.ProtoSetup.messagePackageNames', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portablePackageNames', full_name='communication.ProtoSetup.portablePackageNames', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=186,
)


_WARMUPMESSAGE = _descriptor.Descriptor(
  name='WarmUpMessage',
  full_name='communication.WarmUpMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='needed', full_name='communication.WarmUpMessage.needed', index=0,
      number=1, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=219,
)


_OUTPUT_AGENTTYPE_FIELD = _descriptor.Descriptor(
  name='Field',
  full_name='communication.Output.AgentType.Field',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieldId', full_name='communication.Output.AgentType.Field.fieldId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fieldName', full_name='communication.Output.AgentType.Field.fieldName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=460,
)

_OUTPUT_AGENTTYPE = _descriptor.Descriptor(
  name='AgentType',
  full_name='communication.Output.AgentType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='className', full_name='communication.Output.AgentType.className', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='communication.Output.AgentType.field', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OUTPUT_AGENTTYPE_FIELD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=331,
  serialized_end=460,
)

_OUTPUT_SERIES_LINE_COLUMN = _descriptor.Descriptor(
  name='Column',
  full_name='communication.Output.Series.Line.Column',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fieldId', full_name='communication.Output.Series.Line.Column.fieldId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='communication.Output.Series.Line.Column.value', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=642,
  serialized_end=682,
)

_OUTPUT_SERIES_LINE = _descriptor.Descriptor(
  name='Line',
  full_name='communication.Output.Series.Line',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeStep', full_name='communication.Output.Series.Line.timeStep', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='column', full_name='communication.Output.Series.Line.column', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OUTPUT_SERIES_LINE_COLUMN, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=558,
  serialized_end=682,
)

_OUTPUT_SERIES = _descriptor.Descriptor(
  name='Series',
  full_name='communication.Output.Series',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='className', full_name='communication.Output.Series.className', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentId', full_name='communication.Output.Series.agentId', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='line', full_name='communication.Output.Series.line', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OUTPUT_SERIES_LINE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=463,
  serialized_end=682,
)

_OUTPUT = _descriptor.Descriptor(
  name='Output',
  full_name='communication.Output',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agentType', full_name='communication.Output.agentType', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='series', full_name='communication.Output.series', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_OUTPUT_AGENTTYPE, _OUTPUT_SERIES, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=682,
)


_ADDRESSBOOK = _descriptor.Descriptor(
  name='AddressBook',
  full_name='communication.AddressBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='processId', full_name='communication.AddressBook.processId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agentId', full_name='communication.AddressBook.agentId', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=684,
  serialized_end=733,
)

_OUTPUT_AGENTTYPE_FIELD.containing_type = _OUTPUT_AGENTTYPE
_OUTPUT_AGENTTYPE.fields_by_name['field'].message_type = _OUTPUT_AGENTTYPE_FIELD
_OUTPUT_AGENTTYPE.containing_type = _OUTPUT
_OUTPUT_SERIES_LINE_COLUMN.containing_type = _OUTPUT_SERIES_LINE
_OUTPUT_SERIES_LINE.fields_by_name['column'].message_type = _OUTPUT_SERIES_LINE_COLUMN
_OUTPUT_SERIES_LINE.containing_type = _OUTPUT_SERIES
_OUTPUT_SERIES.fields_by_name['line'].message_type = _OUTPUT_SERIES_LINE
_OUTPUT_SERIES.containing_type = _OUTPUT
_OUTPUT.fields_by_name['agentType'].message_type = _OUTPUT_AGENTTYPE
_OUTPUT.fields_by_name['series'].message_type = _OUTPUT_SERIES
DESCRIPTOR.message_types_by_name['ScheduledTime'] = _SCHEDULEDTIME
DESCRIPTOR.message_types_by_name['ProtoSetup'] = _PROTOSETUP
DESCRIPTOR.message_types_by_name['WarmUpMessage'] = _WARMUPMESSAGE
DESCRIPTOR.message_types_by_name['Output'] = _OUTPUT
DESCRIPTOR.message_types_by_name['AddressBook'] = _ADDRESSBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScheduledTime = _reflection.GeneratedProtocolMessageType('ScheduledTime', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULEDTIME,
  '__module__' : 'Services_pb2'
  # @@protoc_insertion_point(class_scope:communication.ScheduledTime)
  })
_sym_db.RegisterMessage(ScheduledTime)

ProtoSetup = _reflection.GeneratedProtocolMessageType('ProtoSetup', (_message.Message,), {
  'DESCRIPTOR' : _PROTOSETUP,
  '__module__' : 'Services_pb2'
  # @@protoc_insertion_point(class_scope:communication.ProtoSetup)
  })
_sym_db.RegisterMessage(ProtoSetup)

WarmUpMessage = _reflection.GeneratedProtocolMessageType('WarmUpMessage', (_message.Message,), {
  'DESCRIPTOR' : _WARMUPMESSAGE,
  '__module__' : 'Services_pb2'
  # @@protoc_insertion_point(class_scope:communication.WarmUpMessage)
  })
_sym_db.RegisterMessage(WarmUpMessage)

Output = _reflection.GeneratedProtocolMessageType('Output', (_message.Message,), {

  'AgentType' : _reflection.GeneratedProtocolMessageType('AgentType', (_message.Message,), {

    'Field' : _reflection.GeneratedProtocolMessageType('Field', (_message.Message,), {
      'DESCRIPTOR' : _OUTPUT_AGENTTYPE_FIELD,
      '__module__' : 'Services_pb2'
      # @@protoc_insertion_point(class_scope:communication.Output.AgentType.Field)
      })
    ,
    'DESCRIPTOR' : _OUTPUT_AGENTTYPE,
    '__module__' : 'Services_pb2'
    # @@protoc_insertion_point(class_scope:communication.Output.AgentType)
    })
  ,

  'Series' : _reflection.GeneratedProtocolMessageType('Series', (_message.Message,), {

    'Line' : _reflection.GeneratedProtocolMessageType('Line', (_message.Message,), {

      'Column' : _reflection.GeneratedProtocolMessageType('Column', (_message.Message,), {
        'DESCRIPTOR' : _OUTPUT_SERIES_LINE_COLUMN,
        '__module__' : 'Services_pb2'
        # @@protoc_insertion_point(class_scope:communication.Output.Series.Line.Column)
        })
      ,
      'DESCRIPTOR' : _OUTPUT_SERIES_LINE,
      '__module__' : 'Services_pb2'
      # @@protoc_insertion_point(class_scope:communication.Output.Series.Line)
      })
    ,
    'DESCRIPTOR' : _OUTPUT_SERIES,
    '__module__' : 'Services_pb2'
    # @@protoc_insertion_point(class_scope:communication.Output.Series)
    })
  ,
  'DESCRIPTOR' : _OUTPUT,
  '__module__' : 'Services_pb2'
  # @@protoc_insertion_point(class_scope:communication.Output)
  })
_sym_db.RegisterMessage(Output)
_sym_db.RegisterMessage(Output.AgentType)
_sym_db.RegisterMessage(Output.AgentType.Field)
_sym_db.RegisterMessage(Output.Series)
_sym_db.RegisterMessage(Output.Series.Line)
_sym_db.RegisterMessage(Output.Series.Line.Column)

AddressBook = _reflection.GeneratedProtocolMessageType('AddressBook', (_message.Message,), {
  'DESCRIPTOR' : _ADDRESSBOOK,
  '__module__' : 'Services_pb2'
  # @@protoc_insertion_point(class_scope:communication.AddressBook)
  })
_sym_db.RegisterMessage(AddressBook)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
