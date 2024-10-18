import time

def calculate_takt_time(available_production_time, customer_demand):
    return available_production_time / customer_demand

def start_timer():
    return time.time()

def countdown_timer(item_time):
    for remaining in range(item_time, 0, -1):
        print(f'Time remaining: {remaining // 60}:{remaining % 60:02d}', end='\r')
        time.sleep(1)
    print('\nTime for the next item!\n')

# Simple run without interactive input
n_items = 3
available_production_time = 9 * 60  # 9 hours
takt_time_n = calculate_takt_time(available_production_time, n_items)

# Test the timer with a lower duration for a quick test
for i in range(n_items):
    print(f"Starting timer for item {i + 1}")
    countdown_timer(15)  # 5 seconds for quick test
    print(f"Completed item {i + 1}\n")