##########################################################################
#
#    randSelect.py
#    randomized selection
#
#    Includes function definitions for partition and randSelect.
#
##########################################################################

from typing import List
import random

def partition(ray: List[int], left: int, right: int) -> int:
    """
    In-place partition of the list around a pivot chosen at random.

    Args:
    ray: The list of integers to partition.
    left: The starting index for the partition range.
    right: The ending index for the partition range.

    Returns:
    The index where the pivot element finally resides.
    """
    pivot_index = random.randint(left, right)  # Random pivot
    pivot_value = ray[pivot_index]
    ray[pivot_index], ray[right] = ray[right], ray[pivot_index]  # Move pivot to end
    store_index = left

    for j in range(left, right):
        if ray[j] <= pivot_value:
            ray[j], ray[store_index] = ray[store_index], ray[j]  # Move smaller element to the left
            store_index += 1

    ray[store_index], ray[right] = ray[right], ray[store_index]  # Place pivot after all smaller elements
    return store_index

def randSelect(ray: List[int], index: int) -> int:
    """
    Selects the element at the given index as if the array was sorted without actually sorting it.

    Args:
    ray: The list of integers from which to select the element.
    index: The 0-based index indicating the order of the element to select.

    Returns:
    The value that would be at the given index if the list were sorted.

    Raises:
    IndexError: If the index is out of the bounds of the list.
    """
    def select(left: int, right: int, index: int) -> int:
        if left == right:
            return ray[left]  # Base case: only one element

        print(f"Looking for value with rank {index} in the array:")
        print(ray[left:right+1])

        pivot_index = partition(ray, left, right)
        pivot_rank = pivot_index - left  # Pivot rank in the subarray

        # Determine the direction of recursion based on pivot's rank
        direction = 'left' if index < pivot_index else 'right'
        if index != pivot_index:
            direction += '.'

        print(f"Selected {ray[pivot_index]} as the pivot; its rank is {pivot_rank}; Thus, we recurse on {direction}")
        if index == pivot_index:
            # If pivot index matches the desired index, we have found the element
            return ray[pivot_index]
        elif index < pivot_index:
            # If desired index is less, recurse on left subarray
            return select(left, pivot_index - 1, index)
        else:
            # If desired index is more, recurse on right subarray
            return select(pivot_index + 1, right, index)

    if index < 0 or index >= len(ray):
        raise IndexError("Index is out of bounds")  # Validate the index

    return select(0, len(ray) - 1, index)  # Initiate the recursive selection process
