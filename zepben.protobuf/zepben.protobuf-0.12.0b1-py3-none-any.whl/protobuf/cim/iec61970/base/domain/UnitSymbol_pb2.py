# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: zepben/protobuf/cim/iec61970/base/domain/UnitSymbol.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='zepben/protobuf/cim/iec61970/base/domain/UnitSymbol.proto',
  package='zepben.protobuf.cim.iec61970.base.domain',
  syntax='proto3',
  serialized_options=b'\n,com.zepben.protobuf.cim.iec61970.base.domainP\001\252\002(Zepben.Protobuf.CIM.IEC61970.Base.Domain',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n9zepben/protobuf/cim/iec61970/base/domain/UnitSymbol.proto\x12(zepben.protobuf.cim.iec61970.base.domain*\xe2\x0b\n\nUnitSymbol\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06METRES\x10\x01\x12\x06\n\x02KG\x10\x02\x12\x0b\n\x07SECONDS\x10\x03\x12\x05\n\x01\x41\x10\x04\x12\x05\n\x01K\x10\x05\x12\x07\n\x03MOL\x10\x06\x12\x06\n\x02\x43\x44\x10\x07\x12\x07\n\x03\x44\x45G\x10\x08\x12\x07\n\x03RAD\x10\t\x12\x06\n\x02SR\x10\n\x12\x06\n\x02GY\x10\x0b\x12\x06\n\x02\x42Q\x10\x0c\x12\x08\n\x04\x44\x45GC\x10\r\x12\x06\n\x02SV\x10\x0e\x12\x05\n\x01\x46\x10\x0f\x12\x05\n\x01\x43\x10\x10\x12\x0b\n\x07SIEMENS\x10\x11\x12\n\n\x06HENRYS\x10\x12\x12\x05\n\x01V\x10\x13\x12\x07\n\x03OHM\x10\x14\x12\x05\n\x01J\x10\x15\x12\x05\n\x01N\x10\x16\x12\x06\n\x02HZ\x10\x17\x12\x06\n\x02LX\x10\x18\x12\x06\n\x02LM\x10\x19\x12\x06\n\x02WB\x10\x1a\x12\x05\n\x01T\x10\x1b\x12\x05\n\x01W\x10\x1c\x12\x06\n\x02PA\x10\x1d\x12\x06\n\x02M2\x10\x1e\x12\x06\n\x02M3\x10\x1f\x12\t\n\x05MPERS\x10 \x12\n\n\x06MPERS2\x10!\x12\n\n\x06M3PERS\x10\"\x12\n\n\x06MPERM3\x10#\x12\x07\n\x03KGM\x10$\x12\x0b\n\x07KGPERM3\x10%\x12\n\n\x06M2PERS\x10&\x12\n\n\x06WPERMK\x10\'\x12\t\n\x05JPERK\x10(\x12\x07\n\x03PPM\x10)\x12\x0b\n\x07ROTPERS\x10*\x12\x0b\n\x07RADPERS\x10+\x12\n\n\x06WPERM2\x10,\x12\n\n\x06JPERM2\x10-\x12\t\n\x05SPERM\x10.\x12\t\n\x05KPERS\x10/\x12\n\n\x06PAPERS\x10\x30\x12\x0b\n\x07JPERKGK\x10\x31\x12\x06\n\x02VA\x10\x32\x12\x07\n\x03VAR\x10\x33\x12\n\n\x06\x43OSPHI\x10\x34\x12\x06\n\x02VS\x10\x35\x12\x06\n\x02V2\x10\x36\x12\x06\n\x02\x41S\x10\x37\x12\x06\n\x02\x41\x32\x10\x38\x12\x07\n\x03\x41\x32S\x10\x39\x12\x07\n\x03VAH\x10:\x12\x06\n\x02WH\x10;\x12\x08\n\x04VARH\x10<\x12\n\n\x06VPERHZ\x10=\x12\n\n\x06HZPERS\x10>\x12\r\n\tCHARACTER\x10?\x12\x0c\n\x08\x43HARPERS\x10@\x12\x08\n\x04KGM2\x10\x41\x12\x06\n\x02\x44\x42\x10\x42\x12\t\n\x05WPERS\x10\x43\x12\t\n\x05LPERS\x10\x44\x12\x07\n\x03\x44\x42M\x10\x45\x12\t\n\x05HOURS\x10\x46\x12\x07\n\x03MIN\x10G\x12\x05\n\x01Q\x10H\x12\x06\n\x02QH\x10I\x12\x08\n\x04OHMM\x10J\x12\t\n\x05\x41PERM\x10K\x12\x07\n\x03V2H\x10L\x12\x07\n\x03\x41\x32H\x10M\x12\x06\n\x02\x41H\x10N\x12\t\n\x05\x43OUNT\x10O\x12\x07\n\x03\x46T3\x10P\x12\n\n\x06M3PERH\x10Q\x12\x07\n\x03GAL\x10R\x12\x07\n\x03\x42TU\x10S\x12\x05\n\x01L\x10T\x12\t\n\x05LPERH\x10U\x12\t\n\x05LPERL\x10V\x12\t\n\x05GPERG\x10W\x12\x0c\n\x08MOLPERM3\x10X\x12\r\n\tMOLPERMOL\x10Y\x12\x0c\n\x08MOLPERKG\x10Z\x12\t\n\x05SPERS\x10[\x12\x0b\n\x07HZPERHZ\x10\\\x12\t\n\x05VPERV\x10]\x12\t\n\x05\x41PERA\x10^\x12\n\n\x06VPERVA\x10_\x12\x07\n\x03REV\x10`\x12\x07\n\x03KAT\x10\x61\x12\n\n\x06JPERKG\x10\x62\x12\x13\n\x0fM3UNCOMPENSATED\x10\x63\x12\x11\n\rM3COMPENSATED\x10\x64\x12\t\n\x05WPERW\x10\x65\x12\t\n\x05THERM\x10\x66\x12\x0b\n\x07ONEPERM\x10g\x12\x0b\n\x07M3PERKG\x10h\x12\x07\n\x03PAS\x10i\x12\x06\n\x02NM\x10j\x12\t\n\x05NPERM\x10k\x12\x0c\n\x08RADPERS2\x10l\x12\n\n\x06JPERM3\x10m\x12\t\n\x05VPERM\x10n\x12\n\n\x06\x43PERM3\x10o\x12\n\n\x06\x43PERM2\x10p\x12\t\n\x05\x46PERM\x10q\x12\t\n\x05HPERM\x10r\x12\x0b\n\x07JPERMOL\x10s\x12\x0c\n\x08JPERMOLK\x10t\x12\n\n\x06\x43PERKG\x10u\x12\n\n\x06GYPERS\x10v\x12\n\n\x06WPERSR\x10w\x12\x0c\n\x08WPERM2SR\x10x\x12\x0c\n\x08KATPERM3\x10y\x12\x05\n\x01\x44\x10z\x12\x0c\n\x08\x41NGLEMIN\x10{\x12\x0c\n\x08\x41NGLESEC\x10|\x12\x06\n\x02HA\x10}\x12\t\n\x05TONNE\x10~\x12\x07\n\x03\x42\x41R\x10\x7f\x12\t\n\x04MMHG\x10\x80\x01\x12\x13\n\x0eMILES_NAUTICAL\x10\x81\x01\x12\x07\n\x02KN\x10\x82\x01\x12\x07\n\x02MX\x10\x83\x01\x12\x06\n\x01G\x10\x84\x01\x12\x07\n\x02OE\x10\x85\x01\x12\x07\n\x02VH\x10\x86\x01\x12\n\n\x05WPERA\x10\x87\x01\x12\r\n\x08ONEPERHZ\x10\x88\x01\x12\x0c\n\x07VPERVAR\x10\x89\x01\x12\x0c\n\x07OHMPERM\x10\x8a\x01\x12\x0b\n\x06KGPERJ\x10\x8b\x01\x12\n\n\x05JPERS\x10\x8c\x01\x42[\n,com.zepben.protobuf.cim.iec61970.base.domainP\x01\xaa\x02(Zepben.Protobuf.CIM.IEC61970.Base.Domainb\x06proto3'
)

_UNITSYMBOL = _descriptor.EnumDescriptor(
  name='UnitSymbol',
  full_name='zepben.protobuf.cim.iec61970.base.domain.UnitSymbol',
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
      name='METRES', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KG', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SECONDS', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='A', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='K', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOL', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CD', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEG', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RAD', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SR', index=10, number=10,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GY', index=11, number=11,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BQ', index=12, number=12,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEGC', index=13, number=13,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SV', index=14, number=14,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='F', index=15, number=15,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='C', index=16, number=16,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIEMENS', index=17, number=17,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HENRYS', index=18, number=18,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V', index=19, number=19,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OHM', index=20, number=20,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='J', index=21, number=21,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='N', index=22, number=22,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HZ', index=23, number=23,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LX', index=24, number=24,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LM', index=25, number=25,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WB', index=26, number=26,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='T', index=27, number=27,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='W', index=28, number=28,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PA', index=29, number=29,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M2', index=30, number=30,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M3', index=31, number=31,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MPERS', index=32, number=32,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MPERS2', index=33, number=33,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M3PERS', index=34, number=34,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MPERM3', index=35, number=35,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KGM', index=36, number=36,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KGPERM3', index=37, number=37,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M2PERS', index=38, number=38,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPERMK', index=39, number=39,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERK', index=40, number=40,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PPM', index=41, number=41,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROTPERS', index=42, number=42,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RADPERS', index=43, number=43,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPERM2', index=44, number=44,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERM2', index=45, number=45,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPERM', index=46, number=46,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KPERS', index=47, number=47,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAPERS', index=48, number=48,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERKGK', index=49, number=49,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VA', index=50, number=50,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VAR', index=51, number=51,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COSPHI', index=52, number=52,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VS', index=53, number=53,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V2', index=54, number=54,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AS', index=55, number=55,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='A2', index=56, number=56,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='A2S', index=57, number=57,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VAH', index=58, number=58,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WH', index=59, number=59,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VARH', index=60, number=60,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPERHZ', index=61, number=61,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HZPERS', index=62, number=62,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHARACTER', index=63, number=63,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CHARPERS', index=64, number=64,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KGM2', index=65, number=65,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DB', index=66, number=66,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPERS', index=67, number=67,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LPERS', index=68, number=68,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DBM', index=69, number=69,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HOURS', index=70, number=70,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MIN', index=71, number=71,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='Q', index=72, number=72,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='QH', index=73, number=73,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OHMM', index=74, number=74,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APERM', index=75, number=75,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='V2H', index=76, number=76,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='A2H', index=77, number=77,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AH', index=78, number=78,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COUNT', index=79, number=79,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FT3', index=80, number=80,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M3PERH', index=81, number=81,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAL', index=82, number=82,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BTU', index=83, number=83,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='L', index=84, number=84,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LPERH', index=85, number=85,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LPERL', index=86, number=86,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GPERG', index=87, number=87,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOLPERM3', index=88, number=88,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOLPERMOL', index=89, number=89,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MOLPERKG', index=90, number=90,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SPERS', index=91, number=91,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HZPERHZ', index=92, number=92,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPERV', index=93, number=93,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='APERA', index=94, number=94,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPERVA', index=95, number=95,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REV', index=96, number=96,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KAT', index=97, number=97,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERKG', index=98, number=98,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M3UNCOMPENSATED', index=99, number=99,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M3COMPENSATED', index=100, number=100,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPERW', index=101, number=101,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='THERM', index=102, number=102,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONEPERM', index=103, number=103,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='M3PERKG', index=104, number=104,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PAS', index=105, number=105,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NM', index=106, number=106,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NPERM', index=107, number=107,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='RADPERS2', index=108, number=108,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERM3', index=109, number=109,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPERM', index=110, number=110,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CPERM3', index=111, number=111,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CPERM2', index=112, number=112,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FPERM', index=113, number=113,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HPERM', index=114, number=114,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERMOL', index=115, number=115,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERMOLK', index=116, number=116,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CPERKG', index=117, number=117,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GYPERS', index=118, number=118,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPERSR', index=119, number=119,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPERM2SR', index=120, number=120,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KATPERM3', index=121, number=121,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='D', index=122, number=122,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANGLEMIN', index=123, number=123,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANGLESEC', index=124, number=124,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HA', index=125, number=125,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TONNE', index=126, number=126,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BAR', index=127, number=127,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MMHG', index=128, number=128,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MILES_NAUTICAL', index=129, number=129,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KN', index=130, number=130,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='MX', index=131, number=131,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='G', index=132, number=132,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OE', index=133, number=133,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VH', index=134, number=134,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='WPERA', index=135, number=135,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONEPERHZ', index=136, number=136,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='VPERVAR', index=137, number=137,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OHMPERM', index=138, number=138,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='KGPERJ', index=139, number=139,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='JPERS', index=140, number=140,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=104,
  serialized_end=1610,
)
_sym_db.RegisterEnumDescriptor(_UNITSYMBOL)

UnitSymbol = enum_type_wrapper.EnumTypeWrapper(_UNITSYMBOL)
NONE = 0
METRES = 1
KG = 2
SECONDS = 3
A = 4
K = 5
MOL = 6
CD = 7
DEG = 8
RAD = 9
SR = 10
GY = 11
BQ = 12
DEGC = 13
SV = 14
F = 15
C = 16
SIEMENS = 17
HENRYS = 18
V = 19
OHM = 20
J = 21
N = 22
HZ = 23
LX = 24
LM = 25
WB = 26
T = 27
W = 28
PA = 29
M2 = 30
M3 = 31
MPERS = 32
MPERS2 = 33
M3PERS = 34
MPERM3 = 35
KGM = 36
KGPERM3 = 37
M2PERS = 38
WPERMK = 39
JPERK = 40
PPM = 41
ROTPERS = 42
RADPERS = 43
WPERM2 = 44
JPERM2 = 45
SPERM = 46
KPERS = 47
PAPERS = 48
JPERKGK = 49
VA = 50
VAR = 51
COSPHI = 52
VS = 53
V2 = 54
AS = 55
A2 = 56
A2S = 57
VAH = 58
WH = 59
VARH = 60
VPERHZ = 61
HZPERS = 62
CHARACTER = 63
CHARPERS = 64
KGM2 = 65
DB = 66
WPERS = 67
LPERS = 68
DBM = 69
HOURS = 70
MIN = 71
Q = 72
QH = 73
OHMM = 74
APERM = 75
V2H = 76
A2H = 77
AH = 78
COUNT = 79
FT3 = 80
M3PERH = 81
GAL = 82
BTU = 83
L = 84
LPERH = 85
LPERL = 86
GPERG = 87
MOLPERM3 = 88
MOLPERMOL = 89
MOLPERKG = 90
SPERS = 91
HZPERHZ = 92
VPERV = 93
APERA = 94
VPERVA = 95
REV = 96
KAT = 97
JPERKG = 98
M3UNCOMPENSATED = 99
M3COMPENSATED = 100
WPERW = 101
THERM = 102
ONEPERM = 103
M3PERKG = 104
PAS = 105
NM = 106
NPERM = 107
RADPERS2 = 108
JPERM3 = 109
VPERM = 110
CPERM3 = 111
CPERM2 = 112
FPERM = 113
HPERM = 114
JPERMOL = 115
JPERMOLK = 116
CPERKG = 117
GYPERS = 118
WPERSR = 119
WPERM2SR = 120
KATPERM3 = 121
D = 122
ANGLEMIN = 123
ANGLESEC = 124
HA = 125
TONNE = 126
BAR = 127
MMHG = 128
MILES_NAUTICAL = 129
KN = 130
MX = 131
G = 132
OE = 133
VH = 134
WPERA = 135
ONEPERHZ = 136
VPERVAR = 137
OHMPERM = 138
KGPERJ = 139
JPERS = 140


DESCRIPTOR.enum_types_by_name['UnitSymbol'] = _UNITSYMBOL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
