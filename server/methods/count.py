from database.db import votes, candidates


def count(data):
    votes_per_candidate = []

    votes_list = votes.find_all()
    candidates_list = candidates.find_all()

    for candidate in candidates_list:
        votes_per_candidate.append(
            [vote for vote in votes_list if vote.candidato.id == candidate.id])

    votes_count = {}
    for list_votes in votes_per_candidate:
        votes_count[f"{list_votes[0].candidate}": len(list_votes)]

    return votes_count
