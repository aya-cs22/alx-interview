#!/usr/bin/python3
"""Lockboxes"""


def canUnlockAll(boxes):
    """Determine if all boxes can be unlocked."""
    open_boxes = set()
    open_boxes.add(0)
    keys = [0]
    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < len(boxes) and key not in open_boxes:
                open_boxes.add(key)
                keys.append(key)
    return len(open_boxes) == len(boxes)
