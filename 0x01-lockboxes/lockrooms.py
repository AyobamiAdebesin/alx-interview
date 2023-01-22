#!/usr/bin/python3
""" Lockrooms """
from typing import List, Set
def canUnlockAll(rooms: List[List[int]]) -> bool:
    """ Can we  unlock all rooms? 
    Return True if we can visit and unlock all rooms
    else return False
    """
    if not isinstance(rooms, list):
        raise TypeError("rooms must be a list of lists")
    keys_found: Set[int] = set(rooms[0])
    rooms_not_opened: List[int] = []

    for idx in range(1, len(rooms)):        
        if idx in keys_found:
            keys = rooms[idx]
            if len(keys) != 0:
                keys_found.update(keys)
                for key in keys:
                    if key in rooms_not_opened:
                        new_keys = rooms[key]
                        if len(new_keys) != 0:
                                keys_found.update(new_keys)
                                rooms_not_opened.remove(key)
                        else:
                            rooms_not_opened.remove(key)
        else:
            rooms_not_opened.append(idx)
    if len(rooms_not_opened) != 0:
        return False
    else:
        return True
