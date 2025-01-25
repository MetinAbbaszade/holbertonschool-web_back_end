#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ asyncio function """
    delays = [wait_random(max_delay) for _ in range(n)]
    print(delays)
    return [await delay for delay in asyncio.as_completed(delays)]
