#!/usr/bin/python3
def multiple_returns(sentence):
    tuple(sentence)
    if sentence == "":
        return None
    else:
        return (len(tuple(sentence)), sentence[0])
