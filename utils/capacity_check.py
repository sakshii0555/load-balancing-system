def capacity_status(load, capacity):

    if load > capacity:
        return "🚨 Overloaded"

    elif load >= 0.9 * capacity:
        return "⚠ Near Capacity"

    else:
        return "✅ Safe"