import os
import turtle
import xml.etree.ElementTree as ET
from svg.path import parse_path

class Hendry:
    def __init__(self, svg_file=None, x_offset=0, y_offset=0):
        """
        Initializes the turtle screen and loads the default SVG if no file is provided.

        :param svg_file: Optional path to an SVG file. If None, uses the default.
        :param x_offset: Optional additional x offset.
        :param y_offset: Optional additional y offset.
        """
        # If no file is provided, use the default one inside the package
        if svg_file is None:
            svg_file = os.path.join(os.path.dirname(__file__), "assets", "my_image.svg")

        self.svg_file = svg_file
        self.x_offset = x_offset
        self.y_offset = y_offset

        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        # Update the screen after every move (change this value if you need fewer updates)
        self.screen.tracer(1)

        self.pen = turtle.Turtle()
        self.pen.shape("arrow")
        # Lower the speed to slow down the drawing (adjust as needed)
        self.pen.speed(2)
        self.pen.width(2)

        self.load_svg()

    def load_svg(self):
        """Loads the SVG file and prepares for drawing."""
        try:
            tree = ET.parse(self.svg_file)
            self.root = tree.getroot()
        except Exception as e:
            print("Error loading SVG file:", e)
            self.root = None
            return

        viewBox = self.root.get("viewBox")
        if viewBox:
            parts = viewBox.split()
            self.vb_x, self.vb_y, self.vb_width, self.vb_height = map(float, parts)
        else:
            self.vb_x = 0
            self.vb_y = 0
            self.vb_width = float(self.root.get("width", "800"))
            self.vb_height = float(self.root.get("height", "600"))

        sw = self.screen.window_width()
        sh = self.screen.window_height()
        self.scale = min(sw / self.vb_width, sh / self.vb_height)

    def transform(self, x, y):
        """Transforms SVG coordinates to turtle screen coordinates."""
        new_x = (x - self.vb_x) * self.scale - (self.vb_width * self.scale) / 2 + self.x_offset
        new_y = (self.vb_height * self.scale) / 2 - (y - self.vb_y) * self.scale + self.y_offset
        return new_x, new_y

    def draw_path(self, d, color="#000000", thickness=2):
        """Draws an SVG path with turtle.
        
        In this version, the pen is never lifted so that every move is drawn,
        including the movement from the end of one segment to the start of the next.
        """
        try:
            path = parse_path(d)
        except Exception as e:
            print("Error parsing path:", e)
            return

        self.pen.color(color)
        self.pen.width(thickness)

        for segment in path:
            seg_length = segment.length(error=1e-2)
            steps = max(int(seg_length / 2), 10)
            for i in range(steps + 1):
                pt = segment.point(i / steps)
                new_x, new_y = self.transform(pt.real, pt.imag)
                self.pen.goto(new_x, new_y)

    def draw(self):
        """Draws the default or user-provided SVG."""
        if self.root is None:
            print("SVG file not loaded.")
            return

        # Iterate through all SVG path elements in the file.
        for path_elem in self.root.findall('.//{http://www.w3.org/2000/svg}path'):
            d = path_elem.get('d')
            fill = path_elem.get('fill', "#000000")
            self.draw_path(d, color=fill, thickness=2)

        turtle.done()

# Example usage when running this module directly.
if __name__ == "__main__":
    drawer = Hendry()  # No need to provide an SVG file if the default is acceptable
    drawer.draw()
