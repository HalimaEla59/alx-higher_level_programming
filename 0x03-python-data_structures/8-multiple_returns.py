#!/usr/bin/python3
def multple_returns(sentence):
    if len(sentence) > 0:
        return((len(sentence), sentence[0]))
    return((len(sentence), None))
