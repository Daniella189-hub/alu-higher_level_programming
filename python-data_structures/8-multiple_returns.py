#!/usr/bin/python3
def multiple_returns(sentence):
    tuple(sentence)
    if sentence == "":
        return (len(tuple(sentence)), None)
    else:
        return (len(tuple(sentence)), sentence[0])
