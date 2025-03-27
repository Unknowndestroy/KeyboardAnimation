import pyautogui
import time

# Function to create the dynamic animation with various effects including blink-reverse
def dynamic_animation():
    # Set how many cycles to repeat (make it long-lasting)
    cycles = 3  # Adjust for more or fewer cycles of the effect
    
    for _ in range(cycles):
        # ---- Exploding Effect: All keys ON at once ----
        print("Exploding Effect: All keys ON")
        pyautogui.press('numlock')
        pyautogui.press('capslock')
        pyautogui.press('scrolllock')
        time.sleep(1)  # Hold the explosion effect for a while
        
        # ---- Increasing Effect: Turn on keys one by one ----
        print("Increasing Effect: Turning on one by one")
        pyautogui.press('numlock')
        time.sleep(0.5)
        pyautogui.press('capslock')
        time.sleep(0.5)
        pyautogui.press('scrolllock')
        time.sleep(1)  # Pause before starting to turn them off
        
        # ---- Blinking Effect: Blink the lights ON and OFF ----
        print("Blinking Effect: Blinking the keys")
        for _ in range(6):  # Blink for 3 cycles
            pyautogui.press('numlock')
            pyautogui.press('capslock')
            pyautogui.press('scrolllock')
            time.sleep(0.3)  # Short ON time
            pyautogui.press('numlock')
            pyautogui.press('capslock')
            pyautogui.press('scrolllock')
            time.sleep(0.3)  # Short OFF time
        
        # ---- Slide Effect: Keys slide in from left to right ----
        print("Slide Effect: Keys turning ON one after the other")
        pyautogui.press('numlock')  # NumLock first (leftmost)
        time.sleep(0.5)
        pyautogui.press('capslock')  # CapsLock second
        time.sleep(0.5)
        pyautogui.press('scrolllock')  # ScrollLock last (rightmost)
        time.sleep(1)  # Pause before the next cycle
        
        # ---- Blink and Reverse Blink Effect ----
        print("Blink and Reverse Blink Effect")
        # First, blink the keys (like the blinking effect above)
        for _ in range(3):  # Blink for 3 cycles
            pyautogui.press('numlock')
            pyautogui.press('capslock')
            pyautogui.press('scrolllock')
            time.sleep(0.3)  # Short ON time
            pyautogui.press('numlock')
            pyautogui.press('capslock')
            pyautogui.press('scrolllock')
            time.sleep(0.3)  # Short OFF time

        # Now reverse the blink (turn off first, then on)
        print("Reversing Blink Effect")
        for _ in range(3):  # Reverse blink for 3 cycles
            pyautogui.press('numlock')  # Turn OFF first
            pyautogui.press('capslock')
            pyautogui.press('scrolllock')
            time.sleep(0.3)  # Short OFF time
            pyautogui.press('numlock')  # Then turn ON
            pyautogui.press('capslock')
            pyautogui.press('scrolllock')
            time.sleep(0.3)  # Short ON time

        # ---- All OFF for a smooth transition ----
        print("Turning off all keys")
        pyautogui.press('numlock')
        pyautogui.press('capslock')
        pyautogui.press('scrolllock')
        time.sleep(1)  # Pause before starting the next effect

# Run the dynamic animation
dynamic_animation()
