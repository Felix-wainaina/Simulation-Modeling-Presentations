# ==========================================
# FILE: vehicles.py
# ROLE: Backend Logic & Drawing Functions
# ==========================================

# IMPORTING LIBRARIES:
# We import 'random' to access random number generators. 
# This is the core of our Monte Carlo simulation, allowing us to generate 
# the random variable 'u' for sizing, as well as random numbers for colors and positions.
import random

def generate_random_color():
    """
    Generates a random Hex color code (e.g., #FF00A2).
    Logic: An RGB color is made of Red, Green, and Blue values ranging from 0 to 255.
    We randomly select three integers in this range and format them into a Hex string.
    """
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # The {:02x} formats the integer into a 2-character hexadecimal string
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def get_random_size(a, b):
    """
    Calculates the random scale factor using the assigned formula: Size = a + u(b - a)
    - 'a' is the minimum scale.
    - 'b' is the maximum scale.
    - 'u' is a random float between 0.0 and 1.0 (Uniform Distribution).
    """
    u = random.random() # Generates our 'u' variable
    size = a + u * (b - a)
    return size

def draw_flowers(canvas, canvas_width, canvas_height):
    """
    Draws at least 6 flowers in the "Grass Zone" to prevent the car from crushing them.
    The Grass Zone is defined as the bottom 40% of the canvas.
    """
    # Define our safe zone boundaries
    grass_start_y = canvas_height * 0.60
    
    # Loop to generate exactly 6 flowers (as per requirements)
    for _ in range(6):
        # Random X position across the entire width
        x = random.randint(50, canvas_width - 50)
        # Random Y position strictly restricted to the grass zone
        y = random.randint(int(grass_start_y) + 20, canvas_height - 20)
        
        # 1. Draw the stem (a simple green line)
        canvas.create_line(x, y, x, y + 30, fill="green", width=3)
        
        # 2. Draw the petals with a randomly generated color
        petal_color = generate_random_color()
        # Drawing an oval centered at (x, y)
        canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill=petal_color, outline="black")
        # Drawing the center of the flower
        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill="yellow")

def draw_vehicle(canvas, vehicle_type, canvas_width, canvas_height):
    """
    Draws the selected vehicle type.
    It applies the Monte Carlo random size multiplier to all coordinates
    so the car and wheels scale proportionally.
    """
    # 1. Clear the canvas from the previous simulation
    canvas.delete("all")
    
    # 2. Draw the environment background to show the distinct zones
    road_height = canvas_height * 0.60
    # Road Zone (Top 60%)
    canvas.create_rectangle(0, 0, canvas_width, road_height, fill="#D3D3D3", outline="")
    # Grass Zone (Bottom 40%)
    canvas.create_rectangle(0, road_height, canvas_width, canvas_height, fill="#90EE90", outline="")
    
    # 3. Draw the 6 flowers in the safe grass zone
    draw_flowers(canvas, canvas_width, canvas_height)
    
    # 4. Determine Vehicle Traits (Size and Color)
    # Using our formula: a = 0.5 (half size), b = 1.5 (1.5x size)
    scale = get_random_size(0.5, 1.5)
    car_color = generate_random_color()
    
    # Base anchor point for the vehicle (positioned in the middle of the road zone)
    base_x = canvas_width / 2
    base_y = road_height / 1.5 
    
    # 5. Draw the specific vehicle based on the button clicked
    # We multiply every width/height dimension by our 'scale' variable
    if vehicle_type == "Sedan":
        # Draw Body
        canvas.create_rectangle(base_x - (100 * scale), base_y - (20 * scale), 
                                base_x + (100 * scale), base_y + (20 * scale), fill=car_color)
        # Draw Roof
        canvas.create_rectangle(base_x - (50 * scale), base_y - (60 * scale), 
                                base_x + (50 * scale), base_y - (20 * scale), fill=car_color)
        
    elif vehicle_type == "Truck":
        # Draw Truck Bed (Longer back)
        canvas.create_rectangle(base_x - (120 * scale), base_y - (10 * scale), 
                                base_x + (20 * scale), base_y + (20 * scale), fill=car_color)
        # Draw Truck Cab (Front)
        canvas.create_rectangle(base_x + (20 * scale), base_y - (50 * scale), 
                                base_x + (80 * scale), base_y + (20 * scale), fill=car_color)
        
    elif vehicle_type == "SUV":
        # Draw Bulky Body
        canvas.create_rectangle(base_x - (110 * scale), base_y - (20 * scale), 
                                base_x + (90 * scale), base_y + (30 * scale), fill=car_color)
        # Draw Extended Roof
        canvas.create_rectangle(base_x - (90 * scale), base_y - (70 * scale), 
                                base_x + (50 * scale), base_y - (20 * scale), fill=car_color)

    # 6. Draw Wheels (These mathematically fit the vehicle because they use the same 'scale')
    wheel_radius = 20 * scale
    # Rear wheel
    rw_x = base_x - (60 * scale)
    rw_y = base_y + (20 * scale)
    canvas.create_oval(rw_x - wheel_radius, rw_y - wheel_radius, 
                       rw_x + wheel_radius, rw_y + wheel_radius, fill="black")
    
    # Front wheel
    fw_x = base_x + (40 * scale)
    fw_y = base_y + (20 * scale)
    canvas.create_oval(fw_x - wheel_radius, fw_y - wheel_radius, 
                       fw_x + wheel_radius, fw_y + wheel_radius, fill="black")