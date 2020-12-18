from database.db import votes, candidates


def count():
    votes_count = []

    votes_list = votes.find_all()
    candidates_list = candidates.find_all()

    for candidate in candidates_list:
        votes_count.append(
            [vote for vote in votes_list if vote.candidato.id == candidate.id])

    return votes_count
