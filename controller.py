from evdev import InputDevice, categorize, ecodes
gamepads = []
try:
    gamepads0 = InputDevice('/dev/input/event0')
    gamepads.append(gamepads0)
except OSError:
    z = 1
try:
    gamepads1 = InputDevice('/dev/input/event1')
    gamepads.append(gamepads1)
except OSError:
    z = 1
try:
    gamepads2 = InputDevice('/dev/input/event2')
    gamepads.append(gamepads2)
except OSError:
    z = 1
try:
    gamepads3 = InputDevice('/dev/input/event3')
    gamepads.append(gamepads3)
except OSError:
    z = 1

count = 0
controller_list=["Logitech Gamepad F310","Logitech Gamepad F710","Microsoft X-Box 360 pad","Logitech Logitech Cordless RumblePad 2", "Logitech Logitech Dual Action"]
for c in controller_list:
    for i in gamepads:
        if i.name == c:
            gamepad = i
            print(gamepad)
    else:
        count += 1
if count == 4:
    print("controller not found")
