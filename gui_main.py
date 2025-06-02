import tkinter as tk
from tkinter import ttk
from speed_test import get_speed_results  # Import the new function

def run_speed_test():
    result_label.config(text="Running speed test...")
    window.update()

    results = get_speed_results()

    result_text = (
        f"Download Speed: {results['download']} Mbps\n"
        f"Upload Speed: {results['upload']} Mbps\n"
        f"Ping: {results['ping']} ms"
    )
    result_label.config(text=result_text)

# Create the main window
window = tk.Tk()
window.title("Internet Speed Test")
window.geometry("400x250")

heading = ttk.Label(window, text="Speed Test App", font=("Helvetica", 18))
heading.pack(pady=10)

run_button = ttk.Button(window, text="Run Speed Test", command=run_speed_test)
run_button.pack(pady=10)

result_label = ttk.Label(window, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

window.mainloop()
