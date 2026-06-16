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
