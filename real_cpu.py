import psutil # type: ignore

print(dir(psutil)) #dir is used to get all the attributes and methods of the module
print(psutil.cpu_percent(interval=1))