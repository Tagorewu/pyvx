from cffi import FFI
import numpy
from pyvx.inc.vx import *

class CHANNEL_R: pass
class CHANNEL_G: pass
class CHANNEL_B: pass
class CHANNEL_A: pass
class CHANNEL_Y: pass
class CHANNEL_U: pass
class CHANNEL_V: pass

channel_char = {
    CHANNEL_0: '0',
    CHANNEL_1: '1',
    CHANNEL_2: '2',
    CHANNEL_3: '3',
    CHANNEL_R: 'r',
    CHANNEL_G: 'g',
    CHANNEL_B: 'b',
    CHANNEL_A: 'a',
    CHANNEL_Y: 'y',
    CHANNEL_U: 'u',
    CHANNEL_V: 'v',
}

class ImageFormatMeta(type):
    def __new__(cls, name, bases, attrs):
        cls = type.__new__(cls, name, bases, attrs)
        if cls.dtype is not None:
            ImageFormat.color2image_format[cls.color] = cls
            cls.dtype = numpy.dtype(cls.dtype)
            if not cls.ctype:
                cls.ctype = cls.dtype.name + '_t'
            assert FFI().sizeof(cls.ctype) == cls.dtype.itemsize
            if cls.items == 1:
                assert cls.dtype not in ImageFormat.dtype2color
                ImageFormat.dtype2color[cls.dtype] = cls.color
            try:
                cls.maxval = numpy.iinfo(cls.dtype).max
                cls.minval = numpy.iinfo(cls.dtype).min
                cls.inttype = True
            except ValueError:
                cls.maxval = numpy.finfo(cls.dtype).max
                cls.minval = numpy.finfo(cls.dtype).min
                cls.inttype = False
        return cls

class ImageFormat(object):
    __metaclass__ = ImageFormatMeta
    dtype2color = {}
    color2image_format = {}

    items = 1
    channels = [CHANNEL_0]
    channel_offsets = [0]
    channel_subsamp = [False]
    dtype = None
    ctype = None

    @classmethod
    def subsamp(cls, channel):
        if cls.channel_subsamp[cls.channels.index(channel)]:
            return 'subsample'
        return ''

    @classmethod
    def offset(cls, channel):
        return cls.channel_offsets[cls.channels.index(channel)]

    @classmethod
    def imagepatch_addressing(cls, width, height):
        stride = len(cls.channels)
        ss = cls.channel_subsamp[:cls.items]
        steps = [2 if s else 1 for s in ss]
        return [imagepatch_addressing(dim_x=width, dim_y=height,
                                      stride_x=stride, stride_y=stride*width,
                                      step_x=st, step_y=1,
                                      scale_x=SCALE_UNITY/st, scale_y=SCALE_UNITY)
                for st in steps]

class ImageFormatVIRT(ImageFormat): 
    color = DF_IMAGE_VIRT

class ImageFormatRGB(ImageFormat):
    items = 3
    dtype = 'uint8'
    channels = [CHANNEL_R, CHANNEL_G, CHANNEL_B, CHANNEL_0, CHANNEL_1, CHANNEL_2]
    channel_offsets = [0, 1, 2] * 2
    channel_subsamp = [False, False, False] * 2
    color = DF_IMAGE_RGB

class ImageFormatRGBX(ImageFormat):
    items = 4
    dtype = 'uint8'
    channels = [CHANNEL_R, CHANNEL_G, CHANNEL_B, CHANNEL_0, CHANNEL_1, CHANNEL_2, CHANNEL_3]
    channel_offsets = [0, 1, 2, 0, 1, 2, 3]
    channel_subsamp = [False, False, False, False, False, False, False] 
    color = DF_IMAGE_RGBX

class ImageFormatUYVY(ImageFormat):
    items = 2
    dtype = 'uint8'
    channels = [CHANNEL_Y, CHANNEL_U, CHANNEL_V, CHANNEL_0, CHANNEL_1, CHANNEL_2]
    channel_offsets = [1, 0, 2] * 2
    channel_subsamp = [False, True, True] * 2
    color = DF_IMAGE_UYVY

class ImageFormatYUYV(ImageFormat):
    items = 2
    dtype = 'uint8'
    channels = [CHANNEL_Y, CHANNEL_U, CHANNEL_V, CHANNEL_0, CHANNEL_1, CHANNEL_2]
    channel_offsets = [0, 1, 3] * 2
    channel_subsamp = [False, True, True] * 2
    color = DF_IMAGE_YUYV

class ImageFormatU8(ImageFormat): 
    dtype = 'uint8'
    color = DF_IMAGE_U8

class ImageFormatS8(ImageFormat): 
    dtype = 'int8'
    color = DF_IMAGE_S8

class ImageFormatU16(ImageFormat): 
    dtype = 'uint16'
    color = DF_IMAGE_U16

class ImageFormatS16(ImageFormat): 
    dtype = 'int16'
    color = DF_IMAGE_S16

class ImageFormatU32(ImageFormat): 
    dtype = 'uint32'
    color = DF_IMAGE_U32

class ImageFormatS32(ImageFormat): 
    dtype = 'int32'
    color = DF_IMAGE_S32

class ImageFormatU64(ImageFormat): 
    dtype = 'uint64'
    color = DF_IMAGE_U64

class ImageFormatS64(ImageFormat): 
    dtype = 'int64'
    color = DF_IMAGE_S64

class ImageFormatF32(ImageFormat): 
    dtype = 'float32'
    ctype = 'float'
    color = DF_IMAGE_F32

class ImageFormatF64(ImageFormat): 
    dtype = 'float64'
    ctype = 'double'
    color = DF_IMAGE_F64

try:
    class ImageFormatF128(ImageFormat):
        dtype = 'float128'
        ctype = 'long double'
        color = DF_IMAGE_F128
except TypeError:
    pass

def result_color(t0, *formats):
    if numpy.result_type is None:
        return t0 # FIXME
    dt = numpy.result_type(*[c.dtype for c in formats])
    return ImageFormat.dtype2color[dt]

def value_color_type(val):
    dt = numpy.array([val]).dtype
    return ImageFormat.dtype2color[dt]

def signed_format(col):
    return {ImageFormatU8: ImageFormatS8,
            ImageFormatS8: ImageFormatS8,
            ImageFormatU16: ImageFormatS16,
            ImageFormatS16: ImageFormatS16,
            ImageFormatU32: ImageFormatS32,
            ImageFormatS32: ImageFormatS32,
            ImageFormatU64: ImageFormatS64,
            ImageFormatS64: ImageFormatS64,
            ImageFormatF32: ImageFormatF32,
            ImageFormatF64: ImageFormatF64,
            ImageFormatF128: ImageFormatF128,
           }[col]

def image_format(color):
    return ImageFormat.color2image_format[color]

class VxError(Exception): pass
class VerificationError(VxError): pass

class MultipleWritersError(VerificationError): errno = ERROR_MULTIPLE_WRITERS
class InvalidGraphError(VerificationError):    errno = ERROR_INVALID_GRAPH
class InvalidValueError(VerificationError):    errno = ERROR_INVALID_VALUE
class InvalidFormatError(VerificationError):   errno = ERROR_INVALID_FORMAT
class InvalidNodeError(VerificationError):     errno = ERROR_INVALID_NODE

class GraphAbandonedError(VxError): errno = ERROR_GRAPH_ABANDONED
class InvalidReferenceError(VxError): errno = ERROR_INVALID_REFERENCE
class InvalidParametersError(VxError): errno = ERROR_INVALID_PARAMETERS

enum2ctype = {
    TYPE_CHAR    : 'vx_char',
    TYPE_INT8    : 'vx_int8',
    TYPE_UINT8   : 'vx_uint8',
    TYPE_INT16   : 'vx_int16',
    TYPE_UINT16  : 'vx_uint16',
    TYPE_INT32   : 'vx_int32',
    TYPE_UINT32  : 'vx_uint32',
    TYPE_INT64   : 'vx_int64',
    TYPE_UINT64  : 'vx_uint64',
    TYPE_FLOAT32 : 'vx_float32',
    TYPE_FLOAT64 : 'vx_float64',
    TYPE_ENUM    : 'vx_enum',
    TYPE_SIZE    : 'vx_size',
    TYPE_DF_IMAGE: 'vx_df_image',
    TYPE_BOOL    : 'vx_bool',
}
