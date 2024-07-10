import json
import pystray
from pystray import MenuItem as item
from PIL import Image
from pynput import keyboard
import threading

HOTKEYS_FILE = 'hotkeys.json'

def start_hotkeys():
    controller = keyboard.Controller()

    hotkey = None

    try:
        with open(HOTKEYS_FILE, 'r') as file:
            hotkey = json.load(file)
    except FileNotFoundError:
        pass  # No saved hotkeys yet

    def type_cancel():
        hotkey_combination = hotkey["\\cancel{x}"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\cancel{x}')

    def type_large():
        hotkey_combination = hotkey["\\large"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\large{x}')

    def type_approx():
        hotkey_combination = hotkey["\\approx"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\approx')

    def type_cdot():
        hotkey_combination = hotkey["\\cdot"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\cdot')

    def type_sqrt_index():
        hotkey_combination = hotkey["\\sqrt[x]{y}"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\sqrt[x]{y}')

    def type_sqrt():
        hotkey_combination = hotkey["\\sqrt{x}"].split('+')
        print(hotkey_combination)
        for press in hotkey_combination:
            if press == '<none>':
                return
            elif '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\sqrt{x}')

    def type_triangle():
        hotkey_combination = hotkey["\\triangle"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\triangle')

    def type_comma():
        hotkey_combination = hotkey["\\textsf{,}"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\textsf{,}')

    def type_dot():
        hotkey_combination = hotkey["\\textsf{.}"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\\textsf{.}')

    def type_latex():
        hotkey_combination = hotkey["Generic LaTeX"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type(
"""
$$ latex
\\large\\begin{align}
equation 1
\\\[-0.9em]\\\ equation 2
\end{align}
$$
""")

    def type_frac():
        hotkey_combination = hotkey["\\dfrac{x}{y}"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type('\dfrac{x}{y}')

    def type_system():
        hotkey_combination = hotkey["System of Equations"].split('+')
        for press in hotkey_combination:
            if '<' in press or '>' in press:
                new_press = press.replace("<", "").replace(">", "")
                controller.release(getattr(keyboard.Key, new_press))
            else:
                controller.release(f'{press}')
        controller.type(
"""
$$ latex
\\large\\begin{equation*} 
\left\{ 
\\begin{aligned} 
equation 1 
\\\[-0.9em]\\\ equation 2 
\end{aligned} 
\\right. 
\end{equation*}
$$
""")

    valid_hotkeys = {k: v for k, v in hotkey.items() if v is not None}

    if "\\textsf{.}" in valid_hotkeys:
        valid_hotkeys.pop("\\textsf{.}")
        valid_hotkeys[hotkey["\\textsf{.}"]]=type_dot

    if "\\textsf{,}" in valid_hotkeys:
        valid_hotkeys.pop("\\textsf{,}")
        valid_hotkeys[hotkey["\\textsf{,}"]]=type_comma

    if "\\dfrac{x}{y}" in valid_hotkeys:
        valid_hotkeys.pop("\\dfrac{x}{y}")
        valid_hotkeys[hotkey["\\dfrac{x}{y}"]]=type_frac

    if "\\cancel{x}" in valid_hotkeys:
        valid_hotkeys.pop("\\cancel{x}")
        valid_hotkeys[hotkey["\\cancel{x}"]]=type_cancel

    if "\\large" in valid_hotkeys:
        valid_hotkeys.pop("\\large")
        valid_hotkeys[hotkey["\\large"]]=type_large

    if "\\approx" in valid_hotkeys:
        valid_hotkeys.pop("\\approx")
        valid_hotkeys[hotkey["\\approx"]]=type_approx

    if "\\cdot" in valid_hotkeys:
        valid_hotkeys.pop("\\cdot")
        valid_hotkeys[hotkey["\\cdot"]]=type_cdot

    if "\\sqrt[x]{y}" in valid_hotkeys:
        valid_hotkeys.pop("\\sqrt[x]{y}")
        valid_hotkeys[hotkey["\\sqrt[x]{y}"]]=type_sqrt_index

    if "\\sqrt{x}" in valid_hotkeys:
        valid_hotkeys.pop("\\sqrt{x}")
        valid_hotkeys[hotkey["\\sqrt{x}"]]=type_sqrt

    if "\\triangle" in valid_hotkeys:
        valid_hotkeys.pop("\\triangle")
        valid_hotkeys[hotkey["\\triangle"]]=type_triangle

    if "System of Equations" in valid_hotkeys:
        valid_hotkeys.pop("System of Equations")
        valid_hotkeys[hotkey["System of Equations"]]=type_system

    if "Generic LaTeX" in valid_hotkeys:
        valid_hotkeys.pop("Generic LaTeX")
        valid_hotkeys[hotkey["Generic LaTeX"]]=type_latex

    print(valid_hotkeys)
    with keyboard.GlobalHotKeys(
        valid_hotkeys) as h:
        h.join()

    # with keyboard.GlobalHotKeys({
    #     hotkey["\\textsf{,}"]: type_comma,
    #     hotkey["\\textsf{.}"]: type_dot,
    #     hotkey["\\dfrac{x}{y}"]: type_frac,
    #     hotkey["\\cancel{x}"]: type_cancel,
    #     hotkey["\\large"]: type_large,
    #     hotkey["\\approx"]: type_approx,
    #     hotkey["\\cdot"]: type_cdot,
    #     hotkey["\\sqrt[x]{y}"]: type_sqrt_index,
    #     hotkey["\\sqrt{x}"]: type_sqrt,
    #     hotkey["\\triangle"]: type_triangle,
    #     hotkey["System of Equations"]: type_system,
    #     hotkey["Generic LaTeX"]: type_latex
    # }) as h:
    #     h.join()

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

create_tray_icon()