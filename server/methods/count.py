from database.db import votes, candidates


def count(data):
    votes_per_candidate = {}

    votes_list = votes.find_all()

    for vote in votes_list:
        try:
            votes_per_candidate[f"{vote['candidate']}"] += 1
        except:
            votes_per_candidate[f"{vote['candidate']}"] = 1

    return votes_per_candidate
