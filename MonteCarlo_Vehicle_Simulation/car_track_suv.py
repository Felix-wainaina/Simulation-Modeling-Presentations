# ==========================================
# FILE: car_track_suv.py
# ROLE: Main GUI Application (Frontend)
# ==========================================

# IMPORTING LIBRARIES:
# tkinter: The standard Python interface to the Tk GUI toolkit. Used to build our window.
import tkinter as tk
# vehicles: Our custom module containing the Monte Carlo math and drawing logic.
import vehicles 

def main():
    """
    This is the main initialization function. It builds the GUI from the 
    buyer's perspective, featuring the control buttons and the canvas display.
    """
    # 1. Initialize the main window
    root = tk.Tk()
    root.title("Monte Carlo Vehicle Simulation")
    root.geometry("800x600") # Set initial window size
    
    # Canvas dimensions
    CANVAS_WIDTH = 800
    CANVAS_HEIGHT = 500

    # 2. Create the Control Panel Frame
    # This frame sits at the top and holds our three vehicle buttons
    control_frame = tk.Frame(root, pady=10)
    control_frame.pack(side=tk.TOP, fill=tk.X)

    # 3. Create the Drawing Canvas
    # This is the visual output area for our simulation
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.pack(pady=10)

    # 4. Define Button Actions
    # Lambda functions allow us to pass arguments (the vehicle type) to our imported function
    # without executing it immediately when the program starts.
    def on_sedan_click():
        vehicles.draw_vehicle(canvas, "Sedan", CANVAS_WIDTH, CANVAS_HEIGHT)

    def on_truck_click():
        vehicles.draw_vehicle(canvas, "Truck", CANVAS_WIDTH, CANVAS_HEIGHT)

    def on_suv_click():
        vehicles.draw_vehicle(canvas, "SUV", CANVAS_WIDTH, CANVAS_HEIGHT)

    # 5. Build the 3 Buttons (The Buyer's Perspective)
    # We place them in the control_frame using the grid layout for neat spacing
    btn_sedan = tk.Button(control_frame, text="Generate Sedan", font=("Arial", 12), command=on_sedan_click)
    btn_sedan.grid(row=0, column=0, padx=20)

    btn_truck = tk.Button(control_frame, text="Generate Truck", font=("Arial", 12), command=on_truck_click)
    btn_truck.grid(row=0, column=1, padx=20)

    btn_suv = tk.Button(control_frame, text="Generate SUV", font=("Arial", 12), command=on_suv_click)
    btn_suv.grid(row=0, column=2, padx=20)

    # Center the buttons in the frame
    control_frame.grid_columnconfigure(0, weight=1)
    control_frame.grid_columnconfigure(1, weight=1)
    control_frame.grid_columnconfigure(2, weight=1)

    # 6. Start the Application Loop
    # This keeps the window open and listening for button clicks
    root.mainloop()

# Standard Python idiom to execute the main function only if this script is run directly
if __name__ == "__main__":
    main()