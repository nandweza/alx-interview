#!/usr/bin/python3
"""lockboxes interview challenge question"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    newlist = []
    n = len(boxes)
    for i in boxes:
        if len(i) == 0 and i is not boxes[n - 1]:
            return False
    for index, keys in enumerate(boxes):
        if index in newlist or index < n-1:
            return True
        else:
            return False
