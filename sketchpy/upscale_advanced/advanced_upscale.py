#!/usr/bin/env python
"""
advanced_upscale.py

An advanced upscaling script and module that supports:
1. OpenCV interpolation (nearest, linear, cubic, lanczos)
2. Pillow resampling (nearest, bilinear, bicubic, lanczos)
3. Real-ESRGAN (AI-based super-resolution) [optional install]

Dependencies:
    pip install opencv-python pillow

For Real-ESRGAN (optional):
    pip install realesrgan

Usage (command line):
    python advanced_upscale.py <input> <output> --method opencv --scale 3 --interp lanczos

Usage (as a module):
    from advanced_upscale import advanced_upscale
    advanced_upscale("input.png", "output.png", method="pil", scale=2, interp="lanczos")
"""

import sys
import argparse
import cv2
import numpy as np
from PIL import Image

try:
    from realesrgan import RealESRGAN
    REAL_ESRGAN_AVAILABLE = True
except ImportError:
    REAL_ESRGAN_AVAILABLE = False

def advanced_upscale(input_path: str,
                     output_path: str,
                     method: str = "opencv",
                     scale: float = 2.0,
                     interp: str = "lanczos") -> None:
    """
    Upscales an image using one of several methods:
      - "opencv":    Uses OpenCV with chosen interpolation (nearest, linear, cubic, lanczos).
      - "pil":       Uses Pillow with chosen resampling (nearest, bilinear, bicubic, lanczos).
      - "realesrgan": Uses Real-ESRGAN for AI super-resolution (optional install).

    :param input_path:  Path to the input image.
    :param output_path: Path to save the upscaled image.
    :param method:      'opencv', 'pil', or 'realesrgan'.
    :param scale:       Scale factor (e.g., 2 = double size, 3 = triple).
    :param interp:      Interpolation/resampling method for OpenCV/Pillow. 
                       For OpenCV:  'nearest', 'linear', 'cubic', 'lanczos'
                       For Pillow:  'nearest', 'bilinear', 'bicubic', 'lanczos'
                       (Real-ESRGAN ignores 'interp', using a model-based approach)
    """
    # 1. Load the image
    image_cv = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if image_cv is None:
        raise FileNotFoundError(f"Could not load image from '{input_path}'")

    # 2. Choose method
    method = method.lower()
    if method == "opencv":
        _upscale_opencv(image_cv, output_path, scale, interp)
    elif method == "pil":
        _upscale_pil(image_cv, output_path, scale, interp)
    elif method == "realesrgan":
        if not REAL_ESRGAN_AVAILABLE:
            raise ImportError("RealESRGAN is not installed. Please run: pip install realesrgan")
        _upscale_realesrgan(image_cv, output_path, scale)
    else:
        raise ValueError(f"Unknown method '{method}'. Use 'opencv', 'pil', or 'realesrgan'.")

    print(f"[advanced_upscale] Upscaled image saved to: {output_path}")

def _upscale_opencv(image_cv, output_path, scale, interp):
    """
    Helper function for OpenCV-based upscaling.
    """
    interp_map = {
        'nearest': cv2.INTER_NEAREST,
        'linear': cv2.INTER_LINEAR,
        'cubic': cv2.INTER_CUBIC,
        'lanczos': cv2.INTER_LANCZOS4
    }
    chosen = interp_map.get(interp.lower(), cv2.INTER_LANCZOS4)

    h, w = image_cv.shape[:2]
    new_w = int(w * scale)
    new_h = int(h * scale)

    upscaled = cv2.resize(image_cv, (new_w, new_h), interpolation=chosen)
    success = cv2.imwrite(output_path, upscaled)
    if not success:
        raise IOError(f"Failed to save image to '{output_path}'")

def _upscale_pil(image_cv, output_path, scale, interp):
    """
    Helper function for Pillow-based upscaling.
    """
    # Convert OpenCV BGR to RGB
    pil_image = Image.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))

    # Map method strings to Pillow resampling filters
    interp_map = {
        'nearest': Image.Resampling.NEAREST,
        'bilinear': Image.Resampling.BILINEAR,
        'bicubic': Image.Resampling.BICUBIC,
        'lanczos': Image.Resampling.LANCZOS
    }
    chosen = interp_map.get(interp.lower(), Image.Resampling.LANCZOS)

    w, h = pil_image.size
    new_w = int(w * scale)
    new_h = int(h * scale)

    upscaled_pil = pil_image.resize((new_w, new_h), resample=chosen)
    upscaled_pil.save(output_path)

def _upscale_realesrgan(image_cv, output_path, scale):
    """
    Helper function for Real-ESRGAN-based upscaling (AI super-resolution).
    """
    # Convert to RGB
    pil_image = Image.fromarray(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))

    # Initialize RealESRGAN with a default model
    model = RealESRGAN("cuda", scale=scale)
    # For CPU-only usage (much slower), you can do:
    # model = RealESRGAN("cpu", scale=scale)

    model.load_weights("RealESRGAN_x4plus.pth", download=True)
    sr_image = model.predict(pil_image)
    sr_image.save(output_path)

def main():
    """
    CLI entry point:
      python advanced_upscale.py <input> <output> --method opencv --scale 3 --interp lanczos

    Example:
      python advanced_upscale.py my_image.png my_upscaled.png --method pil --scale 2 --interp bicubic
    """
    parser = argparse.ArgumentParser(
        description="Advanced image upscaling with OpenCV, Pillow, or Real-ESRGAN."
    )
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to save upscaled image")
    parser.add_argument("--method", default="opencv", choices=["opencv", "pil", "realesrgan"],
                        help="Upscaling method (opencv, pil, realesrgan). Default=opencv")
    parser.add_argument("--scale", type=float, default=2.0,
                        help="Upscale factor. Default=2.0 (2x)")
    parser.add_argument("--interp", default="lanczos",
                        help="Interpolation for OpenCV/PIL. "
                             "Possible: nearest, linear, cubic, bilinear, bicubic, lanczos. "
                             "Default=lanczos.")
    args = parser.parse_args()

    advanced_upscale(
        input_path=args.input,
        output_path=args.output,
        method=args.method,
        scale=args.scale,
        interp=args.interp
    )

if __name__ == "__main__":
    main()
