"""
Christian DeCoske
11/26/24
Lucid Black Projects
CPU Usage Logic Bomb 
The goal of this program is to create a
logic bomb that is set off by a certian cpu 
threshold.
"""

#CPU monitor works for Linux and Windows OS.
import psutil

#This is the function we will use for monotoring cpu output.
def monitor_resources():
    """
    The gool of this is function is to 
    make sure we dont destroy my computer
    we are only monitoring cpu usage with a cut off
    at 20% of max capaity. 
    """
import psutil
import time

# This is the function we will use for monitoring CPU output.
def monitor_resources(cpu_limit=20):
    """
    Monitor CPU usage and stop when it exceeds a safe limit (default 20%).
    """
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"CPU: {cpu_usage}%")  # Display CPU usage
        if cpu_usage > cpu_limit:
            print("Warning: Resource usage is too high! Stopping the test.")
            break  # Stop monitoring if CPU exceeds threshold
        time.sleep(1)  # Pause to avoid excessive CPU usage by the monitor itself

# This is the function that simulates a payload, which can cause high CPU usage.
def payload():
    """
    A high resource-consuming task (can be adjusted for educational purposes).
    """
    print("Payload started... Simulating high CPU usage.")
    while True:
        # Simulating high CPU usage by performing unnecessary calculations.
        _ = [i ** 2 for i in range(10000)]  # Do something resource-intensive

# Main function to run the monitoring and payload in parallel
def main():
    import threading

    # Start the monitor in a separate thread
    monitor_thread = threading.Thread(target=monitor_resources, args=(20,))
    monitor_thread.daemon = True  # Daemon thread will exit when the main program exits
    monitor_thread.start()

    # Start the payload function
    payload()

if __name__ == "__main__":
    main()