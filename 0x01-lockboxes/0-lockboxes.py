#!/usr/bin/python3
"""lockboxes interview challenge question"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    n = len(boxes)
    for i in boxes:
        if len(i) == 0 and i is not boxes[n - 1]:
            return False
    for index, keys in enumerate(boxes):
        return True
