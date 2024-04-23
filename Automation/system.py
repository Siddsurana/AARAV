import psutil

def get_system_status():
    # Get system's RAM usage in percentage
    ram_usage = psutil.virtual_memory().percent

    # Get system's battery health if available (only applicable for laptops)
    battery_health = None
    try:
        battery = psutil.sensors_battery()
        if battery is not None:
            battery_health = battery.percent
    except Exception as e:
        print("Failed to retrieve battery health:", e)

    # Get system's CPU usage in percentage
    cpu_usage = psutil.cpu_percent()

    return ram_usage, battery_health, cpu_usage

def system_status():
    ram_usage, battery_health, cpu_usage = get_system_status()
    status_message = f"System Status:\nRAM Usage: {ram_usage}%\nCPU Usage: {cpu_usage}%"
    if battery_health is not None:
        status_message += f"\nBattery Health: {battery_health}%"
    return status_message

status_message = system_status()
print(status_message)