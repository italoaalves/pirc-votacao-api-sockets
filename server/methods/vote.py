from database.db import votes


def vote(data):
    votes.insert(data)

    return {"status": "success"}
