from setuptools import setup, find_packages,  Extension
import codecs
import os




VERSION = '0.3.3'
DESCRIPTION = 'sketchpy'
LONG_DESCRIPTION = """ 
Sketchpy (Raelyaan’s Edition)

Sketchpy (Raelyaan’s Edition) is a customized Python library for creating sketches and drawings programmatically. Inspired by the original Sketchpy project, this edition introduces enhancements, optimizations, and personal touches by Raelyaan. With Sketchpy, you can transform images into line art, silhouettes, or pencil-style drawings—all through the convenience of Python’s turtle graphics module.

Overview: This library provides an intuitive API that allows you to generate a variety of sketch effects with minimal code. By leveraging the turtle module, Sketchpy (Raelyaan’s Edition) opens a window where your drawings come to life, stroke by stroke. Whether you’re an experienced Python developer or a newcomer curious about graphical programming, Sketchpy offers a fun, interactive way to explore creative coding.

Key Features:

Straightforward Setup: Installation is quick, and getting started is as simple as importing the library and calling a few functions.
Image Tracing: Convert your favorite photos into line drawings or silhouettes by adjusting threshold and resolution settings.
Turtle Graphics: Watch each stroke appear in real time, allowing for an engaging and visually appealing experience.
Extensible Codebase: Thanks to Python’s flexibility, you can integrate Sketchpy’s drawing capabilities into larger applications or modify it to suit your needs.
Raelyaan’s Enhancements: Additional improvements in stability, performance, and user-friendliness ensure a smoother experience for all users.
Installation: Use pip to install Sketchpy (Raelyaan’s Edition). If you plan to publish this on PyPI, the command might look like: pip install sketchpy-raelyaan Otherwise, if you’re installing locally or from a repository, make sure to include any dependencies in your environment, such as OpenCV (for advanced image processing) or Tkinter (for the turtle module, if needed on certain operating systems).

Usage Example:

Import the library: from sketchpy3 import canvas
Create a tracing object from an image: obj = canvas.trace_from_image("path_to_your_image.jpg")
Draw the sketch: obj.draw() These steps will open a new window where turtle graphics render your image as a line drawing.
Community and Contributions: Sketchpy (Raelyaan’s Edition) is distributed under the permissive MIT License, allowing anyone to use, modify, and redistribute the code. Community contributions are encouraged—whether through bug reports, feature requests, or pull requests. If you find a way to improve performance or add a new feature, feel free to share your work.

Credits:

Original Sketchpy Authors: Provided the foundation for this library.
Raelyaan: Enhanced, maintained, and refined this custom edition.
Open-Source Community: Continues to support and contribute to the library’s growth.
License (MIT): This project is released under the MIT License, which allows free usage, modification, and distribution of the software. Users must retain the original copyright and license notice in all copies or significant portions of the software.

Conclusion: Sketchpy (Raelyaan’s Edition) offers a playful yet powerful toolkit for anyone interested in creating programmatic art. By merging the simplicity of Python with the dynamism of turtle graphics, it delivers an accessible entry point into both coding and digital illustration. Feel free to experiment, customize, and share your creations, all while crediting the community that made it possible. Happy sketching!
"""
# Setting up
setup(
    name="sketchpy",
    version=VERSION,
    author="Mr Mystery",
    author_email="sriramanand23@gmail.com",
    maintainer="Raelyaan (Aadil Asif Badhra)",
    maintainer_email="aadilbadhra@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    package_data={"sketchpy": ["files/*", "assets/*.svg"]}
    include_package_data=True,
    install_requires=[
        'opencv-python',
        'wheel',
        'Pillow',
        'svg.path',
        'svgpathtools',
        'tqdm',
        'requests',
        'geocoder',
        'geopy',
        'torch',
        'numpy'
    ],
    keywords=[
        'python', 'sketch', 'drawing', 'animation',
        'code hub', 'pencil sketch', 'painting',
        'sketchpy', 'draw', 'sketching'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
) 
