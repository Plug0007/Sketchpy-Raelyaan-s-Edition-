"""
sketchpy_complement.py

A more advanced Python module that enhances the `sketchpy` library with additional
image-processing and sketching features, including:

1. Pencil Sketch (B/W)
2. Color Sketch
3. ASCII Art (B/W)
4. Colorized ASCII Art
5. Cartoonify
6. Watercolor Effect
7. Detail Enhancement
8. Canny Edge Detection
9. Negative Effect
10. Direct integration with `sketchpy` for console-based drawing

Dependencies:
    pip install opencv-python pillow numpy sketchpy
"""

import cv2
import numpy as np
from PIL import Image
from sketchpy import canvas


class SketchpyComplement:
    def __init__(self, image_path: str):
        """
        Initializes the SketchpyComplement object.

        :param image_path: Path to the input image file.
        """
        self.image_path = image_path
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if self.image is None:
            raise ValueError(f"Could not load image from path: {image_path}")

    # --------------------------------------------------------
    # 1. Pencil Sketch (B/W)
    # --------------------------------------------------------
    def pencil_sketch(self, save_path: str = 'pencil_sketch.png') -> str:
        """
        Generates a traditional black-and-white pencil sketch from the image
        using a manual blending approach.

        :param save_path: File path to save the pencil sketch output.
        :return: The path to the saved pencil sketch image.
        """
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        inverted = cv2.bitwise_not(gray)
        blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
        inverted_blurred = cv2.bitwise_not(blurred)
        sketch = cv2.divide(gray, inverted_blurred, scale=256.0)
        cv2.imwrite(save_path, sketch)
        return save_path

    # --------------------------------------------------------
    # 2. Color Sketch
    # --------------------------------------------------------
    def color_sketch(self, save_path: str = 'color_sketch.png') -> str:
        """
        Generates a color pencil sketch from the image using OpenCV's built-in pencilSketch.

        :param save_path: File path to save the color sketch output.
        :return: The path to the saved color sketch image.
        """
        # cv2.pencilSketch returns two images: grayscale sketch and color sketch
        _, color_output = cv2.pencilSketch(
            self.image, sigma_s=60, sigma_r=0.07, shade_factor=0.05
        )
        cv2.imwrite(save_path, color_output)
        return save_path

    # --------------------------------------------------------
    # 3. ASCII Art (B/W)
    # --------------------------------------------------------
    def ascii_art(self, output_width: int = 80) -> str:
        """
        Converts the image into grayscale ASCII art.

        :param output_width: The desired width of the ASCII art in characters.
        :return: A string containing the ASCII art representation of the image.
        """
        image_pil = Image.open(self.image_path).convert('L')
        width, height = image_pil.size

        # Maintain aspect ratio
        aspect_ratio = height / width
        new_height = int(output_width * aspect_ratio * 0.5)
        resized_image = image_pil.resize((output_width, new_height))

        # ASCII character set from dark to light
        ascii_chars = "@%#*+=-:. "

        # Convert each pixel to an ASCII character
        pixels = np.array(resized_image)
        rows = []
        for row in pixels:
            row_chars = [ascii_chars[pixel // 25] for pixel in row]
            rows.append("".join(row_chars))
        ascii_str = "\n".join(rows)

        return ascii_str

    # --------------------------------------------------------
    # 4. Colorized ASCII Art
    # --------------------------------------------------------
    def ascii_art_color(self, output_width: int = 80) -> str:
        """
        Converts the image into colorized ASCII art using ANSI escape codes.
        This will display color in terminals that support ANSI colors.

        :param output_width: The desired width of the ASCII art in characters.
        :return: A string containing the colorized ASCII art representation.
        """
        image_pil = Image.open(self.image_path).convert('RGB')
        width, height = image_pil.size

        # Maintain aspect ratio
        aspect_ratio = height / width
        new_height = int(output_width * aspect_ratio * 0.5)
        resized_image = image_pil.resize((output_width, new_height))

        # ASCII character set from dark to light
        ascii_chars = "@%#*+=-:. "

        # Convert each pixel to an ASCII character, plus an ANSI color code
        pixels = np.array(resized_image)
        rows = []
        for row in pixels:
            row_str = []
            for (r, g, b) in row:
                # Map brightness to ASCII char
                brightness = int((r + g + b) / 3)
                char = ascii_chars[brightness // 25]

                # ANSI 24-bit color: \\x1b[38;2;<r>;<g>;<b>m
                # Then we reset color at the end with \\x1b[0m
                row_str.append(f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m")
            rows.append("".join(row_str))
        return "\n".join(rows)

    # --------------------------------------------------------
    # 5. Cartoonify
    # --------------------------------------------------------
    def cartoonify(self, save_path: str = 'cartoonified.png') -> str:
        """
        Applies a cartoon effect to the image.

        :param save_path: File path to save the cartoonified output.
        :return: The path to the saved cartoonified image.
        """
        # Convert to grayscale
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # Apply a median blur
        gray = cv2.medianBlur(gray, 7)
        # Use adaptive thresholding to create an edge mask
        edges = cv2.adaptiveThreshold(gray, 255,
                                      cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, 9, 9)
        # Bilateral filter to remove noise and keep color
        color = cv2.bilateralFilter(self.image, 9, 300, 300)
        # Combine edges with color
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        cv2.imwrite(save_path, cartoon)
        return save_path

    # --------------------------------------------------------
    # 6. Watercolor Effect
    # --------------------------------------------------------
    def watercolor(self, save_path: str = 'watercolor.png',
                   sigma_s: float = 60, sigma_r: float = 0.6) -> str:
        """
        Applies a watercolor-like stylization to the image using OpenCV.

        :param save_path: File path to save the watercolor output.
        :param sigma_s: Range between 0 to 200. Controls the size of the brush stroke.
        :param sigma_r: Range between 0 to 1. Controls the intensity of the effect.
        :return: The path to the saved watercolor-styled image.
        """
        stylized = cv2.stylization(self.image, sigma_s=sigma_s, sigma_r=sigma_r)
        cv2.imwrite(save_path, stylized)
        return save_path

    # --------------------------------------------------------
    # 7. Detail Enhancement
    # --------------------------------------------------------
    def detail_enhance(self, save_path: str = 'detail_enhanced.png',
                       sigma_s: float = 10, sigma_r: float = 0.15) -> str:
        """
        Enhances details in the image using OpenCV's detailEnhance function.

        :param save_path: File path to save the detail-enhanced output.
        :param sigma_s: Filter size, typically between 1 and 200.
        :param sigma_r: Range between 0 and 1. Larger means stronger smoothing.
        :return: The path to the saved detail-enhanced image.
        """
        enhanced = cv2.detailEnhance(self.image, sigma_s=sigma_s, sigma_r=sigma_r)
        cv2.imwrite(save_path, enhanced)
        return save_path

    # --------------------------------------------------------
    # 8. Canny Edge Detection
    # --------------------------------------------------------
    def canny_edges(self, threshold1: int = 100, threshold2: int = 200,
                    save_path: str = 'edges.png') -> str:
        """
        Performs Canny edge detection on the image.

        :param threshold1: First threshold for the hysteresis procedure.
        :param threshold2: Second threshold for the hysteresis procedure.
        :param save_path: File path to save the edge-detected output.
        :return: The path to the saved edges image.
        """
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, threshold1, threshold2)
        cv2.imwrite(save_path, edges)
        return save_path

    # --------------------------------------------------------
    # 9. Negative Effect
    # --------------------------------------------------------
    def negative(self, save_path: str = 'negative.png') -> str:
        """
        Creates a negative (inverted) version of the image.

        :param save_path: File path to save the negative output.
        :return: The path to the saved negative image.
        """
        negative_img = cv2.bitwise_not(self.image)
        cv2.imwrite(save_path, negative_img)
        return save_path

    # --------------------------------------------------------
    # 10. sketchpy Integration (Console Drawing)
    # --------------------------------------------------------
    def sketchpy_draw(self, threshold: int = 127):
        """
        Demonstrates integration with `sketchpy` by drawing the image
        in the console at a given threshold.

        :param threshold: Threshold value for converting the image to sketch lines.
        """
        c = canvas.sketchFromImage(self.image_path)
        c.draw(threshold=threshold)


# -------------------------------------------------------------------
# Example usage
# -------------------------------------------------------------------
if __name__ == '__main__':
    # Replace 'your_image.jpg' with the path to an actual image file
    image_file = 'your_image.jpg'
    enhancer = SketchpyComplement(image_file)

    # 1. Pencil Sketch
    pencil_path = enhancer.pencil_sketch()
    print(f"Pencil sketch saved at: {pencil_path}")

    # 2. Color Sketch
    color_path = enhancer.color_sketch()
    print(f"Color sketch saved at: {color_path}")

    # 3. ASCII Art (B/W)
    ascii_bw = enhancer.ascii_art(output_width=80)
    print("\nASCII Art (B/W):\n")
    print(ascii_bw)

    # 4. Colorized ASCII Art
    ascii_colored = enhancer.ascii_art_color(output_width=60)
    print("\nASCII Art (Color):\n")
    print(ascii_colored)

    # 5. Cartoonify
    cartoon_path = enhancer.cartoonify()
    print(f"\nCartoonified image saved at: {cartoon_path}")

    # 6. Watercolor Effect
    watercolor_path = enhancer.watercolor()
    print(f"Watercolor effect image saved at: {watercolor_path}")

    # 7. Detail Enhancement
    detail_path = enhancer.detail_enhance()
    print(f"Detail-enhanced image saved at: {detail_path}")

    # 8. Canny Edges
    edges_path = enhancer.canny_edges()
    print(f"Edges image saved at: {edges_path}")

    # 9. Negative Effect
    negative_path = enhancer.negative()
    print(f"Negative image saved at: {negative_path}")

    # 10. Draw in Console via sketchpy
    print("\nDrawing in console using sketchpy...\n")
    enhancer.sketchpy_draw(threshold=100)
