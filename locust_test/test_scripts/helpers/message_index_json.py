from datetime import datetime


def create_message(message_id):
    return {
        "id": message_id,
        "created_by": "Lightyear",
        "message": "Ao infinito e além",
        "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    }
