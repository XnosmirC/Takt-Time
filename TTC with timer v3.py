import time

def calculate_takt_time(available_production_time, customer_demand):
    return available_production_time / customer_demand

def start_timer():
    return time.time()

def items_completed(start_time, takt_time):
    elapsed_time = time.time() - start_time
    completed_items = int(elapsed_time // takt_time)
    return completed_items

def countdown_timer(item_time):
    for remaining in range(item_time, 0, -1):
        print(f'Time remaining: {remaining // 60}:{remaining % 60:02d}', end='\r')
        time.sleep(1)

# Get user input
n_items = int(input("Enter the number of items: "))
available_production_time = int(input("Enter the available production time (minutes): "))  # convert to minutes
takt_time_n = calculate_takt_time(available_production_time, n_items)
start_time = start_timer()

# Create a countdown timer for each item and track progress
for i in range(n_items):
    item_start_time = start_timer()  # Restart the timer for each item
    while True:
        elapsed_time = time.time() - item_start_time
        remaining_time = int(takt_time_n * 60 - elapsed_time)
        if remaining_time <= 0:
            print('\nTime for the next item!\n')
            break
        print(f'Time remaining: {remaining_time // 60}:{remaining_time % 60:02d}', end='\r')
        if input('Press Enter to move to the next item...') == '':
            break

    completed_items = i + 1
    expected_items = items_completed(start_time, takt_time_n)
    print(f"Items completed: {completed_items}")
    print(f"Expected items completed: {expected_items}"