'''
Features:
- Rich-text-like editor but specific for LaTeX formats
- Highlight text then press command to format it depending on the command (e.g. highlight 1/2 -> press command -> convert to \dfrac{1}{2})

if logic for commands -> search for specific command, then execute code.

Formatting that can be included:
- fractions
- square root
- exponent
- system of equations
'''

import pystray
from pystray import MenuItem as item
from PIL import Image
from pynput import keyboard
import threading

def start_hotkeys():
    controller = keyboard.Controller()

    def type_cancel():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('c')
        controller.type('\\cancel{x}')

    def type_large():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('l')
        controller.type('\\large{x}')

    def type_approx():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('a')
        controller.type('\\approx')

    def type_cdot():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('m')
        controller.type('\\cdot')

    def type_sqrt_index():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('s')
        controller.type('\\sqrt[x]{y}')

    def type_sqrt():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('q')
        controller.type('\\sqrt{x}')

    def type_triangle():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('t')
        controller.type('\\triangle')

    def type_comma():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release(',')
        controller.type('\\textsf{,}')


    def type_comma():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release(',')
        controller.type('\\textsf{,}')

    def type_dot():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('.')
        controller.type('\\textsf{.}')

    def type_latex():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.shift)
        controller.release('x')
        controller.type(
"""
$$ latex
\\begin{align}
equation 1
\\\[0.5em] equation 2
\end{align}
$$
""")

    def type_frac():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.alt)
        controller.release('f')
        controller.type('\dfrac{x}{y}')

    def type_system():
        controller.release(keyboard.Key.ctrl)
        controller.release(keyboard.Key.shift)
        controller.release('e')
        controller.type(
"""
$$ latex
\\begin{equation*} 
\left\{ 
\\begin{aligned} 
equation 1 
\\\[0.5em] equation 2 
\end{aligned} 
\\right. 
\end{equation*}
$$
""")

    with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+,': type_comma,
        '<ctrl>+<alt>+.': type_dot,
        '<ctrl>+<alt>+f': type_frac,
        '<ctrl>+<alt>+c': type_cancel,
        '<ctrl>+<alt>+l': type_large,
        '<ctrl>+<alt>+a': type_approx,
        '<ctrl>+<alt>+m': type_cdot,
        '<ctrl>+<alt>+s': type_sqrt_index,
        '<ctrl>+<alt>+q': type_sqrt,
        '<ctrl>+<alt>+t': type_triangle,
        '<ctrl>+<shift>+e': type_system,
        '<ctrl>+<shift>+x': type_latex
    }) as h:
        h.join()

# Function to be called when the tray icon is clicked
def on_clicked(icon, item):
    print("Tray icon clicked!")

# Function to create and run the tray icon
def create_tray_icon():
    # Create an image for the tray icon
    image = Image.open("LaTeX_logo.png")

    # Create the menu items
    menu = (item('Quit', lambda icon: icon.stop()),)

    # Create the tray icon
    icon = pystray.Icon("name", image, "Latex Hotkey", menu)

    # Run the icon
    icon.run()

# Start hotkeys in a separate thread
hotkey_thread = threading.Thread(target=start_hotkeys)
hotkey_thread.daemon = True
hotkey_thread.start()

# Create and run the tray icon
create_tray_icon()