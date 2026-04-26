def recommend_project(risk_score, cost):

    if risk_score > 60 and cost > 50000000:
        return "❌ Not Recommended"

    elif risk_score > 40:
        return "⚠️ Proceed with Caution"

    else:
        return "✅ Safe to Execute"