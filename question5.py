def analyze_power_consumption(readings):
    if any(reading < 10 or reading > 200 for reading in readings):
        return "INVALID INPUT"
    sensor_averages = []
    for i in range(5):
        average = sum(readings[i::5]) / 4
        sensor_averages.append(round(average))
    max_average = max(sensor_averages)
    if max_average < 50:
        return "Energy consumption is optimal."
    highest_sensors = [i + 1 for i, avg in enumerate(sensor_averages) if avg == max_average]
    return f"Sensor Number : {', '.join(map(str, highest_sensors))}"

input_data = list(map(int, input().strip().split()))
result = analyze_power_consumption(input_data)
print(result)