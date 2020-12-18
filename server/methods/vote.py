from model.vote import Vote
from database import db


def vote(data):
    vote = Vote(data["voter"], data["cadidate"])

    
        db.votes.insert(vote)

