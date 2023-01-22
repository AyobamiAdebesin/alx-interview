#!/usr/bin/env python3
""" Lockboxes """
from typing import List, Sequence


def canUnlockAll(boxes: Sequence[List[int]]) -> bool:
    if not isinstance(boxes, list):
        raise TypeError("boxes must be a list of lists")
    keys_found = [x for x in boxes[0]]
    boxes_opened = [0]
    boxes_not_opened = []

    for idx in range(1, len(boxes)):
        if idx in keys_found:
            boxes_opened.append(idx)
            keys = boxes[idx]
            if len(keys) != 0:
                temp = [x for x in keys if x not in keys_found]
                keys_found.extend(temp)
            else:
                continue
            for key in keys:
                if key in boxes_not_opened:
                    new_keys = boxes[key]
                    if len(new_keys) != 0:
                        temp_holder = [y for y in keys if y not in keys_found]
                        keys_found.extend(temp_holder)
                        boxes_not_opened.remove(key)
                else:
                    continue
        else:
            boxes_not_opened.append(idx)
    if len(boxes_not_opened) != 0:
        return False
    else:
        return True
