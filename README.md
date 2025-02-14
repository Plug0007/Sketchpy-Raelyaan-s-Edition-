# Sketchpy (Raelyaan’s Edition)

**Sketchpy (Raelyaan’s Edition)** is a customized Python library for creating sketches and drawings programmatically. Built upon the original Sketchpy project by Mr Mystery, this edition includes additional optimizations and personal enhancements contributed by Raelyaan. It leverages Python’s built-in `turtle` module to convert images into engaging line art and sketches.

---

## Table of Contents

1. [Introduction](#introduction)  
2. [Installation](#installation)  
   - [Git Clone Installation](#git-clone-installation)  
   - [PyPI Installation (Hypothetical)](#pypi-installation-hypothetical)  
3. [Usage](#usage)  
   - [Tracing from an Image](#tracing-from-an-image)  
   - [Drawing from an SVG File](#drawing-from-an-svg-file)  
   - [Converting an Image to SVG Format](#converting-an-image-to-svg-format)  
   - [Sketching from a .npy File](#sketching-from-a-npy-file)  
   - [Library Examples](#library-examples)  
4. [Uninstallation](#uninstallation)  
5. [Credits and Thanks](#credits-and-thanks)  
6. [License (MIT)](#license-mit)

---

## Introduction

Sketchpy (Raelyaan’s Edition) simplifies programmatic drawing by converting images into sketches. Whether you’re tracing from an image, converting images to SVG for further manipulation, or using pre-saved sketch data, this library provides an interactive and fun way to create art with code.

---

## Installation

### Git Clone Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-.git
Change to the Project Directory:

bash
Copy
Edit
cd Sketchpy-Raelyaan-s-Edition-
Install the Package:

bash
Copy
Edit
pip install .
PyPI Installation (Hypothetical)
If available on PyPI, you can install via:

bash
Copy
Edit
pip install sketchpy
Usage
Tracing from an Image
Convert an image into a sketch using:

python
Copy
Edit
from sketchpy import canvas

# Trace sketch from an image
obj = canvas.trace_from_image(r"path_to_image.jpg")
obj.draw()
Drawing from an SVG File
Sketch directly from an SVG file (ensure your SVG meets the required format):

python
Copy
Edit
from sketchpy import canvas

if __name__ == "__main__":
    obj = canvas.color_sketch_from_svg(r"path_to_image.svg")
    obj.draw()
Converting an Image to SVG Format
Convert your image to a compatible SVG format using the built-in converter.
Note: You may need to complete a one-time verification in Brave browser (approx. 20 seconds).

python
Copy
Edit
from sketchpy import canvas

# Convert image to SVG format
canvas.get_svg(r"path_to_image.jpg")
Sketching from a .npy File
After generating an SVG, save the sketch data as a .npy file for faster subsequent loading:

python
Copy
Edit
from sketchpy import canvas

# Draw sketch from saved .npy data file
obj = canvas.color_sketch_from_svg(None)
obj.draw(file='data.npy')
Library Examples
Sketch famous personalities directly using pre-built library functions:

Drawing Robert Downey Jr.:

python
Copy
Edit
from sketchpy import library as lib

obj = lib.rdj()
obj.draw()
Drawing Tom Holland:

python
Copy
Edit
from sketchpy import library

myObject = library.tom_holland()
myObject.draw()
Uninstallation
To remove Sketchpy (Raelyaan’s Edition) from your system, follow these steps:

Uninstall via pip:

bash
Copy
Edit
pip uninstall sketchpy
Remove the Cloned Directory (if installed via Git Clone):

On Windows: Open Command Prompt and run:

bash
Copy
Edit
rmdir /S /Q "C:\path\to\Sketchpy-Raelyaan-s-Edition-"
On macOS/Linux: Open Terminal and run:

bash
Copy
Edit
rm -rf /path/to/Sketchpy-Raelyaan-s-Edition-
These steps ensure that both the package and its source directory are removed from your system.

Credits and Thanks
Original Author: Mr Mystery (sriramanand23@gmail.com)
Many thanks to Mr Mystery for creating the initial Sketchpy library under the MIT License.

Custom Edition: Raelyaan
Responsible for enhancements, optimizations, and additional features in this edition.

Maintaining Author: Aadil Asif Badhra (aadilbadhra@gmail.com)
Overseeing ongoing updates, documentation, and community support.

License (MIT)
sql
Copy
Edit
MIT License

Copyright (c) 2022 Sriram

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
