import psutil # type: ignore

#print(dir(psutil)) #dir is used to get all the attributes and methods of the module
#print(psutil.subprocess.__doc__) #__doc__ is used to get the documentation of the module
threshold = float(input("Enter the CPU threshold: "))
for i in range (5):
    if psutil.cpu_percent(interval=1) > threshold:
        print("CPU is Unhealthy")
    else:
        print("CPU is Normal")  