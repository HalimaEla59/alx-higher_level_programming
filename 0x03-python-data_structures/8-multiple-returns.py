#!/usr/bin/python3
def multple_returns(sentence):
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
