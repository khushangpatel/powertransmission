def calculate_cost(length, voltage, terrain, experience, material_index, labor):

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

    experience_factor = 1 - (experience * 0.01)
    labor_factor = 1 + ((100 - labor) / 200)

    cost = length * base_cost_per_km[voltage] * terrain_multiplier[terrain]

    final_cost = cost * material_index * labor_factor * experience_factor

    return final_cost