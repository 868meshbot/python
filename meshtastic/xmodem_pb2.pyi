"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class XModem(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Control:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ControlEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[XModem._Control.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NUL: XModem._Control.ValueType  # 0
        SOH: XModem._Control.ValueType  # 1
        STX: XModem._Control.ValueType  # 2
        EOT: XModem._Control.ValueType  # 4
        ACK: XModem._Control.ValueType  # 6
        NAK: XModem._Control.ValueType  # 21
        CAN: XModem._Control.ValueType  # 24
        CTRLZ: XModem._Control.ValueType  # 26

    class Control(_Control, metaclass=_ControlEnumTypeWrapper): ...
    NUL: XModem.Control.ValueType  # 0
    SOH: XModem.Control.ValueType  # 1
    STX: XModem.Control.ValueType  # 2
    EOT: XModem.Control.ValueType  # 4
    ACK: XModem.Control.ValueType  # 6
    NAK: XModem.Control.ValueType  # 21
    CAN: XModem.Control.ValueType  # 24
    CTRLZ: XModem.Control.ValueType  # 26

    CONTROL_FIELD_NUMBER: builtins.int
    SEQ_FIELD_NUMBER: builtins.int
    CRC16_FIELD_NUMBER: builtins.int
    BUFFER_FIELD_NUMBER: builtins.int
    control: global___XModem.Control.ValueType
    seq: builtins.int
    crc16: builtins.int
    buffer: builtins.bytes
    def __init__(
        self,
        *,
        control: global___XModem.Control.ValueType = ...,
        seq: builtins.int = ...,
        crc16: builtins.int = ...,
        buffer: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["buffer", b"buffer", "control", b"control", "crc16", b"crc16", "seq", b"seq"]) -> None: ...

global___XModem = XModem
