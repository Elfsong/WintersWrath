# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: html.proto

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
  name='html.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\nhtml.proto\"+\n\x0chtml_segment\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07segment\x18\x02 \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_HTML_SEGMENT = _descriptor.Descriptor(
  name='html_segment',
  full_name='html_segment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='html_segment.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='segment', full_name='html_segment.segment', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=57,
)

DESCRIPTOR.message_types_by_name['html_segment'] = _HTML_SEGMENT

html_segment = _reflection.GeneratedProtocolMessageType('html_segment', (_message.Message,), dict(
  DESCRIPTOR = _HTML_SEGMENT,
  __module__ = 'html_pb2'
  # @@protoc_insertion_point(class_scope:html_segment)
  ))
_sym_db.RegisterMessage(html_segment)


# @@protoc_insertion_point(module_scope)