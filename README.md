# IBM Punch Card Editor

A simple browser-based UI and Python program for generating IBM punch cards using a grid of checkboxes. This tool allows you to visually design punch cards, export them as CSV, then convert them to SVG/PDF using the companion Python script. The SVGs may then be fed into a laser cutter to cut actual IBM punch cards.

![image](https://github.com/user-attachments/assets/9c5fb486-b7bd-498f-8ff1-88803c3a580f)


## 🖱 Basic Usage

**Edit the Punch Card**
   - Click any cell to toggle it on (punched) or off (unpunched).
   - Click and hold, then drag the mouse over cells to "paint" or "draw" multiple cells.
   - Click any cell, then hold **Shift** and click another cell to draw a straight line between the two points (works diagonally, vertically, or horizontally) using Bresenham's line algortihm.
     - If the first clicked cell is checked, the entire line will be checked.
     - If it's unchecked, the entire line will be unchecked.

**Save Your Work**
   - Click the **"Save"** link below the grid to download a CSV file containing your punched cell data. It will be named `punchcard.csv` by default.

**Convert to SVG/PDF**
   - Move or copy `punchcard.csv` into the same directory as the Python converter script (`punchard.py`).
   - Run the following command in your terminal to install dependencies and run the conversion script:
     ```bash
     pip install -r requirements.txt
     
     ./punchard.py punchard.csv
     ```
   - This will generate an SVG and PDF version of your punch card, named `output.csv` and `output.pdf`, respectively.


**Laser Cutter**

The script `punchcard.py` has a number of configurable parameters, which will need to be calibrated to suit the laser cutter and IBM punchcards. The number of columns and rows, cell widths, cell spacing, grid offsets, and laser kerf (width of the laser cut itself) are all configurable, and will need to be adjusted.
