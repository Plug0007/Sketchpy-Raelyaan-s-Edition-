# Sketchpy-Raelyaan-s-Edition-

## Sketchpy (Raelyaan’s Edition)

- **Author (Original):** Mr Mystery (sriramanand23@gmail.com)  
- **Author (Custom Edition):** Raelyaan  
- **Maintaining Author:** Aadil Asif Badhra (aadilbadhra@gmail.com)

Sketchpy (Raelyaan’s Edition) is a customized Python library for creating sketches and drawings programmatically. It is based on the original Sketchpy project by Mr Mystery, who has graciously licensed the code under the MIT License. This edition includes additional optimizations and personal touches contributed by Raelyaan.

---

### TABLE OF CONTENTS

1. [Introduction](#introduction)  
2. [Installation](#installation)  
   - [Git Clone Installation](#git-clone-installation)  
   - [PyPI Installation (Hypothetical)](#pypi-installation-hypothetical)  
3. [Usage](#usage)  
4. [Credits and Thanks](#credits-and-thanks)  
5. [License (MIT)](#license-mit)

---

## Introduction

Sketchpy (Raelyaan’s Edition) allows users to convert images into line art or silhouettes using Python’s built-in `turtle` module. The goal is to simplify programmatic drawing tasks and provide a fun, interactive way to visualize images as sketches.

---

## Installation

### Git Clone Installation

```bash
# 1. Clone the repository
git clone https://github.com/Plug0007/Sketchpy-Raelyaan-s-Edition-.git

# 2. Change directory to the cloned folder
cd Sketchpy-Raelyaan-s-Edition-

# 3. Install the package
pip install .
```



### PyPI Installation (Hypothetical)

```bash
pip install sketchpy
```
*

---

## Usage

A quick example:

```python
from sketchpy import canvas

# Trace from an image
obj = canvas.trace_from_image(r"path_to_image.jpg")

# Draw the sketch
obj.draw()
```
##🔗🖇️Drawing From SVG file
You can sketch image uinsg the class color_sketch_from_svg, which takes the inpu in svg formate and then sketches it. Example Code:
```bash
from sketchpy import canvas

if __name__ == "__main__":
    obj = canvas.color_sketch_from_svg("Image Path")
    obj.draw()


```

##🔗Converting Image to SVG formate
Sketchpy requires specific type of SVG file formate to work properly, hence this version includes a standalone svg converter function with it use the follow code to convert you images to svg files
```
bash
    from sketchpy import canvas
    canvas.get_svg(IMG_PATH)
```

It takes the image from the IMG_PATH and converts it into an svg file
But to access this SVG converter you have to complete a shorturl, don't worry you need to do this only once a day
Use brave browser to complete it with ih 20 sec.
---
##Sketching form .npy file
Insted of waiting for the svg file to load, you can saved .npy file and use that for future use, use the following code to draw your image from saved data file
```
bash

from sketchpy import canvas
obj = canvas.color_sketch_from_svg(None)
obj.draw(file = 'data.npy')
```
###Library Example
Open your code editor and write the example Python code snippets given below. Run your code and see the magic by yourself.

##Drawing Robert Downey Jr. Using Python
```
bash

from sketchpy import library as lib
obj = lib.rdj()
obj.draw()
```
##Drawing Tom Holland Using Python
```
bash

from sketchpy import library
myObject = library.tom_holland()
myObject.draw()
```


### Credits and Thanks

- **Original Author:** Mr Mystery (sriramanand23@gmail.com)  
  Many thanks to Mr Mystery for creating the initial Sketchpy library and sharing it under the MIT License.

- **Custom Edition:** Raelyaan  
  Responsible for enhancements, performance tweaks, and additional features in this edition.

- **Maintaining Author:** Aadil Asif Badhra (aadilbadhra@gmail.com)  
  Overseeing ongoing updates, documentation, and support for Sketchpy (Raelyaan’s Edition).

---

## License (MIT)

Below is the full text of the original MIT License, which applies to this project:

```
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
```
