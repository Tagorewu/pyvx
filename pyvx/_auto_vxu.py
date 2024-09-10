from pyvx.backend import lib, ffi

def ColorConvert(context, input, output):
    '''
:brief: [Immediate] Invokes an immediate Color Conversion.
:param: [in] context The reference to the overall context.
:param: [in] input The input image.
:param: [out] output The output image.
:ingroup: group_vision_function_colorconvert
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuColorConvert(context, input, output)
    
def ChannelExtract(context, input, channel, output):
    '''
:brief: [Immediate] Invokes an immediate Channel Extract.
:param: [in] context The reference to the overall context.
:param: [in] input The input image. Must be one of the defined *vx_df_image_e* multi-channel formats.
:param: [in] channel The *vx_channel_e* enumeration to extract.
:param: [out] output The output image. Must be *VX_DF_IMAGE_U8*.
:ingroup: group_vision_function_channelextract
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuChannelExtract(context, input, channel, output)
    
def ChannelCombine(context, plane0, plane1, plane2, plane3, output):
    '''
:brief: [Immediate] Invokes an immediate Channel Combine.
:param: [in] context The reference to the overall context.
:param: [in] plane0 The plane that forms channel 0. Must be *VX_DF_IMAGE_U8*.
:param: [in] plane1 The plane that forms channel 1. Must be *VX_DF_IMAGE_U8*.
:param: [in] plane2 [optional] The plane that forms channel 2. Must be *VX_DF_IMAGE_U8*.
:param: [in] plane3 [optional] The plane that forms channel 3. Must be *VX_DF_IMAGE_U8*.
:param: [out] output The output image.
:ingroup: group_vision_function_channelcombine
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuChannelCombine(context, plane0, plane1, plane2, plane3, output)
    
def Sobel3x3(context, input, output_x, output_y):
    '''
:brief: [Immediate] Invokes an immediate Sobel 3x3.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output_x [optional] The output gradient in the x direction in *VX_DF_IMAGE_S16*.
:param: [out] output_y [optional] The output gradient in the y direction in *VX_DF_IMAGE_S16*.
:ingroup: group_vision_function_sobel3x3
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuSobel3x3(context, input, output_x, output_y)
    
def Magnitude(context, grad_x, grad_y, mag):
    '''
:brief: [Immediate] Invokes an immediate Magnitude.
:param: [in] context The reference to the overall context.
:param: [in] grad_x The input x image. This must be in *VX_DF_IMAGE_S16* format.
:param: [in] grad_y The input y image. This must be in *VX_DF_IMAGE_S16* format.
:param: [out] mag The magnitude image. This will be in *VX_DF_IMAGE_S16* format.
:ingroup: group_vision_function_magnitude
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuMagnitude(context, grad_x, grad_y, mag)
    
def Phase(context, grad_x, grad_y, orientation):
    '''
:brief: [Immediate] Invokes an immediate Phase.
:param: [in] context The reference to the overall context.
:param: [in] grad_x The input x image. This must be in *VX_DF_IMAGE_S16* format.
:param: [in] grad_y The input y image. This must be in *VX_DF_IMAGE_S16* format.
:param: [out] orientation The phase image. This will be in *VX_DF_IMAGE_U8* format.
:ingroup: group_vision_function_phase
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuPhase(context, grad_x, grad_y, orientation)
    
def ScaleImage(context, src, dst, type):
    '''
:brief: [Immediate] Scales an input image to an output image.
:param: [in] context The reference to the overall context.
:param: [in] src The source image of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1*.
:param: [out] dst The destination image of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1*.
Must be of the same format as the input image.
:param: [in] type The interpolation type. :see: vx_interpolation_type_e.
:ingroup: group_vision_function_scale_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuScaleImage(context, src, dst, type)
    
def TableLookup(context, input, lut, output):
    '''
:brief: [Immediate] Processes the image through the LUT.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] lut The LUT which is of type *VX_TYPE_UINT8* if input image is *VX_DF_IMAGE_U8* or *VX_TYPE_INT16* if input image is *VX_DF_IMAGE_S16*.
:param: [out] output The output image of the same size as the input image.
:ingroup: group_vision_function_lut
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTableLookup(context, input, lut, output)
    
def Histogram(context, input, distribution):
    '''
:brief: [Immediate] Generates a distribution from an image.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8*
:param: [out] distribution The output distribution.
:ingroup: group_vision_function_histogram
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuHistogram(context, input, distribution)
    
def EqualizeHist(context, input, output):
    '''
:brief: [Immediate] Equalizes the Histogram of a grayscale image.
:param: [in] context The reference to the overall context.
:param: [in] input The grayscale input image in *VX_DF_IMAGE_U8*
:param: [out] output The grayscale output image of type *VX_DF_IMAGE_U8* with equalized brightness and contrast.
:ingroup: group_vision_function_equalize_hist
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuEqualizeHist(context, input, output)
    
def AbsDiff(context, in1, in2, out):
    '''
:brief: [Immediate] Computes the absolute difference between two images.
:param: [in] context The reference to the overall context.
:param: [in] in1 An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [in] in2 An input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [out] out The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:ingroup: group_vision_function_absdiff
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuAbsDiff(context, in1, in2, out)
    
def MeanStdDev(context, input, mean, stddev):
    '''
:brief: [Immediate] Computes the mean value and optionally the standard deviation.
:param: [in] context The reference to the overall context.
:param: [in] input The input image. *VX_DF_IMAGE_U8* and *VX_DF_IMAGE_U1* are supported.
:param: [out] mean The average pixel value.
:param: [out] stddev [optional] The standard deviation of the pixel values.
:ingroup: group_vision_function_meanstddev
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuMeanStdDev(context, input, mean, stddev)
    
def Threshold(context, input, thresh, output):
    '''
:brief: [Immediate] Threshold's an input image and produces a *VX_DF_IMAGE_U8* boolean image.
:param: [in] context The reference to the overall context.
:param: [in] input The input image. Only images with format *VX_DF_IMAGE_U8*
and *VX_DF_IMAGE_S16* are supported.
:param: [in] thresh The thresholding object that defines the parameters of
the operation. The *VX_THRESHOLD_INPUT_FORMAT* must be the same as the input image format and
the *VX_THRESHOLD_OUTPUT_FORMAT* must be the same as the output image format.
:param: [out] output The output image, that will contain as pixel values true and false values defined by :p: thresh.
Only images with format *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* are supported.
Must be of the same size as the input image.
:ingroup: group_vision_function_threshold
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuThreshold(context, input, thresh, output)
    
def NonMaxSuppression(context, input, mask, win_size, output):
    '''
:brief: [Immediate] Performs Non-Maxima Suppression on an image, producing an image of the same type.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [in] mask [optional] Constrict suppression to a ROI. The mask image is of type *VX_DF_IMAGE_U8*
or *VX_DF_IMAGE_U1* and must be the same dimensions as the input image.
:param: [in] win_size The size of window over which to perform the localized non-maxima suppression.  Must be odd,
and less than or equal to the smallest dimension of the input image.
:param: [out] output The output image, of the same type as the input, that has been non-maxima suppressed.
:ingroup: group_vision_function_nms
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuNonMaxSuppression(context, input, mask, win_size, output)
    
def IntegralImage(context, input, output):
    '''
:brief: [Immediate] Computes the integral image of the input.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output The output image in *VX_DF_IMAGE_U32* format.
:ingroup: group_vision_function_integral_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuIntegralImage(context, input, output)
    
def Erode3x3(context, input, output):
    '''
:brief: [Immediate] Erodes an image by a 3x3 window.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which
must have the same dimensions and type as the input image.
:ingroup: group_vision_function_erode_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuErode3x3(context, input, output)
    
def Dilate3x3(context, input, output):
    '''
:brief: [Immediate] Dilates an image by a 3x3 window.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which
must have the same dimensions and type as the input image.
:ingroup: group_vision_function_dilate_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuDilate3x3(context, input, output)
    
def Median3x3(context, input, output):
    '''
:brief: [Immediate] Computes a median filter on the image by a 3x3 window.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which
must have the same dimensions and type as the input image.
:ingroup: group_vision_function_median_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuMedian3x3(context, input, output)
    
def Box3x3(context, input, output):
    '''
:brief: [Immediate] Computes a box filter on the image by a 3x3 window.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* format.
:ingroup: group_vision_function_box_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuBox3x3(context, input, output)
    
def Gaussian3x3(context, input, output):
    '''
:brief: [Immediate] Computes a gaussian filter on the image by a 3x3 window.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [out] output The output image in *VX_DF_IMAGE_U8* format.
:ingroup: group_vision_function_gaussian_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuGaussian3x3(context, input, output)
    
def NonLinearFilter(context, function, input, mask, output):
    '''
:brief: [Immediate] Performs Non-linear Filtering.
:param: [in] context The reference to the overall context.
:param: [in] function The non-linear filter function. See *vx_non_linear_filter_e*.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format.
:param: [in] mask The mask to be applied to the Non-linear function. *VX_MATRIX_ORIGIN* attribute is used
to place the mask appropriately when computing the resulting image. See *vxCreateMatrixFromPattern* and *vxCreateMatrixFromPatternAndOrigin*.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* format, which
must have the same dimensions and type as the input image.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
:ingroup: group_vision_function_nonlinear_filter
    '''
    return lib.vxuNonLinearFilter(context, function, input, mask, output)
    
def Convolve(context, input, conv, output):
    '''
:brief: [Immediate] Computes a convolution on the input image with the supplied
matrix.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* format.
:param: [in] conv The *vx_int16* convolution matrix.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:ingroup: group_vision_function_custom_convolution
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuConvolve(context, input, conv, output)
    
def GaussianPyramid(context, input, gaussian):
    '''
:brief: [Immediate] Computes a Gaussian pyramid from an input image.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8*
:param: [out] gaussian The Gaussian pyramid with *VX_DF_IMAGE_U8* to construct.
:ingroup: group_vision_function_gaussian_pyramid
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuGaussianPyramid(context, input, gaussian)
    
def LaplacianPyramid(context, input, laplacian, output):
    '''
:brief: [Immediate] Computes a Laplacian pyramid from an input image.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [out] laplacian The Laplacian pyramid with *VX_DF_IMAGE_S16* to construct.
:param: [out] output The lowest resolution image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format necessary to reconstruct the input image from the pyramid. The output image format should be same as input image format.
:ingroup: group_vision_function_laplacian_pyramid
:see: group_pyramid
:return: A *vx_status* enumeration.
:retval: VX_SUCCESS Success.
:retval:An error occured. See *vx_status_e*
    '''
    return lib.vxuLaplacianPyramid(context, input, laplacian, output)
    
def LaplacianReconstruct(context, laplacian, input, output):
    '''
:brief: [Immediate] Reconstructs an image from a Laplacian Image pyramid.
:param: [in] context The reference to the overall context.
:param: [in] laplacian The Laplacian pyramid with *VX_DF_IMAGE_S16* format.
:param: [in] input The lowest resolution image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format for the Laplacian pyramid.
:param: [out] output The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format with the highest possible resolution reconstructed from the Laplacian pyramid. The output image format should be same as input image format.
:ingroup: group_vision_function_laplacian_reconstruct
:see: group_pyramid
:return: A *vx_status* enumeration.
:retval: VX_SUCCESS Success.
:retval:An error occured. See *vx_status_e*
    '''
    return lib.vxuLaplacianReconstruct(context, laplacian, input, output)
    
def WeightedAverage(context, img1, alpha, img2, output):
    '''
:brief: [Immediate] Computes a weighted average image.
:param: [in] context The reference to the overall context.
:param: [in] img1 The first *VX_DF_IMAGE_U8* image.
:param: [in] alpha A *VX_TYPE_FLOAT32* type, the input value with the range :f:$ 0.0 :le: :alpha: :le: 1.0 :f:$.
:param: [in] img2 The second *VX_DF_IMAGE_U8* image.
:param: [out] output The output *VX_DF_IMAGE_U8* image.
:ingroup: group_vision_function_weighted_average
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuWeightedAverage(context, img1, alpha, img2, output)
    
def MinMaxLoc(context, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount):
    '''
:brief: [Immediate] Computes the minimum and maximum values of the image.
:param: [in] context The reference to the overall context.
:param: [in] input The input image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:param: [out] minVal The minimum value in the image, which corresponds to the type of the input.
:param: [out] maxVal The maximum value in the image, which corresponds to the type of the input.
:param: [out] minLoc [optional] The minimum *VX_TYPE_COORDINATES2D* locations. If the input image has several minimums, the kernel will return up to the capacity of the array.
:param: [out] maxLoc [optional] The maximum *VX_TYPE_COORDINATES2D* locations. If the input image has several maximums, the kernel will return up to the capacity of the array.
:param: [out] minCount [optional] The total number of detected minimums in image. Use a *VX_TYPE_SIZE* scalar.
:param: [out] maxCount [optional] The total number of detected maximums in image. Use a *VX_TYPE_SIZE* scalar.
:ingroup: group_vision_function_minmaxloc
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuMinMaxLoc(context, input, minVal, maxVal, minLoc, maxLoc, minCount, maxCount)
    
def Min(context, in1, in2, out):
    '''
:brief: [Immediate] Computes pixel-wise minimum values between two images.
:param: [in] context The reference to the overall context.
:param: [in] in1 The first input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] in2 The second input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [out] out The output image which will hold the result of min.
:ingroup: group_vision_function_min
:return:  A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuMin(context, in1, in2, out)
    
def Max(context, in1, in2, out):
    '''
:brief: [Immediate] Computes pixel-wise maximum values between two images.
:param: [in]  context The reference to the overall context.
:param: [in] in1 The first input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [in] in2 The second input image. Must be of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*.
:param: [out] out The output image which will hold the result of max.
:ingroup: group_vision_function_max
:return:  A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuMax(context, in1, in2, out)
    
def ConvertDepth(context, input, output, policy, shift):
    '''
:brief: [Immediate] Converts the input images bit-depth into the output image.
:param: [in] context The reference to the overall context.
:param: [in] input The input image.
:param: [out] output The output image.
:param: [in] policy A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
:param: [in] shift A scalar containing a *VX_TYPE_INT32* of the shift value.
:ingroup: group_vision_function_convertdepth
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*..
    '''
    return lib.vxuConvertDepth(context, input, output, policy, shift)
    
def CannyEdgeDetector(context, input, hyst, gradient_size, norm_type, output):
    '''
:brief: [Immediate] Computes Canny Edges on the input image into the output image.
:param: [in] context The reference to the overall context.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] hyst The double threshold for hysteresis. The *VX_THRESHOLD_INPUT_FORMAT* shall be either
*VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16*. The *VX_THRESHOLD_OUTPUT_FORMAT* is ignored.
:param: [in] gradient_size The size of the Sobel filter window, must support at least 3, 5 and 7.
:param: [in] norm_type A flag indicating the norm used to compute the gradient, *VX_NORM_L1* or *VX_NORM_L2*.
:param: [out] output The binary output image in *VX_DF_IMAGE_U1* or *VX_DF_IMAGE_U8* format
with values either 0 and 1 (*VX_DF_IMAGE_U1*), or 0 and 255 (*VX_DF_IMAGE_U8*).
:ingroup: group_vision_function_canny
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuCannyEdgeDetector(context, input, hyst, gradient_size, norm_type, output)
    
def HalfScaleGaussian(context, input, output, kernel_size):
    '''
:brief: [Immediate] Performs a Gaussian Blur on an image then half-scales it. The interpolation mode used is nearest-neighbor.
:param: [in] context The reference to the overall context.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [out] output The output *VX_DF_IMAGE_U8* image.
:param: [in] kernel_size The input size of the Gaussian filter. Supported values are 1, 3 and 5.
:ingroup: group_vision_function_scale_image
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuHalfScaleGaussian(context, input, output, kernel_size)
    
def And(context, in1, in2, out):
    '''
:brief: [Immediate] Computes the bitwise and between two images.
:param: [in] context The reference to the overall context.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] out The *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* output image, which must have the
same dimensions and type as the input images.
:ingroup: group_vision_function_and
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuAnd(context, in1, in2, out)
    
def Or(context, in1, in2, out):
    '''
:brief: [Immediate] Computes the bitwise inclusive-or between two images.
:param: [in] context The reference to the overall context.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] out The *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* output image, which must have the
same dimensions and type as the input images.
:ingroup: group_vision_function_or
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuOr(context, in1, in2, out)
    
def Xor(context, in1, in2, out):
    '''
:brief: [Immediate] Computes the bitwise exclusive-or between two images.
:param: [in] context The reference to the overall context.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] out The *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* output image, which must have the
same dimensions and type as the input images.
:ingroup: group_vision_function_xor
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuXor(context, in1, in2, out)
    
def Not(context, input, output):
    '''
:brief: [Immediate] Computes the bitwise not of an image.
:param: [in] context The reference to the overall context.
:param: [in] input A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1* input image.
:param: [out] output The *VX_DF_IMAGE_U8*  or *VX_DF_IMAGE_U1* output image, which must have
the same dimensions and type as the input image.
:ingroup: group_vision_function_not
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuNot(context, input, output)
    
def Multiply(context, in1, in2, scale, overflow_policy, rounding_policy, out):
    '''
:brief: [Immediate] Performs elementwise multiplications on pixel values in the input images and a scale.
:param: [in] context The reference to the overall context.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
:param: [in] scale A non-negative *VX_TYPE_FLOAT32* multiplied to each product before overflow handling.
:param: [in] overflow_policy A *vx_convert_policy_e* enumeration.
:param: [in] rounding_policy A *vx_round_policy_e* enumeration.
:param: [out] out The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:ingroup: group_vision_function_mult
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuMultiply(context, in1, in2, scale, overflow_policy, rounding_policy, out)
    
def Add(context, in1, in2, policy, out):
    '''
:brief: [Immediate] Performs arithmetic addition on pixel values in the input images.
:param: [in] context The reference to the overall context.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image.
:param: [in] policy A vx_convert_policy_e enumeration.
:param: [out] out The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:ingroup: group_vision_function_add
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuAdd(context, in1, in2, policy, out)
    
def Subtract(context, in1, in2, policy, out):
    '''
:brief: [Immediate] Performs arithmetic subtraction on pixel values in the input images.
:param: [in] context The reference to the overall context.
:param: [in] in1 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image, the minuend.
:param: [in] in2 A *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* input image, the subtrahend.
:param: [in] policy A vx_convert_policy_e enumeration.
:param: [out] out The output image in *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_S16* format.
:ingroup: group_vision_function_sub
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuSubtract(context, in1, in2, policy, out)
    
def WarpAffine(context, input, matrix, type, output):
    '''
:brief: [Immediate] Performs an Affine warp on an image.
:param: [in] context The reference to the overall context.
:param: [in] input The input *VX_DF_IMAGE_U1* or *VX_DF_IMAGE_U8* image.
:param: [in] matrix The affine matrix. Must be 2x3 of type VX_TYPE_FLOAT32.
:param: [in] type The interpolation type from vx_interpolation_type_e.
VX_INTERPOLATION_AREA is not supported.
:param: [out] output The output *VX_DF_IMAGE_U1* or *VX_DF_IMAGE_U8* image of the same
format as the input image.
:ingroup: group_vision_function_warp_affine
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuWarpAffine(context, input, matrix, type, output)
    
def WarpPerspective(context, input, matrix, type, output):
    '''
:brief: [Immediate] Performs an Perspective warp on an image.
:param: [in] context The reference to the overall context.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] matrix The perspective matrix. Must be 3x3 of type VX_TYPE_FLOAT32.
:param: [in] type The interpolation type from vx_interpolation_type_e.
VX_INTERPOLATION_AREA is not supported.
:param: [out] output The output *VX_DF_IMAGE_U8* image.
:ingroup: group_vision_function_warp_perspective
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuWarpPerspective(context, input, matrix, type, output)
    
def HarrisCorners(context, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners):
    '''
:brief: [Immediate] Computes the Harris Corners over an image and produces the array of scored points.
:param: [in] context The reference to the overall context.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] strength_thresh The *VX_TYPE_FLOAT32* minimum threshold which to eliminate Harris Corner scores (computed using the normalized Sobel kernel).
:param: [in] min_distance The *VX_TYPE_FLOAT32* radial Euclidean distance for non-maximum suppression.
:param: [in] sensitivity The *VX_TYPE_FLOAT32* scalar sensitivity threshold :f:$ k :f:$ from the Harris-Stephens equation.
:param: [in] gradient_size The gradient window size to use on the input. The
implementation must support at least 3, 5, and 7.
:param: [in] block_size The block window size used to compute the harris corner score.
The implementation must support at least 3, 5, and 7.
:param: [out] corners The array of *VX_TYPE_KEYPOINT* structs. The order of the keypoints in this array is implementation dependent.
:param: [out] num_corners [optional] The total number of detected corners in image. Use a VX_TYPE_SIZE scalar
:ingroup: group_vision_function_harris
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuHarrisCorners(context, input, strength_thresh, min_distance, sensitivity, gradient_size, block_size, corners, num_corners)
    
def FastCorners(context, input, strength_thresh, nonmax_suppression, corners, num_corners):
    '''
:brief: [Immediate] Computes corners on an image using FAST algorithm and produces the array of feature points.
:param: [in] context The reference to the overall context.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] strength_thresh Threshold on difference between intensity of the central pixel and pixels on Bresenham's circle
of radius 3 (*VX_TYPE_FLOAT32* scalar), with a value in the range of 0.0 :f:$:le::f:$ strength_thresh < 256.0.
 Any fractional value will be truncated to an integer.
:param: [in] nonmax_suppression If true, non-maximum suppression is applied to
detected corners before being places in the *vx_array* of *VX_TYPE_KEYPOINT* structs.
:param: [out] corners Output corner *vx_array* of *VX_TYPE_KEYPOINT*. The order of the keypoints in this array is implementation dependent.
:param: [out] num_corners [optional] The total number of detected corners in image. Use a VX_TYPE_SIZE scalar.
:ingroup: group_vision_function_fast
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:         An error occurred. See *vx_status_e*.
    '''
    return lib.vxuFastCorners(context, input, strength_thresh, nonmax_suppression, corners, num_corners)
    
def OpticalFlowPyrLK(context, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension):
    '''
:brief: [Immediate] Computes an optical flow on two images.
:param: [in] context The reference to the overall context.
:param: [in] old_images Input of first (old) image pyramid in *VX_DF_IMAGE_U8*.
:param: [in] new_images Input of destination (new) image pyramid in *VX_DF_IMAGE_U8*
:param: [in] old_points an array of key points in a vx_array of *VX_TYPE_KEYPOINT* those key points are defined at
 the old_images high resolution pyramid
:param: [in] new_points_estimates an array of estimation on what is the output key points in a *vx_array* of
*VX_TYPE_KEYPOINT* those keypoints are defined at the new_images high resolution pyramid
:param: [out] new_points an output array of key points in a *vx_array* of *VX_TYPE_KEYPOINT* those key points are
 defined at the new_images high resolution pyramid
:param: [in] termination termination can be *VX_TERM_CRITERIA_ITERATIONS* or *VX_TERM_CRITERIA_EPSILON* or
*VX_TERM_CRITERIA_BOTH*
:param: [in] epsilon is the *vx_float32* error for terminating the algorithm
:param: [in] num_iterations is the number of iterations. Use a *VX_TYPE_UINT32* scalar.
:param: [in] use_initial_estimate Can be set to either *vx_false_e* or *vx_true_e*.
:param: [in] window_dimension The size of the window on which to perform the algorithm. See
 *VX_CONTEXT_OPTICAL_FLOW_MAX_WINDOW_DIMENSION*

:ingroup: group_vision_function_opticalflowpyrlk
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuOpticalFlowPyrLK(context, old_images, new_images, old_points, new_points_estimates, new_points, termination, epsilon, num_iterations, use_initial_estimate, window_dimension)
    
def MatchTemplate(context, src, templateImage, matchingMethod, output):
    '''
:brief: [Immediate]  The function compares an image template against overlapped image regions.
:details: The detailed equation to the matching can be found in *vx_comp_metric_e*.
The output of the template matching node is a comparison map as described in *vx_comp_metric_e*.
The Node have a limitation on the template image size (width*height). It should not be larger then 65535.
If the valid region of the template image is smaller than the entire template image, the result in the destination image is implementation-dependent.
:param: [in] context The reference to the overall context.
:param: [in] src The input image of type *VX_DF_IMAGE_U8*.
:param: [in] templateImage Searched template of type *VX_DF_IMAGE_U8*.
:param: [in] matchingMethod attribute specifying the comparison method *vx_comp_metric_e*. This function support only *VX_COMPARE_CCORR_NORM* and *VX_COMPARE_L2*.
:param: [out] output Map of comparison results. The output is an image of type *VX_DF_IMAGE_S16*
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
:ingroup: group_vision_function_match_template
    '''
    return lib.vxuMatchTemplate(context, src, templateImage, matchingMethod, output)
    
def LBP(context, _in, format, kernel_size, out):
    '''
:brief: [Immediate] The function extracts LBP image from an input image
:param: [in] context The reference to the overall context.
:param: [in] in		An input image in *vx_image*. Or :f:$ SrcImg:f:$ in the equations. the image is of type *VX_DF_IMAGE_U8*
:param: [in] format	A variation of LBP like original LBP and mLBP. see * vx_lbp_format_e *
:param: [in] kernel_size Kernel size. Only size of 3 and 5 are supported
:param: [out] out	An output image in *vx_image*.Or :f:$ DstImg:f:$ in the equations. the image is of type *VX_DF_IMAGE_U8*
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
:ingroup: group_vision_function_lbp
    '''
    return lib.vxuLBP(context, _in, format, kernel_size, out)
    
def HOGCells(context, input, cell_width, cell_height, num_bins, magnitudes, bins):
    '''
:brief: [Immediate] Performs cell calculations for the average gradient magnitude and gradient orientation histograms.
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
:param: [in] context The reference to the overall context.
:param: [in] input The input image of type *VX_DF_IMAGE_U8*.
:param: [in] cell_width The histogram cell width of type *VX_TYPE_INT32*.
:param: [in] cell_height The histogram cell height of type *VX_TYPE_INT32*.
:param: [in] num_bins  The histogram size of type *VX_TYPE_INT32*.
:param: [out] magnitudes The output average gradient magnitudes per cell of *vx_tensor* of type *VX_TYPE_INT16* of size :f:$ [floor(image_{width}/cell_{width}) ,floor(image_{height}/cell_{height}) ] :f:$.
:param: [out] bins       The output gradient orientation histograms per cell of *vx_tensor* of type *VX_TYPE_INT16* of size :f:$ [floor(image_{width}/cell_{width}) ,floor(image_{height}/cell_{height}), num_{bins}] :f:$.

:ingroup: group_vision_function_hog
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuHOGCells(context, input, cell_width, cell_height, num_bins, magnitudes, bins)
    
def HOGFeatures(context, input, magnitudes, bins, params, hog_param_size, features):
    '''
:brief: [Immediate]  Computes Histogram of Oriented Gradients features for the W1xW2 window in a sliding window fashion over the whole input image.
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
*  :f:[ (((block_{width}block_{height}) / (cell_{width}cell_{height}))num_{bins})] :f:]
See *vxCreateTensor* and *vxCreateVirtualTensor*.
The output tensor from this function may be very large.  For this reason, is it not recommended that this "immediate mode" version of the function be used.
The preferred method to perform this function is as graph node with a virtual tensor as the output.
:param: [in] context The reference to the overall context.
:param: [in] input The input image of type *VX_DF_IMAGE_U8*.
:param: [in] magnitudes The averge gradient magnitudes per cell of *vx_tensor* of type *VX_TYPE_INT16*. It is the output of *vxuHOGCells*.
:param: [in] bins       The gradient orientation histogram per cell of *vx_tensor* of type *VX_TYPE_INT16*. It is the output of *vxuHOGCells*.
:param: [in] params The parameters of type *vx_hog_t*.
:param: [in] hog_param_size Size of *vx_hog_t* in bytes.
:param: [out] features The output HOG features of *vx_tensor* of type *VX_TYPE_INT16*.

:ingroup: group_vision_function_hog
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuHOGFeatures(context, input, magnitudes, bins, params, hog_param_size, features)
    
def HoughLinesP(context, input, params, lines_array, num_lines):
    '''
:brief: [Immediate] Finds the Probabilistic Hough Lines detected in the input binary image, each line is stored in the output array as a set of points (x1, y1, x2, y2) .
:details: Some implementations of the algorithm may have a random or non-deterministic element. If the target application is in a safety-critical environment this
should be borne in mind and steps taken in the implementation, the application or both to achieve the level of determinism required by the system design.
:param: [in] context The reference to the overall context.
:param: [in] input A single channel binary source image of type *VX_DF_IMAGE_U8* or *VX_DF_IMAGE_U1*.
:param: [in] params parameters of the struct *vx_hough_lines_p_t*
:param: [out] lines_array lines_array contains array of lines, see *vx_line2d_t* The order of lines in implementation dependent
:param: [out] num_lines [optional] The total number of detected lines in image. Use a VX_TYPE_SIZE scalar
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
:ingroup: group_vision_function_hough_lines_p
    '''
    return lib.vxuHoughLinesP(context, input, params, lines_array, num_lines)
    
def Remap(context, input, table, policy, output):
    '''
:brief: [Immediate] Remaps an output image from an input image.
:param: [in] context The reference to the overall context.
:param: [in] input The input *VX_DF_IMAGE_U8* image.
:param: [in] table The remap table object.
:param: [in] policy The interpolation policy from vx_interpolation_type_e.
VX_INTERPOLATION_AREA is not supported.
:param: [out] output The output *VX_DF_IMAGE_U8* image.
:return: A *vx_status_e* enumeration.
:ingroup: group_vision_function_remap
    '''
    return lib.vxuRemap(context, input, table, policy, output)
    
def BilateralFilter(context, src, diameter, sigmaSpace, sigmaValues, dst):
    '''
:brief: [Immediate] The function applies bilateral filtering to the input tensor.
* :param: [in] context The reference to the overall context.
* :param: [in] src The input data a *vx_tensor*. maximum 3 dimension and minimum 2. The tensor is of type *VX_TYPE_UINT8* or *VX_TYPE_INT16*.
* dimensions are [radiometric ,width,height] or [width,height]
* :param: [in] diameter of each pixel neighbourhood that is used during filtering. Values of diameter must be odd. Bigger then 3 and smaller then 10.
* :param: [in] sigmaValues Filter sigma in the radiometric space. Supported values are bigger then 0 and smaller or equal 20.
* :param: [in] sigmaSpace Filter sigma in the spatial space. Supported values are bigger then 0 and smaller or equal 20.
* :param: [out] dst The output data a *vx_tensor*,Of type *VX_TYPE_UINT8* or *VX_TYPE_INT16*. And must be the same type and size of the input.
* :note: The border modes
*  *VX_NODE_BORDER* value
*  *VX_BORDER_REPLICATE* and *VX_BORDER_CONSTANT* are supported.
* :return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
* :ingroup: group_vision_function_bilateral_filter
*/
    '''
    return lib.vxuBilateralFilter(context, src, diameter, sigmaSpace, sigmaValues, dst)
    
def TensorMultiply(context, input1, input2, scale, overflow_policy, rounding_policy, output):
    '''
:brief: [Immediate] Performs element wise multiplications on element values in the input tensor data with a scale.
:param: [in] context The reference to the overall context.
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
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTensorMultiply(context, input1, input2, scale, overflow_policy, rounding_policy, output)
    
def TensorAdd(context, input1, input2, policy, output):
    '''
:brief: [Immediate] Performs arithmetic addition on element values in the input tensor data.
:param: [in] context The reference to the overall context.
:param: [in] input1 Input tensor data.  Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [in] input2 Input tensor data. The dimensions and sizes of input2 match those of input1, unless the vx_tensor of one or more dimensions in input2 is 1.
In this case, those dimensions are treated as if this tensor was expanded to match the size of the corresponding dimension of input1,
and data was duplicated on all terms in that dimension. After this expansion, the dimensions will be equal.
The data type must match the data type of Input1.
:param: [in] policy A *vx_convert_policy_e* enumeration.
:param: [out] output The output tensor data with the same dimensions as the input tensor data.
:ingroup: group_vision_function_tensor_add
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTensorAdd(context, input1, input2, policy, output)
    
def TensorSubtract(context, input1, input2, policy, output):
    '''
:brief: [Immediate] Performs arithmetic subtraction on element values in the input tensor data.
:param: [in] context The reference to the overall context.
:param: [in] input1 Input tensor data.  Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [in] input2 Input tensor data. The dimensions and sizes of input2 match those of input1, unless the vx_tensor of one or more dimensions in input2 is 1.
In this case, those dimensions are treated as if this tensor was expanded to match the size of the corresponding dimension of input1,
and data was duplicated on all terms in that dimension. After this expansion, the dimensions will be equal.
The data type must match the data type of Input1.
:param: [in] policy A *vx_convert_policy_e* enumeration.
:param: [out] output The output tensor data with the same dimensions as the input tensor data.
:ingroup: group_vision_function_tensor_subtract
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTensorSubtract(context, input1, input2, policy, output)
    
def TensorTableLookup(context, input1, lut, output):
    '''
:brief: [Immediate] Performs LUT on element values in the input tensor data.
:param: [in] context The reference to the overall context.
:param: [in] input1 Input tensor data. Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8*, with fixed_point_position 0.
:param: [in] lut The look-up table to use, of type *vx_lut*.
The elements of input1 are treated as unsigned integers to determine an index into the look-up table.
The data type of the items in the look-up table must match that of the output tensor.
:param: [out] output The output tensor data with the same dimensions as the input tensor data.
:ingroup: group_vision_function_tensor_tablelookup
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTensorTableLookup(context, input1, lut, output)
    
def TensorTranspose(context, input, output, dimension1, dimension2):
    '''
:brief: [Immediate] Performs transpose on the input tensor.
The tensor is transposed according to a specified 2 indexes in the tensor (0-based indexing)
:param: [in] context The reference to the overall context.
:param: [in] input Input tensor data, Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [out] output output tensor data,
:param: [in] dimension1 Dimension index that is transposed with dim 2.
:param: [in] dimension2 Dimension index that is transposed with dim 1.
:ingroup: group_vision_function_tensor_transpose
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTensorTranspose(context, input, output, dimension1, dimension2)
    
def TensorConvertDepth(context, input, policy, norm, offset, output):
    '''
:brief: [Immediate] Performs a bit-depth conversion.
:param: [in] context The reference to the overall context.
:param: [in] input The input tensor. Implementations must support input tensor data type *VX_TYPE_INT16* with fixed_point_position 8,
and tensor data types *VX_TYPE_UINT8* and *VX_TYPE_INT8*, with fixed_point_position 0.
:param: [in] policy A *VX_TYPE_ENUM* of the *vx_convert_policy_e* enumeration.
:param: [in] norm A scalar containing a *VX_TYPE_FLOAT32* of the normalization value.
:param: [in] offset A scalar containing a *VX_TYPE_FLOAT32* of the offset value subtracted before normalization.
:param: [out] output The output tensor. Implementations must support input tensor data type *VX_TYPE_INT16*. with fixed_point_position 8.
And *VX_TYPE_UINT8* with fixed_point_position 0.
:ingroup: group_vision_function_tensor_convert_depth
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTensorConvertDepth(context, input, policy, norm, offset, output)
    
def TensorMatrixMultiply(context, input1, input2, input3, matrix_multiply_params, output):
    '''
:brief: [Immediate] Performs a generalized matrix multiplication.
:param: [in] context The reference to the overall context.
:param: [in] input1 The first input 2D tensor of type *VX_TYPE_INT16* with fixed_point_pos 8, or tensor data types *VX_TYPE_UINT8* or *VX_TYPE_INT8*, with fixed_point_pos 0.
:param: [in] input2 The second 2D tensor. Must be in the same data type as input1.
:param: [in] input3 The third 2D tensor. Must be in the same data type as input1. [optional].
:param: [in] matrix_multiply_params Matrix multiply parameters, see *vx_tensor_matrix_multiply_params_t *.
:param: [out] output The output 2D tensor. Must be in the same data type as input1. Output dimension must agree the formula in the description.
:ingroup: group_vision_function_tensor_matrix_multiply
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
    '''
    return lib.vxuTensorMatrixMultiply(context, input1, input2, input3, matrix_multiply_params, output)
    
def Copy(context, input, output):
    '''
:brief: [Immediate] Copy data from one object to another.
:param: [in] context The reference to the overall context.
:param: [in] input The input data object.
:param: [out] output The output data object.
:return: A *vx_status_e* enumeration.
:retval: VX_SUCCESS Success
:retval:An error occurred. See *vx_status_e*.
:ingroup: group_vision_function_copy
    '''
    return lib.vxuCopy(context, input, output)
    