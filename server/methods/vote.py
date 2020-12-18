from model.vote import Vote
from database import db


def vote(data):
    vote = Vote(data["voter"], data["candidate"])

    db.votes.insert(vote)

    return "success"