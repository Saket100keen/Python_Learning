import psutil # type: ignore

print(dir(psutil))
print(psutil.cpu_percent(interval=1))