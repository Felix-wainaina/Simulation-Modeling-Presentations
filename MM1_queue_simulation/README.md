# M/M/1 Queue Simulation (Barbershop Model)

## 📌 Concept Overview

This simulation models a **single-server queue system** using a **barbershop analogy**:

* Customers arrive randomly
* One barber (server)
* If barber is busy → customers wait in a queue
* If idle → customer is served immediately

---

## 📌 What M/M/1 Means

* First M → Random arrivals (Markovian / exponential)
* Second M → Random service times
* 1 → One server

---

## 📌 Key Variables

* `sim_time` → current simulation time
* `server_status` → BUSY or IDLE
* `num_in_q` → number of customers waiting
* `time_arrival[]` → stores arrival times of customers
* `time_next_event[]` → stores next arrival & departure times
* `total_of_delays` → total waiting time

---

## 📌 Key Idea: Event-Based Simulation

We do NOT move time step-by-step.

Instead:

* Jump from one event to another
* Events = Arrival or Departure

---

## 📌 Simulation Flow

1. Initialize system
2. Find next event
3. Move time forward
4. Update statistics
5. Process event (arrival/departure)
6. Repeat until enough customers
7. Generate report

---

## 📌 Arrival Logic

IF server is busy:

* Customer joins queue
* Store arrival time

IF server is idle:

* Delay = 0
* Customer is served immediately
* Schedule departure

---

## 📌 Departure Logic

IF queue empty:

* Server becomes idle

IF queue not empty:

* Take next customer
* Compute delay = current time - arrival time
* Schedule next departure

---

## 📌 Important Formulas

### Delay:

delay = time service starts - arrival time

### Average Delay:

total_of_delays / number_of_customers

### Average Queue Length:

area_num_in_q / sim_time

### Server Utilization:

area_server_status / sim_time

---

## 📌 Why We Store Arrival Times

To compute:
delay = current_time - arrival_time

---

## 📌 Why We Divide by sim_time

To get **time-based averages**, not totals.

---

## 📌 Randomness

* Arrivals and service times are random
* Generated using exponential distribution

---

## 📌 Expected Results

* Average delay ≈ 0.4–0.5 minutes
* Queue length ≈ 0.4–0.5
* Utilization ≈ 45–50%

---

## 📌 Key Insight

This simulation answers:

"How long do customers wait in a real-life random system like a barbershop?"

---
