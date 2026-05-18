from datetime import datetime, timedelta


def generate_slot_names(start_time="08:00", period_minutes=120, slots_per_day=4):
    slots = []

    current = datetime.strptime(start_time, "%H:%M")

    for i in range(1, slots_per_day + 1):
        end = current + timedelta(minutes=period_minutes)

        slots.append(
            f"{current.strftime('%H:%M')} - "
            f"{end.strftime('%H:%M')}"
        )
        current = end

    return slots


def generate_day_names(day_count):
    if day_count == 5:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    else:
        return [f"Day {i+1}" for i in range(day_count)]


# Example
slots = generate_slot_names(
    start_time="08:00",
    period_minutes=120,
    slots_per_day=4
)

print(generate_day_names(6))

print(slots)
