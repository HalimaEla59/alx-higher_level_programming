#!/usr/bin/python3
def multple_returns(sentence):
    tpl = ()
    if len(sentence) == 0:
        tpl = 0, "None"
    else:
        tpl = len(sentence), sentence[0]
    return tpl
