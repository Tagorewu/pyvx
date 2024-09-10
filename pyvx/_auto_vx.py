from pyvx.backend import lib, ffi
ACTION_ABANDON = lib.VX_ACTION_ABANDON
ACTION_COMPLETE = lib.VX_ACTION_COMPLETE
ACTION_CONTINUE = lib.VX_ACTION_CONTINUE
ARRAY_CAPACITY = lib.VX_ARRAY_CAPACITY
ARRAY_ITEMSIZE = lib.VX_ARRAY_ITEMSIZE
ARRAY_ITEMTYPE = lib.VX_ARRAY_ITEMTYPE
ARRAY_NUMITEMS = lib.VX_ARRAY_NUMITEMS
ATTRIBUTE_ID_MASK = lib.VX_ATTRIBUTE_ID_MASK
BORDER_CONSTANT = lib.VX_BORDER_CONSTANT
BORDER_POLICY_DEFAULT_TO_UNDEFINED = lib.VX_BORDER_POLICY_DEFAULT_TO_UNDEFINED
BORDER_POLICY_RETURN_ERROR = lib.VX_BORDER_POLICY_RETURN_ERROR
BORDER_REPLICATE = lib.VX_BORDER_REPLICATE
BORDER_UNDEFINED = lib.VX_BORDER_UNDEFINED
CHANNEL_0 = lib.VX_CHANNEL_0
CHANNEL_1 = lib.VX_CHANNEL_1
CHANNEL_2 = lib.VX_CHANNEL_2
CHANNEL_3 = lib.VX_CHANNEL_3
CHANNEL_A = lib.VX_CHANNEL_A
CHANNEL_B = lib.VX_CHANNEL_B
CHANNEL_G = lib.VX_CHANNEL_G
CHANNEL_R = lib.VX_CHANNEL_R
CHANNEL_RANGE_FULL = lib.VX_CHANNEL_RANGE_FULL
CHANNEL_RANGE_RESTRICTED = lib.VX_CHANNEL_RANGE_RESTRICTED
CHANNEL_U = lib.VX_CHANNEL_U
CHANNEL_V = lib.VX_CHANNEL_V
CHANNEL_Y = lib.VX_CHANNEL_Y
COLOR_SPACE_BT601_525 = lib.VX_COLOR_SPACE_BT601_525
COLOR_SPACE_BT601_625 = lib.VX_COLOR_SPACE_BT601_625
COLOR_SPACE_BT709 = lib.VX_COLOR_SPACE_BT709
COLOR_SPACE_DEFAULT = lib.VX_COLOR_SPACE_DEFAULT
COLOR_SPACE_NONE = lib.VX_COLOR_SPACE_NONE
COMPARE_CCORR = lib.VX_COMPARE_CCORR
COMPARE_CCORR_NORM = lib.VX_COMPARE_CCORR_NORM
COMPARE_HAMMING = lib.VX_COMPARE_HAMMING
COMPARE_L1 = lib.VX_COMPARE_L1
COMPARE_L2 = lib.VX_COMPARE_L2
COMPARE_L2_NORM = lib.VX_COMPARE_L2_NORM
CONTEXT_CONVOLUTION_MAX_DIMENSION = lib.VX_CONTEXT_CONVOLUTION_MAX_DIMENSION
CONTEXT_EXTENSIONS = lib.VX_CONTEXT_EXTENSIONS
CONTEXT_EXTENSIONS_SIZE = lib.VX_CONTEXT_EXTENSIONS_SIZE
CONTEXT_IMMEDIATE_BORDER = lib.VX_CONTEXT_IMMEDIATE_BORDER
CONTEXT_IMMEDIATE_BORDER_POLICY = lib.VX_CONTEXT_IMMEDIATE_BORDER_POLICY
CONTEXT_IMPLEMENTATION = lib.VX_CONTEXT_IMPLEMENTATION
CONTEXT_MAX_TENSOR_DIMS = lib.VX_CONTEXT_MAX_TENSOR_DIMS
CONTEXT_MODULES = lib.VX_CONTEXT_MODULES
CONTEXT_NONLINEAR_MAX_DIMENSION = lib.VX_CONTEXT_NONLINEAR_MAX_DIMENSION
CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION = lib.VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION
CONTEXT_REFERENCES = lib.VX_CONTEXT_REFERENCES
CONTEXT_UNIQUE_KERNELS = lib.VX_CONTEXT_UNIQUE_KERNELS
CONTEXT_UNIQUE_KERNEL_TABLE = lib.VX_CONTEXT_UNIQUE_KERNEL_TABLE
CONTEXT_VENDOR_ID = lib.VX_CONTEXT_VENDOR_ID
CONTEXT_VERSION = lib.VX_CONTEXT_VERSION
CONVERT_POLICY_SATURATE = lib.VX_CONVERT_POLICY_SATURATE
CONVERT_POLICY_WRAP = lib.VX_CONVERT_POLICY_WRAP
CONVOLUTION_COLUMNS = lib.VX_CONVOLUTION_COLUMNS
CONVOLUTION_ROWS = lib.VX_CONVOLUTION_ROWS
CONVOLUTION_SCALE = lib.VX_CONVOLUTION_SCALE
CONVOLUTION_SIZE = lib.VX_CONVOLUTION_SIZE
DELAY_SLOTS = lib.VX_DELAY_SLOTS
DELAY_TYPE = lib.VX_DELAY_TYPE
DF_IMAGE_IYUV = lib.VX_DF_IMAGE_IYUV
DF_IMAGE_NV12 = lib.VX_DF_IMAGE_NV12
DF_IMAGE_NV21 = lib.VX_DF_IMAGE_NV21
DF_IMAGE_RGB = lib.VX_DF_IMAGE_RGB
DF_IMAGE_RGBX = lib.VX_DF_IMAGE_RGBX
DF_IMAGE_S16 = lib.VX_DF_IMAGE_S16
DF_IMAGE_S32 = lib.VX_DF_IMAGE_S32
DF_IMAGE_U1 = lib.VX_DF_IMAGE_U1
DF_IMAGE_U16 = lib.VX_DF_IMAGE_U16
DF_IMAGE_U32 = lib.VX_DF_IMAGE_U32
DF_IMAGE_U8 = lib.VX_DF_IMAGE_U8
DF_IMAGE_UYVY = lib.VX_DF_IMAGE_UYVY
DF_IMAGE_VIRT = lib.VX_DF_IMAGE_VIRT
DF_IMAGE_YUV4 = lib.VX_DF_IMAGE_YUV4
DF_IMAGE_YUYV = lib.VX_DF_IMAGE_YUYV
DIRECTIVE_DISABLE_LOGGING = lib.VX_DIRECTIVE_DISABLE_LOGGING
DIRECTIVE_DISABLE_PERFORMANCE = lib.VX_DIRECTIVE_DISABLE_PERFORMANCE
DIRECTIVE_ENABLE_LOGGING = lib.VX_DIRECTIVE_ENABLE_LOGGING
DIRECTIVE_ENABLE_PERFORMANCE = lib.VX_DIRECTIVE_ENABLE_PERFORMANCE
DISTRIBUTION_BINS = lib.VX_DISTRIBUTION_BINS
DISTRIBUTION_DIMENSIONS = lib.VX_DISTRIBUTION_DIMENSIONS
DISTRIBUTION_OFFSET = lib.VX_DISTRIBUTION_OFFSET
DISTRIBUTION_RANGE = lib.VX_DISTRIBUTION_RANGE
DISTRIBUTION_SIZE = lib.VX_DISTRIBUTION_SIZE
DISTRIBUTION_WINDOW = lib.VX_DISTRIBUTION_WINDOW
ENUM_ACCESSOR = lib.VX_ENUM_ACCESSOR
ENUM_ACTION = lib.VX_ENUM_ACTION
ENUM_BORDER = lib.VX_ENUM_BORDER
ENUM_BORDER_POLICY = lib.VX_ENUM_BORDER_POLICY
ENUM_CHANNEL = lib.VX_ENUM_CHANNEL
ENUM_COLOR_RANGE = lib.VX_ENUM_COLOR_RANGE
ENUM_COLOR_SPACE = lib.VX_ENUM_COLOR_SPACE
ENUM_COMPARISON = lib.VX_ENUM_COMPARISON
ENUM_COMP_METRIC = lib.VX_ENUM_COMP_METRIC
ENUM_CONVERT_POLICY = lib.VX_ENUM_CONVERT_POLICY
ENUM_DIRECTION = lib.VX_ENUM_DIRECTION
ENUM_DIRECTIVE = lib.VX_ENUM_DIRECTIVE
ENUM_GRAPH_STATE = lib.VX_ENUM_GRAPH_STATE
ENUM_HINT = lib.VX_ENUM_HINT
ENUM_INTERPOLATION = lib.VX_ENUM_INTERPOLATION
ENUM_LBP_FORMAT = lib.VX_ENUM_LBP_FORMAT
ENUM_MASK = lib.VX_ENUM_MASK
ENUM_MEMORY_TYPE = lib.VX_ENUM_MEMORY_TYPE
ENUM_NONLINEAR = lib.VX_ENUM_NONLINEAR
ENUM_NORM_TYPE = lib.VX_ENUM_NORM_TYPE
ENUM_OVERFLOW = lib.VX_ENUM_OVERFLOW
ENUM_PARAMETER_STATE = lib.VX_ENUM_PARAMETER_STATE
ENUM_PATTERN = lib.VX_ENUM_PATTERN
ENUM_ROUND_POLICY = lib.VX_ENUM_ROUND_POLICY
ENUM_SCALAR_OPERATION = lib.VX_ENUM_SCALAR_OPERATION
ENUM_TARGET = lib.VX_ENUM_TARGET
ENUM_TERM_CRITERIA = lib.VX_ENUM_TERM_CRITERIA
ENUM_THRESHOLD_TYPE = lib.VX_ENUM_THRESHOLD_TYPE
ENUM_TYPE_MASK = lib.VX_ENUM_TYPE_MASK
ERROR_GRAPH_ABANDONED = lib.VX_ERROR_GRAPH_ABANDONED
ERROR_GRAPH_SCHEDULED = lib.VX_ERROR_GRAPH_SCHEDULED
ERROR_INVALID_DIMENSION = lib.VX_ERROR_INVALID_DIMENSION
ERROR_INVALID_FORMAT = lib.VX_ERROR_INVALID_FORMAT
ERROR_INVALID_GRAPH = lib.VX_ERROR_INVALID_GRAPH
ERROR_INVALID_LINK = lib.VX_ERROR_INVALID_LINK
ERROR_INVALID_MODULE = lib.VX_ERROR_INVALID_MODULE
ERROR_INVALID_NODE = lib.VX_ERROR_INVALID_NODE
ERROR_INVALID_PARAMETERS = lib.VX_ERROR_INVALID_PARAMETERS
ERROR_INVALID_REFERENCE = lib.VX_ERROR_INVALID_REFERENCE
ERROR_INVALID_SCOPE = lib.VX_ERROR_INVALID_SCOPE
ERROR_INVALID_TYPE = lib.VX_ERROR_INVALID_TYPE
ERROR_INVALID_VALUE = lib.VX_ERROR_INVALID_VALUE
ERROR_MULTIPLE_WRITERS = lib.VX_ERROR_MULTIPLE_WRITERS
ERROR_NOT_ALLOCATED = lib.VX_ERROR_NOT_ALLOCATED
ERROR_NOT_COMPATIBLE = lib.VX_ERROR_NOT_COMPATIBLE
ERROR_NOT_IMPLEMENTED = lib.VX_ERROR_NOT_IMPLEMENTED
ERROR_NOT_SUFFICIENT = lib.VX_ERROR_NOT_SUFFICIENT
ERROR_NOT_SUPPORTED = lib.VX_ERROR_NOT_SUPPORTED
ERROR_NO_MEMORY = lib.VX_ERROR_NO_MEMORY
ERROR_NO_RESOURCES = lib.VX_ERROR_NO_RESOURCES
ERROR_OPTIMIZED_AWAY = lib.VX_ERROR_OPTIMIZED_AWAY
ERROR_REFERENCE_NONZERO = lib.VX_ERROR_REFERENCE_NONZERO
FAILURE = lib.VX_FAILURE
GRAPH_NUMNODES = lib.VX_GRAPH_NUMNODES
GRAPH_NUMPARAMETERS = lib.VX_GRAPH_NUMPARAMETERS
GRAPH_PERFORMANCE = lib.VX_GRAPH_PERFORMANCE
GRAPH_STATE = lib.VX_GRAPH_STATE
GRAPH_STATE_ABANDONED = lib.VX_GRAPH_STATE_ABANDONED
GRAPH_STATE_COMPLETED = lib.VX_GRAPH_STATE_COMPLETED
GRAPH_STATE_RUNNING = lib.VX_GRAPH_STATE_RUNNING
GRAPH_STATE_UNVERIFIED = lib.VX_GRAPH_STATE_UNVERIFIED
GRAPH_STATE_VERIFIED = lib.VX_GRAPH_STATE_VERIFIED
HINT_PERFORMANCE_DEFAULT = lib.VX_HINT_PERFORMANCE_DEFAULT
HINT_PERFORMANCE_HIGH_SPEED = lib.VX_HINT_PERFORMANCE_HIGH_SPEED
HINT_PERFORMANCE_LOW_POWER = lib.VX_HINT_PERFORMANCE_LOW_POWER
ID_AMD = lib.VX_ID_AMD
ID_ARM = lib.VX_ID_ARM
ID_AXIS = lib.VX_ID_AXIS
ID_BDTI = lib.VX_ID_BDTI
ID_BOSCH = lib.VX_ID_BOSCH
ID_BROADCOM = lib.VX_ID_BROADCOM
ID_CADENCE = lib.VX_ID_CADENCE
ID_CEVA = lib.VX_ID_CEVA
ID_DEFAULT = lib.VX_ID_DEFAULT
ID_FREESCALE = lib.VX_ID_FREESCALE
ID_HUAWEI = lib.VX_ID_HUAWEI
ID_IMAGINATION = lib.VX_ID_IMAGINATION
ID_INTEL = lib.VX_ID_INTEL
ID_ITSEEZ = lib.VX_ID_ITSEEZ
ID_KHRONOS = lib.VX_ID_KHRONOS
ID_MARVELL = lib.VX_ID_MARVELL
ID_MAX = lib.VX_ID_MAX
ID_MEDIATEK = lib.VX_ID_MEDIATEK
ID_MOVIDIUS = lib.VX_ID_MOVIDIUS
ID_NVIDIA = lib.VX_ID_NVIDIA
ID_NXP = lib.VX_ID_NXP
ID_QUALCOMM = lib.VX_ID_QUALCOMM
ID_RENESAS = lib.VX_ID_RENESAS
ID_SAMSUNG = lib.VX_ID_SAMSUNG
ID_SOCIONEXT = lib.VX_ID_SOCIONEXT
ID_ST = lib.VX_ID_ST
ID_SYNOPSYS = lib.VX_ID_SYNOPSYS
ID_TI = lib.VX_ID_TI
ID_USER = lib.VX_ID_USER
ID_VIDEANTIS = lib.VX_ID_VIDEANTIS
ID_VIVANTE = lib.VX_ID_VIVANTE
ID_XILINX = lib.VX_ID_XILINX
IMAGE_FORMAT = lib.VX_IMAGE_FORMAT
IMAGE_HEIGHT = lib.VX_IMAGE_HEIGHT
IMAGE_IS_UNIFORM = lib.VX_IMAGE_IS_UNIFORM
IMAGE_MEMORY_TYPE = lib.VX_IMAGE_MEMORY_TYPE
IMAGE_PLANES = lib.VX_IMAGE_PLANES
IMAGE_RANGE = lib.VX_IMAGE_RANGE
IMAGE_SPACE = lib.VX_IMAGE_SPACE
IMAGE_UNIFORM_VALUE = lib.VX_IMAGE_UNIFORM_VALUE
IMAGE_WIDTH = lib.VX_IMAGE_WIDTH
INPUT = lib.VX_INPUT
INTERPOLATION_AREA = lib.VX_INTERPOLATION_AREA
INTERPOLATION_BILINEAR = lib.VX_INTERPOLATION_BILINEAR
INTERPOLATION_NEAREST_NEIGHBOR = lib.VX_INTERPOLATION_NEAREST_NEIGHBOR
KERNEL_ABSDIFF = lib.VX_KERNEL_ABSDIFF
KERNEL_ADD = lib.VX_KERNEL_ADD
KERNEL_AND = lib.VX_KERNEL_AND
KERNEL_BILATERAL_FILTER = lib.VX_KERNEL_BILATERAL_FILTER
KERNEL_BOX_3x3 = lib.VX_KERNEL_BOX_3x3
KERNEL_CANNY_EDGE_DETECTOR = lib.VX_KERNEL_CANNY_EDGE_DETECTOR
KERNEL_CHANNEL_COMBINE = lib.VX_KERNEL_CHANNEL_COMBINE
KERNEL_CHANNEL_EXTRACT = lib.VX_KERNEL_CHANNEL_EXTRACT
KERNEL_COLOR_CONVERT = lib.VX_KERNEL_COLOR_CONVERT
KERNEL_CONVERTDEPTH = lib.VX_KERNEL_CONVERTDEPTH
KERNEL_COPY = lib.VX_KERNEL_COPY
KERNEL_CUSTOM_CONVOLUTION = lib.VX_KERNEL_CUSTOM_CONVOLUTION
KERNEL_DILATE_3x3 = lib.VX_KERNEL_DILATE_3x3
KERNEL_ENUM = lib.VX_KERNEL_ENUM
KERNEL_EQUALIZE_HISTOGRAM = lib.VX_KERNEL_EQUALIZE_HISTOGRAM
KERNEL_ERODE_3x3 = lib.VX_KERNEL_ERODE_3x3
KERNEL_FAST_CORNERS = lib.VX_KERNEL_FAST_CORNERS
KERNEL_GAUSSIAN_3x3 = lib.VX_KERNEL_GAUSSIAN_3x3
KERNEL_GAUSSIAN_PYRAMID = lib.VX_KERNEL_GAUSSIAN_PYRAMID
KERNEL_HALFSCALE_GAUSSIAN = lib.VX_KERNEL_HALFSCALE_GAUSSIAN
KERNEL_HARRIS_CORNERS = lib.VX_KERNEL_HARRIS_CORNERS
KERNEL_HISTOGRAM = lib.VX_KERNEL_HISTOGRAM
KERNEL_HOG_CELLS = lib.VX_KERNEL_HOG_CELLS
KERNEL_HOG_FEATURES = lib.VX_KERNEL_HOG_FEATURES
KERNEL_HOUGH_LINES_P = lib.VX_KERNEL_HOUGH_LINES_P
KERNEL_IF_BRANCH = lib.VX_KERNEL_IF_BRANCH
KERNEL_INTEGRAL_IMAGE = lib.VX_KERNEL_INTEGRAL_IMAGE
KERNEL_LAPLACIAN_PYRAMID = lib.VX_KERNEL_LAPLACIAN_PYRAMID
KERNEL_LAPLACIAN_RECONSTRUCT = lib.VX_KERNEL_LAPLACIAN_RECONSTRUCT
KERNEL_LBP = lib.VX_KERNEL_LBP
KERNEL_LOCAL_DATA_SIZE = lib.VX_KERNEL_LOCAL_DATA_SIZE
KERNEL_MAGNITUDE = lib.VX_KERNEL_MAGNITUDE
KERNEL_MASK = lib.VX_KERNEL_MASK
KERNEL_MATCH_TEMPLATE = lib.VX_KERNEL_MATCH_TEMPLATE
KERNEL_MAX = lib.VX_KERNEL_MAX
KERNEL_MAX_1_0 = lib.VX_KERNEL_MAX_1_0
KERNEL_MAX_1_1 = lib.VX_KERNEL_MAX_1_1
KERNEL_MAX_1_2 = lib.VX_KERNEL_MAX_1_2
KERNEL_MEAN_STDDEV = lib.VX_KERNEL_MEAN_STDDEV
KERNEL_MEDIAN_3x3 = lib.VX_KERNEL_MEDIAN_3x3
KERNEL_MIN = lib.VX_KERNEL_MIN
KERNEL_MINMAXLOC = lib.VX_KERNEL_MINMAXLOC
KERNEL_MOVE = lib.VX_KERNEL_MOVE
KERNEL_MULTIPLY = lib.VX_KERNEL_MULTIPLY
KERNEL_NAME = lib.VX_KERNEL_NAME
KERNEL_NON_LINEAR_FILTER = lib.VX_KERNEL_NON_LINEAR_FILTER
KERNEL_NON_MAX_SUPPRESSION = lib.VX_KERNEL_NON_MAX_SUPPRESSION
KERNEL_NOT = lib.VX_KERNEL_NOT
KERNEL_OPTICAL_FLOW_PYR_LK = lib.VX_KERNEL_OPTICAL_FLOW_PYR_LK
KERNEL_OR = lib.VX_KERNEL_OR
KERNEL_PARAMETERS = lib.VX_KERNEL_PARAMETERS
KERNEL_PHASE = lib.VX_KERNEL_PHASE
KERNEL_REMAP = lib.VX_KERNEL_REMAP
KERNEL_SCALAR_OPERATION = lib.VX_KERNEL_SCALAR_OPERATION
KERNEL_SCALE_IMAGE = lib.VX_KERNEL_SCALE_IMAGE
KERNEL_SELECT = lib.VX_KERNEL_SELECT
KERNEL_SOBEL_3x3 = lib.VX_KERNEL_SOBEL_3x3
KERNEL_SUBTRACT = lib.VX_KERNEL_SUBTRACT
KERNEL_SWAP = lib.VX_KERNEL_SWAP
KERNEL_TABLE_LOOKUP = lib.VX_KERNEL_TABLE_LOOKUP
KERNEL_TENSOR_ADD = lib.VX_KERNEL_TENSOR_ADD
KERNEL_TENSOR_CONVERT_DEPTH = lib.VX_KERNEL_TENSOR_CONVERT_DEPTH
KERNEL_TENSOR_MATRIX_MULTIPLY = lib.VX_KERNEL_TENSOR_MATRIX_MULTIPLY
KERNEL_TENSOR_MULTIPLY = lib.VX_KERNEL_TENSOR_MULTIPLY
KERNEL_TENSOR_SUBTRACT = lib.VX_KERNEL_TENSOR_SUBTRACT
KERNEL_TENSOR_TABLE_LOOKUP = lib.VX_KERNEL_TENSOR_TABLE_LOOKUP
KERNEL_TENSOR_TRANSPOSE = lib.VX_KERNEL_TENSOR_TRANSPOSE
KERNEL_THRESHOLD = lib.VX_KERNEL_THRESHOLD
KERNEL_WARP_AFFINE = lib.VX_KERNEL_WARP_AFFINE
KERNEL_WARP_PERSPECTIVE = lib.VX_KERNEL_WARP_PERSPECTIVE
KERNEL_WEIGHTED_AVERAGE = lib.VX_KERNEL_WEIGHTED_AVERAGE
KERNEL_XOR = lib.VX_KERNEL_XOR
LBP = lib.VX_LBP
LIBRARY_KHR_BASE = lib.VX_LIBRARY_KHR_BASE
LIBRARY_MASK = lib.VX_LIBRARY_MASK
LUT_COUNT = lib.VX_LUT_COUNT
LUT_OFFSET = lib.VX_LUT_OFFSET
LUT_SIZE = lib.VX_LUT_SIZE
LUT_TYPE = lib.VX_LUT_TYPE
MATRIX_COLUMNS = lib.VX_MATRIX_COLUMNS
MATRIX_ORIGIN = lib.VX_MATRIX_ORIGIN
MATRIX_PATTERN = lib.VX_MATRIX_PATTERN
MATRIX_ROWS = lib.VX_MATRIX_ROWS
MATRIX_SIZE = lib.VX_MATRIX_SIZE
MATRIX_TYPE = lib.VX_MATRIX_TYPE
MAX_IMPLEMENTATION_NAME = lib.VX_MAX_IMPLEMENTATION_NAME
MAX_KERNEL_NAME = lib.VX_MAX_KERNEL_NAME
MAX_LOG_MESSAGE_LEN = lib.VX_MAX_LOG_MESSAGE_LEN
MAX_REFERENCE_NAME = lib.VX_MAX_REFERENCE_NAME
MEMORY_TYPE_HOST = lib.VX_MEMORY_TYPE_HOST
MEMORY_TYPE_NONE = lib.VX_MEMORY_TYPE_NONE
MLBP = lib.VX_MLBP
NODE_BORDER = lib.VX_NODE_BORDER
NODE_CONDITION = lib.VX_NODE_CONDITION
NODE_IS_REPLICATED = lib.VX_NODE_IS_REPLICATED
NODE_LOCAL_DATA_PTR = lib.VX_NODE_LOCAL_DATA_PTR
NODE_LOCAL_DATA_SIZE = lib.VX_NODE_LOCAL_DATA_SIZE
NODE_LOOP_COUNT = lib.VX_NODE_LOOP_COUNT
NODE_PARAMETERS = lib.VX_NODE_PARAMETERS
NODE_PERFORMANCE = lib.VX_NODE_PERFORMANCE
NODE_PROPERTY_STRING = lib.VX_NODE_PROPERTY_STRING
NODE_REPLICATE_FLAGS = lib.VX_NODE_REPLICATE_FLAGS
NODE_STATUS = lib.VX_NODE_STATUS
NODE_VALID_RECT_RESET = lib.VX_NODE_VALID_RECT_RESET
NOGAP_X = lib.VX_NOGAP_X
NONLINEAR_FILTER_MAX = lib.VX_NONLINEAR_FILTER_MAX
NONLINEAR_FILTER_MEDIAN = lib.VX_NONLINEAR_FILTER_MEDIAN
NONLINEAR_FILTER_MIN = lib.VX_NONLINEAR_FILTER_MIN
NORM_L1 = lib.VX_NORM_L1
NORM_L2 = lib.VX_NORM_L2
OBJECT_ARRAY_ITEMTYPE = lib.VX_OBJECT_ARRAY_ITEMTYPE
OBJECT_ARRAY_NUMITEMS = lib.VX_OBJECT_ARRAY_NUMITEMS
OUTPUT = lib.VX_OUTPUT
PARAMETER_DIRECTION = lib.VX_PARAMETER_DIRECTION
PARAMETER_INDEX = lib.VX_PARAMETER_INDEX
PARAMETER_META_FORMAT = lib.VX_PARAMETER_META_FORMAT
PARAMETER_REF = lib.VX_PARAMETER_REF
PARAMETER_STATE = lib.VX_PARAMETER_STATE
PARAMETER_STATE_OPTIONAL = lib.VX_PARAMETER_STATE_OPTIONAL
PARAMETER_STATE_REQUIRED = lib.VX_PARAMETER_STATE_REQUIRED
PARAMETER_TYPE = lib.VX_PARAMETER_TYPE
PATTERN_BOX = lib.VX_PATTERN_BOX
PATTERN_CROSS = lib.VX_PATTERN_CROSS
PATTERN_DISK = lib.VX_PATTERN_DISK
PATTERN_OTHER = lib.VX_PATTERN_OTHER
PYRAMID_FORMAT = lib.VX_PYRAMID_FORMAT
PYRAMID_HEIGHT = lib.VX_PYRAMID_HEIGHT
PYRAMID_LEVELS = lib.VX_PYRAMID_LEVELS
PYRAMID_SCALE = lib.VX_PYRAMID_SCALE
PYRAMID_WIDTH = lib.VX_PYRAMID_WIDTH
READ_AND_WRITE = lib.VX_READ_AND_WRITE
READ_ONLY = lib.VX_READ_ONLY
REFERENCE_COUNT = lib.VX_REFERENCE_COUNT
REFERENCE_IS_INVALID = lib.VX_REFERENCE_IS_INVALID
REFERENCE_NAME = lib.VX_REFERENCE_NAME
REFERENCE_TYPE = lib.VX_REFERENCE_TYPE
REMAP_DESTINATION_HEIGHT = lib.VX_REMAP_DESTINATION_HEIGHT
REMAP_DESTINATION_WIDTH = lib.VX_REMAP_DESTINATION_WIDTH
REMAP_SOURCE_HEIGHT = lib.VX_REMAP_SOURCE_HEIGHT
REMAP_SOURCE_WIDTH = lib.VX_REMAP_SOURCE_WIDTH
ROUND_POLICY_TO_NEAREST_EVEN = lib.VX_ROUND_POLICY_TO_NEAREST_EVEN
ROUND_POLICY_TO_ZERO = lib.VX_ROUND_POLICY_TO_ZERO
SCALAR_ITEMSIZE = lib.VX_SCALAR_ITEMSIZE
SCALAR_OP_ADD = lib.VX_SCALAR_OP_ADD
SCALAR_OP_AND = lib.VX_SCALAR_OP_AND
SCALAR_OP_DIVIDE = lib.VX_SCALAR_OP_DIVIDE
SCALAR_OP_EQUAL = lib.VX_SCALAR_OP_EQUAL
SCALAR_OP_GREATER = lib.VX_SCALAR_OP_GREATER
SCALAR_OP_GREATEREQ = lib.VX_SCALAR_OP_GREATEREQ
SCALAR_OP_LESS = lib.VX_SCALAR_OP_LESS
SCALAR_OP_LESSEQ = lib.VX_SCALAR_OP_LESSEQ
SCALAR_OP_MAX = lib.VX_SCALAR_OP_MAX
SCALAR_OP_MIN = lib.VX_SCALAR_OP_MIN
SCALAR_OP_MODULUS = lib.VX_SCALAR_OP_MODULUS
SCALAR_OP_MULTIPLY = lib.VX_SCALAR_OP_MULTIPLY
SCALAR_OP_NAND = lib.VX_SCALAR_OP_NAND
SCALAR_OP_NOTEQUAL = lib.VX_SCALAR_OP_NOTEQUAL
SCALAR_OP_OR = lib.VX_SCALAR_OP_OR
SCALAR_OP_SUBTRACT = lib.VX_SCALAR_OP_SUBTRACT
SCALAR_OP_XOR = lib.VX_SCALAR_OP_XOR
SCALAR_TYPE = lib.VX_SCALAR_TYPE
SCALE_UNITY = lib.VX_SCALE_UNITY
STATUS_MIN = lib.VX_STATUS_MIN
SUCCESS = lib.VX_SUCCESS
TARGET_ANY = lib.VX_TARGET_ANY
TARGET_STRING = lib.VX_TARGET_STRING
TARGET_VENDOR_BEGIN = lib.VX_TARGET_VENDOR_BEGIN
TENSOR_DATA_TYPE = lib.VX_TENSOR_DATA_TYPE
TENSOR_DIMS = lib.VX_TENSOR_DIMS
TENSOR_FIXED_POINT_POSITION = lib.VX_TENSOR_FIXED_POINT_POSITION
TENSOR_NUMBER_OF_DIMS = lib.VX_TENSOR_NUMBER_OF_DIMS
TERM_CRITERIA_BOTH = lib.VX_TERM_CRITERIA_BOTH
TERM_CRITERIA_EPSILON = lib.VX_TERM_CRITERIA_EPSILON
TERM_CRITERIA_ITERATIONS = lib.VX_TERM_CRITERIA_ITERATIONS
THRESHOLD_INPUT_FORMAT = lib.VX_THRESHOLD_INPUT_FORMAT
THRESHOLD_OUTPUT_FORMAT = lib.VX_THRESHOLD_OUTPUT_FORMAT
THRESHOLD_TYPE = lib.VX_THRESHOLD_TYPE
THRESHOLD_TYPE_BINARY = lib.VX_THRESHOLD_TYPE_BINARY
THRESHOLD_TYPE_RANGE = lib.VX_THRESHOLD_TYPE_RANGE
TYPE_ARRAY = lib.VX_TYPE_ARRAY
TYPE_BOOL = lib.VX_TYPE_BOOL
TYPE_CHAR = lib.VX_TYPE_CHAR
TYPE_CONTEXT = lib.VX_TYPE_CONTEXT
TYPE_CONVOLUTION = lib.VX_TYPE_CONVOLUTION
TYPE_COORDINATES2D = lib.VX_TYPE_COORDINATES2D
TYPE_COORDINATES2DF = lib.VX_TYPE_COORDINATES2DF
TYPE_COORDINATES3D = lib.VX_TYPE_COORDINATES3D
TYPE_DELAY = lib.VX_TYPE_DELAY
TYPE_DF_IMAGE = lib.VX_TYPE_DF_IMAGE
TYPE_DISTRIBUTION = lib.VX_TYPE_DISTRIBUTION
TYPE_ENUM = lib.VX_TYPE_ENUM
TYPE_ERROR = lib.VX_TYPE_ERROR
TYPE_FLOAT16 = lib.VX_TYPE_FLOAT16
TYPE_FLOAT32 = lib.VX_TYPE_FLOAT32
TYPE_FLOAT64 = lib.VX_TYPE_FLOAT64
TYPE_GRAPH = lib.VX_TYPE_GRAPH
TYPE_HOG_PARAMS = lib.VX_TYPE_HOG_PARAMS
TYPE_HOUGH_LINES_PARAMS = lib.VX_TYPE_HOUGH_LINES_PARAMS
TYPE_IMAGE = lib.VX_TYPE_IMAGE
TYPE_INT16 = lib.VX_TYPE_INT16
TYPE_INT32 = lib.VX_TYPE_INT32
TYPE_INT64 = lib.VX_TYPE_INT64
TYPE_INT8 = lib.VX_TYPE_INT8
TYPE_INVALID = lib.VX_TYPE_INVALID
TYPE_KERNEL = lib.VX_TYPE_KERNEL
TYPE_KEYPOINT = lib.VX_TYPE_KEYPOINT
TYPE_KHRONOS_OBJECT_END = lib.VX_TYPE_KHRONOS_OBJECT_END
TYPE_KHRONOS_OBJECT_START = lib.VX_TYPE_KHRONOS_OBJECT_START
TYPE_KHRONOS_STRUCT_MAX = lib.VX_TYPE_KHRONOS_STRUCT_MAX
TYPE_LINE_2D = lib.VX_TYPE_LINE_2D
TYPE_LUT = lib.VX_TYPE_LUT
TYPE_MASK = lib.VX_TYPE_MASK
TYPE_MATRIX = lib.VX_TYPE_MATRIX
TYPE_META_FORMAT = lib.VX_TYPE_META_FORMAT
TYPE_NODE = lib.VX_TYPE_NODE
TYPE_OBJECT_ARRAY = lib.VX_TYPE_OBJECT_ARRAY
TYPE_PARAMETER = lib.VX_TYPE_PARAMETER
TYPE_PYRAMID = lib.VX_TYPE_PYRAMID
TYPE_RECTANGLE = lib.VX_TYPE_RECTANGLE
TYPE_REFERENCE = lib.VX_TYPE_REFERENCE
TYPE_REMAP = lib.VX_TYPE_REMAP
TYPE_SCALAR = lib.VX_TYPE_SCALAR
TYPE_SIZE = lib.VX_TYPE_SIZE
TYPE_TENSOR = lib.VX_TYPE_TENSOR
TYPE_TENSOR_MATRIX_MULTIPLY_PARAMS = lib.VX_TYPE_TENSOR_MATRIX_MULTIPLY_PARAMS
TYPE_THRESHOLD = lib.VX_TYPE_THRESHOLD
TYPE_UINT16 = lib.VX_TYPE_UINT16
TYPE_UINT32 = lib.VX_TYPE_UINT32
TYPE_UINT64 = lib.VX_TYPE_UINT64
TYPE_UINT8 = lib.VX_TYPE_UINT8
TYPE_USER_STRUCT_END = lib.VX_TYPE_USER_STRUCT_END
TYPE_USER_STRUCT_START = lib.VX_TYPE_USER_STRUCT_START
TYPE_VENDOR_OBJECT_END = lib.VX_TYPE_VENDOR_OBJECT_END
TYPE_VENDOR_OBJECT_START = lib.VX_TYPE_VENDOR_OBJECT_START
TYPE_VENDOR_STRUCT_END = lib.VX_TYPE_VENDOR_STRUCT_END
TYPE_VENDOR_STRUCT_START = lib.VX_TYPE_VENDOR_STRUCT_START
ULBP = lib.VX_ULBP
VALID_RECT_CALLBACK = lib.VX_VALID_RECT_CALLBACK
VENDOR_MASK = lib.VX_VENDOR_MASK
VERSION = lib.VX_VERSION
VERSION_1_0 = lib.VX_VERSION_1_0
VERSION_1_1 = lib.VX_VERSION_1_1
VERSION_1_2 = lib.VX_VERSION_1_2
VERSION_1_3 = lib.VX_VERSION_1_3
WRITE_ONLY = lib.VX_WRITE_ONLY
false_e = lib.vx_false_e
true_e = lib.vx_true_e

def CreateContext():
    '''
:brief: Creates a *vx_context*.
:details: This creates a top-level object context for OpenVX.
:note: This is required to do anything else.
:returns: The reference to the implementation context *vx_context*. Any possible errors
preventing a successful creation should be checked using *vxGetStatus*.
:ingroup: group_context
:post: *vxReleaseContext*
    '''
    return lib.vxCreateContext()
    
def ReleaseContext(context):
    '''
:brief: Releases the OpenVX object context.
:details: All reference counted objects are garbage-collected by the return of this call.
No calls are possible using the parameter context after the context has been
released until a new reference from *vxCreateContext* is returned.
All outstanding references to OpenVX objects from this context are invalid
after this call.
:param: [in] context The pointer to the reference to the context.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE context is not a valid *vx_context* reference.
:ingroup: group_context
:pre: *vxCreateContext*
    '''
    return lib.vxReleaseContext(context)
    
def GetContext(reference):
    '''
:brief: Retrieves the context from any reference from within a context.
:param: [in] reference The reference from which to extract the context.
:ingroup: group_context
:return: The overall context that created the particular
reference. Any possible errors preventing a successful completion of this function
should be checked using *vxGetStatus*.
    '''
    return lib.vxGetContext(reference)
    
def QueryContext(context, attribute, ptr, size):
    '''
:brief: Queries the context for some specific information.
:param: [in] context The reference to the context.
:param: [in] attribute The attribute to query. Use a *vx_context_attribute_e*.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE context is not a valid *vx_context* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute is not supported on this implementation.
:ingroup: group_context
    '''
    return lib.vxQueryContext(context, attribute, ptr, size)
    
def SetContextAttribute(context, attribute, ptr, size):
    '''
:brief: Sets an attribute on the context.
:param: [in] context The handle to the overall context.
:param: [in] attribute The attribute to set from *vx_context_attribute_e*.
:param: [in] ptr The pointer to the data to which to set the attribute.
:param: [in] size The size in bytes of the data to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE context is not a valid *vx_context* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute is not settable.
:ingroup: group_context
    '''
    return lib.vxSetContextAttribute(context, attribute, ptr, size)
    
def Hint(reference, hint, data, data_size):
    '''
:brief: Provides a generic API to give platform-specific hints to the implementation.
:param: [in] reference The reference to the object to hint at.
This could be *vx_context*, *vx_graph*, *vx_node*, *vx_image*, *vx_array*, or any other reference.
:param: [in] hint A *vx_hint_e* :a: hint to give to a vx_context. This is a platform-specific optimization or implementation mechanism.
:param: [in] data Optional vendor specific data.
:param: [in] data_size Size of the data structure :p: data.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE reference is not a valid *vx_reference* reference.
:retval: VX_ERROR_NOT_SUPPORTED If the hint is not supported.
:ingroup: group_hint
    '''
    return lib.vxHint(reference, hint, data, data_size)
    
def Directive(reference, directive):
    '''
:brief: Provides a generic API to give platform-specific directives to the implementations.
:param: [in] reference The reference to the object to set the directive on.
This could be *vx_context*, *vx_graph*, *vx_node*, *vx_image*, *vx_array*, or any other reference.
:param: [in] directive The directive to set. See *vx_directive_e*.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE reference is not a valid *vx_reference* reference.
:retval: VX_ERROR_NOT_SUPPORTED If the directive is not supported.
:note: The performance counter directives are only available for the reference vx_context.
      Error VX_ERROR_NOT_SUPPORTED is returned when used with any other reference.
:ingroup: group_directive
    '''
    return lib.vxDirective(reference, directive)
    
def GetStatus(reference):
    '''
:brief: Provides a generic API to return status values from Object constructors if they
fail.
:note: Users do not need to strictly check every object creator as the errors
should properly propagate and be detected during verification time or run-time.
:code:
vx_image img = vxCreateImage(context, 639, 480, VX_DF_IMAGE_UYVY);
vx_status status = vxGetStatus((vx_reference)img);
// status == VX_ERROR_INVALID_DIMENSIONS
vxReleaseImage(&img);
:endcode:
:pre: Appropriate Object Creator function.
:post: Appropriate Object Release function.
:param: [in] reference The reference to check for construction errors.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval:Some error occurred, please check enumeration list and constructor.
:ingroup: group_basic_features
    '''
    return lib.vxGetStatus(reference)
    
def RegisterUserStruct(context, size):
    '''
:brief: Registers user-defined structures to the context.
:param: [in] context  The reference to the implementation context.
:param: [in] size     The size of user struct in bytes.
:return: A *vx_enum* value that is a type given to the User
to refer to their custom structure when declaring a *vx_array*
of that structure.
:retval: VX_TYPE_INVALID If the namespace of types has been exhausted.
:note: This call should only be used once within the lifetime of a context for
a specific structure.
:ingroup: group_adv_array
    '''
    return lib.vxRegisterUserStruct(context, size)
    
def RegisterUserStructWithName(context, size, type_name):
    '''
:brief: Registers user-defined structures to the context, and associates a name to it.
:param: [in] context     The reference to the implementation context.
:param: [in] size        The size of user struct in bytes.
:param: [in]type_name  Pointer to the '\0' terminated string that identifies the
                        user struct type. The string is copied by the function so
                        that it stays the property of the caller. NULL means that
                        the user struct is not named. The length of the string
                        shall be lower than VX_MAX_REFERENCE_NAME bytes.
:return: A *vx_enum* value that is a type given to the User
to refer to their custom structure when declaring a *vx_array*
of that structure.
:retval: VX_TYPE_INVALID If the namespace of types has been exhausted.
:note: This call should only be used once within the lifetime of a context for
a specific structure.
:ingroup: group_adv_array
    '''
    return lib.vxRegisterUserStructWithName(context, size, type_name)
    
def GetUserStructNameByEnum(context, user_struct_type, type_name, name_size):
    '''
:brief: Returns the name of the user-defined structure associated with the enumeration given.
:param: [in] context     The reference to the implementation context.
:param: [in] type_name   The enumeration value of the user struct
:param: [out] name_size  Name of the user struct
:param: [in] name_size   The size of allocated buffer pointed to by type_name
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS user_struct_type was valid, and name was found and returned
:retval: VX_ERROR_INVALID_PARAMETERS user_struct_type was not a valid user struct enumeration.
:retval: VX_ERROR_NO_MEMORY name_size is too small to hold the name of the user struct type.
:retval: VX_FAILURE user_struct_type does not have an associated type name.
:pre: *vxRegisterUserStructWithName* should be called for this user struct.
:ingroup: group_adv_array
    '''
    return lib.vxGetUserStructNameByEnum(context, user_struct_type, type_name, name_size)
    
def GetUserStructEnumByName(context, type_name, user_struct_type):
    '''
:brief: Returns the enum of the user-defined structure associated with the name given
:param: [in] context           The reference to the implementation context.
:param: [in] type_name         Pointer to the '\0' terminated string that identifies the user
                              struct type. The length of the string shall be lower than VX_MAX_REFERENCE_NAME bytes.
:param: [out] user_struct_type The enumeration value of the user struct
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS type_name was valid, and enumeration was found and returned
:retval: VX_FAILURE type_name does not match any user struct enumeration.
* :pre: *vxRegisterUserStructWithName* should be called for this user struct.
:ingroup: group_adv_array
    '''
    return lib.vxGetUserStructEnumByName(context, type_name, user_struct_type)
    
def AllocateUserKernelId(context, pKernelEnumId):
    '''
:brief: Allocates and registers user-defined kernel enumeration to a context.
The allocated enumeration is from available pool of 4096 enumerations reserved
for dynamic allocation from VX_KERNEL_BASE(VX_ID_USER,0).
:param: [in] context  The reference to the implementation context.
:param: [out] pKernelEnumId  pointer to return *vx_enum* for user-defined kernel.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE If the context is not a valid *vx_context* reference.
:retval: VX_ERROR_NO_RESOURCES The enumerations has been exhausted.
:ingroup: group_user_kernels
    '''
    return lib.vxAllocateUserKernelId(context, pKernelEnumId)
    
def AllocateUserKernelLibraryId(context, pLibraryId):
    '''
:brief: Allocates and registers user-defined kernel library ID to a context.

The allocated library ID is from available pool of library IDs (1..255)
reserved for dynamic allocation. The returned libraryId can be used by
user-kernel library developer to specify individual kernel enum IDs in
a header file, shown below:
:code:
#define MY_KERNEL_ID1(libraryId) (VX_KERNEL_BASE(VX_ID_USER,libraryId) + 0);
#define MY_KERNEL_ID2(libraryId) (VX_KERNEL_BASE(VX_ID_USER,libraryId) + 1);
#define MY_KERNEL_ID3(libraryId) (VX_KERNEL_BASE(VX_ID_USER,libraryId) + 2);
:endcode:
:param: [in] context  The reference to the implementation context.
:param: [out] pLibraryId  pointer to *vx_enum* for user-kernel libraryId.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_NO_RESOURCES The enumerations has been exhausted.
:ingroup: group_user_kernels
    '''
    return lib.vxAllocateUserKernelLibraryId(context, pLibraryId)
    
def SetImmediateModeTarget(context, target_enum, target_string):
    '''
:brief: Sets the default target of the immediate mode. Upon successful execution of this
function any future execution of immediate mode function is attempted on the new default
target of the context.
:param: [in] context  The reference to the implementation context.
:param: [in] target_enum  The default immediate mode target enum to be set
to the *vx_context* object. Use a *vx_target_e*.
:param: [in] target_string  The target name ASCII string. This contains a valid value
when target_enum is set to *VX_TARGET_STRING*, otherwise it is ignored.
:ingroup: group_context
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Default target set; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE If the context is not a valid *vx_context* reference.
:retval: VX_ERROR_NOT_SUPPORTED If the specified target is not supported in this context.
    '''
    return lib.vxSetImmediateModeTarget(context, target_enum, target_string)
    
def CreateImage(context, width, height, color):
    '''
:brief: Creates an opaque reference to an image buffer.
:details: Not guaranteed to exist until the *vx_graph* containing it has been verified.
:param: [in] context The reference to the implementation context.
:param: [in] width The image width in pixels. The image in the formats of
*VX_DF_IMAGE_NV12*, *VX_DF_IMAGE_NV21*, *VX_DF_IMAGE_IYUV*,
*VX_DF_IMAGE_UYVY*, *VX_DF_IMAGE_YUYV* must have even width.
:param: [in] height The image height in pixels. The image in the formats of
*VX_DF_IMAGE_NV12*, *VX_DF_IMAGE_NV21*, *VX_DF_IMAGE_IYUV*
must have even height.
:param: [in] color The VX_DF_IMAGE (*vx_df_image_e*) code that represents the format
of the image and the color space.
:returns: An image reference *vx_image*. Any possible errors preventing a successful
creation should be checked using *vxGetStatus*.
:see: vxMapImagePatch to obtain direct memory access to the image data.
:ingroup: group_image
    '''
    return lib.vxCreateImage(context, width, height, color)
    
def CreateImageFromROI(img, rect):
    '''
:brief: Creates an image from another image given a rectangle. This second
reference refers to the data in the original image. Updates to this image
updates the parent image. The rectangle must be defined within the pixel space
of the parent image.
:param: [in] img The reference to the parent image.
:param: [in] rect The region of interest rectangle. Must contain points within
the parent image pixel space.
:returns: An image reference *vx_image* to the sub-image. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_image
    '''
    return lib.vxCreateImageFromROI(img, rect)
    
def CreateUniformImage(context, width, height, color, value):
    '''
:brief: Creates a reference to an image object that has a singular,
uniform value in all pixels. The uniform image created is read-only.
:param: [in] context The reference to the implementation context.
:param: [in] width The image width in pixels. The image in the formats of
*VX_DF_IMAGE_NV12*, *VX_DF_IMAGE_NV21*, *VX_DF_IMAGE_IYUV*,
*VX_DF_IMAGE_UYVY*, *VX_DF_IMAGE_YUYV* must have even width.
:param: [in] height The image height in pixels. The image in the formats of
*VX_DF_IMAGE_NV12*, *VX_DF_IMAGE_NV21*,
*VX_DF_IMAGE_IYUV* must have even height.
:param: [in] color The VX_DF_IMAGE (vx_df_image_e) code that represents the format of the image and the color space.
:param: [in] value The pointer to the pixel value to which to set all pixels. See *vx_pixel_value_t*.
:returns: An image reference *vx_image*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
*:see: vxMapImagePatch* to obtain direct memory access to the image data.
:note: *vxMapImagePatch* and *vxUnmapImagePatch* may be called with
a uniform image reference.
:ingroup: group_image
    '''
    return lib.vxCreateUniformImage(context, width, height, color, value)
    
def CreateVirtualImage(graph, width, height, color):
    '''
:brief: Creates an opaque reference to an image buffer with no direct
user access. This function allows setting the image width, height, or format.
:details: Virtual data objects allow users to connect various nodes within a
graph via data references without access to that data, but they also permit the
implementation to take maximum advantage of possible optimizations. Use this
API to create a data reference to link two or more nodes together when the
intermediate data are not required to be accessed by outside entities. This API
in particular allows the user to define the image format of the data without
requiring the exact dimensions. Virtual objects are scoped within the graph
they are declared a part of, and can't be shared outside of this scope.
All of the following constructions of virtual images are valid.
:code:
vx_context context = vxCreateContext();
vx_graph graph = vxCreateGraph(context);
vx_image virt[] = {
    vxCreateVirtualImage(graph, 0, 0, VX_DF_IMAGE_U8), // no specified dimension
    vxCreateVirtualImage(graph, 320, 240, VX_DF_IMAGE_VIRT), // no specified format
    vxCreateVirtualImage(graph, 640, 480, VX_DF_IMAGE_U8), // no user access
};
:endcode:
:param: [in] graph The reference to the parent graph.
:param: [in] width The width of the image in pixels. A value of zero informs the interface
that the value is unspecified. The image in the formats of *VX_DF_IMAGE_NV12*,
*VX_DF_IMAGE_NV21*, *VX_DF_IMAGE_IYUV*, *VX_DF_IMAGE_UYVY*,
*VX_DF_IMAGE_YUYV* must have even width.
:param: [in] height The height of the image in pixels. A value of zero informs the interface
that the value is unspecified. The image in the formats of *VX_DF_IMAGE_NV12*,
*VX_DF_IMAGE_NV21*, *VX_DF_IMAGE_IYUV* must have even height.
:param: [in] color The VX_DF_IMAGE (*vx_df_image_e*) code that represents the format
of the image and the color space. A value of *VX_DF_IMAGE_VIRT* informs the
interface that the format is unspecified.
:returns: An image reference *vx_image*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:note: Passing this reference to *vxMapImagePatch* will return an error.
:ingroup: group_image
    '''
    return lib.vxCreateVirtualImage(graph, width, height, color)
    
def CreateImageFromHandle(context, color, addrs, ptrs, memory_type):
    '''
:brief: Creates a reference to an image object that was externally allocated.
:param: [in] context The reference to the implementation context.
:param: [in] color See the *vx_df_image_e* codes. This mandates the
number of planes needed to be valid in the :a: addrs and :a: ptrs arrays based on the format given.
:param: [in] addrs[] The array of image patch addressing structures that
define the dimension and stride of the array of pointers. See note below.
:param: [in] ptrs[] The array of platform-defined references to each plane. See note below.
:param: [in] memory_type *vx_memory_type_e*. When giving *VX_MEMORY_TYPE_HOST*
the :a: ptrs array is assumed to be HOST accessible pointers to memory.
:returns: An image reference *vx_image*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:note: The user must call vxMapImagePatch prior to accessing the pixels of an image, even if the
image was created via *vxCreateImageFromHandle*. Reads or writes to memory referenced
by ptrs[ ] after calling *vxCreateImageFromHandle* without first calling
*vxMapImagePatch* will result in undefined behavior.
The property of addr[] and ptrs[] arrays is kept by the caller (It means that the implementation will
make an internal copy of the provided information. :a: addr and :a: ptrs can then simply be application's
local variables).
Only :a: dim_x, :a: dim_y, :a: stride_x and :a: stride_y fields of the *vx_imagepatch_addressing_t* need to be
provided by the application. Other fields (:a: step_x, :a: step_y, :a: scale_x & :a: scale_y) are ignored by this function.
The layout of the imported memory must follow a row-major order. In other words, :a: stride_x should be
sufficiently large so that there is no overlap between data elements corresponding to different
pixels, and :a: stride_y >= :a: stride_x:a: dim_x.

In order to release the image back to the application we should use *vxSwapImageHandle*.
An exception is for *VX_DF_IMAGE_U1* images where :a: stride_x == 0 and instead
:a: stride_y >= &lceil;:a: dim_x / 8&rceil;.

Import type of the created image is available via the image attribute *vx_image_attribute_e* parameter.

:ingroup: group_image
    '''
    return lib.vxCreateImageFromHandle(context, color, addrs, ptrs, memory_type)
    
def SwapImageHandle(image, new_ptrs, prev_ptrs, num_planes):
    '''
:brief: Swaps the image handle of an image previously created from handle.

This function sets the new image handle (i.e. pointer to all image planes)
and returns the previous one.

Once this function call has completed, the application gets back the
ownership of the memory referenced by the previous handle. This memory
contains up-to-date pixel data, and the application can safely reuse or
release it.

The memory referenced by the new handle must have been allocated
consistently with the image properties since the import type,
memory layout and dimensions are unchanged (see addrs, color, and
memory_type in *vxCreateImageFromHandle*).

All images created from ROI or channel with this image as parent or ancestor
will automatically use the memory referenced by the new handle.

The behavior of *vxSwapImageHandle* when called from a user node is undefined.
:param: [in] image The reference to an image created from handle
:param: [in] new_ptrs[] pointer to a caller owned array that contains
the new image handle (image plane pointers)
:arg: new_ptrs is non NULL. new_ptrs[i] must be non NULL for each i such as
0 < i < nbPlanes, otherwise, this is an error. The address of the storage memory
for image plane i is set to new_ptrs[i]
:arg: new_ptrs is NULL: the previous image storage memory is reclaimed by the
caller, while no new handle is provided.
:param: [out] prev_ptrs[] pointer to a caller owned array in which
the application returns the previous image handle
:arg: prev_ptrs is non NULL. prev_ptrs must have at least as many
elements as the number of image planes. For each i such as
0 < i < nbPlanes , prev_ptrs[i] is set to the address of the previous storage
memory for plane i.
:arg: prev_ptrs NULL: the previous handle is not returned.
:param: [in] num_planes Number of planes in the image. This must be set equal to the number of planes of the input image.
 The number of elements in new_ptrs and prev_ptrs arrays must be equal to or greater than num_planes.
If either array has more than num_planes elements, the extra elements are ignored. If either array is smaller
than num_planes, the results are undefined.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
reference.
:retval: VX_ERROR_INVALID_PARAMETERS The image was not created from handle or
the content of new_ptrs is not valid.
:retval: VX_FAILURE The image was already being accessed.
:ingroup: group_image
    '''
    return lib.vxSwapImageHandle(image, new_ptrs, prev_ptrs, num_planes)
    
def QueryImage(image, attribute, ptr, size):
    '''
:brief: Retrieves various attributes of an image.
:param: [in] image The reference to the image to query.
:param: [in] attribute The attribute to query. Use a *vx_image_attribute_e*.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute is not supported on this implementation.
:ingroup: group_image
    '''
    return lib.vxQueryImage(image, attribute, ptr, size)
    
def SetImageAttribute(image, attribute, ptr, size):
    '''
:brief: Allows setting attributes on the image.
:param: [in] image The reference to the image on which to set the attribute.
:param: [in] attribute The attribute to set. Use a *vx_image_attribute_e* enumeration.
:param: [in] ptr The pointer to the location from which to read the value.
:param: [in] size The size in bytes of the object pointed to by :a: ptr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:ingroup: group_image
    '''
    return lib.vxSetImageAttribute(image, attribute, ptr, size)
    
def SetImagePixelValues(image, pixel_value):
    '''
:brief: Initialize an image with the given pixel value.
:param: [in] image The reference to the image to initialize.
:param: [in] pixel_value The pointer to the constant pixel value to initialize all image pixels. See *vx_pixel_value_t*.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If the image is a uniform image, a virtual image, or not a *vx_image*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:note: All pixels of the entire image are initialized to the indicated pixel value, independently from the valid region.
The valid region of the image is unaffected by this function. The image remains mutable after the call to this function,
so its pixels and mutable attributes may be changed by subsequent functions.
:ingroup: group_image
    '''
    return lib.vxSetImagePixelValues(image, pixel_value)
    
def ReleaseImage(image):
    '''
:brief: Releases a reference to an image object.
The object may not be garbage collected until its total reference count is zero.

An implementation may defer the actual object destruction after its total
reference count is zero (potentially until context destruction). Thus,
releasing an image created from handle
(see *vxCreateImageFromHandle*) and all others objects that may
reference it (nodes, ROI, or channel for instance) are not sufficient to get back the
ownership of the memory referenced by the current image handle. The only way
for this is to call *vxSwapImageHandle*) before releasing the
image.

:param: [in] image The pointer to the image to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
:ingroup: group_image
    '''
    return lib.vxReleaseImage(image)
    
def FormatImagePatchAddress1d(ptr, index, addr):
    '''
:brief: Accesses a specific indexed pixel in an image patch.
:param: [in] ptr The base pointer of the patch as returned from *vxMapImagePatch*.
:param: [in] index The 0 based index of the pixel count in the patch. Indexes increase horizontally by 1 then wrap around to the next row.
:param: [in] addr The pointer to the addressing mode information returned from *vxMapImagePatch*.
:return: voidReturns the pointer to the specified pixel.
:pre: *vxMapImagePatch*
:note: Some special restrictions apply to *VX_DF_IMAGE_U1* images.
:ingroup: group_image
    '''
    return lib.vxFormatImagePatchAddress1d(ptr, index, addr)
    
def FormatImagePatchAddress2d(ptr, x, y, addr):
    '''
:brief: Accesses a specific pixel at a 2d coordinate in an image patch.
:param: [in] ptr The base pointer of the patch as returned from *vxMapImagePatch*.
:param: [in] x The x dimension within the patch.
:param: [in] y The y dimension within the patch.
:param: [in] addr The pointer to the addressing mode information returned from *vxMapImagePatch*.
:return: voidReturns the pointer to the specified pixel.
:pre: *vxMapImagePatch*
:note: Some special restrictions apply to *VX_DF_IMAGE_U1* images.
:ingroup: group_image
    '''
    return lib.vxFormatImagePatchAddress2d(ptr, x, y, addr)
    
def GetValidRegionImage(image, rect):
    '''
:brief: Retrieves the valid region of the image as a rectangle.
:param: [in] image The image from which to retrieve the valid region.
:param: [out] rect The destination rectangle.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
:retval: VX_ERROR_INVALID_PARAMETERS Invalid rect.
:note: This rectangle can be passed directly to *vxMapImagePatch* to get
the full valid region of the image.
:note: Some special restrictions apply to *VX_DF_IMAGE_U1* images.
:ingroup: group_image
    '''
    return lib.vxGetValidRegionImage(image, rect)
    
def CopyImagePatch(image, image_rect, image_plane_index, user_addr, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy a rectangular patch from/into an image object plane.
:param: [in] image The reference to the image object that is the source or the
destination of the copy.
:param: [in] image_rect The coordinates of the image patch. The patch must be within
the bounds of the image. (start_x, start_y) gives the coordinates of the topleft
pixel inside the patch, while (end_x, end_y) gives the coordinates of the bottomright
element out of the patch. Must be 0 <= start < end <= number of pixels in the image dimension.
:param: [in] image_plane_index The plane index of the image object that is the source or the
destination of the patch copy.
:param: [in] user_addr The address of a structure describing the layout of the
user memory location pointed by user_ptr. In the structure, only dim_x, dim_y,
stride_x and stride_y fields must be provided, other fields are ignored by the function.
The layout of the user memory must follow a row major order:
stride_x >= pixel size in bytes, and stride_y >= stride_xdim_x.
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the image
object if the copy was requested in write mode. The accessible memory must be large enough
to contain the specified patch with the specified layout:
accessible memory in bytes >= (end_y - start_y)stride_y.
:param: [in] usage This declares the effect of the copy with regard to the image object
using the *vx_accessor_e* enumeration. For uniform images, only VX_READ_ONLY
is supported. For other images, Only *VX_READ_ONLY* and *VX_WRITE_ONLY* are supported:
:arg: *VX_READ_ONLY* means that data is copied from the image object into the application memory
:arg: *VX_WRITE_ONLY* means that data is copied into the image object from the application memory
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual image that cannot be
accessed by the application.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:note: The application may ask for data outside the bounds of the valid region, but
such data has an undefined value.
:note: Some special restrictions apply to *VX_DF_IMAGE_U1* images.
:ingroup: group_image
    '''
    return lib.vxCopyImagePatch(image, image_rect, image_plane_index, user_addr, user_ptr, usage, user_mem_type)
    
def MapImagePatch(image, rect, plane_index, map_id, addr, ptr, usage, mem_type, flags):
    '''
:brief: Allows the application to get direct access to a rectangular patch of an image object plane.
:param: [in] image The reference to the image object that contains the patch to map.
:param: [in] rect The coordinates of image patch. The patch must be within the
bounds of the image. (start_x, start_y) gives the coordinate of the topleft
element inside the patch, while (end_x, end_y) give the coordinate of
the bottomright element out of the patch. Must be 0 <= start < end.
:param: [in] plane_index The plane index of the image object to be accessed.
:param: [out] map_id The address of a *vx_map_id* variable where the function
returns a map identifier.
:arg: (*map_id) must eventually be provided as the map_id parameter of a call to
*vxUnmapImagePatch*.
:param: [out] addr The address of a *vx_imagepatch_addressing_t* structure
describing the memory layout of the image patch to access. The function fills the
structure pointed by addr with the layout information that the application must
consult to access the pixel data at address (*ptr). The layout of the mapped memory
follows a row-major order: stride_x>0, stride_y>0 and stride_y >= stride_xdim_x.
An exception is for *VX_DF_IMAGE_U1* where :a: stride_x == 0,
_stride_x_bits_ > 0 and _stride_y_ {geq} (_stride_x_bits__dim_x_ + 7) / 8
(i.e., at least the number of bytes needed to hold _dim_x_ pixels).
If the image object being accessed was created via
*vxCreateImageFromHandle*, then the returned memory layout will be
the identical to that of the addressing structure provided when
*vxCreateImageFromHandle* was called.
:param: [out] ptr The address of a pointer that the function sets to the
address where the requested data can be accessed. This returned (*ptr) address
is only valid between the call to this function and the corresponding call to
*vxUnmapImagePatch*.
If image was created via *vxCreateImageFromHandle* then the returned
address (*ptr) will be the address of the patch in the original pixel buffer
provided when image was created.
:param: [in] usage This declares the access mode for the image patch, using
the *vx_accessor_e* enumeration. For uniform images, only VX_READ_ONLY
is supported.
:arg: *VX_READ_ONLY*: after the function call, the content of the memory location
pointed by (*ptr) contains the image patch data. Writing into this memory location
is forbidden and its behavior is undefined.
:arg: *VX_READ_AND_WRITE*: after the function call, the content of the memory
location pointed by (*ptr) contains the image patch data; writing into this memory
is allowed only for the location of pixels only and will result in a modification
of the written pixels in the image object once the patch is unmapped. Writing into
a gap between pixels (when addr->stride_x > pixel size in bytes or addr->stride_y > addr->stride_x*addr->dim_x)
is forbidden and its behavior is undefined.
:arg: *VX_WRITE_ONLY*: after the function call, the memory location pointed by (*ptr)
contains undefined data; writing each pixel of the patch is required prior to
unmapping. Pixels not written by the application before unmap will become
undefined after unmap, even if they were well defined before map. Like for
VX_READ_AND_WRITE, writing into a gap between pixels is forbidden and its behavior
is undefined.
:param: [in] mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory where the image patch is requested to be mapped.
:param: [in] flags An integer that allows passing options to the map operation.
Use the *vx_map_flag_e* enumeration.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual image that cannot be
accessed by the application.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:note: The user may ask for data outside the bounds of the valid region, but
such data has an undefined value.
:ingroup: group_image
:post: *vxUnmapImagePatch * with same (*map_id) value.
    '''
    return lib.vxMapImagePatch(image, rect, plane_index, map_id, addr, ptr, usage, mem_type, flags)
    
def UnmapImagePatch(image, map_id):
    '''
:brief: Unmap and commit potential changes to a image object patch that were previously mapped.
Unmapping an image patch invalidates the memory location from which the patch could
be accessed by the application. Accessing this memory location after the unmap function
completes has an undefined behavior.
:param: [in] image The reference to the image object to unmap.
:param: [out] map_id The unique map identifier that was returned by *vxMapImagePatch* .
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_image
:pre: *vxMapImagePatch* with same map_id value
    '''
    return lib.vxUnmapImagePatch(image, map_id)
    
def CreateImageFromChannel(img, channel):
    '''
:brief: Create a sub-image from a single plane channel of another image.

The sub-image refers to the data in the original image. Updates to this image
update the parent image and reversely.

The function supports only channels that occupy an entire plane of a multi-planar
images, as listed below. Other cases are not supported.
    VX_CHANNEL_Y from YUV4, IYUV, NV12, NV21
    VX_CHANNEL_U from YUV4, IYUV
    VX_CHANNEL_V from YUV4, IYUV

:param: [in] img          The reference to the parent image.
:param: [in] channel      The *vx_channel_e* channel to use.

:returns: An image reference *vx_image* to the sub-image. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_image
    '''
    return lib.vxCreateImageFromChannel(img, channel)
    
def SetImageValidRectangle(image, rect):
    '''
:brief: Sets the valid rectangle for an image according to a supplied rectangle.
:note: Setting or changing the valid region from within a user node by means other than the call-back, for
example by calling *vxSetImageValidRectangle*, might result in an incorrect valid region calculation
by the framework.
:param: [in] image  The reference to the image.
:param: [in] rect   The value to be set to the image valid rectangle. A NULL indicates that the valid region is the entire image.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE image is not a valid *vx_image* reference.
:retval: VX_ERROR_INVALID_PARAMETERS The rect does not define a proper valid rectangle.
:ingroup: group_image
    '''
    return lib.vxSetImageValidRectangle(image, rect)
    
def RegisterKernelLibrary(context, module, publish, unpublish):
    '''
:brief: Registers a module with kernels in a context.
:details: This function registers the appropriate publish and unpublish functions
with the module name if the module is not a dynamic library, so *vxLoadKernels* and
*vxUnloadKernels* can be called.
:param: [in] context The reference to the context the kernels must be added to.
:param: [in] module The short name of the module to load.
:param: [in] publish must add kernels to the context by calling *vxAddUserKernel*
for each new kernel. It is called by *vxLoadKernels*.
:param: [in] unpublish must remove kernels from the context by calling *vxRemoveKernel*
for each kernel the *vxPublishKernels* has added. It is called by *vxUnloadKernels*.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE context is not a valid *vx_context* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:ingroup: group_user_kernels
:see: vxLoadKernels

//
    '''
    return lib.vxRegisterKernelLibrary(context, module, publish, unpublish)
    
def LoadKernels(context, module):
    '''
:brief: Loads a library of kernels, called module, into a context.

The module must be registered by *vxRegisterKernelLibrary* if it is not
a dynamic library or the module must be a dynamic library with by convention, two exported functions
named *vxPublishKernels* and *vxUnpublishKernels*.

*vxPublishKernels* must have type *vx_publish_kernels_f*,
and must add kernels to the context by calling *vxAddUserKernel*
for each new kernel. *vxPublishKernels* is called by *vxLoadKernels*.

*vxUnpublishKernels* must have type *vx_unpublish_kernels_f*,
and must remove kernels from the context by calling *vxRemoveKernel*
for each kernel the *vxPublishKernels* has added.
*vxUnpublishKernels* is called by *vxUnloadKernels*.

:note: When all references to loaded kernels are released, the module
may be automatically unloaded.
:param: [in] context The reference to the context the kernels must be added to.
:param: [in] module The short name of the module to load. On systems where
there are specific naming conventions for modules, the name passed
should ignore such conventions. For example: :c: libxyz.so should be
passed as just :c: xyz and the implementation will <i>do the right thing</i> that
the platform requires.
:note: This API uses the system pre-defined paths for modules.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE context is not a valid *vx_context* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:ingroup: group_user_kernels
:pre: *vxRegisterKernelLibrary* if the module is not a dynamic library
:see: vxGetKernelByName
    '''
    return lib.vxLoadKernels(context, module)
    
def UnloadKernels(context, module):
    '''
:brief: Unloads all kernels from the OpenVX context that had been loaded from
the module using the vxLoadKernels function.

The kernel unloading is performed by calling the *vxUnpublishKernels*
exported function of the module.
:note: *vxUnpublishKernels* is defined in the description of
*vxLoadKernels*.

:param: [in] context The reference to the context the kernels must be removed from.
:param: [in] module The short name of the module to unload. On systems where
there are specific naming conventions for modules, the name passed
should ignore such conventions. For example: :c: libxyz.so should be
passed as just :c: xyz and the implementation will <i>do the right thing</i>
that the platform requires.
:note: This API uses the system pre-defined paths for modules.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE context is not a valid *vx_context* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are
 incorrect.
:ingroup: group_user_kernels
:see: vxLoadKernels
    '''
    return lib.vxUnloadKernels(context, module)
    
def GetKernelByName(context, name):
    '''
:brief: Obtains a reference to a kernel using a string to specify the name.
:details: User Kernels follow a "dotted" heirarchical syntax. For example:
"com.company.example.xyz". The following are strings specifying the kernel names:

org.khronos.openvx.color_convert

org.khronos.openvx.channel_extract

org.khronos.openvx.channel_combine

org.khronos.openvx.sobel_3x3

org.khronos.openvx.magnitude

org.khronos.openvx.phase

org.khronos.openvx.scale_image

org.khronos.openvx.table_lookup

org.khronos.openvx.histogram

org.khronos.openvx.equalize_histogram

org.khronos.openvx.absdiff

org.khronos.openvx.mean_stddev

org.khronos.openvx.threshold

org.khronos.openvx.integral_image

org.khronos.openvx.dilate_3x3

org.khronos.openvx.erode_3x3

org.khronos.openvx.median_3x3

org.khronos.openvx.box_3x3

org.khronos.openvx.gaussian_3x3

org.khronos.openvx.custom_convolution

org.khronos.openvx.gaussian_pyramid

org.khronos.openvx.minmaxloc

org.khronos.openvx.convertdepth

org.khronos.openvx.canny_edge_detector

org.khronos.openvx.and

org.khronos.openvx.or

org.khronos.openvx.xor

org.khronos.openvx.not

org.khronos.openvx.multiply

org.khronos.openvx.add

org.khronos.openvx.subtract

org.khronos.openvx.warp_affine

org.khronos.openvx.warp_perspective

org.khronos.openvx.harris_corners

org.khronos.openvx.fast_corners

org.khronos.openvx.optical_flow_pyr_lk

org.khronos.openvx.remap

org.khronos.openvx.halfscale_gaussian

org.khronos.openvx.laplacian_pyramid

org.khronos.openvx.laplacian_reconstruct

org.khronos.openvx.non_linear_filter

org.khronos.openvx.match_template

org.khronos.openvx.lbp

org.khronos.openvx.hough_lines_p

org.khronos.openvx.tensor_multiply

org.khronos.openvx.tensor_add

org.khronos.openvx.tensor_subtract

org.khronos.openvx.tensor_table_lookup

org.khronos.openvx.tensor_transpose

org.khronos.openvx.tensor_convert_depth

org.khronos.openvx.tensor_matrix_multiply

org.khronos.openvx.copy

org.khronos.openvx.non_max_suppression

org.khronos.openvx.scalar_operation

org.khronos.openvx.hog_features

org.khronos.openvx.hog_cells

org.khronos.openvx.bilateral_filter

org.khronos.openvx.select

org.khronos.openvx.min

org.khronos.openvx.max

org.khronos.openvx.weighted_average

:param: [in] context The reference to the implementation context.
:param: [in] name The string of the name of the kernel to get.
:return: A kernel reference. Any possible errors preventing a successful
completion of the function should be checked using *vxGetStatus*.
:ingroup: group_kernel
:pre: *vxLoadKernels* if the kernel is not provided by the
OpenVX implementation.
:note: User Kernels should follow a "dotted" hierarchical syntax. For example:
"com.company.example.xyz".
    '''
    return lib.vxGetKernelByName(context, name)
    
def GetKernelByEnum(context, kernel):
    '''
:brief: Obtains a reference to the kernel using the *vx_kernel_e* enumeration.
:details: Enum values above the standard set are assumed to apply to
loaded libraries.
:param: [in] context The reference to the implementation context.
:param: [in] kernel A value from *vx_kernel_e* or a vendor or client-defined value.
:return: A *vx_kernel* reference. Any possible errors preventing a successful completion
of the function should be checked using *vxGetStatus*.
:ingroup: group_kernel
:pre: *vxLoadKernels* if the kernel is not provided by the
OpenVX implementation.
    '''
    return lib.vxGetKernelByEnum(context, kernel)
    
def QueryKernel(kernel, attribute, ptr, size):
    '''
:brief: This allows the client to query the kernel to get information about
the number of parameters, enum values, etc.
:param: [in] kernel The kernel reference to query.
:param: [in] attribute The attribute to query. Use a *vx_kernel_attribute_e*.
:param: [out] ptr The pointer to the location at which to store the resulting value.
:param: [in] size The size of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE kernel is not a valid *vx_kernel* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:retval: VX_ERROR_NOT_SUPPORTED If the attribute value is not supported in this implementation.
:ingroup: group_kernel
    '''
    return lib.vxQueryKernel(kernel, attribute, ptr, size)
    
def ReleaseKernel(kernel):
    '''
:brief: Release the reference to the kernel.
The object may not be garbage collected until its total reference count is zero.
:param: [in] kernel The pointer to the kernel reference to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE kernel is not a valid *vx_kernel* reference.
:ingroup: group_kernel
    '''
    return lib.vxReleaseKernel(kernel)
    
def AddUserKernel(context, name, enumeration, func_ptr, numParams, validate, init, deinit):
    '''
:brief: Allows users to add custom kernels to a context at run-time.
:param: [in] context The reference to the context the kernel must be added to.
:param: [in] name The string to use to match the kernel.  The length of the string
shall be lower than VX_MAX_KERNEL_NAME bytes.
:param: [in] enumeration The enumerated value of the kernel to be used by clients.
:param: [in] func_ptr The process-local function pointer to be invoked.
:param: [in] numParams The number of parameters for this kernel.
:param: [in] validate The pointer to *vx_kernel_validate_f*, which validates
parameters to this kernel.
:param: [in] init The kernel initialization function.
:param: [in] deinit The kernel de-initialization function.
:return: A *vx_kernel* reference. Any possible errors
preventing a successful creation should be checked using *vxGetStatus*.
:ingroup: group_user_kernels
    '''
    return lib.vxAddUserKernel(context, name, enumeration, func_ptr, numParams, validate, init, deinit)
    
def FinalizeKernel(kernel):
    '''
:brief: This API is called after all parameters have been added to the
kernel and the kernel is :e: ready to be used. Notice that the reference to the kernel created
by vxAddUserKernel is still valid after the call to vxFinalizeKernel.
If an error occurs, the kernel is not available for usage by the clients of OpenVX. Typically
this is due to a mismatch between the number of parameters requested and given.
:param: [in] kernel The reference to the loaded kernel from *vxAddUserKernel*.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE kernel is not a valid *vx_kernel* reference.
:pre: *vxAddUserKernel* and *vxAddParameterToKernel*
:ingroup: group_user_kernels
    '''
    return lib.vxFinalizeKernel(kernel)
    
def AddParameterToKernel(kernel, index, dir, data_type, state):
    '''
:brief: Allows users to set the signatures of the custom kernel.
:param: [in] kernel The reference to the kernel added with *vxAddUserKernel*.
:param: [in] index The index of the parameter to add.
:param: [in] dir The direction of the parameter. This must be either *VX_INPUT* or
*VX_OUTPUT*.
:param: [in] data_type The type of parameter. This must be a value from *vx_type_e*.
:param: [in] state The state of the parameter (required or not). This must be a value from *vx_parameter_state_e*.
:return: A *vx_status_e* enumerated value.
:retval: VX_SUCCESS Parameter is successfully set on kernel; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE kernel is not a valid *vx_kernel* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If the parameter is not valid for any reason.
:pre: *vxAddUserKernel*
:ingroup: group_user_kernels
    '''
    return lib.vxAddParameterToKernel(kernel, index, dir, data_type, state)
    
def RemoveKernel(kernel):
    '''
:brief: Removes a custom kernel from its context and releases it.
:param: [in] kernel The reference to the kernel to remove. Returned from *vxAddUserKernel*.
:note: Any kernel enumerated in the base standard
cannot be removed; only kernels added through *vxAddUserKernel* can
be removed.
:return: A *vx_status_e* enumeration. The function returns to the
application full control over the memory resources provided at the kernel creation time.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE kernel is not a valid *vx_kernel* reference.
:retval: VX_ERROR_INVALID_PARAMETERS If a base kernel is passed in.
:retval: VX_FAILURE If the application has not released all references to the kernel
object OR if the application has not released all references to a node that is using
this kernel OR if the application has not released all references to a graph which
has nodes that is using this kernel.
:ingroup: group_user_kernels
    '''
    return lib.vxRemoveKernel(kernel)
    
def SetKernelAttribute(kernel, attribute, ptr, size):
    '''
:brief: Sets kernel attributes.
:param: [in] kernel The reference to the kernel.
:param: [in] attribute The enumeration of the attributes. See *vx_kernel_attribute_e*.
:param: [in] ptr The pointer to the location from which to read the attribute.
:param: [in] size The size in bytes of the data area indicated by :a: ptr in bytes.
:note: After a kernel has been passed to *vxFinalizeKernel*, no attributes
can be altered.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE kernel is not a valid *vx_kernel* reference.
:ingroup: group_user_kernels
    '''
    return lib.vxSetKernelAttribute(kernel, attribute, ptr, size)
    
def GetKernelParameterByIndex(kernel, index):
    '''
:brief: Retrieves a *vx_parameter* from a *vx_kernel*.
:param: [in] kernel The reference to the kernel.
:param: [in] index The index of the parameter.
:return: A *vx_parameter* reference. Any possible errors preventing a
successful completion of the function should be checked using *vxGetStatus*.
:ingroup: group_parameter
    '''
    return lib.vxGetKernelParameterByIndex(kernel, index)
    
def CreateGraph(context):
    '''
:brief: Creates an empty graph.
:param: [in] context The reference to the implementation context.
:returns: A graph reference *vx_graph*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_graph
    '''
    return lib.vxCreateGraph(context)
    
def ReleaseGraph(graph):
    '''
:brief: Releases a reference to a graph.
The object may not be garbage collected until its total reference count is zero.
Once the reference count is zero, all node references in the graph are automatically
released as well. Releasing the graph will only release the nodes if the nodes were
not previously released by the application. Data referenced by those nodes may not
be released as the user may still have references to the data.
:param: [in] graph The pointer to the graph to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference.
:ingroup: group_graph
    '''
    return lib.vxReleaseGraph(graph)
    
def VerifyGraph(graph):
    '''
:brief: Verifies the state of the graph before it is executed.
This is useful to catch programmer errors and contract errors. If not verified,
the graph verifies before being processed.
:pre: Memory for data objects is not guarenteed to exist before
this call. :post: After this call data objects exist unless
the implementation optimized them out.
:param: [in] graph The reference to the graph to verify.
:return: A status code for graphs with more than one error; it is
undefined which error will be returned. Register a log callback using *vxRegisterLogCallback*
to receive each specific error in the graph.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference.
:retval: VX_ERROR_MULTIPLE_WRITERS If the graph contains more than one writer
to any data object.
:retval: VX_ERROR_INVALID_NODE If a node in the graph is invalid or failed be created.
:retval: VX_ERROR_INVALID_GRAPH If the graph contains cycles or some other invalid topology.
:retval: VX_ERROR_INVALID_TYPE If any parameter on a node is given the wrong type.
:retval: VX_ERROR_INVALID_VALUE If any value of any parameter is out of bounds of specification.
:retval: VX_ERROR_INVALID_FORMAT If the image format is not compatible.
:ingroup: group_graph
:see: vxProcessGraph
    '''
    return lib.vxVerifyGraph(graph)
    
def ProcessGraph(graph):
    '''
:brief: This function causes the synchronous processing of a graph. If the graph
has not been verified, then the implementation verifies the graph
immediately. If verification fails this function returns a status
identical to what *vxVerifyGraph* would return. After
the graph verfies successfully then processing occurs. If the graph was
previously verified via *vxVerifyGraph* or *vxProcessGraph*
then the graph is processed. This function blocks until the graph is completed.
:param: [in] graph The graph to execute.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Graph has been processed; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference.
:retval: VX_FAILURE A catastrophic error occurred during processing.
:ingroup: group_graph
    '''
    return lib.vxProcessGraph(graph)
    
def ScheduleGraph(graph):
    '''
:brief: Schedules a graph for future execution. If the graph
has not been verified, then the implementation verifies the graph
immediately. If verification fails this function returns a status
identical to what *vxVerifyGraph* would return. After
the graph verfies successfully then processing occurs. If the graph was
previously verified via *vxVerifyGraph* or *vxProcessGraph*
then the graph is processed.
:param: [in] graph The graph to schedule.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The graph has been scheduled; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference.
:retval: VX_ERROR_NO_RESOURCES The graph cannot be scheduled now.
:retval: VX_ERROR_NOT_SUFFICIENT The graph is not verified and has failed
forced verification.
:ingroup: group_graph
    '''
    return lib.vxScheduleGraph(graph)
    
def WaitGraph(graph):
    '''
:brief: Waits for a specific graph to complete. If the graph has been scheduled multiple
times since the last call to vxWaitGraph, then vxWaitGraph returns only when the last
scheduled execution completes.
:param: [in] graph The graph to wait on.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The graph has successfully completed execution and its outputs are the
valid results of the most recent execution; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference.
:retval: VX_FAILURE An error occurred or the graph was never scheduled. Output data of the
graph is undefined.
:pre: *vxScheduleGraph*
:ingroup: group_graph
    '''
    return lib.vxWaitGraph(graph)
    
def QueryGraph(graph, attribute, ptr, size):
    '''
:brief: Allows the user to query attributes of the Graph.
:param: [in] graph The reference to the created graph.
:param: [in] attribute The *vx_graph_attribute_e* type needed.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference.
:ingroup: group_graph
    '''
    return lib.vxQueryGraph(graph, attribute, ptr, size)
    
def SetGraphAttribute(graph, attribute, ptr, size):
    '''
:brief: Allows the attributes of the Graph to be set to the provided value.
:param: [in] graph The reference to the graph.
:param: [in] attribute The *vx_graph_attribute_e* type needed.
:param: [in] ptr The location from which to read the value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference.
:ingroup: group_graph
    '''
    return lib.vxSetGraphAttribute(graph, attribute, ptr, size)
    
def AddParameterToGraph(graph, parameter):
    '''
:brief: Adds the given parameter extracted from a *vx_node* to the graph.
:param: [in] graph The graph reference that contains the node.
:param: [in] parameter The parameter reference to add to the graph from the node.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Parameter added to Graph; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference or parameter is not a valid *vx_parameter* reference.
:retval: VX_ERROR_INVALID_PARAMETERS The parameter is of a node not in this
graph.
:ingroup: group_graph_parameters
    '''
    return lib.vxAddParameterToGraph(graph, parameter)
    
def SetGraphParameterByIndex(graph, index, value):
    '''
:brief: Sets a reference to the parameter on the graph. The implementation
must set this parameter on the originating node as well.
:param: [in] graph The graph reference.
:param: [in] index The parameter index.
:param: [in] value The reference to set to the parameter.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Parameter set to Graph; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference or
value is not a valid *vx_reference*.
:retval: VX_ERROR_INVALID_PARAMETERS The parameter index is out of bounds or the
dir parameter is incorrect.
:ingroup: group_graph_parameters
    '''
    return lib.vxSetGraphParameterByIndex(graph, index, value)
    
def GetGraphParameterByIndex(graph, index):
    '''
:brief: Retrieves a *vx_parameter* from a *vx_graph*.
:param: [in] graph The graph.
:param: [in] index The index of the parameter.
:return: *vx_parameter* reference. Any possible errors preventing a successful
function completion should be checked using *vxGetStatus*.
:ingroup: group_graph_parameters
    '''
    return lib.vxGetGraphParameterByIndex(graph, index)
    
def IsGraphVerified(graph):
    '''
:brief: Returns a Boolean to indicate the state of graph verification.
:param: [in] graph The reference to the graph to check.
:return: A *vx_bool* value.
:retval: vx_true_e The graph is verified.
:retval: vx_false_e The graph is not verified. It must be verified before
execution either through *vxVerifyGraph* or automatically through
*vxProcessGraph* or *vxScheduleGraph*.
:ingroup: group_graph
    '''
    return lib.vxIsGraphVerified(graph)
    
def CreateGenericNode(graph, kernel):
    '''
:brief: Creates a reference to a node object for a given kernel.
:details: This node has no references assigned as parameters after completion.
The client is then required to set these parameters manually by *vxSetParameterByIndex*.
When clients supply their own node creation functions (for use with User Kernels), this is the API
to use along with the parameter setting API.
:param: [in] graph The reference to the graph in which this node exists.
:param: [in] kernel The kernel reference to associate with this new node.
:returns: A node reference *vx_node*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:note: A call to this API sets all parameters to NULL.
:ingroup: group_adv_node
:post: Call *vxSetParameterByIndex* for as many parameters as needed to be set.
    '''
    return lib.vxCreateGenericNode(graph, kernel)
    
def QueryNode(node, attribute, ptr, size):
    '''
:brief: Allows a user to query information out of a node.
:param: [in] node The reference to the node to query.
:param: [in] attribute Use *vx_node_attribute_e* value to query for information.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytesin bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE node is not a valid *vx_node* reference.
:retval: VX_ERROR_INVALID_PARAMETERS The type or size is incorrect.
:ingroup: group_node
    '''
    return lib.vxQueryNode(node, attribute, ptr, size)
    
def SetNodeAttribute(node, attribute, ptr, size):
    '''
:brief: Allows a user to set attribute of a node before Graph Validation.
:param: [in] node The reference to the node to set.
:param: [in] attribute Use *vx_node_attribute_e* value to set the desired attribute.
:param: [in] ptr The pointer to the desired value of the attribute.
:param: [in] size The size in bytes of the objects to which :a: ptr points.
:note: Some attributes are inherited from the *vx_kernel*, which was used
to create the node. Some of these can be overridden using this API, notably
VX_NODE_LOCAL_DATA_SIZE and VX_NODE_LOCAL_DATA_PTR.
:ingroup: group_node
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The attribute was set; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE node is not a valid *vx_node* reference.
:retval: VX_ERROR_INVALID_PARAMETERS size is not correct for the type needed.
    '''
    return lib.vxSetNodeAttribute(node, attribute, ptr, size)
    
def ReleaseNode(node):
    '''
:brief: Releases a reference to a Node object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] node The pointer to the reference of the node to release.
:ingroup: group_node
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE node is not a valid *vx_node* reference.
    '''
    return lib.vxReleaseNode(node)
    
def RemoveNode(node):
    '''
:brief: Removes a Node from its parent Graph and releases it.
:param: [in] node The pointer to the node to remove and release.
:ingroup: group_node
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE node is not a valid *vx_node* reference.
    '''
    return lib.vxRemoveNode(node)
    
def AssignNodeCallback(node, callback):
    '''
:brief: Assigns a callback to a node.
If a callback already exists in this node, this function must return an error
and the user may clear the callback by passing a NULL pointer as the callback.
:param: [in] node The reference to the node.
:param: [in] callback The callback to associate with completion of this
specific node.
:warning: This must be used with <b><i>extreme</i></b> caution as it can :e: ruin
optimizations in the power/performance efficiency of a graph.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Callback assigned; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE node is not a valid *vx_node* reference.
:ingroup: group_node_callback
    '''
    return lib.vxAssignNodeCallback(node, callback)
    
def RetrieveNodeCallback(node):
    '''
:brief: Retrieves the current node callback function pointer set on the node.
:param: [in] node The reference to the *vx_node* object.
:ingroup: group_node_callback
:return: vx_nodecomplete_f The pointer to the callback function.
:retval: NULL No callback is set.
:retval:The node callback function.
    '''
    return lib.vxRetrieveNodeCallback(node)
    
def SetNodeTarget(node, target_enum, target_string):
    '''
:brief: Sets the node target to the provided value. A success invalidates the graph
that the node belongs to (*vxVerifyGraph* must be called before the next execution)
:param: [in] node  The reference to the *vx_node* object.
:param: [in] target_enum  The target enum to be set to the *vx_node* object.
Use a *vx_target_e*.
:param: [in] target_string  The target name ASCII string. This contains a valid value
when target_enum is set to *VX_TARGET_STRING*, otherwise it is ignored.
:ingroup: group_node
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Node target set; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE node is not a valid *vx_node* reference.
:retval: VX_ERROR_NOT_SUPPORTED If the node kernel is not supported by the specified target.
    '''
    return lib.vxSetNodeTarget(node, target_enum, target_string)
    
def ReplicateNode(graph, first_node, replicate, number_of_parameters):
    '''
:brief: Creates replicas of the same node first_node to process a set of objects
stored in *vx_pyramid* or *vx_object_array*.
first_node needs to have as parameter levels 0 of a *vx_pyramid* or the index 0 of a *vx_object_array*.
Replica nodes are not accessible by the application through any means. An application request for removal of
first_node from the graph will result in removal of all replicas. Any change of parameter or attribute of
first_node will be propagated to the replicas. *vxVerifyGraph* shall enforce consistency of parameters and attributes
in the replicas.
:param: [in] graph The reference to the graph.
:param: [in] first_node The reference to the node in the graph that will be replicated.
:param: [in] replicate an array of size equal to the number of node parameters, vx_true_e for the parameters
that should be iterated over (should be a reference to a vx_pyramid or a vx_object_array),
vx_false_e for the parameters that should be the same across replicated nodes and for optional
parameters that are not used. Should be vx_true_e for all output parameters.
:param: [in] number_of_parameters number of elements in the replicate array
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference, or first_node is not a
valid *vx_node* reference.
:retval: VX_ERROR_NOT_COMPATIBLE At least one of replicated parameters is not of level 0 of a pyramid or at index 0 of an object array.
:retval: VX_FAILURE If the node does not belong to the graph, or the number of objects in the parent objects of inputs and output are not the same.
:ingroup: group_node
    '''
    return lib.vxReplicateNode(graph, first_node, replicate, number_of_parameters)
    
def GetParameterByIndex(node, index):
    '''
:brief: Retrieves a *vx_parameter* from a *vx_node*.
:param: [in] node The node from which to extract the parameter.
:param: [in] index The index of the parameter to which to get a reference.
:return: A parameter reference *vx_parameter*. Any possible errors preventing a successful
completion of the function should be checked using *vxGetStatus*.
:ingroup: group_parameter
    '''
    return lib.vxGetParameterByIndex(node, index)
    
def ReleaseParameter(param):
    '''
:brief: Releases a reference to a parameter object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] param The pointer to the parameter to release.
:ingroup: group_parameter
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE param is not a valid *vx_parameter* reference.
    '''
    return lib.vxReleaseParameter(param)
    
def SetParameterByIndex(node, index, value):
    '''
:brief: Sets the specified parameter data for a kernel on the node.
:param: [in] node The node that contains the kernel.
:param: [in] index The index of the parameter desired.
:param: [in] value The desired value of the parameter.
:note: A user may not provide a NULL value for a mandatory parameter of this API.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE node is not a valid *vx_node* reference, or value
is not a valid *vx_reference* reference.
:ingroup: group_parameter
:see: vxSetParameterByReference
    '''
    return lib.vxSetParameterByIndex(node, index, value)
    
def SetParameterByReference(parameter, value):
    '''
:brief: Associates a parameter reference and a data reference with a kernel
on a node.
:param: [in] parameter The reference to the kernel parameter.
:param: [in] value The value to associate with the kernel parameter.
:note: A user may not provide a NULL value for a mandatory parameter of this API.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE parameter is not a valid *vx_parameter* reference,
or value is not a valid *vx_reference* reference..
:ingroup: group_parameter
:see: vxGetParameterByIndex
    '''
    return lib.vxSetParameterByReference(parameter, value)
    
def QueryParameter(parameter, attribute, ptr, size):
    '''
:brief: Allows the client to query a parameter to determine its meta-information.
:param: [in] parameter The reference to the parameter.
:param: [in] attribute The attribute to query. Use a *vx_parameter_attribute_e*.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE parameter is not a valid *vx_parameter* reference.
:ingroup: group_parameter
    '''
    return lib.vxQueryParameter(parameter, attribute, ptr, size)
    
def CreateScalar(context, data_type, ptr):
    '''
:brief: Creates a reference to a scalar object. Also see sub_node_parameters.
:param: [in] context The reference to the system context.
:param: [in] data_type The type of data to hold. Must be greater than
*VX_TYPE_INVALID* and less than or equal to *VX_TYPE_VENDOR_STRUCT_END*.
Or must be a *vx_enum* returned from *vxRegisterUserStruct*.
:param: [in] ptr The pointer to the initial value of the scalar or NULL. If NULL,
            the initial value of the scalar, if any, is implementation dependent.
:ingroup: group_scalar
:returns: A scalar reference *vx_scalar*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxCreateScalar(context, data_type, ptr)
    
def CreateScalarWithSize(context, data_type, ptr, size):
    '''
:brief: Creates a reference to a scalar object. Also see sub_node_parameters.
:param: [in] context The reference to the system context.
:param: [in] data_type The type of data to hold. Must be greater than
*VX_TYPE_INVALID* and less than or equal to *VX_TYPE_VENDOR_STRUCT_END*.
Or must be a *vx_enum* returned from *vxRegisterUserStruct*.
:param: [in] ptr The pointer to the initial value of the scalar.
:param: [in] size Size of data at ptr in bytes.
:ingroup: group_scalar
:returns: A scalar reference *vx_scalar*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxCreateScalarWithSize(context, data_type, ptr, size)
    
def CreateVirtualScalar(graph, data_type):
    '''
:brief: Creates an opaque reference to a scalar object with no direct user access.
:param: [in] graph The reference to the parent graph.
:param: [in] data_type The type of data to hold. Must be greater than
*VX_TYPE_INVALID* and less than or equal to *VX_TYPE_VENDOR_STRUCT_END*.
Or must be a *vx_enum* returned from *vxRegisterUserStruct*.
:see: *vxCreateScalar*
:ingroup: group_scalar
:returns: A scalar reference *vx_scalar*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxCreateVirtualScalar(graph, data_type)
    
def ReleaseScalar(scalar):
    '''
:brief: Releases a reference to a scalar object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] scalar The pointer to the scalar to release.
:ingroup: group_scalar
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE scalar is not a valid *vx_scalar* reference.
    '''
    return lib.vxReleaseScalar(scalar)
    
def QueryScalar(scalar, attribute, ptr, size):
    '''
:brief: Queries attributes from a scalar.
:param: [in] scalar The scalar object.
:param: [in] attribute The enumeration to query. Use a *vx_scalar_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE scalar is not a valid *vx_scalar* reference.
:ingroup: group_scalar
    '''
    return lib.vxQueryScalar(scalar, attribute, ptr, size)
    
def CopyScalar(scalar, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy from/into a scalar object.
:param: [in] scalar The reference to the scalar object that is the source or the
destination of the copy.
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the
scalar object if the copy was requested in write mode. In the user memory, the scalar is
a variable of the type corresponding to *VX_SCALAR_TYPE*.
The accessible memory must be large enough to contain this variable.
:param: [in] usage This declares the effect of the copy with regard to the scalar object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY*
are supported:
:arg: *VX_READ_ONLY* means that data are copied from the scalar object into the user memory.
:arg: *VX_WRITE_ONLY* means that data are copied into the scalar object from the user memory.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE scalar is not a valid *vx_scalar* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_scalar
    '''
    return lib.vxCopyScalar(scalar, user_ptr, usage, user_mem_type)
    
def CopyScalarWithSize(scalar, size, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy from/into a scalar object with size.
:param: [in] scalar The reference to the scalar object that is the source or the
destination of the copy.
:param: [in] size The size in bytes of the container to which :a: user_ptr points.
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the
scalar object if the copy was requested in write mode. In the user memory, the scalar is
a variable of the type corresponding to *VX_SCALAR_TYPE*.
The accessible memory must be large enough to contain this variable.
:param: [in] usage This declares the effect of the copy with regard to the scalar object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY*
are supported:
:arg: *VX_READ_ONLY* means that data are copied from the scalar object into the user memory.
:arg: *VX_WRITE_ONLY* means that data are copied into the scalar object from the user memory.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The scalar reference is not actually a scalar reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_scalar
    '''
    return lib.vxCopyScalarWithSize(scalar, size, user_ptr, usage, user_mem_type)
    
def QueryReference(ref, attribute, ptr, size):
    '''
:brief: Queries any reference type for some basic information like count or type.
:param: [in] ref The reference to query.
:param: [in] attribute The value for which to query. Use *vx_reference_attribute_e*.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE ref is not a valid *vx_reference* reference.
:ingroup: group_reference
    '''
    return lib.vxQueryReference(ref, attribute, ptr, size)
    
def ReleaseReference(ref_ptr):
    '''
:brief: Releases a reference. The reference may potentially refer to multiple OpenVX objects of different types.
This function can be used instead of calling a specific release function for each individual object type
(e.g. vxRelease<object>). The object will not be destroyed until its total reference count is zero.
:note: After returning from this function the reference is zeroed.
:param: [in] ref_ptr The pointer to the reference of the object to release.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE ref_ptr is not a valid *vx_reference* reference.
:ingroup: group_reference
    '''
    return lib.vxReleaseReference(ref_ptr)
    
def RetainReference(ref):
    '''
:brief: Increments the reference counter of an object
This function is used to express the fact that the OpenVX object is referenced
multiple times by an application. Each time this function is called for
an object, the application will need to release the object one additional
time before it can be destructed
:param: [in] ref The reference to retain.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE ref is not a valid *vx_reference* reference.
:ingroup: group_reference
    '''
    return lib.vxRetainReference(ref)
    
def SetReferenceName(ref, name):
    '''
:brief: Name a reference
:ingroup: group_reference

This function is used to associate a name to a referenced object. This name
can be used by the OpenVX implementation in log messages and any
other reporting mechanisms.

The OpenVX implementation will not check if the name is unique in
the reference scope (context or graph). Several references can then
have the same name.

:param: [in] ref The reference to the object to be named.
:param: [in] name Pointer to the '\0' terminated string that identifies
            the referenced object.
            The string is copied by the function so that it
            stays the property of the caller.
            NULL means that the reference is not named.
            The length of the string shall be lower than VX_MAX_REFERENCE_NAME bytes.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE ref is not a valid *vx_reference* reference.
    '''
    return lib.vxSetReferenceName(ref, name)
    
def QueryDelay(delay, attribute, ptr, size):
    '''
:brief: Queries a *vx_delay* object attribute.
:param: [in] delay The reference to a delay object.
:param: [in] attribute The attribute to query. Use a *vx_delay_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE delay is not a valid *vx_delay* reference.
:ingroup: group_delay
    '''
    return lib.vxQueryDelay(delay, attribute, ptr, size)
    
def ReleaseDelay(delay):
    '''
:brief: Releases a reference to a delay object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] delay The pointer to the delay object reference to release.
:post: After returning from this function the reference is zeroed.
:ingroup: group_delay
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE delay is not a valid *vx_delay* reference.
    '''
    return lib.vxReleaseDelay(delay)
    
def CreateDelay(context, exemplar, num_slots):
    '''
:brief: Creates a Delay object.
:details: This function creates a delay object with :p: num_slots slots. Each slot
contains a clone of the exemplar. The clones only inherit the metadata of the
exemplar. The data content of the exemplar is ignored and the clones have their
data undefined at delay creation time.
The function does not alter the exemplar. Also, it doesn't retain or release the
reference to the exemplar.
:note: For the definition of metadata attributes see vxSetMetaFormatAttribute.
:param: [in] context The reference to the context.
:param: [in] exemplar The exemplar object. Supported exemplar object types are:<br>
:arg: VX_TYPE_ARRAY
:arg: VX_TYPE_CONVOLUTION
:arg: VX_TYPE_DISTRIBUTION
:arg: VX_TYPE_IMAGE
:arg: VX_TYPE_LUT
:arg: VX_TYPE_MATRIX
:arg: VX_TYPE_OBJECT_ARRAY
:arg: VX_TYPE_PYRAMID
:arg: VX_TYPE_REMAP
:arg: VX_TYPE_SCALAR
:arg: VX_TYPE_THRESHOLD
:arg: VX_TYPE_TENSOR
:param: [in] num_slots The number of objects in the delay. This value must be greater than zero.
:returns: A delay reference *vx_delay*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_delay
    '''
    return lib.vxCreateDelay(context, exemplar, num_slots)
    
def GetReferenceFromDelay(delay, index):
    '''
:brief: Retrieves a reference to a delay slot object.
:param: [in] delay The reference to the delay object.
:param: [in] index The index of the delay slot from which to extract the object reference.
:return: *vx_reference*. Any possible errors preventing a successful
completion of the function should be checked using *vxGetStatus*.
:note: The delay index is in the range :f:$ [-count+1,0] :f:$. 0 is always the
:e: current object.
:ingroup: group_delay
:note: A reference retrieved with this function must not be given to its associated
release API (e.g. *vxReleaseImage*) unless *vxRetainReference* is used.
    '''
    return lib.vxGetReferenceFromDelay(delay, index)
    
def AgeDelay(delay):
    '''
:brief: Shifts the internal delay ring by one.

This function performs a shift of the internal delay ring by one. This means that,
the data originally at index 0 move to index -1 and so forth until index
:f:$ -count+1 :f:$. The data originally at index :f:$ -count+1 :f:$ move to index 0.
Here :f:$ count :f:$ is the number of slots in delay ring.
When a delay is aged, any graph making use of this delay (delay object itself or data
objects in delay slots) gets its data automatically updated accordingly.
:param: [in] delay
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Delay was aged; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE delay is not a valid *vx_delay* reference.
:ingroup: group_delay
    '''
    return lib.vxAgeDelay(delay)
    
def RegisterAutoAging(graph, delay):
    '''
:brief: Register a delay for auto-aging.

This function registers a delay object to be auto-aged by the graph.
This delay object will be automatically aged after each successful completion of
this graph. Aging of a delay object cannot be called during graph execution.
A graph abandoned due to a node callback will trigger an auto-aging.

If a delay is registered for auto-aging multiple times in a same graph,
the delay will be only aged a single time at each graph completion.
If a delay is registered for auto-aging in multiple graphs, this delay will
aged automatically after each successful completion of any of these graphs.

:param: [in] graph The graph to which the delay is registered for auto-aging.
:param: [in] delay The delay to automatically age.

:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE graph is not a valid *vx_graph* reference, or
delay is not a valid *vx_delay* reference.
:ingroup: group_graph
    '''
    return lib.vxRegisterAutoAging(graph, delay)
    
def AddLogEntry(ref, status, message):
    '''
:brief: Adds a line to the log.
:param: [in] ref The reference to add the log entry against. Some valid value must be provided.
:param: [in] status The status code. *VX_SUCCESS* status entries are ignored and not added.
:param: [in] message The human readable message to add to the log.
:param: [in] ... a list of variable arguments to the message.
:note: Messages may not exceed *VX_MAX_LOG_MESSAGE_LEN* bytes and will be truncated in the log if they exceed this limit.
:ingroup: group_log
    '''
    return lib.vxAddLogEntry(ref, status, message)
    
def RegisterLogCallback(context, callback, reentrant):
    '''
:brief: Registers a callback facility to the OpenVX implementation to receive error logs.
:param: [in] context The overall context to OpenVX.
:param: [in] callback The callback function. If NULL, the previous callback is removed.
:param: [in] reentrant If reentrancy flag is *vx_true_e*, then the callback may be entered from multiple
simultaneous tasks or threads (if the host OS supports this).
:ingroup: group_log
    '''
    return lib.vxRegisterLogCallback(context, callback, reentrant)
    
def CreateLUT(context, data_type, count):
    '''
:brief: Creates LUT object of a given type. The value of *VX_LUT_OFFSET* is equal to 0
for data_type = *VX_TYPE_UINT8*, and (vx_uint32)(count/2) for *VX_TYPE_INT16*.
:param: [in] context The reference to the context.
:param: [in] data_type The type of data stored in the LUT.
:param: [in] count The number of entries desired.
:note: data_type can only be VX_TYPE_UINT8 or VX_TYPE_INT16. If data_type
is VX_TYPE_UINT8, count should be not greater than 256. If data_type is VX_TYPE_INT16,
count should not be greater than 65536.
:returns: An LUT reference *vx_lut*. Any possible errors preventing a successful creation should be checked using *vxGetStatus*.
:ingroup: group_lut
    '''
    return lib.vxCreateLUT(context, data_type, count)
    
def CreateVirtualLUT(graph, data_type, count):
    '''
:brief: Creates an opaque reference to a LUT object with no direct user access.
:param: [in] graph The reference to the parent graph.
:param: [in] data_type The type of data stored in the LUT.
:param: [in] count The number of entries desired.
:see: *vxCreateLUT*
:note: data_type can only be VX_TYPE_UINT8 or VX_TYPE_INT16. If data_type
is VX_TYPE_UINT8, count should be not greater than 256. If data_type is VX_TYPE_INT16,
count should not be greater than 65536.
:returns: An LUT reference *vx_lut*. Any possible errors preventing a successful creation should be checked using *vxGetStatus*.
:ingroup: group_lut
    '''
    return lib.vxCreateVirtualLUT(graph, data_type, count)
    
def ReleaseLUT(lut):
    '''
:brief: Releases a reference to a LUT object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] lut The pointer to the LUT to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE lut is not a valid *vx_lut* reference.
:ingroup: group_lut
    '''
    return lib.vxReleaseLUT(lut)
    
def QueryLUT(lut, attribute, ptr, size):
    '''
:brief: Queries attributes from a LUT.
:param: [in] lut The LUT to query.
:param: [in] attribute The attribute to query. Use a *vx_lut_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE lut is not a valid *vx_lut* reference.
:ingroup: group_lut
    '''
    return lib.vxQueryLUT(lut, attribute, ptr, size)
    
def CopyLUT(lut, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy from/into a LUT object.
:param: [in] lut The reference to the LUT object that is the source or the
destination of the copy.
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the LUT
object if the copy was requested in write mode. In the user memory, the LUT is
represented as a array with elements of the type corresponding to
*VX_LUT_TYPE*, and with a number of elements equal to the value
returned via *VX_LUT_COUNT*. The accessible memory must be large enough
to contain this array:
accessible memory in bytes >= sizeof(data_element)count.
:param: [in] usage This declares the effect of the copy with regard to the LUT object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY*
are supported:
:arg: *VX_READ_ONLY* means that data are copied from the LUT object into the user memory.
:arg: *VX_WRITE_ONLY* means that data are copied into the LUT object from the user memory.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE lut is not a valid *vx_lut* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_lut
    '''
    return lib.vxCopyLUT(lut, user_ptr, usage, user_mem_type)
    
def MapLUT(lut, map_id, ptr, usage, mem_type, flags):
    '''
:brief: Allows the application to get direct access to LUT object.
:param: [in] lut The reference to the LUT object to map.
:param: [out] map_id The address of a *vx_map_id* variable where the function
returns a map identifier.
:arg: (*map_id) must eventually be provided as the map_id parameter of a call to
*vxUnmapLUT*.
:param: [out] ptr The address of a pointer that the function sets to the
address where the requested data can be accessed. In the mapped memory area,
the LUT data are structured as an array with elements of the type corresponding
to *VX_LUT_TYPE*, with a number of elements equal to
the value returned via *VX_LUT_COUNT*. Accessing the
memory out of the bound of this array is forbidden and has an undefined behavior.
The returned (*ptr) address is only valid between the call to the function and
the corresponding call to *vxUnmapLUT*.
:param: [in] usage This declares the access mode for the LUT, using
the *vx_accessor_e* enumeration.
:arg: *VX_READ_ONLY*: after the function call, the content of the memory location
pointed by (*ptr) contains the LUT data. Writing into this memory location
is forbidden and its behavior is undefined.
:arg: *VX_READ_AND_WRITE*: after the function call, the content of the memory
location pointed by (*ptr) contains the LUT data; writing into this memory
is allowed only for the location of entries and will result in a modification
of the affected entries in the LUT object once the LUT is unmapped.
:arg: *VX_WRITE_ONLY*: after the function call, the memory location pointed by(*ptr)
contains undefined data; writing each entry of LUT is required prior to
unmapping. Entries not written by the application before unmap will become
undefined after unmap, even if they were well defined before map.
:param: [in] mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory where the LUT is requested to be mapped.
:param: [in] flags An integer that allows passing options to the map operation.
Use 0 for this option.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE lut is not a valid *vx_lut* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_lut
:post: *vxUnmapLUT * with same (*map_id) value.
    '''
    return lib.vxMapLUT(lut, map_id, ptr, usage, mem_type, flags)
    
def UnmapLUT(lut, map_id):
    '''
:brief: Unmap and commit potential changes to LUT object that was previously mapped.
Unmapping a LUT invalidates the memory location from which the LUT data could
be accessed by the application. Accessing this memory location after the unmap function
completes has an undefined behavior.
:param: [in] lut The reference to the LUT object to unmap.
:param: [out] map_id The unique map identifier that was returned when calling
*vxMapLUT* .
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE lut is not a valid *vx_lut* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_lut
:pre: *vxMapLUT* returning the same map_id value
    '''
    return lib.vxUnmapLUT(lut, map_id)
    
def CreateDistribution(context, numBins, offset, range):
    '''
:brief: Creates a reference to a 1D Distribution of a consecutive interval [offset, offset + range - 1]
defined by a start offset and valid range, divided equally into numBins parts.
:param: [in] context The reference to the overall context.
:param: [in] numBins The number of bins in the distribution.
:param: [in] offset The start offset into the range value that marks the begining of the 1D Distribution.
:param: [in] range  The total number of the consecutive values of the distribution interval.
:returns: A distribution reference *vx_distribution*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_distribution
    '''
    return lib.vxCreateDistribution(context, numBins, offset, range)
    
def CreateVirtualDistribution(graph, numBins, offset, range):
    '''
:brief: Creates an opaque reference to a 1D Distribution object without direct user access.
:param: [in] graph The reference to the parent graph.
:param: [in] numBins The number of bins in the distribution.
:param: [in] offset The start offset into the range value that marks the begining of the 1D Distribution.
:param: [in] range  The total number of the consecutive values of the distribution interval.
:see: *vxCreateDistribution*
:returns: A distribution reference *vx_distribution*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_distribution
    '''
    return lib.vxCreateVirtualDistribution(graph, numBins, offset, range)
    
def ReleaseDistribution(distribution):
    '''
:brief: Releases a reference to a distribution object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] distribution The reference to the distribution to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE distribution is not a valid *vx_distribution* reference.
:ingroup: group_distribution
    '''
    return lib.vxReleaseDistribution(distribution)
    
def QueryDistribution(distribution, attribute, ptr, size):
    '''
:brief: Queries a Distribution object.
:param: [in] distribution The reference to the distribution to query.
:param: [in] attribute The attribute to query. Use a *vx_distribution_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE distribution is not a valid *vx_distribution* reference.
:ingroup: group_distribution
    '''
    return lib.vxQueryDistribution(distribution, attribute, ptr, size)
    
def CopyDistribution(distribution, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy from/into a distribution object.
:param: [in] distribution The reference to the distribution object that is the source or the
destination of the copy.
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the distribution
object if the copy was requested in write mode. In the user memory, the distribution is
represented as a *vx_uint32* array with a number of elements equal to the value returned via
*VX_DISTRIBUTION_BINS*. The accessible memory must be large enough
to contain this vx_uint32 array:
accessible memory in bytes >= sizeof(vx_uint32)num_bins.
:param: [in] usage This declares the effect of the copy with regard to the distribution object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY*
are supported:
:arg: *VX_READ_ONLY* means that data are copied from the distribution object into the user memory.
:arg: *VX_WRITE_ONLY* means that data are copied into the distribution object from the user memory.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE distribution is not a valid *vx_distribution* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_distribution
    '''
    return lib.vxCopyDistribution(distribution, user_ptr, usage, user_mem_type)
    
def MapDistribution(distribution, map_id, ptr, usage, mem_type, flags):
    '''
:brief: Allows the application to get direct access to distribution object.
:param: [in] distribution The reference to the distribution object to map.
:param: [out] map_id The address of a *vx_map_id* variable where the function
returns a map identifier.
:arg: (*map_id) must eventually be provided as the map_id parameter of a call to
*vxUnmapDistribution*.
:param: [out] ptr The address of a pointer that the function sets to the
address where the requested data can be accessed. In the mapped memory area,
data are structured as a vx_uint32 array with a number of elements equal to
the value returned via *VX_DISTRIBUTION_BINS*. Each
element of this array corresponds to a bin of the distribution, with a range-major
ordering. Accessing the memory out of the bound of this array
is forbidden and has an undefined behavior. The returned (*ptr) address
is only valid between the call to the function and the corresponding call to
*vxUnmapDistribution*.
:param: [in] usage This declares the access mode for the distribution, using
the *vx_accessor_e* enumeration.
:arg: *VX_READ_ONLY*: after the function call, the content of the memory location
pointed by (*ptr) contains the distribution data. Writing into this memory location
is forbidden and its behavior is undefined.
:arg: *VX_READ_AND_WRITE*: after the function call, the content of the memory
location pointed by (*ptr) contains the distribution data; writing into this memory
is allowed only for the location of bins and will result in a modification of the
affected bins in the distribution object once the distribution is unmapped.
:arg: *VX_WRITE_ONLY*: after the function call, the memory location pointed by (*ptr)
contains undefined data; writing each bin of distribution is required prior to
unmapping. Bins not written by the application before unmap will become
undefined after unmap, even if they were well defined before map.
:param: [in] mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory where the distribution is requested to be mapped.
:param: [in] flags An integer that allows passing options to the map operation.
Use 0 for this option.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE distribution is not a valid *vx_distribution* reference.
reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_distribution
:post: *vxUnmapDistribution * with same (*map_id) value.
    '''
    return lib.vxMapDistribution(distribution, map_id, ptr, usage, mem_type, flags)
    
def UnmapDistribution(distribution, map_id):
    '''
:brief: Unmap and commit potential changes to distribution object that was previously mapped.
Unmapping a distribution invalidates the memory location from which the distribution data
could be accessed by the application. Accessing this memory location after the unmap
function completes has an undefined behavior.
:param: [in] distribution The reference to the distribution object to unmap.
:param: [out] map_id The unique map identifier that was returned when calling
*vxMapDistribution* .
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE distribution is not a valid *vx_distribution* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_distribution
:pre: *vxMapDistribution* returning the same map_id value
    '''
    return lib.vxUnmapDistribution(distribution, map_id)
    
def CreateThresholdForImage(context, thresh_type, input_format, output_format):
    '''
:brief: Creates a threshold object and returns a reference to it.

The threshold object defines the parameters of a thresholding operation
to an input image, that generates an output image that can have a different
format. The thresholding 'false' or 'true' output values are specified per
pixel channels of the output format and can be modified with
*vxCopyThresholdOutput*. The default 'false' output value of
pixels channels should be 0, and the default 'true' value should be non-zero.
For standard image formats, default output pixel values are defined as
following:
 :arg: VX_DF_IMAGE_RGB : false={0, 0, 0}, true={255,255,255}
 :arg: VX_DF_IMAGE_RGBX : false={0, 0, 0, 0}, true={255,255,255,255}
 :arg: VX_DF_IMAGE_NV12 : false={0, 0, 0}, true={255,255,255}
 :arg: VX_DF_IMAGE_NV21 : false={0, 0, 0}, true={255,255,255}
 :arg: VX_DF_IMAGE_UYVY : false={0, 0, 0}, true={255,255,255}
 :arg: VX_DF_IMAGE_YUYV : false={0, 0, 0}, true={255,255,255}
 :arg: VX_DF_IMAGE_IYUV : false={0, 0, 0}, true={255,255,255}
 :arg: VX_DF_IMAGE_YUV4 : false={0, 0, 0}, true={255,255,255}
 :arg: VX_DF_IMAGE_U8 : false=0, true=0xFF
 :arg: VX_DF_IMAGE_S16 : false=0, true=-1
 :arg: VX_DF_IMAGE_U16 : false=0, true=0xFFFF
 :arg: VX_DF_IMAGE_S32 : false=0, true=-1
 :arg: VX_DF_IMAGE_U32 : false=0, true=0xFFFFFFFF
:param: [in] context The reference to the context in which the object is
created.
:param: [in] thresh_type The type of thresholding operation.
:param: [in] input_format The format of images that will be used as input of
the thresholding operation.
:param: [in] output_format The format of images that will be generated by the
thresholding operation.
:returns: A threshold reference *vx_threshold*. Any possible
errors preventing a successful creation should be checked using
*vxGetStatus*.
:ingroup: group_threshold
    '''
    return lib.vxCreateThresholdForImage(context, thresh_type, input_format, output_format)
    
def CreateVirtualThresholdForImage(graph, thresh_type, input_format, output_format):
    '''
:brief: Creates an opaque reference to a threshold object without direct user access.

:param: [in] graph The reference to the parent graph.
:param: [in] thresh_type The type of thresholding operation.
:param: [in] input_format The format of images that will be used as input of
the thresholding operation.
:param: [in] output_format The format of images that will be generated by the
thresholding operation.
:see: *vxCreateThresholdForImage*
:returns: A threshold reference *vx_threshold*. Any possible
errors preventing a successful creation should be checked using
*vxGetStatus*.
:ingroup: group_threshold
    '''
    return lib.vxCreateVirtualThresholdForImage(graph, thresh_type, input_format, output_format)
    
def CopyThresholdValue(thresh, value_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy the thresholding value from/into a
threshold object with type *VX_THRESHOLD_TYPE_BINARY*.
:param: [in] thresh The reference to the threshold object that is the source
or the destination of the copy.
:param: [in,out] value_ptr The address of the memory location where to store
the thresholding value if the copy was requested in read mode, or from where
to get the thresholding value to store into the threshold object if the copy
was requested in write mode.
:param: [in] usage This declares the effect of the copy with regard to the
threshold object using the *vx_accessor_e* enumeration. Only
*VX_READ_ONLY* and *VX_WRITE_ONLY* are supported:
:arg: *VX_READ_ONLY* means that the thresholding value is copied
from the threshold object into the user memory. After the copy, only the
field of the (*value_ptr) union that corresponds to the input image format
of the threshold object is meaningful.
:arg: *VX_WRITE_ONLY* means the field of the (*value_ptr) union
corresponding  to the input format of the threshold object is copied into
the threshold object.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory referenced by :p: value_ptr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The threshold reference is not actually a
threshold reference.
:retval: VX_ERROR_NOT_COMPATIBLE The threshold object doesn't have type
*VX_THRESHOLD_TYPE_BINARY*
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_threshold
    '''
    return lib.vxCopyThresholdValue(thresh, value_ptr, usage, user_mem_type)
    
def CopyThresholdRange(thresh, lower_value_ptr, upper_value_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy thresholding values from/into a
threshold object with type *VX_THRESHOLD_TYPE_RANGE*.
:param: [in] thresh The reference to the threshold object that is the source
or the destination of the copy.
:param: [in,out] lower_value_ptr The address of the memory location where to
store the lower thresholding value if the copy was requested in read mode,
or from where to get the lower thresholding value to store into the threshold
object if the copy was requested in write mode.
:param: [in,out] upper_value_ptr The address of the memory location where to
store the upper thresholding value if the copy was requested in read mode, or
from where to get the upper thresholding value to store into the threshold
object if the copy was requested in write mode.
:param: [in] usage This declares the effect of the copy with regard to the
threshold object using the *vx_accessor_e* enumeration. Only
*VX_READ_ONLY* and *VX_WRITE_ONLY* are supported:
:arg: *VX_READ_ONLY* means that thresholding values are copied
from the threshold object into the user memory. After the copy, only the
field of (*lower_value_ptr) and (*upper_value_ptr) unions that corresponds
to the input image format of the threshold object is meaningful.
:arg: *VX_WRITE_ONLY* means the field of the (*lower_value_ptr)
and (*upper_value_ptr) unions corresponding to the input format of the
threshold object is copied into the threshold object.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory referenced by :p: lower_value_ptr and
:p: upper_value_ptr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The threshold reference is not actually
a threshold reference.
:retval: VX_ERROR_NOT_COMPATIBLE The threshold object doesn't have type
*VX_THRESHOLD_TYPE_RANGE*
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_threshold
    '''
    return lib.vxCopyThresholdRange(thresh, lower_value_ptr, upper_value_ptr, usage, user_mem_type)
    
def CopyThresholdOutput(thresh, true_value_ptr, false_value_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy the true and false output values
from/into a threshold object.
:param: [in] thresh The reference to the threshold object that is the source
or the destination of the copy.
:param: [in,out] true_value_ptr The address of the memory location where to
store the true output value if the copy was requested in read mode,
or from where to get the true output value to store into the threshold
object if the copy was requested in write mode.
:param: [in,out] false_value_ptr The address of the memory location where to
store the false output value if the copy was requested in read mode, or
from where to get the false output value to store into the threshold
object if the copy was requested in write mode.
:param: [in] usage This declares the effect of the copy with regard to the
threshold object using the *vx_accessor_e* enumeration. Only
*VX_READ_ONLY* and *VX_WRITE_ONLY* are supported:
:arg: *VX_READ_ONLY* means that true and false output values
are copied from the threshold object into the user memory. After the copy,
only the field of (*true_value_ptr) and (*false_value_ptr) unions that
corresponds to the output image format of the threshold object is meaningful.
:arg: *VX_WRITE_ONLY* means the field of the (*true_value_ptr)
and (*false_value_ptr) unions corresponding to the output format of the
threshold object is copied into the threshold object.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory referenced by :p: true_value_ptr and
:p: false_value_ptr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The threshold reference is not actually
a threshold reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_threshold
    '''
    return lib.vxCopyThresholdOutput(thresh, true_value_ptr, false_value_ptr, usage, user_mem_type)
    
def ReleaseThreshold(thresh):
    '''
:brief: Releases a reference to a threshold object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] thresh The pointer to the threshold to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE thresh is not a valid *vx_threshold* reference.
:ingroup: group_threshold
    '''
    return lib.vxReleaseThreshold(thresh)
    
def SetThresholdAttribute(thresh, attribute, ptr, size):
    '''
:brief: Sets attributes on the threshold object.
:param: [in] thresh The threshold object to set.
:param: [in] attribute The attribute to modify. Use a *vx_threshold_attribute_e* enumeration.
:param: [in] ptr The pointer to the value to which to set the attribute.
:param: [in] size The size of the data pointed to by :a: ptr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE thresh is not a valid *vx_threshold* reference.
:ingroup: group_threshold
    '''
    return lib.vxSetThresholdAttribute(thresh, attribute, ptr, size)
    
def QueryThreshold(thresh, attribute, ptr, size):
    '''
:brief: Queries an attribute on the threshold object.
:param: [in] thresh The threshold object to set.
:param: [in] attribute The attribute to query. Use a *vx_threshold_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE thresh is not a valid *vx_threshold* reference.
:ingroup: group_threshold
    '''
    return lib.vxQueryThreshold(thresh, attribute, ptr, size)
    
def CreateMatrix(c, data_type, columns, rows):
    '''
:brief: Creates a reference to a matrix object.
:param: [in] c The reference to the overall context.
:param: [in] data_type The vx_type_e that represents the data type of the matrix data elements.
:param: [in] columns The first dimensionality.
:param: [in] rows The second dimensionality.
:returns: An matrix reference *vx_matrix*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_matrix
    '''
    return lib.vxCreateMatrix(c, data_type, columns, rows)
    
def CreateVirtualMatrix(graph, data_type, columns, rows):
    '''
:brief: Creates an opaque reference to a matrix object without direct user access.
:param: [in] graph The reference to the parent graph.
:param: [in] data_type The vx_type_e that represents the data type of the matrix data elements.
:param: [in] columns The first dimensionality.
:param: [in] rows The second dimensionality.
:see: *vxCreateMatrix*
:returns: An matrix reference *vx_matrix*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_matrix
    '''
    return lib.vxCreateVirtualMatrix(graph, data_type, columns, rows)
    
def ReleaseMatrix(mat):
    '''
:brief: Releases a reference to a matrix object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] mat The matrix reference to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE mat is not a valid *vx_matrix* reference.
:ingroup: group_matrix
    '''
    return lib.vxReleaseMatrix(mat)
    
def QueryMatrix(mat, attribute, ptr, size):
    '''
:brief: Queries an attribute on the matrix object.
:param: [in] mat The matrix object to set.
:param: [in] attribute The attribute to query. Use a *vx_matrix_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE mat is not a valid *vx_matrix* reference.
:ingroup: group_matrix
    '''
    return lib.vxQueryMatrix(mat, attribute, ptr, size)
    
def CopyMatrix(matrix, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy from/into a matrix object.
:param: [in] matrix The reference to the matrix object that is the source or the
destination of the copy.
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the matrix
object if the copy was requested in write mode. In the user memory, the matrix is
structured as a row-major 2D array with elements of the type corresponding to
*VX_MATRIX_TYPE*, with a number of rows corresponding to
*VX_MATRIX_ROWS* and a number of columns corresponding to
*VX_MATRIX_COLUMNS*. The accessible memory must be large
enough to contain this 2D array:
accessible memory in bytes >= sizeof(data_element)rowscolumns.
:param: [in] usage This declares the effect of the copy with regard to the matrix object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY*
are supported:
:arg: *VX_READ_ONLY* means that data are copied from the matrix object into the user memory.
:arg: *VX_WRITE_ONLY* means that data are copied into the matrix object from the user memory.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE matrix is not a valid *vx_matrix* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_matrix
    '''
    return lib.vxCopyMatrix(matrix, user_ptr, usage, user_mem_type)
    
def CreateMatrixFromPattern(context, pattern, columns, rows):
    '''
:brief: Creates a reference to a matrix object from a boolean pattern.
:see: *vxCreateMatrixFromPatternAndOrigin* for a description of the matrix patterns.
:param: [in] context The reference to the overall context.
:param: [in] pattern The pattern of the matrix. See *VX_MATRIX_PATTERN*.
:param: [in] columns The first dimensionality.
:param: [in] rows The second dimensionality.
:returns: A matrix reference *vx_matrix* of type *VX_TYPE_UINT8*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_matrix
    '''
    return lib.vxCreateMatrixFromPattern(context, pattern, columns, rows)
    
def CreateMatrixFromPatternAndOrigin(context, pattern, columns, rows, origin_col, origin_row):
    '''
:brief: Creates a reference to a matrix object from a boolean pattern, with a user-specified origin.

The matrix created by this function is of type *VX_TYPE_UINT8*, with the value 0 representing False,
and the value 255 representing True. It supports the patterns as described below:
- VX_PATTERN_BOX is a matrix with dimensions equal to the given number of rows and columns, and all cells equal to 255.
  Dimensions of 3x3 and 5x5 must be supported.
- VX_PATTERN_CROSS is a matrix with dimensions equal to the given number of rows and columns, which both must be odd numbers.
  All cells in the center row and center column are equal to 255, and the rest are equal to zero.
  Dimensions of 3x3 and 5x5 must be supported.
- VX_PATTERN_DISK is a matrix with dimensions equal to the given number of rows (R) and columns (C),
  where R and C are odd and cell (c, r) is 255 if: :n:
  (r-R/2 + 0.5)^2 / (R/2)^2 + (c-C/2 + 0.5)^2/(C/2)^2 is less than or equal to 1,:n: and 0 otherwise.

A matrix created from pattern is read-only. The behavior when attempting to modify such a matrix is undefined.

:param: [in] context The reference to the overall context.
:param: [in] pattern The pattern of the matrix. See *VX_MATRIX_PATTERN*.
:param: [in] columns The first dimensionality.
:param: [in] rows The second dimensionality.
:param: [in] origin_col The origin (first dimensionality).
:param: [in] origin_row The origin (second dimensionality).
:returns: A matrix reference *vx_matrix* of type *VX_TYPE_UINT8*. Any possible errors
preventing a successful creation should be checked using *vxGetStatus*.
:ingroup: group_matrix
    '''
    return lib.vxCreateMatrixFromPatternAndOrigin(context, pattern, columns, rows, origin_col, origin_row)
    
def CreateConvolution(context, columns, rows):
    '''
:brief: Creates a reference to a convolution matrix object.
:param: [in] context The reference to the overall context.
:param: [in] columns The columns dimension of the convolution.
Must be odd and greater than or equal to 3 and less than the value returned
from *VX_CONTEXT_CONVOLUTION_MAX_DIMENSION*.
:param: [in] rows The rows dimension of the convolution.
Must be odd and greater than or equal to 3 and less than the value returned
from *VX_CONTEXT_CONVOLUTION_MAX_DIMENSION*.
:returns: A convolution reference *vx_convolution*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_convolution
    '''
    return lib.vxCreateConvolution(context, columns, rows)
    
def CreateVirtualConvolution(graph, columns, rows):
    '''
:brief: Creates an opaque reference to a convolution matrix object without direct user access.
:param: [in] graph The reference to the parent graph.
:param: [in] columns The columns dimension of the convolution.
Must be odd and greater than or equal to 3 and less than the value returned
from *VX_CONTEXT_CONVOLUTION_MAX_DIMENSION*.
:param: [in] rows The rows dimension of the convolution.
Must be odd and greater than or equal to 3 and less than the value returned
from *VX_CONTEXT_CONVOLUTION_MAX_DIMENSION*.
:see: *vxCreateConvolution*
:returns: A convolution reference *vx_convolution*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_convolution
    '''
    return lib.vxCreateVirtualConvolution(graph, columns, rows)
    
def ReleaseConvolution(conv):
    '''
:brief: Releases the reference to a convolution matrix.
The object may not be garbage collected until its total reference count is zero.
:param: [in] conv The pointer to the convolution matrix to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE conv is not a valid *vx_convolution* reference.
:ingroup: group_convolution
    '''
    return lib.vxReleaseConvolution(conv)
    
def QueryConvolution(conv, attribute, ptr, size):
    '''
:brief: Queries an attribute on the convolution matrix object.
:param: [in] conv The convolution matrix object to set.
:param: [in] attribute The attribute to query. Use a *vx_convolution_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE conv is not a valid *vx_convolution* reference.
:ingroup: group_convolution
    '''
    return lib.vxQueryConvolution(conv, attribute, ptr, size)
    
def SetConvolutionAttribute(conv, attribute, ptr, size):
    '''
:brief: Sets attributes on the convolution object.
:param: [in] conv The coordinates object to set.
:param: [in] attribute The attribute to modify. Use a *vx_convolution_attribute_e* enumeration.
:param: [in] ptr The pointer to the value to which to set the attribute.
:param: [in] size The size in bytes of the data pointed to by :a: ptr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE conv is not a valid *vx_convolution* reference.
:ingroup: group_convolution
    '''
    return lib.vxSetConvolutionAttribute(conv, attribute, ptr, size)
    
def CopyConvolutionCoefficients(conv, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy coefficients from/into a convolution object.
:param: [in] conv The reference to the convolution object that is the source or the destination of the copy.
:param: [in] user_ptr The address of the memory location where to store the requested
coefficient data if the copy was requested in read mode, or from where to get the
coefficient data to store into the convolution object if the copy was requested in
write mode. In the user memory, the convolution coefficient data is structured as a
row-major 2D array with elements of the type corresponding
to *VX_TYPE_CONVOLUTION*, with a number of rows corresponding to
*VX_CONVOLUTION_ROWS* and a number of columns corresponding to
*VX_CONVOLUTION_COLUMNS*. The accessible memory must be large
enough to contain this 2D array:
accessible memory in bytes >= sizeof(data_element)rowscolumns.
:param: [in] usage This declares the effect of the copy with regard to the convolution object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY*
are supported:
:arg: *VX_READ_ONLY* means that data are copied from the convolution object into the user memory.
:arg: *VX_WRITE_ONLY* means that data are copied into the convolution object from the user memory.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE conv is not a valid *vx_convolution* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_convolution
    '''
    return lib.vxCopyConvolutionCoefficients(conv, user_ptr, usage, user_mem_type)
    
def CreatePyramid(context, levels, scale, width, height, format):
    '''
:brief: Creates a reference to a pyramid object of the supplied number of levels.
:param: [in] context The reference to the overall context.
:param: [in] levels The number of levels desired. This is required to be a non-zero value.
:param: [in] scale Used to indicate the scale between pyramid levels. This is required to be a non-zero positive value.
*VX_SCALE_PYRAMID_HALF* and *VX_SCALE_PYRAMID_ORB* must be supported.
:param: [in] width The width of the 0th level image in pixels.
:param: [in] height The height of the 0th level image in pixels.
:param: [in] format The format of all images in the pyramid. NV12, NV21, IYUV, UYVY and YUYV formats are not supported.
:returns: A pyramid reference *vx_pyramid* containing the sub-images. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_pyramid
    '''
    return lib.vxCreatePyramid(context, levels, scale, width, height, format)
    
def CreateVirtualPyramid(graph, levels, scale, width, height, format):
    '''
:brief: Creates a reference to a virtual pyramid object of the supplied number of levels.
:details: Virtual Pyramids can be used to connect Nodes together when the contents of the pyramids will
not be accessed by the user of the API.
All of the following constructions are valid:
:code:
vx_context context = vxCreateContext();
vx_graph graph = vxCreateGraph(context);
vx_pyramid virt[] = {
    vxCreateVirtualPyramid(graph, 4, VX_SCALE_PYRAMID_HALF, 0, 0, VX_DF_IMAGE_VIRT), // no dimension and format specified for level 0
    vxCreateVirtualPyramid(graph, 4, VX_SCALE_PYRAMID_HALF, 640, 480, VX_DF_IMAGE_VIRT), // no format specified.
    vxCreateVirtualPyramid(graph, 4, VX_SCALE_PYRAMID_HALF, 640, 480, VX_DF_IMAGE_U8), // no access
};
:endcode:
:param: [in] graph The reference to the parent graph.
:param: [in] levels The number of levels desired. This is required to be a non-zero value.
:param: [in] scale Used to indicate the scale between pyramid levels. This is required to be a non-zero positive value.
*VX_SCALE_PYRAMID_HALF* and *VX_SCALE_PYRAMID_ORB* must be supported.
:param: [in] width The width of the 0th level image in pixels. This may be set to zero to indicate to the interface that the value is unspecified.
:param: [in] height The height of the 0th level image in pixels. This may be set to zero to indicate to the interface that the value is unspecified.
:param: [in] format The format of all images in the pyramid. This may be set to *VX_DF_IMAGE_VIRT* to indicate that the format is unspecified.
:returns: A pyramid reference *vx_pyramid*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:note: Images extracted with *vxGetPyramidLevel* behave as Virtual Images and
cause *vxMapImagePatch* to return errors.
:ingroup: group_pyramid
    '''
    return lib.vxCreateVirtualPyramid(graph, levels, scale, width, height, format)
    
def ReleasePyramid(pyr):
    '''
:brief: Releases a reference to a pyramid object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] pyr The pointer to the pyramid to release.
:ingroup: group_pyramid
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE pyr is not a valid *vx_pyramid* reference.
:post: After returning from this function the reference is zeroed.
    '''
    return lib.vxReleasePyramid(pyr)
    
def QueryPyramid(pyr, attribute, ptr, size):
    '''
:brief: Queries an attribute from an image pyramid.
:param: [in] pyr The pyramid to query.
:param: [in] attribute The attribute for which to query. Use a *vx_pyramid_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE pyr is not a valid *vx_pyramid* reference.
:ingroup: group_pyramid
    '''
    return lib.vxQueryPyramid(pyr, attribute, ptr, size)
    
def GetPyramidLevel(pyr, index):
    '''
:brief: Retrieves a level of the pyramid as a *vx_image*, which can be used
elsewhere in OpenVX. A call to vxReleaseImage is necessary to release an image for each
call of vxGetPyramidLevel.
:param: [in] pyr The pyramid object.
:param: [in] index The index of the level, such that index is less than levels.
:return: A *vx_image* reference. Any possible errors preventing a successful
function completion should be checked using *vxGetStatus*.
:ingroup: group_pyramid
    '''
    return lib.vxGetPyramidLevel(pyr, index)
    
def CreateRemap(context, src_width, src_height, dst_width, dst_height):
    '''
:brief: Creates a remap table object.
:param: [in] context The reference to the overall context.
:param: [in] src_width Width of the source image in pixel.
:param: [in] src_height Height of the source image in pixels.
:param: [in] dst_width Width of the destination image in pixels.
:param: [in] dst_height Height of the destination image in pixels.
:ingroup: group_remap
:returns: A remap reference *vx_remap*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxCreateRemap(context, src_width, src_height, dst_width, dst_height)
    
def CreateVirtualRemap(graph, src_width, src_height, dst_width, dst_height):
    '''
:brief: Creates an opaque reference to a remap table object without direct user access.
:param: [in] graph The reference to the parent graph.
:param: [in] src_width Width of the source image in pixel.
:param: [in] src_height Height of the source image in pixels.
:param: [in] dst_width Width of the destination image in pixels.
:param: [in] dst_height Height of the destination image in pixels.
:see: *vxCreateRemap*
:ingroup: group_remap
:returns: A remap reference *vx_remap*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxCreateVirtualRemap(graph, src_width, src_height, dst_width, dst_height)
    
def ReleaseRemap(table):
    '''
:brief: Releases a reference to a remap table object. The object may not be
garbage collected until its total reference count is zero.
:param: [in] table The pointer to the remap table to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE table is not a valid *vx_remap* reference.
:ingroup: group_remap
    '''
    return lib.vxReleaseRemap(table)
    
def MapRemapPatch(remap, rect, map_id, stride_y, ptr, coordinate_type, usage, mem_type):
    '''
:brief: Allows the application to get direct access to a rectangular patch of a remap object.

The patch is specified within the destination dimensions and its
data provide the corresponding coordinate within the source dimensions.
The patch is mapped as a 2D array of elements of the type associated
with the :p: coordinate_type parameter (i.e., *vx_coordinates2df_t*
for *VX_TYPE_COORDINATES2DF*).
The memory layout of the mapped 2D array follows a row-major order where rows are
compact (without any gap between elements), and where the potential
padding after each lines is determined by (* :p: stride_y).

:param: [in] remap The reference to the remap object that contains the
patch to map.

:param: [in] rect The coordinates of remap patch. The patch must be specified
within the bounds of the remap destination dimensions
(*VX_REMAP_DESTINATION_WIDTH* x *VX_REMAP_DESTINATION_HEIGHT*).
(start_x, start_y) gives the coordinate of the topleft element inside the patch,
while (end_x, end_y) gives the coordinate of the bottomright element out of the patch.

:param: [out] map_id The address of a *vx_map_id* variable
where the function returns a map identifier.
:arg: (*map_id) must eventually be provided as the map_id parameter of a call
to *vxUnmapRemapPatch*.

:param: [out] stride_y The address of a vx_size variable where the function
returns the difference between the address of the first element of two
successive lines in the mapped remap patch. The stride value follows the
following rule :
(*stride_y) >= sizeof(<ELEMENT_TYPE>)(rect->end_x - rect->start_x)

:param: [out] ptr The address of a pointer where the function returns where
remap patch data can be accessed. (*ptr) is the address of the the top-left
element of the remap patch.
The returned (*ptr) address is only valid between the call to this function
and the corresponding call to *vxUnmapRemapPatch*.

:param: [in] coordinate_type This declares the type of the source coordinate
data that the application wants to access in the remap patch.
It must be *VX_TYPE_COORDINATES2DF*.

:param: [in] usage This declares the access mode for the remap patch, using
the *vx_accessor_e* enumeration.
:arg: *VX_READ_ONLY*: after the function call, the content of the
memory location pointed by (*ptr) contains the remap patch data. Writing into
this memory location is forbidden and its behavior is undefined.
:arg: *VX_READ_AND_WRITE*: after the function call, the content of
the memory location pointed by (*ptr) contains the remap patch data; writing
into this memory is allowed for the location of elements only and will
result in a modification of the written elements in the remap object once the
patch is unmapped. Writing into a gap between element lines
(when (*stride_y) > sizeof(<ELEMENT_TYPE>)(rect->end_x - rect->start_x))
is forbidden and its behavior is undefined.
:arg: *VX_WRITE_ONLY*: after the function call, the memory location
pointed by (*ptr) contains undefined data; writing each element of the patch is
required prior to unmapping. Elements not written by the application before
unmap will become undefined after unmap, even if they were well defined before
map. Like for *VX_READ_AND_WRITE*, writing into a gap between
element lines is forbidden and its behavior is undefined.

:param: [in] mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory where the remap patch is requested to be mapped.

:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE remap is not a valid *vx_remap* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.

:ingroup: group_remap
:post: *vxUnmapRemapPatch * with same (*map_id) value.
    '''
    return lib.vxMapRemapPatch(remap, rect, map_id, stride_y, ptr, coordinate_type, usage, mem_type)
    
def UnmapRemapPatch(remap, map_id):
    '''
:brief: Unmap and commit potential changes to a remap object patch that was previously mapped.

Unmapping a remap patch invalidates the memory location from which the patch could
be accessed by the application. Accessing this memory location after the unmap function
completes has an undefined behavior.
:param: [in] remap The reference to the remap object to unmap.
:param: [out] map_id The unique map identifier that was returned by *vxMapRemapPatch* .
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE remap is not a valid *vx_remap* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_remap
:pre: *vxMapRemapPatch* with same map_id value
*/
    '''
    return lib.vxUnmapRemapPatch(remap, map_id)
    
def CopyRemapPatch(remap, rect, user_stride_y, user_ptr, user_coordinate_type, usage, user_mem_type):
    '''
:brief: Allows the application to copy a rectangular patch from/into a remap object.

The patch is specified within the destination dimensions and its
data provide the corresponding coordinate within the source dimensions.
The patch in user memory is a 2D array of elements of the type associated with the
:p: coordinate_type parameter (i.e., *vx_coordinates2df_t* for
*VX_TYPE_COORDINATES2DF*).
The memory layout of this array follows a row-major order where rows are
compact (without any gap between elements), and where the potential padding
after each line is determined by the :p: user_stride_y parameter.

:param: [in] remap The reference to the remap object that is the source or the
destination of the patch copy.

:param: [in] rect The coordinates of remap patch. The patch must be specified
within the bounds of the remap destination dimensions
(*VX_REMAP_DESTINATION_WIDTH* x *VX_REMAP_DESTINATION_HEIGHT*).
(start_x, start_y) gives the coordinate of the topleft element inside the patch,
while (end_x, end_y) gives the coordinate of the bottomright element out of the patch.

:param: [in] user_stride_y The difference between the address of the first element
of two successive lines of the remap patch in user memory (pointed by
:p: user_ptr). The layout of the user memory must follow a row major order and user_stride_y
must follow the following rule :
 user_stride_y >= sizeof(<ELEMENT_TYPE>)(rect->end_x - rect->start_x).

:param: [in] user_ptr The address of the user memory location where to store the requested
remap data if the copy was requested in read mode, or from where to get the remap data to
store into the remap object if the copy was requested in write mode. :p: user_ptr is the
address of the the top-left element of the remap patch.
The accessible user memory must be large enough to contain the specified patch with
the specified layout:
accessible memory in bytes >= (rect->end_y - rect->start_y)user_stride_y.

:param: [in] user_coordinate_type This declares the type of the source coordinate remap
data in the user memory. It must be *VX_TYPE_COORDINATES2DF*.

:param: [in] usage This declares the effect of the copy with regard to the remap object
using the *vx_accessor_e* enumeration. Only VX_READ_ONLY and VX_WRITE_ONLY are
supported:
:arg: *VX_READ_ONLY* means that data is copied from the remap object into the user
memory pointer by :p: user_ptr. The potential padding after each line in user
memory will stay unchanged.
:arg: *VX_WRITE_ONLY* means that data is copied into the remap object from
the user memory.

:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the type of the memory pointer by :p: user_ptr.

:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE remap is not a valid *vx_remap* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.

:ingroup: group_remap
*/
    '''
    return lib.vxCopyRemapPatch(remap, rect, user_stride_y, user_ptr, user_coordinate_type, usage, user_mem_type)
    
def QueryRemap(table, attribute, ptr, size):
    '''
:brief: Queries attributes from a Remap table.
:param: [in] table The remap to query.
:param: [in] attribute The attribute to query. Use a *vx_remap_attribute_e* enumeration.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE table is not a valid *vx_remap* reference.
:ingroup: group_remap
    '''
    return lib.vxQueryRemap(table, attribute, ptr, size)
    
def CreateArray(context, item_type, capacity):
    '''
:brief: Creates a reference to an Array object.

User must specify the Array capacity (i.e., the maximal number of items that the array can hold).

:param: [in] context      The reference to the overall Context.
:param: [in] item_type The type of data to hold. Must be greater than
*VX_TYPE_INVALID* and less than or equal to *VX_TYPE_VENDOR_STRUCT_END*.
Or must be a *vx_enum* returned from *vxRegisterUserStruct*.
:param: [in] capacity     The maximal number of items that the array can hold. This value must be greater than zero.

:returns: An array reference *vx_array*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.

:ingroup: group_array
    '''
    return lib.vxCreateArray(context, item_type, capacity)
    
def CreateVirtualArray(graph, item_type, capacity):
    '''
:brief: Creates an opaque reference to a virtual Array with no direct user access.

Virtual Arrays are useful when item type or capacity are unknown ahead of time
and the Array is used as internal graph edge. Virtual arrays are scoped within the parent graph only.

All of the following constructions are allowed.
:code:
vx_context context = vxCreateContext();
vx_graph graph = vxCreateGraph(context);
vx_array virt[] = {
    vxCreateVirtualArray(graph, 0, 0), // totally unspecified
    vxCreateVirtualArray(graph, VX_TYPE_KEYPOINT, 0), // unspecified capacity
    vxCreateVirtualArray(graph, VX_TYPE_KEYPOINT, 1000), // no access
};
:endcode:

:param: [in] graph        The reference to the parent graph.
:param: [in] item_type The type of data to hold. Must be greater than
*VX_TYPE_INVALID* and less than or equal to *VX_TYPE_VENDOR_STRUCT_END*.
Or must be a *vx_enum* returned from *vxRegisterUserStruct*.
                         This may to set to zero to indicate an unspecified item type.
:param: [in] capacity     The maximal number of items that the array can hold.
                         This may be to set to zero to indicate an unspecified capacity.
:see: vxCreateArray for a type list.
:returns: A array reference *vx_array*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.

:ingroup: group_array
    '''
    return lib.vxCreateVirtualArray(graph, item_type, capacity)
    
def ReleaseArray(arr):
    '''
:brief: Releases a reference of an Array object.
The object may not be garbage collected until its total reference count is zero.
After returning from this function the reference is zeroed.
:param: [in] arr          The pointer to the Array to release.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE arr is not a valid *vx_array* reference.
:ingroup: group_array
    '''
    return lib.vxReleaseArray(arr)
    
def QueryArray(arr, attribute, ptr, size):
    '''
:brief: Queries the Array for some specific information.

:param: [in] arr          The reference to the Array.
:param: [in] attribute    The attribute to query. Use a *vx_array_attribute_e*.
:param: [out] ptr         The location at which to store the resulting value.
:param: [in] size         The size in bytes of the container to which :a: ptr points.

:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE   arr is not a valid *vx_array* reference.
:retval: VX_ERROR_NOT_SUPPORTED       If the :a: attribute is not a value supported on this implementation.
:retval: VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect.

:ingroup: group_array
    '''
    return lib.vxQueryArray(arr, attribute, ptr, size)
    
def AddArrayItems(arr, count, ptr, stride):
    '''
:brief: Adds items to the Array.

This function increases the container size.

By default, the function does not reallocate memory,
so if the container is already full (number of elements is equal to capacity)
or it doesn't have enough space,
the function returns *VX_FAILURE* error code.

:param: [in] arr          The reference to the Array.
:param: [in] count        The total number of elements to insert.
:param: [in] ptr          The location from which to read the input values.
:param: [in] stride       The number of bytes between the beginning of two consecutive elements.

:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE   arr is not a valid *vx_array* reference.
:retval: VX_FAILURE                   If the Array is full.
:retval: VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect.

:ingroup: group_array
    '''
    return lib.vxAddArrayItems(arr, count, ptr, stride)
    
def TruncateArray(arr, new_num_items):
    '''
:brief: Truncates an Array (remove items from the end).

:param: [in,out] arr          The reference to the Array.
:param: [in] new_num_items    The new number of items for the Array.

:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE   arr is not a valid *vx_array* reference.
:retval: VX_ERROR_INVALID_PARAMETERS  The :a: new_size is greater than the current size.

:ingroup: group_array
    '''
    return lib.vxTruncateArray(arr, new_num_items)
    
def CopyArrayRange(array, range_start, range_end, user_stride, user_ptr, usage, user_mem_type):
    '''
:brief: Allows the application to copy a range from/into an array object.
:param: [in] array The reference to the array object that is the source or the
destination of the copy.
:param: [in] range_start The index of the first item of the array object to copy.
:param: [in] range_end The index of the item following the last item of the
array object to copy. (range_end range_start) items are copied from index
range_start included. The range must be within the bounds of the array:
0 <= range_start < range_end <= number of items in the array.
:param: [in] user_stride The number of bytes between the beginning of two consecutive
items in the user memory pointed by user_ptr. The layout of the user memory must
follow an item major order:
user_stride >= element size in bytes.
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the array
object if the copy was requested in write mode. The accessible memory must be large enough
to contain the specified range with the specified stride:
accessible memory in bytes >= (range_end range_start)user_stride.
:param: [in] usage This declares the effect of the copy with regard to the array object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY*
are supported:
:arg: *VX_READ_ONLY* means that data are copied from the array object into the user memory.
:arg: *VX_WRITE_ONLY* means that data are copied into the array object from the user memory.
:param: [in] user_mem_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual array that cannot be
accessed by the application.
:retval: VX_ERROR_INVALID_REFERENCE array is not a valid *vx_array* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_array
    '''
    return lib.vxCopyArrayRange(array, range_start, range_end, user_stride, user_ptr, usage, user_mem_type)
    
def MapArrayRange(array, range_start, range_end, map_id, stride, ptr, usage, mem_type, flags):
    '''
:brief: Allows the application to get direct access to a range of an array object.
:param: [in] array The reference to the array object that contains the range to map.
:param: [in] range_start The index of the first item of the array object to map.
:param: [in] range_end The index of the item following the last item of the
array object to map. (range_end range_start) items are mapped, starting from index
range_start included. The range must be within the bounds of the array:
Must be 0 <= range_start < range_end <= number of items.
:param: [out] map_id The address of a *vx_map_id* variable where the function
returns a map identifier.
:arg: (*map_id) must eventually be provided as the map_id parameter of a call to
*vxUnmapArrayRange*.
:param: [out] stride The address of a vx_size variable where the function
returns the memory layout of the mapped array range. The function sets (*stride)
to the number of bytes between the beginning of two consecutive items.
The application must consult (*stride) to access the array items starting from
address (*ptr). The layout of the mapped array follows an item major order:
(*stride) >= item size in bytes.
:param: [out] ptr The address of a pointer that the function sets to the
address where the requested data can be accessed. The returned (*ptr) address
is only valid between the call to the function and the corresponding call to
*vxUnmapArrayRange*.
:param: [in] usage This declares the access mode for the array range, using
the *vx_accessor_e* enumeration.
:arg: *VX_READ_ONLY*: after the function call, the content of the memory location
pointed by (*ptr) contains the array range data. Writing into this memory location
is forbidden and its behavior is undefined.
:arg: *VX_READ_AND_WRITE*: after the function call, the content of the memory
location pointed by (*ptr) contains the array range data; writing into this memory
is allowed only for the location of items and will result in a modification of the
affected items in the array object once the range is unmapped. Writing into
a gap between items (when (*stride) > item size in bytes) is forbidden and its
behavior is undefined.
:arg: *VX_WRITE_ONLY*: after the function call, the memory location pointed by (*ptr)
contains undefined data; writing each item of the range is required prior to
unmapping. Items not written by the application before unmap will become
undefined after unmap, even if they were well defined before map. Like for
VX_READ_AND_WRITE, writing into a gap between items is forbidden and its behavior
is undefined.
:param: [in] mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory where the array range is requested to be mapped.
:param: [in] flags An integer that allows passing options to the map operation.
Use the *vx_map_flag_e* enumeration.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual array that cannot be
accessed by the application.
:retval: VX_ERROR_INVALID_REFERENCE array is not a valid *vx_array* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_array
:post: *vxUnmapArrayRange * with same (*map_id) value.
    '''
    return lib.vxMapArrayRange(array, range_start, range_end, map_id, stride, ptr, usage, mem_type, flags)
    
def UnmapArrayRange(array, map_id):
    '''
:brief: Unmap and commit potential changes to an array object range that was previously mapped.
Unmapping an array range invalidates the memory location from which the range could
be accessed by the application. Accessing this memory location after the unmap function
completes has an undefined behavior.
:param: [in] array The reference to the array object to unmap.
:param: [out] map_id The unique map identifier that was returned when calling
*vxMapArrayRange* .
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE array is not a valid *vx_array* reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_array
:pre: *vxMapArrayRange* returning the same map_id value
    '''
    return lib.vxUnmapArrayRange(array, map_id)
    
def CreateObjectArray(context, exemplar, count):
    '''
:brief: Creates a reference to an ObjectArray of count objects.

It uses the metadata of the exemplar to determine the object attributes,
ignoring the object data. It does not alter the exemplar or keep or release
the reference to the exemplar. For the definition of supported attributes see
*vxSetMetaFormatAttribute*. In case the exemplar is a virtual object
it must be of immutable metadata, thus it is not allowed to be dimensionless or formatless.

:param: [in] context      The reference to the overall Context.
:param: [in] exemplar     The exemplar object that defines the metadata of the created objects in the ObjectArray.
:param: [in] count        Number of Objects to create in the ObjectArray. This value must be greater than zero.

:returns: An ObjectArray reference *vx_object_array*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*. Data objects are not initialized by this function.

:ingroup: group_object_array
    '''
    return lib.vxCreateObjectArray(context, exemplar, count)
    
def CreateVirtualObjectArray(graph, exemplar, count):
    '''
:brief: Creates an opaque reference to a virtual ObjectArray with no direct user access.

This function creates an ObjectArray of count objects with similar behavior as
*vxCreateObjectArray*. The only difference is that the objects that are
created are virtual in the given graph.

:param: [in] graph      Reference to the graph where to create the virtual ObjectArray.
:param: [in] exemplar   The exemplar object that defines the type of object in the ObjectArray.
                       Only exemplar type of *vx_image*, *vx_array* and
                       *vx_pyramid* are allowed.
:param: [in] count      Number of Objects to create in the ObjectArray.
:returns:               A ObjectArray reference *vx_object_array*. Any possible errors preventing a
                       successful creation should be checked using *vxGetStatus*.
:ingroup: group_object_array
    '''
    return lib.vxCreateVirtualObjectArray(graph, exemplar, count)
    
def GetObjectArrayItem(arr, index):
    '''
:brief:                 Retrieves the reference to the OpenVX Object in location index of the ObjectArray.

This is a vx_reference, which can be used elsewhere in OpenVX. A call to vxRelease<Object> or *vxReleaseReference*
is necessary to release the Object for each call to this function.

:param: [in] arr       The ObjectArray.
:param: [in] index     The index of the object in the ObjectArray.
:return: A reference to an OpenVX data object. Any possible errors preventing a successful
completion of the function should be checked using *vxGetStatus*.
:ingroup: group_object_array
    '''
    return lib.vxGetObjectArrayItem(arr, index)
    
def ReleaseObjectArray(arr):
    '''
:brief: Releases a reference of an ObjectArray object.

The object may not be garbage collected until its total reference and its contained objects
count is zero. After returning from this function the reference is zeroed/cleared.

:param: [in] arr          The pointer to the ObjectArray to release.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE arr is not a valid *vx_object_array* reference.
:ingroup: group_object_array
    '''
    return lib.vxReleaseObjectArray(arr)
    
def QueryObjectArray(arr, attribute, ptr, size):
    '''
:brief: Queries an atribute from the ObjectArray.

:param: [in] arr          The reference to the ObjectArray.
:param: [in] attribute    The attribute to query. Use a *vx_object_array_attribute_e*.
:param: [out] ptr         The location at which to store the resulting value.
:param: [in] size         The size in bytes of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS                   No errors; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE   arr is not a valid *vx_object_array* reference.
:retval: VX_ERROR_NOT_SUPPORTED       If the :a: attribute is not a value supported on this implementation.
:retval: VX_ERROR_INVALID_PARAMETERS  If any of the other parameters are incorrect.

:ingroup: group_object_array
    '''
    return lib.vxQueryObjectArray(arr, attribute, ptr, size)
    
def SetMetaFormatAttribute(meta, attribute, ptr, size):
    '''
:brief: This function allows a user to set the attributes of a *vx_meta_format* object in a kernel output validator.

The vx_meta_format object contains two types of information: data object meta data and
some specific information that defines how the valid region of an image changes

The meta data attributes that can be set are identified by this list:
- vx_image : VX_IMAGE_FORMAT, VX_IMAGE_HEIGHT, VX_IMAGE_WIDTH
- vx_array : VX_ARRAY_CAPACITY, VX_ARRAY_ITEMTYPE
- vx_pyramid : VX_PYRAMID_FORMAT, VX_PYRAMID_HEIGHT, VX_PYRAMID_WIDTH, VX_PYRAMID_LEVELS, VX_PYRAMID_SCALE
- vx_scalar : VX_SCALAR_TYPE
- vx_matrix : VX_MATRIX_TYPE, VX_MATRIX_ROWS, VX_MATRIX_COLUMNS
- vx_distribution : VX_DISTRIBUTION_BINS, VX_DISTRIBUTION_OFFSET, VX_DISTRIBUTION_RANGE
- vx_remap : VX_REMAP_SOURCE_WIDTH, VX_REMAP_SOURCE_HEIGHT, VX_REMAP_DESTINATION_WIDTH, VX_REMAP_DESTINATION_HEIGHT
- vx_lut : VX_LUT_TYPE, VX_LUT_COUNT
- vx_threshold : VX_THRESHOLD_TYPE, VX_THRESHOLD_INPUT_FORMAT, VX_THRESHOLD_INPUT_FORMAT
- vx_object_array : VX_OBJECT_ARRAY_NUMITEMS, VX_OBJECT_ARRAY_ITEMTYPE
- vx_tensor : VX_TENSOR_NUMBER_OF_DIMS, VX_TENSOR_DIMS, VX_TENSOR_DATA_TYPE, VX_TENSOR_FIXED_POINT_POSITION
- VX_VALID_RECT_CALLBACK
:note: For vx_image, a specific attribute can be used to specify the valid region evolution. This information is not a meta data.

:param: [in] meta The reference to the vx_meta_format struct to set
:param: [in] attribute Use the subset of data object attributes that define the meta data of this object or attributes from *vx_meta_format*.
:param: [in] ptr The input pointer of the value to set on the meta format object.
:param: [in] size The size in bytes of the object to which :a: ptr points.
:ingroup: group_user_kernels
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The attribute was set; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE meta is not a valid *vx_meta_format* reference.
:retval: VX_ERROR_INVALID_PARAMETERS size was not correct for the type needed.
:retval: VX_ERROR_NOT_SUPPORTED the object attribute was not supported on the meta format object.
:retval: VX_ERROR_INVALID_TYPE attribute type did not match known meta format type.
    '''
    return lib.vxSetMetaFormatAttribute(meta, attribute, ptr, size)
    
def SetMetaFormatFromReference(meta, exemplar):
    '''
:brief: Set a meta format object from an exemplar data object reference

This function sets a vx_meta_format object from the meta data of the exemplar

:param: [in] meta The meta format object to set
:param: [in] exemplar The exemplar data object.
:ingroup: group_user_kernels
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The meta format was correctly set; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE meta is not a valid *vx_meta_format* reference,
or exemplar is not a valid *vx_reference* reference.
    '''
    return lib.vxSetMetaFormatFromReference(meta, exemplar)
    
def QueryMetaFormatAttribute(meta, attribute, ptr, size):
    '''
:brief: This function allows a user to query the attributes of a *vx_meta_format* object in a kernel parameter.

The vx_meta_format object contains two types of information: data object meta data and
some specific information that defines how the valid region of an image changes

The meta data attributes that can be queried are identified by this list:
- vx_image : VX_IMAGE_FORMAT, VX_IMAGE_HEIGHT, VX_IMAGE_WIDTH
- vx_array : VX_ARRAY_CAPACITY, VX_ARRAY_ITEMTYPE
- vx_pyramid : VX_PYRAMID_FORMAT, VX_PYRAMID_HEIGHT, VX_PYRAMID_WIDTH, VX_PYRAMID_LEVELS, VX_PYRAMID_SCALE
- vx_scalar : VX_SCALAR_TYPE
- vx_matrix : VX_MATRIX_TYPE, VX_MATRIX_ROWS, VX_MATRIX_COLUMNS
- vx_distribution : VX_DISTRIBUTION_BINS, VX_DISTRIBUTION_OFFSET, VX_DISTRIBUTION_RANGE
- vx_remap : VX_REMAP_SOURCE_WIDTH, VX_REMAP_SOURCE_HEIGHT, VX_REMAP_DESTINATION_WIDTH, VX_REMAP_DESTINATION_HEIGHT
- vx_lut : VX_LUT_TYPE, VX_LUT_COUNT
- vx_threshold : VX_THRESHOLD_TYPE, VX_THRESHOLD_INPUT_FORMAT, VX_THRESHOLD_INPUT_FORMAT
- vx_object_array : VX_OBJECT_ARRAY_NUMITEMS, VX_OBJECT_ARRAY_ITEMTYPE
- vx_tensor : VX_TENSOR_NUMBER_OF_DIMS, VX_TENSOR_DIMS, VX_TENSOR_DATA_TYPE, VX_TENSOR_FIXED_POINT_POSITION
- VX_VALID_RECT_CALLBACK
:note: For vx_image, a specific attribute can be used to query the valid region evolution. This information is not a meta data.

:param: [in] meta The reference to the vx_meta_format struct to query
:param: [in] attribute Use the subset of data object attributes that define the meta data of this object or attributes from *vx_meta_format*.
:param: [out] ptr The output pointer of the value to query on the meta format object.
:param: [in] size The size in bytes of the object to which :a: ptr points.
:ingroup: group_import_kernel
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS The attribute was returned; any other value indicates failure.
:retval: VX_ERROR_INVALID_REFERENCE meta is not a valid *vx_meta_format* reference.
:retval: VX_ERROR_INVALID_PARAMETERS size was not correct for the type needed.
:retval: VX_ERROR_NOT_SUPPORTED the object attribute was not supported on the meta format object.
:retval: VX_ERROR_INVALID_TYPE attribute type did not match known meta format type.
    '''
    return lib.vxQueryMetaFormatAttribute(meta, attribute, ptr, size)
    
def CreateTensor(context, number_of_dims, dims, data_type, fixed_point_position):
    '''
:brief: Creates an opaque reference to a tensor data buffer.
:details: Not guaranteed to exist until the *vx_graph* containing it has been verified.
Since functions using tensors, need to understand the context of each dimension. We describe a layout of the dimensions in each function using tensors.
That layout is not mandatory. It is done specifically to explain the functions and not to mandate layout. Different implementation may have different layout.
Therefore the layout description is logical and not physical. It refers to the order of dimensions given in this function.
:param: [in] context The reference to the implementation context.
:param: [in] number_of_dims The number of dimensions.
:param: [in] dims Dimensions sizes in elements.
:param: [in] data_type The *vx_type_e* that represents the data type of the tensor data elements.
:param: [in] fixed_point_position Specifies the fixed point position when the input element type is integer. if 0, calculations are performed in integer math.
:return: A tensor data reference. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_object_tensor
    '''
    return lib.vxCreateTensor(context, number_of_dims, dims, data_type, fixed_point_position)
    
def CreateImageObjectArrayFromTensor(tensor, rect, array_size, jump, image_format):
    '''
:brief: Creates an array of images into the multi-dimension data, this can be adjacent 2D images or not depending on the stride value.
The stride value is representing bytes in the third dimension.
The OpenVX image object that points to a three dimension data and access it as an array of images.
This has to be portion of the third lowest dimension, and the stride correspond to that third dimension.
The returned Object array is an array of images. Where the image data is pointing to a specific memory in the input tensor.
:param: [in] tensor The tensor data from which to extract the images. Has to be a 3d tensor.
:param: [in] rect Image coordinates within tensor data.
:param: [in] array_size Number of images to extract.
:param: [in] jump Delta between two images in the array.
:param: [in] image_format The requested image format. Should match the tensor data's data type.
:return: An array of images pointing to the tensor data's data.
:ingroup: group_object_tensor
    '''
    return lib.vxCreateImageObjectArrayFromTensor(tensor, rect, array_size, jump, image_format)
    
def CreateTensorFromView(tensor, number_of_dims, view_start, view_end):
    '''
:brief: Creates a tensor data from another tensor data given a view. This second
reference refers to the data in the original tensor data. Updates to this tensor data
updates the parent tensor data. The view must be defined within the dimensions
of the parent tensor data.
:param: [in] tensor The reference to the parent tensor data.
:param: [in] number_of_dims Number of dimensions in the view. Error return if 0 or greater than number of
tensor dimensions. If smaller than number of tensor dimensions, the lower dimensions are assumed.
:param: [in] view_start View start coordinates
:param: [in] view_end View end coordinates
:return: The reference to the sub-tensor. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:ingroup: group_object_tensor
    '''
    return lib.vxCreateTensorFromView(tensor, number_of_dims, view_start, view_end)
    
def CreateVirtualTensor(graph, number_of_dims, dims, data_type, fixed_point_position):
    '''
:brief: Creates an opaque reference to a tensor data buffer with no direct
user access. This function allows setting the tensor data dimensions or data format.
:details: Virtual data objects allow users to connect various nodes within a
graph via data references without access to that data, but they also permit the
implementation to take maximum advantage of possible optimizations. Use this
API to create a data reference to link two or more nodes together when the
intermediate data are not required to be accessed by outside entities. This API
in particular allows the user to define the tensor data format of the data without
requiring the exact dimensions. Virtual objects are scoped within the graph
they are declared a part of, and can't be shared outside of this scope.
Since functions using tensors, need to understand the context of each dimension. We describe a layout of the dimensions in each function.
That layout is not mandated. It is done specifically to explain the functions and not to mandate layout. Different implementation may have different layout.
Therfore the layout description is logical and not physical. It refers to the order of dimensions given in *vxCreateTensor* and *vxCreateVirtualTensor*.
:param: [in] graph The reference to the parent graph.
:param: [in] number_of_dims The number of dimensions.
:param: [in] dims Dimensions sizes in elements.
:param: [in] data_type The *vx_type_e* that represents the data type of the tensor data elements.
:param: [in] fixed_point_position Specifies the fixed point position when the input element type is integer. If 0, calculations are performed in integer math.
:return: A tensor data reference.Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:note: Passing this reference to *vxCopyTensorPatch* will return an error.
:ingroup: group_object_tensor
    '''
    return lib.vxCreateVirtualTensor(graph, number_of_dims, dims, data_type, fixed_point_position)
    
def CreateTensorFromHandle(context, number_of_dims, dims, data_type, fixed_point_position, stride, ptr, memory_type):
    '''
:brief: Creates a reference to an tensor object that was externally allocated.
:param: [in] context The reference to the implementation context.
:param: [in] number_of_dims The number of dimensions.
:param: [in] dims Dimensions sizes in elements.
:param: [in] data_type The *vx_type_e* that represents the data type of the tensor data elements.
:param: [in] fixed_point_position Specifies the fixed point position when the input element type is integer. if 0, calculations are performed in integer math.
:param: [in] stride An array of stride in all dimensions in bytes. The stride value at index 0 must be size of the tensor data element type.
:param: [in] ptr The platform-defined reference to tensor. See note below.
:param: [in] memory_type *vx_memory_type_e*. When giving *VX_MEMORY_TYPE_HOST*
the :a: ptr is assumed to be HOST accessible pointer to memory.
:return: A tensor data reference. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
:note: The user must call vxMapTensorPatch prior to accessing the elements of a tensor, even if the
tensor was created via *vxCreateTensorFromHandle*. Reads or writes to memory referenced
by ptr after calling *vxCreateTensorFromHandle* without first calling
*vxMapTensorPatch* will result in undefined behavior.
The property of stride[] and ptr is kept by the caller (It means that the implementation will
make an internal copy of the provided information. :a: stride and :a: ptr can then simply be application's
local variables).

In order to release the tensor back to the application we should use *vxSwapTensorHandle*.

:ingroup: group_object_tensor
    '''
    return lib.vxCreateTensorFromHandle(context, number_of_dims, dims, data_type, fixed_point_position, stride, ptr, memory_type)
    
def SwapTensorHandle(tensor, new_ptr, prev_ptr):
    '''
:brief: Swaps the tensor handle of an tensor previously created from handle.

This function sets the new tensor handle
and returns the previous one.

Once this function call has completed, the application gets back the
ownership of the memory referenced by the previous handle. This memory
contains up-to-date tensor data, and the application can safely reuse or
release it.

The memory referenced by the new handle must have been allocated
consistently with the tensor properties since the import type,
memory layout and dimensions are unchanged (see stride and
memory_type in *vxCreateTensorFromHandle*).

All tensors created from view with this tensor as parent or ancestor
will automatically use the memory referenced by the new handle.

The behavior of *vxSwapTensorHandle* when called from a user node is undefined.
:param: [in] tensor The reference to an tensor created from handle.
:param: [in] new_ptr new tensor handle
 If new_ptr is NULL,
 If the new_ptr is NULL, the previous tensor storage memory is reclaimed by the
 caller, while no new handle is provided.
:param: [out] prev_ptr pointer to return the previous tensor handle.
If prev_ptr is NULL, the previous handle is not returned.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE tensor is not a valid *vx_tensor* reference.
reference.
:retval: VX_ERROR_INVALID_PARAMETERS The tensor was not created from handle or
the content of new_ptr is not valid.
:retval: VX_FAILURE The tensor was already being accessed.
:ingroup: group_tensor
    '''
    return lib.vxSwapTensorHandle(tensor, new_ptr, prev_ptr)
    
def CopyTensorPatch(tensor, number_of_dims, view_start, view_end, user_stride, user_ptr, usage, user_memory_type):
    '''
:brief: Allows the application to copy a view patch from/into an tensor object .
:param: [in] tensor The reference to the tensor object that is the source or the
destination of the copy.
:param: [in] number_of_dims Number of patch dimension. Error return if 0 or greater than number of
tensor dimensions. If smaller than number of tensor dimensions, the lower dimensions are assumed.
:param: [in] view_start Array of patch start points in each dimension
:param: [in] view_end Array of patch end points in each dimension
:param: [in] user_stride Array of user memory strides in each dimension
:param: [in] user_ptr The address of the memory location where to store the requested data
if the copy was requested in read mode, or from where to get the data to store into the tensor
object if the copy was requested in write mode. The accessible memory must be large enough
to contain the specified patch with the specified layout::n:
accessible memory in bytes >= (end[last_dimension] - start[last_dimension])stride[last_dimension].:n:
The layout of the user memory must follow a row major order.
:param: [in] usage This declares the effect of the copy with regard to the tensor object
using the *vx_accessor_e* enumeration. Only *VX_READ_ONLY* and *VX_WRITE_ONLY* are supported:
:arg: *VX_READ_ONLY* means that data is copied from the tensor object into the application memory
:arg: *VX_WRITE_ONLY* means that data is copied into the tensor object from the application memory
:param: [in] user_memory_type A *vx_memory_type_e* enumeration that specifies
the memory type of the memory referenced by the user_addr.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual tensor that cannot be
accessed by the application.
:retval: VX_ERROR_INVALID_REFERENCE The tensor reference is not actually an tensor reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_object_tensor
    '''
    return lib.vxCopyTensorPatch(tensor, number_of_dims, view_start, view_end, user_stride, user_ptr, usage, user_memory_type)
    
def MapTensorPatch(tensor, number_of_dims, view_start, view_end, map_id, stride, ptr, usage, mem_type):
    '''
:brief: Allows the application to get direct access to a patch of tensor object.
:param: [in] tensor The reference to the tensor object that is the source or the
destination for direct access.
:param: [in] number_of_dims The number of dimensions. Must be same as tensor number_of_dims.
:param: [in] view_start Array of patch start points in each dimension. This is optional parameter and will be zero when NULL.
:param: [in] view_end Array of patch end points in each dimension. This is optional parameter and will be dims[] of tensor when NULL.
:param: [out] map_id The address of a vx_map_id variable where the function returns a map identifier.
:arg: (*map_id) must eventually be provided as the map_id parameter of a call to *vxUnmapTensorPatch*.
:param: [out] stride An array of stride in all dimensions in bytes. The stride value at index 0 must be size of the tensor data element type.
:param: [out] ptr The address of a pointer that the function sets to the
address where the requested data can be accessed. The returned (*ptr) address
is only valid between the call to the function and the corresponding call to
*vxUnmapTensorPatch*.
:param: [in] usage This declares the access mode for the tensor patch, using
the *vx_accessor_e* enumeration.
:arg: VX_READ_ONLY: after the function call, the content of the memory location
pointed by (*ptr) contains the tensor patch data. Writing into this memory location
is forbidden and its behavior is undefined.
:arg: VX_READ_AND_WRITE : after the function call, the content of the memory
location pointed by (*ptr) contains the tensor patch data; writing into this memory
is allowed only for the location of items and will result in a modification of the
affected items in the tensor object once the range is unmapped. Writing into
a gap between items (when (*stride) > item size in bytes) is forbidden and its
behavior is undefined.
:arg: VX_WRITE_ONLY: after the function call, the memory location pointed by (*ptr)
contains undefined data; writing each item of the range is required prior to
unmapping. Items not written by the application before unmap will become
undefined after unmap, even if they were well defined before map. Like for
VX_READ_AND_WRITE, writing into a gap between items is forbidden and its behavior
is undefined.
:param: [in] mem_type A *vx_memory_type_e* enumeration that
specifies the type of the memory where the tensor patch is requested to be mapped.
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_OPTIMIZED_AWAY This is a reference to a virtual tensor that cannot be accessed by the application.
:retval: VX_ERROR_INVALID_REFERENCE The tensor reference is not actually an tensor reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:retval: VX_ERROR_NO_MEMORY Internal memory allocation failed.
:ingroup: group_tensor
:post: *vxUnmapTensorPatch * with same (*map_id) value.
    '''
    return lib.vxMapTensorPatch(tensor, number_of_dims, view_start, view_end, map_id, stride, ptr, usage, mem_type)
    
def UnmapTensorPatch(tensor, map_id):
    '''
:brief: Unmap and commit potential changes to a tensor object patch that was previously mapped.
Unmapping a tensor patch invalidates the memory location from which the patch could
be accessed by the application. Accessing this memory location after the unmap function
completes has an undefined behavior.
:param: [in] tensor The reference to the tensor object to unmap.
:param: [in] map_id The unique map identifier that was returned when calling
*vxMapTensorPatch* .
:return: A *vx_status_e* enumeration.
:retval: VX_ERROR_INVALID_REFERENCE The tensor reference is not actually an tensor reference.
:retval: VX_ERROR_INVALID_PARAMETERS An other parameter is incorrect.
:ingroup: group_tensor
:pre: *vxMapTensorPatch* returning the same map_id value
    '''
    return lib.vxUnmapTensorPatch(tensor, map_id)
    
def QueryTensor(tensor, attribute, ptr, size):
    '''
:brief: Retrieves various attributes of a tensor data.
:param: [in] tensor The reference to the tensor data to query.
:param: [in] attribute The attribute to query. Use a *vx_tensor_attribute_e*.
:param: [out] ptr The location at which to store the resulting value.
:param: [in] size The size of the container to which :a: ptr points.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors.
:retval: VX_ERROR_INVALID_REFERENCE If data is not a *vx_tensor*.
:retval: VX_ERROR_INVALID_PARAMETERS If any of the other parameters are incorrect.
:ingroup: group_object_tensor
    '''
    return lib.vxQueryTensor(tensor, attribute, ptr, size)
    
def ReleaseTensor(tensor):
    '''
:brief: Releases a reference to a tensor data object.
The object may not be garbage collected until its total reference count is zero.
:param: [in] tensor The pointer to the tensor data to release.
:post: After returning from this function the reference is zeroed.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS No errors; all other values indicate failure
:retval:An error occurred. See *vx_status_e*.
:ingroup: group_object_tensor
    '''
    return lib.vxReleaseTensor(tensor)
    
def ColorConvertNode(graph, input, output):
    '''
:brief: [Graph] Creates a color conversion node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image from which to convert.
:param: [out] output The output image to which to convert, which must have the same dimensions as the input image.
:see: *VX_KERNEL_COLOR_CONVERT*
:ingroup: group_vision_function_colorconvert
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxColorConvertNode(graph, input, output)
    
def ChannelExtractNode(graph, input, channel, output):
    '''
:brief: [Graph] Creates a channel extract node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image. Must be one of the defined vx_df_image_e multi-channel formats.
:param: [in] channel The *vx_channel_e* channel to extract.
:param: [out] output The output image. Must be *VX_DF_IMAGE_U8*, and must have the same dimensions as the input image.
*:see: VX_KERNEL_CHANNEL_EXTRACT*
:ingroup: group_vision_function_channelextract
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxChannelExtractNode(graph, input, channel, output)
    
def ChannelCombineNode(graph, plane0, plane1, plane2, plane3, output):
    '''
:brief: [Graph] Creates a channel combine node.
:param: [in] graph The graph reference.
:param: [in] plane0 The plane that forms channel 0. Must be *VX_DF_IMAGE_U8*.
:param: [in] plane1 The plane that forms channel 1. Must be *VX_DF_IMAGE_U8*.
:param: [in] plane2 [optional] The plane that forms channel 2. Must be *VX_DF_IMAGE_U8*.
:param: [in] plane3 [optional] The plane that forms channel 3. Must be *VX_DF_IMAGE_U8*.
:param: [out] output The output image. The format of the image must be defined, even if the image is virtual. Must have the same dimensions as the input images
:see: *VX_KERNEL_CHANNEL_COMBINE*
:ingroup: group_vision_function_channelcombine
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxChannelCombineNode(graph, plane0, plane1, plane2, plane3, output)
    
def PhaseNode(graph, grad_x, grad_y, orientation):
    '''
:brief: [Graph] Creates a Phase node.
:param: [in] graph The reference to the graph.
:param: [in] grad_x The input x image. This must be in *VX_DF_IMAGE_S16* format.
:param: [in] grad_y The input y image. This must be in *VX_DF_IMAGE_S16* format.
:param: [out] orientation The phase image. This is in *VX_DF_IMAGE_U8* format, and must have the same dimensions as the input images.
:see: *VX_KERNEL_PHASE*
:ingroup: group_vision_function_phase
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxPhaseNode(graph, grad_x, grad_y, orientation)
    
def Sobel3x3Node(graph, input, output_x, output_y):
    '''
:brief: [Graph] Creates a Sobel3x3 node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output_x [optional] The output gradient in the x direction in *VX_DF_IMAGE_S16*. Must have the same dimensions as the input image.
:param: [out] output_y [optional] The output gradient in the y direction in *VX_DF_IMAGE_S16*. Must have the same dimensions as the input image.
:see: *VX_KERNEL_SOBEL_3x3*
:ingroup: group_vision_function_sobel3x3
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxSobel3x3Node(graph, input, output_x, output_y)
    
def MagnitudeNode(graph, grad_x, grad_y, mag):
    '''
:brief: [Graph] Create a Magnitude node.
:param: [in] graph The reference to the graph.
:param: [in] grad_x The input x image. This must be in *VX_DF_IMAGE_S16* format.
:param: [in] grad_y The input y image. This must be in *VX_DF_IMAGE_S16* format.
:param: [out] mag The magnitude image. This is in *VX_DF_IMAGE_S16* format. Must have the same dimensions as the input image.
:see: *VX_KERNEL_MAGNITUDE*
:ingroup: group_vision_function_magnitude
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxMagnitudeNode(graph, grad_x, grad_y, mag)
    
def ScaleImageNode(graph, src, dst, type):
    '''
:brief: [Graph] Creates a Scale Image Node.
:param: [in] graph The reference to the graph.
:param: [in] src The source image of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1*.
:param: [out] dst The destination image of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1*. The output type must be the same as that of the input image.
:param: [in] type The interpolation type to use. :see: vx_interpolation_type_e.
:ingroup: group_vision_function_scale_image
:note: The destination image must have a defined size and format. The border modes
 *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED*,
 *VX_BORDER_REPLICATE* and *VX_BORDER_CONSTANT* are supported.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxScaleImageNode(graph, src, dst, type)
    
def TableLookupNode(graph, input, lut, output):
    '''
:brief: [Graph] Creates a Table Lookup node. If a value from the input image is not present in the lookup table, the result is undefined.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] lut The LUT which is of type *VX_TYPE_UINT8* if input image is *VX_DF_IMAGE_U8* or *VX_TYPE_INT16* if input image is *VX_DF_IMAGE_S16*.
:param: [out] output The output image of the same size as the input image.
:ingroup: group_vision_function_lut
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxTableLookupNode(graph, input, lut, output)
    
def HistogramNode(graph, input, distribution):
    '''
:brief: [Graph] Creates a Histogram node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8*.
:param: [out] distribution The output distribution.
:ingroup: group_vision_function_histogram
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxHistogramNode(graph, input, distribution)
    
def EqualizeHistNode(graph, input, output):
    '''
:brief: [Graph] Creates a Histogram Equalization node.
:param: [in] graph The reference to the graph.
:param: [in] input The grayscale input image in *VX_DF_IMAGE_U8*.
:param: [out] output The grayscale output image of type *VX_DF_IMAGE_U8* with equalized brightness and contrast and same size as the input image.
:ingroup: group_vision_function_equalize_hist
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxEqualizeHistNode(graph, input, output)
    
def AbsDiffNode(graph, in1, in2, out):
    '''
:brief: [Graph] Creates an AbsDiff node.
:param: [in] graph The reference to the graph.
:param: [in] in1 An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [in] in2 An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [out] out The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format, which must have the same dimensions as the input image.
:ingroup: group_vision_function_absdiff
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxAbsDiffNode(graph, in1, in2, out)
    
def MeanStdDevNode(graph, input, mean, stddev):
    '''
:brief: [Graph] Creates a mean value and optionally, a standard deviation node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image. *VX_DF_IMAGE_U8* and *VX_DF_IMAGE_U1* are supported.
:param: [out] mean The *VX_TYPE_FLOAT32* average pixel value.
:param: [out] stddev [optional] The *VX_TYPE_FLOAT32* standard deviation of the pixel values.
:ingroup: group_vision_function_meanstddev
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxMeanStdDevNode(graph, input, mean, stddev)
    
def ThresholdNode(graph, input, thresh, output):
    '''
:brief: [Graph] Creates a Threshold node and returns a reference to it.
:param: [in] graph The reference to the graph in which the node is created.
:param: [in] input The input image. Only images with format *VX_DF_IMAGE_U8*
and *VX_DF_IMAGE_S16* are supported.
:param: [in] thresh The thresholding object that defines the parameters of
the operation. The *VX_THRESHOLD_INPUT_FORMAT* must be the same as the input image format and
the *VX_THRESHOLD_OUTPUT_FORMAT* must be the same as the output image format.
:param: [out] output The output image, that will contain as pixel value
true and false values defined by :p: thresh. Images with format
*VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* are supported. The dimensions are the same as the input image.
:ingroup: group_vision_function_threshold
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation
should be checked using *vxGetStatus*
    '''
    return lib.vxThresholdNode(graph, input, thresh, output)
    
def NonMaxSuppressionNode(graph, input, mask, win_size, output):
    '''
:brief: [Graph] Creates a Non-Maxima Suppression node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [in] mask [optional] Constrict suppression to a ROI. The mask image is of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* and must have the same dimensions as the input image.
:param: [in] win_size The size of window over which to perform the localized non-maxima suppression. Must be odd, and less than or equal to the smallest dimension of the input image.
:param: [out] output The output image, of the same type and size as the input, that has been non-maxima suppressed.
:ingroup: group_vision_function_nms
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxNonMaxSuppressionNode(graph, input, mask, win_size, output)
    
def IntegralImageNode(graph, input, output):
    '''
:brief: [Graph] Creates an Integral Image Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output The output image in *VX_DF_IMAGE_U32* format, which must have the same dimensions as the input image.
:ingroup: group_vision_function_integral_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxIntegralImageNode(graph, input, output)
    
def Erode3x3Node(graph, input, output):
    '''
:brief: [Graph] Creates an Erosion Image Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which must have the same dimensions and type as the input image.
:ingroup: group_vision_function_erode_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxErode3x3Node(graph, input, output)
    
def Dilate3x3Node(graph, input, output):
    '''
:brief: [Graph] Creates a Dilation Image Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which must have the same dimensions and type as the input image.
:ingroup: group_vision_function_dilate_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxDilate3x3Node(graph, input, output)
    
def Median3x3Node(graph, input, output):
    '''
:brief: [Graph] Creates a Median Image Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which must have the same dimensions and type as the input image.
:ingroup: group_vision_function_median_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxMedian3x3Node(graph, input, output)
    
def Box3x3Node(graph, input, output):
    '''
:brief: [Graph] Creates a Box Filter Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* format, which must have the same dimensions as the input image.
:ingroup: group_vision_function_box_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxBox3x3Node(graph, input, output)
    
def Gaussian3x3Node(graph, input, output):
    '''
:brief: [Graph] Creates a Gaussian Filter Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* format, which must have the same dimensions as the input image.
:ingroup: group_vision_function_gaussian_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxGaussian3x3Node(graph, input, output)
    
def NonLinearFilterNode(graph, function, input, mask, output):
    '''
:brief: [Graph] Creates a Non-linear Filter Node.
:param: [in] graph The reference to the graph.
:param: [in] function The non-linear filter function. See *vx_non_linear_filter_e*.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [in] mask The mask to be applied to the Non-linear function. *VX_MATRIX_ORIGIN* attribute is used
 to place the mask appropriately when computing the resulting image. See *vxCreateMatrixFromPattern*.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which must have the same dimensions and type as the input image.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
:ingroup: group_vision_function_nonlinear_filter
    '''
    return lib.vxNonLinearFilterNode(graph, function, input, mask, output)
    
def ConvolveNode(graph, input, conv, output):
    '''
:brief: [Graph] Creates a custom convolution node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [in] conv The *vx_int16* convolution matrix.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format, which must have the same dimensions as the input image.
:ingroup: group_vision_function_custom_convolution
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxConvolveNode(graph, input, conv, output)
    
def GaussianPyramidNode(graph, input, gaussian):
    '''
:brief: [Graph] Creates a node for a Gaussian Image Pyramid.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] gaussian The Gaussian pyramid with *VX_DF_IMAGE_U8* to construct.
:ingroup: group_vision_function_gaussian_pyramid
:see: group_pyramid
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxGaussianPyramidNode(graph, input, gaussian)
    
def LaplacianPyramidNode(graph, input, laplacian, output):
    '''
:brief: [Graph] Creates a node for a Laplacian Image Pyramid.
:param: [in] graph The reference to the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [out] laplacian The Laplacian pyramid with *VX_DF_IMAGE_S16* to construct.
:param: [out] output The lowest resolution image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format necessary to reconstruct the input image from the pyramid. The output image format should be same as input image format.
:ingroup: group_vision_function_laplacian_pyramid
:see: group_pyramid
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxLaplacianPyramidNode(graph, input, laplacian, output)
    
def LaplacianReconstructNode(graph, laplacian, input, output):
    '''
:brief: [Graph] Reconstructs an image from a Laplacian Image pyramid.
:param: [in] graph The reference to the graph.
:param: [in] laplacian The Laplacian pyramid with *VX_DF_IMAGE_S16* format.
:param: [in] input The lowest resolution image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format for the Laplacian pyramid.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format with the highest possible resolution reconstructed from the Laplacian pyramid. The output image format should be same as input image format.
:ingroup: group_vision_function_laplacian_reconstruct
:see: group_pyramid
:return: *vx_node*.
:retval: 0 Node could not be created.
:retval:Node handle.
    '''
    return lib.vxLaplacianReconstructNode(graph, laplacian, input, output)
    
def WeightedAverageNode(graph, img1, alpha, img2, output):
    '''
:brief: [Graph] Creates a image weighted average node.
:param: [in] graph The reference to the graph.
:param: [in] img1 The first input *VX_DF_IMAGE_U8* image.
:param: [in] alpha The input *VX_TYPE_FLOAT32* scalar value with a value in the range of :f:$ 0.0 :le: :alpha: :le: 1.0 :f:$.
:param: [in] img2 The second *VX_DF_IMAGE_U8* image, which must have the same dimensions as the img1.
:param: [out] output The output *VX_DF_IMAGE_U8* image, which must have the same dimensions as the img1.
:ingroup: group_vision_function_weighted_average
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxWeightedAverageNode(graph, img1, alpha, img2, output)
    
def MinMaxLocNode(graph, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount):
    '''
:brief: [Graph] Creates a min,max,loc node.
:param: [in] graph The reference to create the graph.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [out] minVal The minimum value in the image, which corresponds to the type of the input.
:param: [out] maxVal The maximum value in the image, which corresponds to the type of the input.
:param: [out] minLoc [optional] The minimum *VX_TYPE_COORDINATES2D* locations. If the input image has several minimums, the kernel will return up to the capacity of the array.
:param: [out] maxLoc [optional] The maximum *VX_TYPE_COORDINATES2D* locations. If the input image has several maximums, the kernel will return up to the capacity of the array.
:param: [out] minCount [optional] The total number of detected minimums in image. Use a *VX_TYPE_SIZE* scalar.
:param: [out] maxCount [optional] The total number of detected maximums in image. Use a *VX_TYPE_SIZE* scalar.
:ingroup: group_vision_function_minmaxloc
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxMinMaxLocNode(graph, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount)
    
def MinNode(graph, in1, in2, out):
    '''
:brief: [Graph] Creates a pixel-wise minimum kernel.
:param: [in] graph The reference to the graph where to create the node.
:param: [in] in1 The first input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] in2 The second input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [out] out The output image which will hold the result of min and will have the same type and dimensions of the imput images.
:ingroup: group_vision_function_min
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxMinNode(graph, in1, in2, out)
    
def MaxNode(graph, in1, in2, out):
    '''
:brief: [Graph] Creates a pixel-wise maximum kernel.
:param: [in] graph The reference to the graph where to create the node.
:param: [in] in1 The first input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] in2 The second input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [out] out The output image which will hold the result of max and will have the same type and dimensions of the imput images.
:ingroup: group_vision_function_max
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxMaxNode(graph, in1, in2, out)
    
def AndNode(graph, in1, in2, out):
    '''
:brief: [Graph] Creates a bitwise AND node.
:param: [in] graph The reference to the graph.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] out The *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* output image, which must have the same dimensions and type as the input images.
:ingroup: group_vision_function_and
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxAndNode(graph, in1, in2, out)
    
def OrNode(graph, in1, in2, out):
    '''
:brief: [Graph] Creates a bitwise INCLUSIVE OR node.
:param: [in] graph The reference to the graph.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] out The *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* output image, which must have the same dimensions and type as the input images.
:ingroup: group_vision_function_or
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxOrNode(graph, in1, in2, out)
    
def XorNode(graph, in1, in2, out):
    '''
:brief: [Graph] Creates a bitwise EXCLUSIVE OR node.
:param: [in] graph The reference to the graph.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] out The *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* output image, which must have the same dimensions and type as the input images.
:ingroup: group_vision_function_xor
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxXorNode(graph, in1, in2, out)
    
def NotNode(graph, input, output):
    '''
:brief: [Graph] Creates a bitwise NOT node.
:param: [in] graph The reference to the graph.
:param: [in] input A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] output The *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* output image, which must have the same dimensions and type as the input image.
:ingroup: group_vision_function_not
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxNotNode(graph, input, output)
    
def ScalarOperationNode(graph, scalar_operation, a, b, output):
    '''
:brief: [Graph] Creates a scalar operation node.
:param: [in] graph The reference to the graph.
:param: [in] scalar_operation A *VX_TYPE_ENUM* of the *vx_scalar_operation_e* enumeration.
:param: [in] a First scalar operand.
:param: [in] b Second scalar operand.
:param: [out] output Result of the scalar operation.
:ingroup: group_control_flow
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxScalarOperationNode(graph, scalar_operation, a, b, output)
    
def SelectNode(graph, condition, true_value, false_value, output):
    '''
:brief: [Graph] Selects one of two data objects depending on the the value of a condition (boolean scalar), and copies its data into another data object.
:details: This node supports predicated execution flow within a graph. All the data objects passed to this kernel shall
have the same object type and meta data. It is important to note that an implementation may optimize away the select and copy when virtual data
objects are used.:n:
If there is a kernel node that contribute only into virtual data objects during the graph execution due to certain data path being eliminated by not
taken argument of select node, then the OpenVX implementation guarantees that there will not be any side effects to graph execution and node state.:n:
If the path to a select node contains non-virtual objects, user nodes, or  nodes with completion callbacks, then that path may not be "optimized out"
because the callback must be executed and the non-virtual objects must be modified.
:param: [in] graph The reference to the graph.
:param: [in] condition *VX_TYPE_BOOL* predicate variable.
:param: [in] true_value Data object for true.
:param: [in] false_value Data object for false.
:param: [out] output Output data object.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
:ingroup: group_control_flow
    '''
    return lib.vxSelectNode(graph, condition, true_value, false_value, output)
    
def IfBranchNode(graph, condition, input, then_value, else_value):
    '''
:brief: [Graph] Selects one of two data output branch depending on the the value of a condition (boolean scalar), and copies input data into the output selected.
:details: This node supports predicated execution flow within a graph. All the data objects passed to this kernel shall
have the same object type and meta data. It is important to note that an implementation may optimize away the select and copy when virtual data
objects are used.:n:
If there is a kernel node that contribute only into virtual data objects during the graph execution due to certain data path being eliminated by not
taken argument of select node, then the OpenVX implementation guarantees that there will not be any side effects to graph execution and node state.:n:
If the path to a select node contains non-virtual objects, user nodes, or  nodes with completion callbacks, then that path may not be "optimized out"
because the callback must be executed and the non-virtual objects must be modified.
:param: [in] graph The reference to the graph.
:param: [in] condition *VX_TYPE_BOOL* predicate variable.
:param: [in] input Data object input.
:param: [out] then_value Output data object for then.
:param: [out] else_value Output data object for else.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
:ingroup: group_control_flow
    '''
    return lib.vxIfBranchNode(graph, condition, input, then_value, else_value)
    
def MultiplyNode(graph, in1, in2, scale, overflow_policy, rounding_policy, out):
    '''
:brief: [Graph] Creates an pixelwise-multiplication node.
:param: [in] graph The reference to the graph.
:param: [in] in1 An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] in2 An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] scale A non-negative *VX_TYPE_FLOAT32* multiplied to each product before overflow handling.
:param: [in] overflow_policy A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
:param: [in] rounding_policy A *VX_TYPE_ENUM* of the *vx_round_policy_e* enumeration.
:param: [out] out The output image, a *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* image. Must have the same type and dimensions of the imput images.
:ingroup: group_vision_function_mult
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxMultiplyNode(graph, in1, in2, scale, overflow_policy, rounding_policy, out)
    
def AddNode(graph, in1, in2, policy, out):
    '''
:brief: [Graph] Creates an arithmetic addition node.
:param: [in] graph The reference to the graph.
:param: [in] in1 An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] in2 An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] policy A *VX_TYPE_ENUM* of the vx_convert_policy_e enumeration.
:param: [out] out The output image, a *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* image, which must have the same dimensions as the input images.
:ingroup: group_vision_function_add
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxAddNode(graph, in1, in2, policy, out)
    
def SubtractNode(graph, in1, in2, policy, out):
    '''
:brief: [Graph] Creates an arithmetic subtraction node.
:param: [in] graph The reference to the graph.
:param: [in] in1 An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*, the minuend.
:param: [in] in2 An input image, *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*, the subtrahend.
:param: [in] policy A *VX_TYPE_ENUM* of the vx_convert_policy_e enumeration.
:param: [out] out The output image, a *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* image, which must have the same dimensions as the input images.
:ingroup: group_vision_function_sub
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxSubtractNode(graph, in1, in2, policy, out)
    
def ConvertDepthNode(graph, input, output, policy, shift):
    '''
:brief: [Graph] Creates a bit-depth conversion node.
:param: [in] graph The reference to the graph.
:param: [in] input The input image.
:param: [out] output The output image with the same dimensions of the input image.
:param: [in] policy A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
:param: [in] shift A scalar containing a *VX_TYPE_INT32* of the shift value.
:ingroup: group_vision_function_convertdepth
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxConvertDepthNode(graph, input, output, policy, shift)
    
def CannyEdgeDetectorNode(graph, input, hyst, gradient_size, norm_type, output):
    '''
:brief: [Graph] Creates a Canny Edge Detection Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] hyst The double threshold for hysteresis. The *VX_THRESHOLD_INPUT_FORMAT* shall be either
*VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*. The *VX_THRESHOLD_OUTPUT_FORMAT* is ignored.
:param: [in] gradient_size The size of the Sobel filter window, must support at least 3, 5, and 7.
:param: [in] norm_type A flag indicating the norm used to compute the gradient, *VX_NORM_L1* or *VX_NORM_L2*.
:param: [out] output The binary output image in *VX_DF_IMAGE_U1* or *VX_DF_IMAGE_U8* format
with values either 0 and 1 (*VX_DF_IMAGE_U1*), or 0 and 255 (*VX_DF_IMAGE_U8*).
:ingroup: group_vision_function_canny
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxCannyEdgeDetectorNode(graph, input, hyst, gradient_size, norm_type, output)
    
def WarpAffineNode(graph, input, matrix, type, output):
    '''
:brief: [Graph] Creates an Affine Warp Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* image.
:param: [in] matrix The affine matrix. Must be 2x3 of type VX_TYPE_FLOAT32.
:param: [in] type The interpolation type from *vx_interpolation_type_e*.
*VX_INTERPOLATION_AREA* is not supported.
:param: [out] output The output *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* image with the same format as the input image.
:ingroup: group_vision_function_warp_affine
:note: The border modes *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED* and
*VX_BORDER_CONSTANT* are supported.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxWarpAffineNode(graph, input, matrix, type, output)
    
def WarpPerspectiveNode(graph, input, matrix, type, output):
    '''
:brief: [Graph] Creates a Perspective Warp Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] matrix The perspective matrix. Must be 3x3 of type *VX_TYPE_FLOAT32*.
:param: [in] type The interpolation type from *vx_interpolation_type_e*.
*VX_INTERPOLATION_AREA* is not supported.
:param: [out] output The output *VX_DF_IMAGE_U8* image.
:ingroup: group_vision_function_warp_perspective
:note: The border modes *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED* and
*VX_BORDER_CONSTANT* are supported.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxWarpPerspectiveNode(graph, input, matrix, type, output)
    
def HarrisCornersNode(graph, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners):
    '''
:brief: [Graph] Creates a Harris Corners Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] strength_thresh The *VX_TYPE_FLOAT32* minimum threshold with which to eliminate Harris Corner scores (computed using the normalized Sobel kernel).
:param: [in] min_distance The *VX_TYPE_FLOAT32* radial Euclidean distance for non-maximum suppression.
:param: [in] sensitivity The *VX_TYPE_FLOAT32* scalar sensitivity threshold :f:$ k :f:$ from the Harris-Stephens equation.
:param: [in] gradient_size The gradient window size to use on the input. The
implementation must support at least 3, 5, and 7.
:param: [in] block_size The block window size used to compute the Harris Corner score.
The implementation must support at least 3, 5, and 7.
:param: [out] corners The array of *VX_TYPE_KEYPOINT* objects. The order of the keypoints in this array is implementation dependent.
:param: [out] num_corners [optional] The total number of detected corners in image. Use a VX_TYPE_SIZE scalar.
:ingroup: group_vision_function_harris
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxHarrisCornersNode(graph, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners)
    
def FastCornersNode(graph, input, strength_thresh, nonmax_suppression, corners, num_corners):
    '''
:brief: [Graph] Creates a FAST Corners Node.
:param: [in] graph The reference to the graph.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] strength_thresh Threshold on difference between intensity of the central pixel and pixels on Bresenham's circle
of radius 3 (*VX_TYPE_FLOAT32* scalar), with a value in the range of 0.0 :f:$:le::f:$ strength_thresh < 256.0.
 Any fractional value will be truncated to an integer.
:param: [in] nonmax_suppression If true, non-maximum suppression is applied to
detected corners before being placed in the *vx_array* of *VX_TYPE_KEYPOINT* objects.
:param: [out] corners Output corner *vx_array* of *VX_TYPE_KEYPOINT*. The order of the
                     keypoints in this array is implementation dependent.
:param: [out] num_corners [optional] The total number of detected corners in image. Use a VX_TYPE_SIZE scalar.
:ingroup: group_vision_function_fast
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxFastCornersNode(graph, input, strength_thresh, nonmax_suppression, corners, num_corners)
    
def OpticalFlowPyrLKNode(graph, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension):
    '''
:brief: [Graph] Creates a Lucas Kanade Tracking Node.
:param: [in] graph The reference to the graph.
:param: [in] old_images Input of first (old) image pyramid in *VX_DF_IMAGE_U8*.
:param: [in] new_images Input of destination (new) image pyramid *VX_DF_IMAGE_U8*.
:param: [in] old_points An array of key points in a *vx_array* of *VX_TYPE_KEYPOINT*; those key points are defined at
 the :a: old_images high resolution pyramid.
:param: [in] new_points_estimates An array of estimation on what is the output key points in a *vx_array* of
 *VX_TYPE_KEYPOINT*; those keypoints are defined at the :a: new_images high resolution pyramid.
:param: [out] new_points An output array of key points in a *vx_array* of *VX_TYPE_KEYPOINT*; those key points are
 defined at the :a: new_images high resolution pyramid.
:param: [in] termination The termination can be *VX_TERM_CRITERIA_ITERATIONS* or *VX_TERM_CRITERIA_EPSILON* or
*VX_TERM_CRITERIA_BOTH*.
:param: [in] epsilon The *vx_float32* error for terminating the algorithm.
:param: [in] num_iterations The number of iterations. Use a *VX_TYPE_UINT32* scalar.
:param: [in] use_initial_estimate Use a *VX_TYPE_BOOL* scalar.
:param: [in] window_dimension The size of the window on which to perform the algorithm. See
 *VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION*
:ingroup: group_vision_function_opticalflowpyrlk
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxOpticalFlowPyrLKNode(graph, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension)
    
def RemapNode(graph, input, table, policy, output):
    '''
:brief: [Graph] Creates a Remap Node.
:param: [in] graph The reference to the graph that will contain the node.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] table The remap table object.
:param: [in] policy An interpolation type from *vx_interpolation_type_e*.
*VX_INTERPOLATION_AREA* is not supported.
:param: [out] output The output *VX_DF_IMAGE_U8* image with the same dimensions as the input image.
:note: The border modes *VX_NODE_BORDER* value *VX_BORDER_UNDEFINED* and
*VX_BORDER_CONSTANT* are supported.
:return: A *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
:ingroup: group_vision_function_remap
    '''
    return lib.vxRemapNode(graph, input, table, policy, output)
    
def HalfScaleGaussianNode(graph, input, output, kernel_size):
    '''
:brief: [Graph] Performs a Gaussian Blur on an image then half-scales it. The interpolation mode used is nearest-neighbor.
:details: The output image size is determined by:
:f:[
W_{output} = :frac:{W_{input} + 1}{2} \\
,
H_{output} = :frac:{H_{input} + 1}{2}
:f:]
:param: [in] graph The reference to the graph.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [out] output The output *VX_DF_IMAGE_U8* image.
:param: [in] kernel_size The input size of the Gaussian filter. Supported values are 1, 3 and 5.
:ingroup: group_vision_function_scale_image
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxHalfScaleGaussianNode(graph, input, output, kernel_size)
    
def MatchTemplateNode(graph, src, templateImage, matchingMethod, output):
    '''
:brief: [Graph]  The Node Compares an image template against overlapped image regions.
:details: The detailed equation to the matching can be found in *vx_comp_metric_e*.
The output of the template matching node is a comparison map as described in *vx_comp_metric_e*.
The Node have a limitation on the template image size (width*height). It should not be larger then 65535.
If the valid region of the template image is smaller than the entire template image, the result in the destination image is implementation-dependent.
:param: [in] graph The reference to the graph.
:param: [in] src The input image of type *VX_DF_IMAGE_U8*.
:param: [in] templateImage Searched template of type *VX_DF_IMAGE_U8*.
:param: [in] matchingMethod attribute specifying the comparison method *vx_comp_metric_e*. This function support only *VX_COMPARE_CCORR_NORM* and *VX_COMPARE_L2*.
:param: [out] output Map of comparison results. The output is an image of type VX_DF_IMAGE_S16
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
:ingroup: group_vision_function_match_template
    '''
    return lib.vxMatchTemplateNode(graph, src, templateImage, matchingMethod, output)
    
def LBPNode(graph, _in, format, kernel_size, out):
    '''
:brief: [Graph] Creates a node that extracts LBP image from an input image
* :param: [in] graph	The reference to the graph.
* :param: [in] in		An input image in *vx_image*. Or :f:$ SrcImg:f:$ in the equations. the image is of type *VX_DF_IMAGE_U8*
* :param: [in] format	A variation of LBP like original LBP and mLBP. see * vx_lbp_format_e *
* :param: [in] kernel_size Kernel size. Only size of 3 and 5 are supported
* :param: [out] out	An output image in *vx_image*.Or :f:$ DstImg:f:$ in the equations. the image is of type *VX_DF_IMAGE_U8* with the same dimensions as the input image.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
* :ingroup: group_vision_function_lbp
*/
    '''
    return lib.vxLBPNode(graph, _in, format, kernel_size, out)
    
def HOGCellsNode(graph, input, cell_width, cell_height, num_bins, magnitudes, bins):
    '''
:brief: [Graph] Performs cell calculations for the average gradient magnitude and gradient orientation histograms.
:details: Firstly, the gradient magnitude and gradient orientation are computed for each pixel in the input image.
Two 1-D centred, point discrete derivative masks are applied to the input image in the horizontal and vertical directions.
:f:[ M_h = [-1, 0, 1] :f:] and :f:[ M_v = [-1, 0, 1]^T :f:]
:f:$G_v:f:$ is the result of applying mask :f:$M_v:f:$ to the input image, and :f:$G_h:f:$ is the result of applying mask :f:$M_h:f:$ to the input image.
The border mode used for the gradient calculation is implementation dependent. Its behavior should be similar to *VX_BORDER_UNDEFINED*.
The gradient magnitudes and gradient orientations for each pixel are then calculated in the following manner.
:f:[ G(x,y) = :sqrt:{G_v(x,y)^2 + G_h(x,y)^2} :f:]
:f:[ :theta:(x,y) = arctan(G_v(x,y), G_h(x,y)) :f:]
where :f:$arctan(v, h):f:$
is :f:$ tan^{-1}(v/h):f:$ when :f:$h!=0:f:$,

:f:$ -pi/2 :f:$ if :f:$v<0:f:$ and :f:$h==0:f:$,

:f:$  pi/2  :f:$ if :f:$v>0:f:$ and :f:$h==0:f:$

and :f:$     0  :f:$ if :f:$v==0:f:$ and :f:$h==0:f:$

Secondly, the gradient magnitudes and orientations are used to compute the bins output tensor and optional magnitudes output tensor.
These tensors are computed on a cell level where the cells are rectangular in shape.
The magnitudes tensor contains the average gradient magnitude for each cell.
:f:[magnitudes(c) = :frac:{1}{(cell\_widthcell\_height)}:sum::limits:_{w=0}^{cell\_width} :sum::limits:_{h=0}^{cell\_height} G_c(w,h):f:]
where :f:$G_c:f:$ is the gradient magnitudes related to cell :f:$c:f:$.
The bins tensor contains histograms of gradient orientations for each cell.
The gradient orientations at each pixel range from 0 to 360 degrees.  These are quantised into a set of histogram bins based on the num_bins parameter.
Each pixel votes for a specific cell histogram bin based on its gradient orientation.  The vote itself is the pixel's gradient magnitude.
:f:[bins(c, n) = :sum::limits:_{w=0}^{cell\_width} :sum::limits:_{h=0}^{cell\_height} G_c(w,h)1[B_c(w, h, num\_bins) == n]:f:]
where :f:$B_c:f:$ produces the histogram bin number based on the gradient orientation of the pixel at location (:f:$w:f:$, :f:$h:f:$) in cell :f:$c:f:$ based on
the :f:$num\_bins:f:$ and :f:[1[B_c(w, h, num\_bins) == n]:f:] is a delta-function with value 1 when :f:$B_c(w, h, num\_bins) == n:f:$ or 0 otherwise.
:param: [in] graph The reference to the graph.
:param: [in] input The input image of type *VX_DF_IMAGE_U8*.
:param: [in] cell_width The histogram cell width of type *VX_TYPE_INT32*.
:param: [in] cell_height The histogram cell height of type *VX_TYPE_INT32*.
:param: [in] num_bins  The histogram size of type *VX_TYPE_INT32*.
:param: [out] magnitudes (Optional) The output average gradient magnitudes per cell of *vx_tensor* of type *VX_TYPE_INT16* of size :f:$ [floor(image_{width}/cell_{width}) ,floor(image_{height}/cell_{height}) ] :f:$.
:param: [out] bins       The output gradient orientation histograms per cell of *vx_tensor* of type *VX_TYPE_INT16* of size :f:$ [floor(image_{width}/cell_{width}) ,floor(image_{height}/cell_{height}), num_{bins}] :f:$.
:return: *vx_node*.
:retval: 0 Node could not be created.
:retval:Node handle.
:ingroup: group_vision_function_hog
    '''
    return lib.vxHOGCellsNode(graph, input, cell_width, cell_height, num_bins, magnitudes, bins)
    
def HOGFeaturesNode(graph, input, magnitudes, bins, params, hog_param_size, features):
    '''
:brief: [Graph] The node produces HOG features for the W1xW2 window in a sliding window fashion over the whole input image. Each position produces a HOG feature vector.
:details: Firstly if a magnitudes tensor is provided the cell histograms in the bins tensor are normalised by the average cell gradient magnitudes.
 :f:[bins(c,n) = :frac:{bins(c,n)}{magnitudes(c)}:f:]
To account for changes in illumination and contrast the cell histograms must be locally normalized which requires grouping the cell histograms together into larger spatially connected blocks.
Blocks are rectangular grids represented by three parameters: the number of cells per block, the number of pixels per cell, and the number of bins per cell histogram.
These blocks typically overlap, meaning that each cell histogram contributes more than once to the final descriptor.
To normalize a block its cell histograms :f:$h:f:$ are grouped together to form a vector :f:$v = [h_1, h_2, h_3, ... , h_n]:f:$.
This vector is normalised using L2-Hys which means performing L2-norm on this vector; clipping the result (by limiting the maximum values of v to be threshold) and renormalizing again. If the threshold is equal to zero then L2-Hys normalization is not performed.
:f:[L2norm(v) = :frac:{v}{:sqrt:{\|v\|_2^2 + :epsilon:^2}}:f:]
where :f:$ \|v\|_k :f:$ be its k-norm for k=1, 2, and :f:$ :epsilon: :f:$ be a small constant.
For a specific window its HOG descriptor is then the concatenated vector of the components of the normalized cell histograms from all of the block regions contained in the window.
The W1xW2 window starting position is at coordinates 0x0.
If the input image has dimensions that are not an integer multiple of W1xW2 blocks with the specified stride, then the last positions that contain only a partial W1xW2 window
will be calculated with the remaining part of the W1xW2 window padded with zeroes.
The Window W1xW2 must also have a size so that it contains an integer number of cells, otherwise the node is not well-defined.
The final output tensor will contain HOG descriptors equal to the number of windows in the input image.
The output features tensor has 3 dimensions, given by::n:
:f:[[ (floor((image_{width}-window_{width})/window_{stride}) + 1),:f:]
:f:[ (floor((image_{height}-window_{height})/window_{stride}) + 1),:f:]
:f:[ floor((window_{width} - block_{width})/block_{stride} + 1)floor((window_{height} - block_{height})/block_{stride} + 1):f:]
:f:[ (((block_{width}block_{height}) / (cell_{width}cell_{height}))num_{bins})] :f:]
See *vxCreateTensor* and *vxCreateVirtualTensor*.
We recommend the output tensors always bevirtual* objects, with this node connected directly to the classifier.
The output tensor will be very large, and using non-virtual tensors will result in a poorly optimized implementation.
Merging of this node with a classifier node such as that described in the classifier extension will result in better performance.
Notice that this node creation function has more parameters than the corresponding kernel. Numbering of kernel parameters (required if you create this node using the generic interface) is explicitly specified here.
:param: [in] graph The reference to the graph.
:param: [in] input The input image of type *VX_DF_IMAGE_U8*. (Kernel parameter #0)
:param: [in] magnitudes (Optional) The gradient magnitudes per cell of *vx_tensor* of type *VX_TYPE_INT16*. It is the output of *vxHOGCellsNode*.  (Kernel parameter #1)
:param: [in] bins       The gradient orientation histograms per cell of *vx_tensor* of type *VX_TYPE_INT16*. It is the output of *vxHOGCellsNode*. (Kernel parameter #2)
:param: [in] params The parameters of type *vx_hog_t*.  (Kernel parameter #3)
:param: [in] hog_param_size Size of *vx_hog_t* in bytes. Note that this parameter is not counted as one of the kernel parameters.
:param: [out] features The output HOG features of *vx_tensor* of type *VX_TYPE_INT16*.  (Kernel parameter #4)
:return: *vx_node*.
:retval: 0 Node could not be created.
:retval:Node handle.
:ingroup: group_vision_function_hog
    '''
    return lib.vxHOGFeaturesNode(graph, input, magnitudes, bins, params, hog_param_size, features)
    
def HoughLinesPNode(graph, input, params, lines_array, num_lines):
    '''
:brief: [Graph] Finds the Probabilistic Hough Lines detected in the input binary image, each line is stored in the output array as a set of points (x1, y1, x2, y2) .
:details: Some implementations of the algorithm may have a random or non-deterministic element. If the target application is in a safety-critical environment this
should be borne in mind and steps taken in the implementation, the application or both to achieve the level of determinism required by the system design.
:param: [in] graph graph handle
:param: [in] input A single channel binary source image of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1*.
:param: [in] params parameters of the struct *vx_hough_lines_p_t*
:param: [out] lines_array lines_array contains array of lines, see *vx_line2d_t* The order of lines in implementation dependent
:param: [out] num_lines [optional] The total number of detected lines in image. Use a VX_TYPE_SIZE scalar
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
:ingroup: group_vision_function_hough_lines_p
    '''
    return lib.vxHoughLinesPNode(graph, input, params, lines_array, num_lines)
    
def BilateralFilterNode(graph, src, diameter, sigmaSpace, sigmaValues, dst):
    '''
:brief: [Graph] The function applies bilateral filtering to the input tensor.
* :param: [in] graph The reference to the graph.
* :param: [in] src The input data a *vx_tensor*. maximum 3 dimension and minimum 2. The tensor is of type *VX_TYPE_UINT8* or *VX_TYPE_INT16*.
* dimensions are [radiometric ,width,height] or [width,height].See *vxCreateTensor* and *vxCreateVirtualTensor*.
* :param: [in] diameter of each pixel neighbourhood that is used during filtering. Values of diameter must be odd. Bigger then 3 and smaller then 10.
* :param: [in] sigmaValues Filter sigma in the radiometric space. Supported values are bigger then 0 and smaller or equal 20.
* :param: [in] sigmaSpace Filter sigma in the spatial space. Supported values are bigger then 0 and smaller or equal 20.
* :param: [out] dst The output data a *vx_tensor*,Of type *VX_TYPE_UINT8* or *VX_TYPE_INT16*. And must be the same type and size of the input.
* :note: The border modes
*  *VX_NODE_BORDER* value
*  *VX_BORDER_REPLICATE* and *VX_BORDER_CONSTANT* are supported.
* :return: *vx_node*.
* :retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
* :ingroup: group_vision_function_bilateral_filter
*/
    '''
    return lib.vxBilateralFilterNode(graph, src, diameter, sigmaSpace, sigmaValues, dst)
    
def TensorMultiplyNode(graph, input1, input2, scale, overflow_policy, rounding_policy, output):
    '''
:brief: [Graph] Performs element wise multiplications on element values in the input tensor data with a scale.
:param: [in] graph The handle to the graph.
:param: [in] input1 Input tensor data.  Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [in] input2 Input tensor data. The dimensions and sizes of input2 match those of input1, unless the vx_tensor of one or more dimensions in input2 is 1.
In this case, those dimensions are treated as if this tensor was expanded to match the size of the corresponding dimension of input1,
and data was duplicated on all terms in that dimension. After this expansion, the dimensions will be equal.
The data type must match the data type of Input1.
:param: [in] scale A non-negative *VX_TYPE_FLOAT32* multiplied to each product before overflow handling.
:param: [in] overflow_policy A *vx_convert_policy_e* enumeration.
:param: [in] rounding_policy A *vx_round_policy_e* enumeration.
:param: [out] output The output tensor data with the same dimensions as the input tensor data.
:ingroup: group_vision_function_tensor_multiply
:return: *vx_node*.
:returns: A node reference *vx_node*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxTensorMultiplyNode(graph, input1, input2, scale, overflow_policy, rounding_policy, output)
    
def TensorAddNode(graph, input1, input2, policy, output):
    '''
:brief: [Graph] Performs arithmetic addition on element values in the input tensor data.
:param: [in] graph The handle to the graph.
:param: [in] input1 Input tensor data.  Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [in] input2 Input tensor data. The dimensions and sizes of input2 match those of input1, unless the vx_tensor of one or more dimensions in input2 is 1.
In this case, those dimensions are treated as if this tensor was expanded to match the size of the corresponding dimension of input1,
and data was duplicated on all terms in that dimension. After this expansion, the dimensions will be equal.
The data type must match the data type of Input1.
:param: [in] policy A *vx_convert_policy_e* enumeration.
:param: [out] output The output tensor data with the same dimensions as the input tensor data.
:ingroup: group_vision_function_tensor_add
:return: *vx_node*.
:returns: A node reference *vx_node*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxTensorAddNode(graph, input1, input2, policy, output)
    
def TensorSubtractNode(graph, input1, input2, policy, output):
    '''
:brief: [Graph] Performs arithmetic subtraction on element values in the input tensor data.
:param: [in] graph The handle to the graph.
:param: [in] input1 Input tensor data.  Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [in] input2 Input tensor data. The dimensions and sizes of input2 match those of input1, unless the vx_tensor of one or more dimensions in input2 is 1.
In this case, those dimensions are treated as if this tensor was expanded to match the size of the corresponding dimension of input1,
and data was duplicated on all terms in that dimension. After this expansion, the dimensions will be equal.
The data type must match the data type of Input1.
:param: [in] policy A *vx_convert_policy_e* enumeration.
:param: [out] output The output tensor data with the same dimensions as the input tensor data.
:ingroup: group_vision_function_tensor_subtract
:return: *vx_node*.
:returns: A node reference *vx_node*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxTensorSubtractNode(graph, input1, input2, policy, output)
    
def TensorTableLookupNode(graph, input1, lut, output):
    '''
:brief: [Graph] Performs LUT on element values in the input tensor data.
:param: [in] graph The handle to the graph.
:param: [in] input1 Input tensor data. Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8*, with fixed_point_position 0.
:param: [in] lut The look-up table to use, of type *vx_lut*.
The elements of input1 are treated as unsigned integers to determine an index into the look-up table.
The data type of the items in the look-up table must match that of the output tensor.
:param: [out] output The output tensor data with the same dimensions as the input tensor data.
:ingroup: group_vision_function_tensor_tablelookup
:return: *vx_node*.
:returns: A node reference *vx_node*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxTensorTableLookupNode(graph, input1, lut, output)
    
def TensorTransposeNode(graph, input, output, dimension1, dimension2):
    '''
:brief: [Graph] Performs transpose on the input tensor.
The node transpose the tensor according to a specified 2 indexes in the tensor (0-based indexing)
:param: [in] graph The handle to the graph.
:param: [in] input Input tensor data, Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [out] output output tensor data,
:param: [in] dimension1 Dimension index that is transposed with dim 2.
:param: [in] dimension2 Dimension index that is transposed with dim 1.
:ingroup: group_vision_function_tensor_transpose
:return: *vx_node*.
:returns: A node reference *vx_node*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxTensorTransposeNode(graph, input, output, dimension1, dimension2)
    
def TensorConvertDepthNode(graph, input, policy, norm, offset, output):
    '''
:brief: [Graph] Creates a bit-depth conversion node.
:param: [in] graph The reference to the graph.
:param: [in] input The input tensor. Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [in] policy A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
:param: [in] norm A scalar containing a *VX_TYPE_FLOAT32* of the normalization value.
:param: [in] offset A scalar containing a *VX_TYPE_FLOAT32* of the offset value subtracted before normalization.
:param: [out] output The output tensor. Implementations must support input tensor data type *VX_TYPE_INT16*. with fixed_point_position 8.
And *VX_TYPE_UINT8* with fixed_point_position 0.
:ingroup: group_vision_function_tensor_convert_depth
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation should be checked using *vxGetStatus*
    '''
    return lib.vxTensorConvertDepthNode(graph, input, policy, norm, offset, output)
    
def TensorMatrixMultiplyNode(graph, input1, input2, input3, matrix_multiply_params, output):
    '''
:brief: [Graph] Creates a generalized matrix multiplication node.
:param: [in] graph The reference to the graph.
:param: [in] input1 The first input 2D tensor of type *VX_TYPE_INT16* with fixed_point_pos 8, or tensor data types *VX_TYPE_UINT8* or *VX_TYPE_INT8*, with fixed_point_pos 0.
:param: [in] input2 The second 2D tensor. Must be in the same data type as input1.
:param: [in] input3 The third 2D tensor. Must be in the same data type as input1. [optional].
:param: [in] matrix_multiply_params Matrix multiply parameters, see *vx_tensor_matrix_multiply_params_t *.
:param: [out] output The output 2D tensor. Must be in the same data type as input1. Output dimension must agree the formula in the description.
:ingroup: group_vision_function_tensor_matrix_multiply
:return: *vx_node*.
:returns: A node reference *vx_node*. Any possible errors preventing a
successful creation should be checked using *vxGetStatus*.
    '''
    return lib.vxTensorMatrixMultiplyNode(graph, input1, input2, input3, matrix_multiply_params, output)
    
def CopyNode(graph, input, output):
    '''
:brief: Copy data from one object to another.
:note: An implementation may optimize away the copy when virtual data objects are used.
:param: [in] graph The reference to the graph.
:param: [in] input The input data object.
:param: [out] output The output data object with meta-data identical to the input data object.
:return: *vx_node*.
:retval: vx_node A node reference. Any possible errors preventing a successful creation
should be checked using *vxGetStatus*
:ingroup: group_vision_function_copy
    '''
    return lib.vxCopyNode(graph, input, output)
    