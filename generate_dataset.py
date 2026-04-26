import pandas as pd
import random

num_records = 5000 

data = []

terrains = ["Plain", "Hilly", "Forest", "Desert"]
weather_levels = ["Low", "Medium", "High"]
voltages = [132, 220, 400, 765]

base_cost_per_km = {
    132: 200000,
    220: 350000,
    400: 600000,
    765: 900000
}

terrain_multiplier = {
    "Plain": 1.0,
    "Hilly": 1.2,
    "Forest": 1.3,
    "Desert": 1.1
}

for i in range(1, num_records + 1):

    length = random.randint(30, 350)
    voltage = random.choice(voltages)
    terrain = random.choice(terrains)

    planned_duration = random.randint(8, 30)

    experience = random.randint(3, 18)
    material_index = round(random.uniform(1.0, 1.5), 2)
    labor = random.randint(55, 95)

    weather = random.choice(weather_levels)

    # Base estimated cost
    base_cost = length * base_cost_per_km[voltage] * terrain_multiplier[terrain]

    # Apply material factor
    estimated_cost = base_cost * material_index

    # Real-world variation (overrun / underrun)
    risk_factor = 1.0

    if weather == "High":
        risk_factor += 0.2
    elif weather == "Medium":
        risk_factor += 0.1

    if terrain in ["Hilly", "Forest"]:
        risk_factor += 0.15

    if experience < 7:
        risk_factor += 0.15

    if labor < 70:
        risk_factor += 0.1

    variation = random.uniform(0.85, 1.2) * risk_factor
    actual_cost = estimated_cost * variation

    # Duration variation
    duration_factor = variation
    actual_duration = int(planned_duration * duration_factor)

    data.append([
        f"P{str(i).zfill(5)}",
        length,
        voltage,
        terrain,
        round(estimated_cost, 2),
        round(actual_cost, 2),
        planned_duration,
        actual_duration,
        weather,
        experience,
        material_index,
        labor
    ])

columns = [
    "Project_ID",
    "Length_km",
    "Voltage_kV",
    "Terrain",
    "Estimated_Cost",
    "Actual_Cost",
    "Planned_Duration",
    "Actual_Duration",
    "Weather_Risk",
    "Contractor_Experience",
    "Material_Cost_Index",
    "Labor_Availability"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("power_transmission_projects_5000.csv", index=False)

print("✅ 5000-record dataset generated successfully!")