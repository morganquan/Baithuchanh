import tkinter as tk
def on_button_click():
    label.config(text="Bạn đã bấm nút!", fg="green")
window = tk.Tk()
window.title("Cửa sổ đồ họa với Tkinter")
window.geometry("400x200")
window.resizable(False, False)
label = tk.Label(window, text="Chào mừng bạn đến với Tkinter!", font=("Arial", 14))
label.pack(pady=20)
button = tk.Button(
    window,
    text="Bấm vào đây",
    bg="blue",
    fg="white",
    font=("Arial", 12),
    command=on_button_click
)
button.pack(pady=10)
window.mainloop()
