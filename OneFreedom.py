import tkinter as tk
import time
import os

os.system('clear')


print("============================================")
print("         LOADING ONEFREEDOM OS              ")
print("============================================")
time.sleep(5)


for i in range(1, 101, 10):
    print(f"Connecting to kernel modules... {i}%")
    time.sleep(0.3)

print("\n[ SUCCESS ] OneFreedomOS is ready, Chief Engineer")

root = tk.Tk()
root.title("OneFreedom-Login")
root.geometry("400x500")
root.configure(bg="#1e1e2e")

title_label = tk.Label(root, text="OneFreedomOS-LOGIN")
title_label.configure(font=("Arial", 24, "bold"))
title_label.configure(bg="#1e1e2e", fg="#ffffff")
title_label.pack(pady=40)

username_entry = tk.Entry(root)
username_entry.configure(font=("Arial", 14), bg="#313244", fg="#ffffff")
username_entry.pack(pady=40)
root.mainloop()
