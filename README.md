# latexhotkeys
A macro that types out LaTex using hotkeys

LaTeX Hotkey Macro
This is a simple hotkey macro script designed to assist with inserting LaTeX commands quickly. The script uses the following libraries:

pystray for accessibility in the system icon tray.
pynput for communicating with input devices (keyboard).
threading for handling processes.

Features
The script currently has five hotkeys:

Ctrl+Alt+,: Generates \textsf{,}
Ctrl+Alt+.: Generates \textsf{.}
Ctrl+Alt+l: Generates the following LaTeX block

$$ latex
\begin{align}
equation 1
\\[0.5em] equation 2
\end{align}
$$

Ctrl+Alt+F: Generates \dfrac{}{}
Ctrl+Alt+S: Generates the following LaTeX block

\begin{equation*} 
\left\{ 
\begin{aligned} 
equation 1 
\\[0.5em] equation 2 
\end{aligned} 
\right. 
\end{equation*}

Usage
Starting the Macro
To start the macro/hotkey script:

Locate the latexhotkey executable in the dist folder.
Double-click on latexhotkey to run the script.
Exiting the Macro
To exit the macro/hotkey script:

Right-click on the latexhotkey icon in the system tray.
Select "Quit" from the context menu.
