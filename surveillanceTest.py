import getpass
import os
import subprocess
from time import sleep
import ctypes
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

username = getpass.getuser()
#print(username)

scary_commands = ['Accessing data backlog...', 'Accessing IP address...', 'Accessing ' + username + ' files', '\033[31mDisabling VPN connection...\033[0m', '\033[1;31mDisconnecting administrator access...\033[0m', 'Tunnelling...', '\033[32mClearing botnet cache...\033[0m', 'Scanning files...', 'Running trace on executable...', '\033[31mDecompiling terminal library...\033[0m', 'Rooting service call...', 'Rerouting transfer requests...', 'Accessing checksum processes...', '\033[1;31mOverwriting stored procedures...\033[0m', 'Analyzing file contents...' 'Analyzing search patterns...', 'Analyzing operating system bash...', 'Analyzing idle webcam feed...', '\033[31mExecuting...\033[0m']


clear()
sleep(1)

for x in scary_commands:
    print(x)
    sleep(.2)
    clear()

os.system("pip install enquiries==0.1.0")
import enquiries
options = ['Yes', 'No']

sleep(.3)
clear()

print("Hello user " + username + "!")
sleep(1)
choice = enquiries.choose("Would you like to continue? ", options)

if choice == "Yes":
    print("YOU CHOSE YES!")
else:
    print("YOU CHOSE NOOOO!")

while True:
    sleep(3)

    import random
    from pathlib import Path

    dir_path = Path("/Users/" + username + "/Downloads")

    # Gather all files in the directory (ignoring subfolders)
    files = [f for f in dir_path.iterdir() if f.is_file()]


    for x in range(0,7):
        if files:
            # Selects one random file
            random_file = random.choice(files)
            print(f"Selected file: {random_file.name}")
            print(f"Full path: {random_file}")
        else:
            print("No files found in the directory.")
    

        #file_name = "Entire Screen - Screencastify - March 31, 2026 5_26 PM (1).gif"

        #file_path = "/Users/" + username + "/Downloads/" + file_name

        if os.path.exists(random_file):
            try:
                os.startfile(random_file)
            except AttributeError:
                subprocess.call(["open", random_file])
        else:
            print("File not found!")
        sleep(.1)
        os.system("osascript -e 'tell application \"Terminal\" to activate'")
    
    #os.system("osascript -e 'tell application \"Terminal\" to activate'")

    os.system("pip install opencv-python")

    import cv2

    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open the camera.")
        exit()

    print("Camera opened.")
    cam = True
    i = 0

    while cam:
        i += 1
        sleep(.2)
        ret, frame = cap.read()
        if not ret:
            print("Error: Can't receive frame.")
            break

        cv2.imshow('Camera Feed', frame)
    
        if (cv2.waitKey(1) & 0xFF == ord('q')) or i > 3:
            break

    sleep(2)
    cam = False

    os.system("osascript -e 'tell application \"Terminal\" to activate'")
    
    for x in range(0,5):
        print("\nScanning biometric facial analysis", end='')
        sleep(.01)
        for x in range(0,5):
            print(".", end='')
            sleep(.05)
    print("\n")
    print("Scan Complete.")

    for x in scary_commands:
        print(x)
        sleep(.2)

    cap.release()
    cv2.destroyAllWindows()

    options = ['Yes', 'Kill switch']
    choice = enquiries.choose("Would you like to continue? ", options)

    import signal

    if choice == "Kill switch":
        print("NOOOOO")
        sleep(.3)
        os.kill(os.getppid(), signal.SIGHUP)
    else:
        continue        
