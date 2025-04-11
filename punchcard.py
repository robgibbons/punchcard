#!/usr/bin/env python3
import csv
import svgwrite
import cairosvg  # Added for PDF conversion

# Constants
GRID_WIDTH = 80  # Number of columns in the grid
GRID_HEIGHT = 12  # Number of rows in the grid
CELL_WIDTH_MM = 5.0 # Width of each cell in millimeters (adjust as needed)
CELL_HEIGHT_MM = 10.0  # Height of each cell in millimeters (adjust as needed)
KERF_MM = 0.254  # Thickness of the laser cut lines in millimeters (adjust as needed)
GRID_OFFSET_X_MM = 25.4  # Offset from the left in millimeters
GRID_OFFSET_Y_MM = 25.4  # Offset from the top in millimeters
CELL_SPACING_X_MM = 5.0  # Spacing between columns in millimeters
CELL_SPACING_Y_MM = 10.01  # Spacing between rows in millimeters

# Function to create an SVG file from CSV data
def create_svg(input_csv, output_svg):
    # Calculate the total canvas width and height in millimeters
    canvas_width_mm = (GRID_WIDTH * CELL_WIDTH_MM) + ((GRID_WIDTH - 1) * CELL_SPACING_X_MM) + (2 * GRID_OFFSET_X_MM)
    canvas_height_mm = (GRID_HEIGHT * CELL_HEIGHT_MM) + ((GRID_HEIGHT - 1) * CELL_SPACING_Y_MM) + (2 * GRID_OFFSET_Y_MM)

    print(f"GRID_WIDTH: {GRID_WIDTH}")
    print(f"GRID_HEIGHT: {GRID_HEIGHT}")
    print(f"CELL_WIDTH_MM: {CELL_WIDTH_MM}")
    print(f"CELL_HEIGHT_MM: {CELL_HEIGHT_MM}")
    print(f"KERF_MM: {KERF_MM}")
    print(f"GRID_OFFSET_X_MM: {GRID_OFFSET_X_MM}")
    print(f"GRID_OFFSET_Y_MM: {GRID_OFFSET_Y_MM}")
    print(f"CELL_SPACING_X_MM: {CELL_SPACING_X_MM}")
    print(f"CELL_SPACING_Y_MM: {CELL_SPACING_Y_MM}")
    print(f"Canvas Width: {canvas_width_mm} mm")
    print(f"Canvas Height: {canvas_height_mm} mm")

    with open(input_csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Create an SVG drawing with the specified canvas width and height
        dwg = svgwrite.Drawing(output_svg, profile='tiny', size=(f'{canvas_width_mm}mm', f'{canvas_height_mm}mm'), viewBox=(f'0 0 {canvas_width_mm} {canvas_height_mm}'))

        for row in csvreader:
            for index in row:
                index = int(index)
                if 0 <= index < GRID_WIDTH * GRID_HEIGHT:
                    col = index % GRID_WIDTH
                    row = index // GRID_WIDTH
                    x = col * (CELL_WIDTH_MM + CELL_SPACING_X_MM) + GRID_OFFSET_X_MM
                    y = row * (CELL_HEIGHT_MM + CELL_SPACING_Y_MM) + GRID_OFFSET_Y_MM
                    rect_width = CELL_WIDTH_MM - KERF_MM
                    rect_height = CELL_HEIGHT_MM - KERF_MM

                    # Create a path data string for the rectangle using SVG path commands:
                    # - 'M' for move to the starting point
                    # - 'h' for draw a horizontal line
                    # - 'v' for draw a vertical line
                    # - 'Z' to close the path
                    path_data = f"M{x},{y} h{rect_width} v{rect_height} h-{rect_width} v-{rect_height} Z"
                    
                    # Create a <path> element for the rectangle
                    path = dwg.path(d=path_data, stroke='black', fill='none')
                    
                    # Add the <path> element to the SVG drawing
                    dwg.add(path)

        # Save the SVG drawing to the output file
        dwg.save()

    cairosvg.svg2pdf(url=output_svg, write_to=output_pdf)

if __name__ == "__main__":
    input_csv = "input.csv"  # Replace with the path to your CSV file
    output_svg = "output.svg"  # Replace with the desired output SVG file name
    output_pdf = "output.pdf"  # Replace with the desired output PDF file name
    create_svg(input_csv, output_svg)
