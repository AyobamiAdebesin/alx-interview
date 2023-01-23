#!/usr/bin/python3
""" Lockrooms """
from typing import List, Set


def canUnlockAll(rooms: List[List[int]]) -> bool:
    """ Can we unlock all rooms?
    Return True if we can visit and unlock all rooms
    else return False
    """
    # Check if it rooms is of type List
    if not isinstance(rooms, list):
        raise TypeError("rooms must be a list of lists")
    keys_found: Set[int] = set(rooms[0])
    rooms_not_opened: List[int] = []

    # Loop through the rooms, starting from the 2nd room
    for idx in range(1, len(rooms)):
        # Check if index is in keys_found
        if idx in keys_found:
            # Extract the list of keys found in that room
            keys = rooms[idx]
            # If the list is not empty, update the keys_found list
            if len(keys) != 0:
                keys_found.update(keys)
                # Loop through the keys to see if it contains keys to
                # some rooms in rooms_not_opened
                for key in keys:
                    # If there is, extract the keys, update the
                    # keys_found list, and remove that room from
                    # the rooms_not_found_list
                    if key in rooms_not_opened:
                        new_keys = rooms[key]
                        if len(new_keys) != 0:
                            keys_found.update(new_keys)
                            rooms_not_opened.remove(key)
                        else:
                            rooms_not_opened.remove(key)
        # If not add room index to the rooms_not_opened list
        else:
            rooms_not_opened.append(idx)
    if len(rooms_not_opened) != 0:
        return False
    else:
        return True
