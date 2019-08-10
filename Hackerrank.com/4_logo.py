#!/bin/python

import math
import os
import random
import re
import sys

scorelist = []
scoredict = {
    "letter" : "",
    "reps" : "",
}

def myFunc(e):
  return e["letter"]

def myFuncreps(e):
  return e["reps"]

def logo(s):
    abc = 'abcdefghijklmnopqrstuvwxyz'

    for i in abc:
        reps = s.count(i)
        scoredict={
            "letter" : i,
            "reps" : reps}
        scorelist.append(scoredict)
            
    scorelist.sort(key=myFunc)
    scorelist.sort(reverse=True , key=myFuncreps)

    i = 0
    while i < 3:
        windict = scorelist[i]
        x = windict.get("letter")
        y = windict.get("reps")
        
        print("{} {}".format(x, y))
        i += 1


if __name__ == '__main__':
    s = raw_input()
    logo(s)
