from typing import Collection


def my_sum(in_list: Collection[int]) -> int:
    result = 0
    for num in in_list:
        result += num
    return result
