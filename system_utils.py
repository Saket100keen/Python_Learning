# Creating a reuseable function to check CPU usage Sytem Health
import psutil # type: ignore
def get_system_health():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    System_Info = {
        "CPU Usage": cpu,
        "Memory Usage": memory,
        "Disk Usage": disk
    }

    print("System Health Information: \n " , System_Info) 