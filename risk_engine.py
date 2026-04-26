def calculate_risk(weather, terrain, experience, labor):

    risk_score = 0

    if weather == "High":
        risk_score += 40
    elif weather == "Medium":
        risk_score += 20
    else:
        risk_score += 10

    if terrain in ["Hilly", "Forest"]:
        risk_score += 30
    else:
        risk_score += 10

    risk_score += max(0, 20 - experience)

    if labor < 70:
        risk_score += 20

    return min(risk_score, 100)