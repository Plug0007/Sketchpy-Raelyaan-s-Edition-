import os
import turtle
import xml.etree.ElementTree as ET
from svg.path import parse_path

class Hendry:
    def __init__(self, svg_file=None, x_offset=0, y_offset=0):
        """
        Initializes the turtle screen and loads the default SVG if no file is provided.
        """
        # Use the default SVG file if none is provided.
        if svg_file is None:
            svg_file = os.path.join(os.path.dirname(__file__), "assets", "my_image.svg")
        self.svg_file = svg_file
        self.x_offset = x_offset
        self.y_offset = y_offset

        self.screen = turtle.Screen()
        self.screen.setup(width=800, height=600)
        # Update the screen every 10 turtle moves for a fast yet animated drawing.
        self.screen.tracer(10)

        self.pen = turtle.Turtle()
        self.pen.hideturtle()  # Hide the turtle for a cleaner drawing
        self.pen.speed(10)     # Maximum animated speed (fast but not instant)
        self.pen.width(2)

        self.load_svg()

    def load_svg(self):
        """Loads the SVG file and sets up the viewBox and scaling."""
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
        """
        Transforms SVG coordinates to turtle screen coordinates.
        """
        new_x = (x - self.vb_x) * self.scale - (self.vb_width * self.scale) / 2 + self.x_offset
        new_y = (self.vb_height * self.scale) / 2 - (y - self.vb_y) * self.scale + self.y_offset
        return new_x, new_y

    def draw_path(self, d, fill_color="#000000", thickness=2):
        """
        Draws an SVG path using turtle.
        
        - Lifts the pen before moving to the start point to avoid connecting lines.
        - Uses fewer interpolation steps (for faster drawing) but still animates.
        - If a fill color is specified (and not "none"), fills the drawn shape.
        """
        try:
            path = parse_path(d)
        except Exception as e:
            print("Error parsing path:", e)
            return

        if not path:
            return

        # Move to the starting point of the first segment.
        pt_start = path[0].point(0)
        start_x, start_y = self.transform(pt_start.real, pt_start.imag)
        self.pen.penup()
        self.pen.goto(start_x, start_y)
        self.pen.pendown()

        self.pen.width(thickness)
        self.pen.pencolor(fill_color)

        if fill_color.lower() != "none":
            self.pen.fillcolor(fill_color)
            self.pen.begin_fill()

        # Draw each segment with fewer steps for speed.
        for segment in path:
            seg_length = segment.length(error=1e-2)
            steps = max(int(seg_length / 10), 5)  # Reduced steps for faster drawing
            for i in range(1, steps + 1):
                pt = segment.point(i / steps)
                new_x, new_y = self.transform(pt.real, pt.imag)
                self.pen.goto(new_x, new_y)

        # Ensure the shape is closed
        self.pen.goto(start_x, start_y)
        if fill_color.lower() != "none":
            self.pen.end_fill()

    def draw(self):
        """Draws all SVG path elements from the file."""
        if self.root is None:
            print("SVG file not loaded.")
            return

        for path_elem in self.root.findall('.//{http://www.w3.org/2000/svg}path'):
            d = path_elem.get('d')
            # Use the SVG fill color if provided; otherwise, default to black.
            fill = path_elem.get('fill', "#000000")
            self.draw_path(d, fill_color=fill, thickness=2)

        self.screen.update()  # Final screen update
        turtle.done()

# Example usage:
if __name__ == "__main__":
    drawer = Hendry()  # Uses the default SVG file
    drawer.draw()
