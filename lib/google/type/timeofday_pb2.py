# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/type/timeofday.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/type/timeofday.proto',
  package='google.type',
  syntax='proto3',
  serialized_pb=_b('\n\x1bgoogle/type/timeofday.proto\x12\x0bgoogle.type\"K\n\tTimeOfDay\x12\r\n\x05hours\x18\x01 \x01(\x05\x12\x0f\n\x07minutes\x18\x02 \x01(\x05\x12\x0f\n\x07seconds\x18\x03 \x01(\x05\x12\r\n\x05nanos\x18\x04 \x01(\x05\x42)\n\x0f\x63om.google.typeB\x0eTimeOfDayProtoP\x01\xa2\x02\x03GTPb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TIMEOFDAY = _descriptor.Descriptor(
  name='TimeOfDay',
  full_name='google.type.TimeOfDay',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hours', full_name='google.type.TimeOfDay.hours', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='google.type.TimeOfDay.minutes', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='google.type.TimeOfDay.seconds', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nanos', full_name='google.type.TimeOfDay.nanos', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['TimeOfDay'] = _TIMEOFDAY

TimeOfDay = _reflection.GeneratedProtocolMessageType('TimeOfDay', (_message.Message,), dict(
  DESCRIPTOR = _TIMEOFDAY,
  __module__ = 'google.type.timeofday_pb2'
  # @@protoc_insertion_point(class_scope:google.type.TimeOfDay)
  ))
_sym_db.RegisterMessage(TimeOfDay)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\017com.google.typeB\016TimeOfDayProtoP\001\242\002\003GTP'))
# @@protoc_insertion_point(module_scope)
