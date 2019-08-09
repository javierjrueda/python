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

def logo(s):
    abc = 'abdefghijklmnopqrstuvwxyz'

    for i in abc:
        reps = s.count(i)
        scorelist.append(
            scoredict={
            "letter" : i,
            "reps" : reps})
    scorelist.sort(key="letter")
    scorelist.sort(reverse=True , key="reps")

    print(scorelist[1])
    print(scorelist[2])
    print(scorelist[3])




if __name__ == '__main__':
    s = raw_input()
    logo(s)
