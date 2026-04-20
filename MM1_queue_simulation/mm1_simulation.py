"""
M/M/1 Queue Simulation (Single Server System)
---------------------------------------------

Real-world analogy: BARBERSHOP 💈

- Customers arrive randomly
- One barber (server)
- If barber is busy → customers wait in a queue
- If barber is idle → customer is served immediately

This simulation estimates:
1. Average waiting time (delay)
2. Average queue length
3. Server (barber) utilization
"""

# -----------------------------
# IMPORTS
# -----------------------------

import math   # used for logarithm in exponential distribution
import random # used to generate random numbers


# -----------------------------
# CONSTANTS (System Limits & States)
# -----------------------------

Q_LIMIT = 100   # Maximum queue size. Prevents the simulation from using infinite memory. If the line hits 101, the program throws an overflow error.
BUSY = 1        # Numeric flag indicating the server (barber) is currently actively cutting hair.
IDLE = 0        # Numeric flag indicating the server (barber) is completely free and waiting.


# -----------------------------
# GLOBAL VARIABLES (System State)
# -----------------------------

# Event tracking
next_event_type = 0   # Determines what event is happening right now: 1 for arrival (customer walks in), 2 for departure (haircut finishes).

# Customer tracking
num_custs_delayed = 0      # Running count of how many customers have started their haircut (completed their delay phase).
num_delays_required = 0    # Stopping condition: The total number of customers we want to serve before shutting the simulation down.
num_in_q = 0               # Current count of customers physically waiting in the line (does NOT include the person currently in the barber chair).

# Server state
server_status = IDLE       # Tracks the current state of the barber. It will flip between IDLE (0) and BUSY (1).

# Time tracking
sim_time = 0.0             # The master clock of the simulation. It doesn't tick second-by-second; it "jumps" instantly to the time of the next event.
time_last_event = 0.0      # Records the 'sim_time' when the previous event happened. Crucial for calculating how much time passed between events to update our averages.

# Event list
# time_next_event stores the exact clock time when future events are scheduled to happen.
# Index 0 is ignored. Index 1 holds the next arrival time. Index 2 holds the next departure time.
time_next_event = [0.0, 0.0, 0.0]  

# Queue storage (stores arrival times of waiting customers)
# Array where index 'i' holds the exact clock time when the 'i'th person in line walked in. We subtract this from the current time when they finally reach the chair to calculate their total wait.
time_arrival = [0.0] * (Q_LIMIT + 1)

# Statistics
total_of_delays = 0.0      # A running sum of all waiting times for all customers combined. At the end, we divide this by num_custs_delayed to get the average wait.
area_num_in_q = 0.0        # Cumulative area under the "number of people in queue" curve over time. Used to calculate the average number of people in the queue throughout the whole day.
area_server_status = 0.0   # Cumulative area under the "server busy status" curve over time. Because BUSY is 1 and IDLE is 0, this helps calculate the percentage of the day the barber was working.

# Input parameters
mean_interarrival = 0.0    # The expected average time (in minutes) between two consecutive customers walking through the door.
mean_service = 0.0         # The expected average time (in minutes) it takes the barber to finish one haircut.

num_events = 2  # The total number of event types our timing loop needs to check (1 = arrival, 2 = departure).


# -----------------------------
# RANDOM FUNCTION (Exponential Distribution)
# -----------------------------

def expon(mean):
    """
    Generate a random time using exponential distribution.

    In barbershop terms:
    - How long until next customer arrives
    - How long a haircut takes
    """
    return -mean * math.log(random.random())


# -----------------------------
# INITIALIZATION FUNCTION
# -----------------------------

def initialize():
    global sim_time, server_status, num_in_q, time_last_event
    global num_custs_delayed, total_of_delays
    global area_num_in_q, area_server_status, time_next_event

    # Shop opens → time starts at 0
    sim_time = 0.0

    # Barber is idle, no customers yet
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0

    # Reset statistics
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0

    # Schedule first arrival (first customer walking into shop)
    time_next_event[1] = sim_time + expon(mean_interarrival)

    # No one is being served → no departure yet
    time_next_event[2] = float('inf')


# -----------------------------
# TIMING FUNCTION
# -----------------------------

def timing():
    global sim_time, next_event_type

    min_time_next_event = float('inf')
    next_event_type = 0

    # Find earliest event (arrival or departure)
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    # If no event found → error
    if next_event_type == 0:
        print(f"Event list empty at time {sim_time}")
        exit(1)

    # Move simulation time forward
    sim_time = min_time_next_event


# -----------------------------
# ARRIVAL EVENT (Customer enters shop)
# -----------------------------

def arrive():
    global num_in_q, server_status, total_of_delays
    global num_custs_delayed, time_next_event

    # Schedule next arrival
    time_next_event[1] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        # Barber busy → customer joins queue
        num_in_q += 1

        if num_in_q > Q_LIMIT:
            print(f"Queue overflow at time {sim_time}")
            exit(2)

        # Store arrival time (needed to compute delay later)
        time_arrival[num_in_q] = sim_time

    else:
        # Barber idle → customer served immediately
        delay = 0.0
        total_of_delays += delay

        num_custs_delayed += 1
        server_status = BUSY

        # Schedule departure (haircut completion)
        time_next_event[2] = sim_time + expon(mean_service)


# -----------------------------
# DEPARTURE EVENT (Customer leaves after haircut)
# -----------------------------

def depart():
    global num_in_q, server_status, total_of_delays
    global num_custs_delayed, time_next_event

    if num_in_q == 0:
        # No one waiting → barber becomes idle
        server_status = IDLE
        time_next_event[2] = float('inf')

    else:
        # Someone is waiting → next customer is served
        num_in_q -= 1

        # Compute delay (waiting time in queue)
        delay = sim_time - time_arrival[1]
        total_of_delays += delay

        num_custs_delayed += 1

        # Schedule next departure
        time_next_event[2] = sim_time + expon(mean_service)

        # Move queue forward (like people stepping up)
        for i in range(1, num_in_q + 1):
            time_arrival[i] = time_arrival[i + 1]


# -----------------------------
# UPDATE STATISTICS OVER TIME
# -----------------------------

def update_time_avg_stats():
    global time_last_event, area_num_in_q, area_server_status

    # Time since last event
    time_since_last_event = sim_time - time_last_event

    # Update last event time
    time_last_event = sim_time

    # Area under queue curve (people waiting over time)
    area_num_in_q += num_in_q * time_since_last_event

    # Area under server busy curve
    area_server_status += server_status * time_since_last_event


# -----------------------------
# REPORT RESULTS
# -----------------------------

def report():
    print("\n--- Simulation Results (Barbershop) ---\n")

    print(f"Average delay in queue: {total_of_delays / num_custs_delayed:.3f} minutes")
    print(f"Average number in queue: {area_num_in_q / sim_time:.3f}")
    print(f"Server (barber) utilization: {area_server_status / sim_time:.3f}")
    print(f"Time simulation ended: {sim_time:.3f} minutes")


# -----------------------------
# MAIN FUNCTION
# -----------------------------

def main():
    global mean_interarrival, mean_service, num_delays_required

    # -----------------------------------------------------------------
    # REPLACED FILE READING WITH HARDCODED VARIABLES HERE
    # -----------------------------------------------------------------
    mean_interarrival = 1.0      # Average time (in mins) between arrivals
    mean_service = 0.5           # Average time (in mins) to cut hair
    num_delays_required = 1000   # Stop simulation after 1000 customers
    # -----------------------------------------------------------------

    # Print initial setup
    print("Single-server queueing system (Barbershop)\n")
    print(f"Mean interarrival time: {mean_interarrival:.3f} minutes")
    print(f"Mean service time: {mean_service:.3f} minutes")
    print(f"Number of customers: {num_delays_required}\n")

    # Initialize system
    initialize()

    # Main simulation loop
    while num_custs_delayed < num_delays_required:
        timing()
        update_time_avg_stats()

        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()

    # Print final report
    report()


# -----------------------------
# RUN PROGRAM
# -----------------------------

if __name__ == "__main__":
    main()