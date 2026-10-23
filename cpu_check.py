cpu = int(input("Enter the CPU: "))
if cpu >50:
    print("CPU is Overloaded")
elif cpu > 20 and cpu <= 50:
    print("CPU is Moderate")
else:
    print("CPU is Normal")