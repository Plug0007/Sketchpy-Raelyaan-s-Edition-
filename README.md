# Sketchpy (Raelyaan’s Edition)

**Sketchpy (Raelyaan’s Edition)** is a customized Python library for creating sketches and drawings programmatically. Built upon the original Sketchpy project by Mr Mystery, this edition includes additional optimizations and personal enhancements contributed by Raelyaan. It leverages Python’s built-in `turtle` module to convert images into engaging line art and sketches.

---

## Table of Contents

1. [Introduction](#introduction) 
2. [Installation](#installation)  
   - [Git Clone Installation](#git-clone-installation)    
3. [Usage](#usage)  
   - [Tracing from an Image](#tracing-from-an-image)  
   - [Drawing from an SVG File](#drawing-from-an-svg-file)   
   - [Sketching from a .npy File](#sketching-from-a-npy-file)
   - [ASCII Art from an Image](#ASCII_ART)  
   - [Library Examples](#library-examples)

4.[Version](#version)
   - [version 0.3.3](#version_0.3.3)
5. [Uninstallation](#uninstallation)  
6. [Credits and Thanks](#credits-and-thanks)  
7. [License (MIT)](#license-mit)

---

## Introduction

Sketchpy (Raelyaan’s Edition) simplifies programmatic drawing by converting images into sketches. Whether you’re tracing from an image, converting images to SVG for further manipulation, or using pre-saved sketch data, this library provides an interactive and fun way to create art with code.

---

## Installation

### Git Clone Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-.git
   ```
2. **Change to the Project Directory:**
      ```bash
   cd Sketchpy-Raelyaan-s-Edition-

   ```
3. **Install the Package:**
      ```bash
   pip install .


   ```
### Example vedio of Installation
<div align = "center">
   <img src = "https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-/blob/main/images/gif/insup4568.gif">
</div>



# Usage

## Tracing from an Image

**Convert an image into a sketch using:**
```python
from sketchpy import canvas

# Trace sketch from an image
obj = canvas.trace_from_image(r"path_to_image.jpg")
obj.draw()
```

### OUTPUT
<div align = "center">
   <img src = "https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-/blob/main/images/gif/3.gif">
</div>




## Drawing from an SVG File

**Sketch directly from an SVG file (ensure your SVG meets the required format):**
```python
from sketchpy import canvas

if __name__ == "__main__":
    obj = canvas.color_sketch_from_svg(r"path_to_image.svg")
    obj.draw()

```

## Sketching from a `.npy` File

**After generating an SVG, save the sketch data as a .npy file for faster subsequent loading:**
```python
from sketchpy import canvas

# Draw sketch from saved .npy data file
obj = canvas.color_sketch_from_svg(None)
obj.draw(file='data.npy')


```


# ASCII_ART
**Perameter:**
```perameter
image_path:
The file path to the source image (e.g., "your_image.jpg").

ascii_width:
The number of characters per line in the generated ASCII art (controls detail).

font_size:
The size of the font used for rendering ASCII art in the Turtle window.

verbose:
A boolean flag that, when set to True, prints version details and an ASCII art header at startup.
```
**Code:**
```python
from my_sketch import MySketch

# Initialize MySketch with your image and desired settings.
# Set verbose=True to display version details and an ASCII art header.
sketch = MySketch(image_path="your_image.jpg", ascii_width=100, font_size=16, verbose=True)

# Display colored ASCII art in a Turtle window.
sketch.draw_color_ascii_turtle()

# Optionally, you can generate a sketch using Sketchpy's built-in functionality:
# sketch.draw()
```
### OUTPUT
<div align = "center">
   <img src = "https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-/blob/main/images/gif/ascup4571.gif">
</div>





## Library Examples

**Sketch famous personalities directly using pre-built library functions:**

**Drawing Dr.APJ Abdul Kalam:**
```python
from sketchpy import library
obj = library.apj()
# Draw the sketch
obj.draw()
```
### OUTPUT
<div align = "center">
   <img src = "https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-/blob/main/images/gif/apjup4569.gif">
</div>

**Drawing `Indian Flag`:**
```python
from sketchpy import library
obj = library.flag()
# Draw the sketch
obj.draw()
```
### OUTPUT
<div align = "center">
    <img src = "https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-/blob/main/images/gif/indup4570.gif">
</div>

**Drawing Robert Downey Jr.:**
```python
from sketchpy import library as lib

obj = lib.rdj()
obj.draw()
```

### OUTPUT
<div align = "center">
   <img src = "https://user-images.githubusercontent.com/80098044/154792552-59c53805-35b9-46e0-be37-2c5dae0a87d1.gif">
</div>

**Drawing Tom Holland:**
```python
from sketchpy import library

myObject = library.tom_holland()
myObject.draw()
```

### OUTPUT
<div align = "center">
   <img src = "https://cdn-0.pythonistaplanet.com/wp-content/uploads/2022/05/image-5.png?ezimgfmt=ng:webp/ngcb19">
</div>

# Uninstallation
**To remove Sketchpy (Raelyaan’s Edition) from your system, follow these steps:**

1. ## Uninstall via pip:
```bash
pip uninstall sketchpy
```
2. ## Remove the Cloned Directory (if installed via Git Clone):
   **On Windows: Open Command Prompt and run:**
   ```bash
   rmdir /S /Q "Sketchpy-Raelyaan-s-Edition-"
   ```
   **On macOS/Linux: Open Terminal and run:**
   ```bash
   rm -rf /path/to/Sketchpy-Raelyaan-s-Edition-
   ```
   **These steps ensure that both the package and its source directory are removed from your system.**

  ### Example vedio of Uninstallation
<div align = "center">
   <img src = "https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-/blob/main/images/gif/delup4567.gif">
</div>

# version

### version_0.3.3

# MySketch Library

**Version: 0.3.3**  
*Creator: Raelyaan*

## Overview

MySketch converts images into colored ASCII art and sketches using Turtle graphics and Sketchpy. In this version, we've added enhanced colored ASCII rendering and Sketchpy integration.

## Key Parameters

- **`image_path`**:  
  The file path to the source image (e.g., `"your_image.jpg"`).

- **`ascii_width`**:  
  Number of characters per line in the ASCII art (controls detail).

- **`font_size`**:  
  The font size used in the Turtle window for rendering the art.

- **`verbose`**:  
  If set to `True`, prints version details and an ASCII art header at startup.

## New in Version 0.3.3

- **Sketchpy Integration:**  
  Generate a sketch of the image using Sketchpy with the `draw()` method.

- **Colored ASCII Art:**  
  Each ASCII character is rendered in a color sampled from the original image.

- **Enhanced Clarity Controls:**  
  Adjust `ascii_width` and `font_size` to improve output quality.

## Acknowledgments

- Built on top of [Sketchpy](https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-).
- Special thanks to the developers of OpenCV and the Python Turtle graphics module.

Enjoy creating beautiful ASCII art!




# Credits and Thanks
**Original Author: Mr Mystery (sriramanand23@gmail.com)
Many thanks to Mr Mystery for creating the initial Sketchpy library under the MIT License.**

**Custom Edition: Raelyaan
Responsible for enhancements, optimizations, and additional features in this edition.**

**Maintaining Author: Aadil Asif Badhra (aadilbadhra@gmail.com)
Overseeing ongoing updates, documentation, and community support.**

# License (MIT)
``` sql
MIT License

Copyright (c) 2022 Sriram
Copyright (c) 2025 Plug0007

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
   
