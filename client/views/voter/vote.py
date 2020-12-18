def vote():
    voter_id = int(input("Seu id: "))
    candidate_id = int(input("Seu voto: "))

    request = {
        "header": {
            "method": "vote"
        },
        "body": {
            "voter": voter_id,
            "candidate": candidate_id
        }
    }

    return request
