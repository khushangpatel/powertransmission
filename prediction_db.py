from db import get_connection

def save_prediction(length, voltage, duration, prediction, probability):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO predictions (length, voltage, duration, prediction, probability) VALUES (?,?,?,?,?)",
        (length, voltage, duration, prediction, probability)
    )

    conn.commit()
    cursor.close()
    conn.close()