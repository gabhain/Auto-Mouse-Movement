import pyautogui
import random
import time

def move_in_random_pattern(total_distance=500, steps=20, duration_per_step=1):

    print("Starting randomized movement...")
    
    # A brief pause before the movement starts, can be adjusted or removed.
    time.sleep(1)

    x_offset = 0
    y_offset = 0

    # The range of movement for each small step
    step_range = (total_distance * 2) / steps

    print("Executing random movements...")
    for _ in range(steps):
        # Generate random small movements for x and y
        dx = random.uniform(-step_range, step_range)
        dy = random.uniform(-step_range, step_range)

        # Move the mouse
        pyautogui.move(dx, dy, duration=duration_per_step)

        # Keep track of the total offset from the start
        x_offset += dx
        y_offset += dy

    print(f"Current offset: (x={x_offset:.2f}, y={y_offset:.2f})")
    print("Returning to the starting point...")

    # Move back to the starting position
    # The duration is slightly longer to make the final move smoother
    pyautogui.move(-x_offset, -y_offset, duration=1)

    print("Movement complete. returned to the start.")

if __name__ == "__main__":
    # --- Define how many times to run the pattern ---
    repeat_count = 2 

    print(f"The pattern will run {repeat_count} times.")
    print("Starting in 3 seconds. Move to the desired start position.")
    time.sleep(3)

    for i in range(repeat_count):
        print("\n" + "="*30)
        print(f"Running pattern: {i + 1} of {repeat_count}")
        print("="*30)
        
        # --- The new randomized pattern ---
        # You can adjust these values to change the pattern's appearance
        move_in_random_pattern(
            total_distance=500,  # How "big" the overall pattern is
            steps=30,            # How many small random moves to make
            duration_per_step=2 # How fast each small move is
        )
        # Pause between repetitions
        time.sleep(10)

    print("\nAll pattern repetitions are complete.")

