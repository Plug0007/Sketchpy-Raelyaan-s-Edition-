import cv2
import turtle
import sketchpy as custom  # Ensure your Sketchpy version supports this import

class MySketch:
    def __init__(self, image_path="your_image.jpg", ascii_width=100, font_size=16):
        """
        Initialize with the image path, desired ASCII art width (in characters),
        and the font size for Turtle rendering.
        """
        self.image_path = image_path
        self.ascii_width = ascii_width
        self.font_size = font_size

    def image_to_color_ascii(self):
        """
        Convert the image to colored ASCII art.
        Returns a 2D list (list of rows) where each element is a tuple (char, color),
        with `color` as an (R, G, B) tuple.
        """
        # Load the image in color (BGR format)
        img = cv2.imread(self.image_path, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError(f"Image not found: {self.image_path}")

        height, width, _ = img.shape
        aspect_ratio = height / width
        new_width = self.ascii_width
        # The multiplier (0.5) adjusts for character aspect ratio in monospace fonts.
        new_height = int(aspect_ratio * new_width * 0.5)
        resized_img = cv2.resize(img, (new_width, new_height))

        # Define ASCII characters from dark to light.
        ascii_chars = "@%#*+=-:. "
        ascii_data = []

        # Process each pixel in the resized image.
        for row in resized_img:
            row_data = []
            for pixel in row:
                # Convert BGR to RGB.
                B, G, R = pixel
                # Compute brightness using standard luminance conversion.
                brightness = 0.299 * R + 0.587 * G + 0.114 * B
                # Map brightness to an ASCII character.
                index = int(brightness / 255 * (len(ascii_chars) - 1))
                char = ascii_chars[index]
                color = (R, G, B)  # Now in RGB order.
                row_data.append((char, color))
            ascii_data.append(row_data)

        return ascii_data

    def draw(self):
        """
        Use Sketchpy's custom function to create a sketch from the image.
        """
        sketch_obj = custom.sketch_from_image(self.image_path)
        sketch_obj.draw()

    def draw_color_ascii_turtle(self):
        """
        Draw the colored ASCII art in a Turtle window.
        Each ASCII character is drawn in the color sampled from the image.
        The window has a white background.
        """
        # Generate the colored ASCII art data.
        ascii_data = self.image_to_color_ascii()  # 2D list: each element is (char, color)
        rows = len(ascii_data)
        cols = self.ascii_width

        # Set Turtle to use 0-255 color range.
        turtle.colormode(255)

        # Estimate character dimensions based on font size.
        char_width = int(self.font_size * 0.6)
        char_height = int(self.font_size * 1.2)
        margin = 20

        # Calculate the window size.
        window_width = cols * char_width + margin
        window_height = rows * char_height + margin

        # Set up the Turtle screen with a white background.
        screen = turtle.Screen()
        screen.bgcolor("white")
        screen.setup(width=window_width, height=window_height)

        # Create a Turtle for drawing text.
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)
        t.penup()

        # Starting position: top-left of the drawing area.
        x_start = -window_width // 2 + margin // 2
        y_start = window_height // 2 - char_height

        font_settings = ("Courier", self.font_size, "normal")

        # Draw each ASCII character individually with its sampled color.
        for row in ascii_data:
            x = x_start
            for (char, color) in row:
                t.goto(x, y_start)
                t.color(color)  # Set pen color to the sampled RGB value.
                t.write(char, font=font_settings, align="left")
                x += char_width
            y_start -= char_height

        turtle.done()
