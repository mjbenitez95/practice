# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
# If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

import math

TEST_CASES = [
    [[3,6,7,11], 8, 4],
    [[30,11,23,4,20], 5, 30],
    [[30,11,23,4,20], 6, 23],
]

def banana_matthew(piles, h):
    for i in range(100):
        num_hours = 0
      
        for pile in piles:
            num_hours += math.ceil(pile/i)
        
        if num_hours <= h:
            return i
      
if __name__ == "__main__":
     for case in TEST_CASES:
          print(banana_matthew(case[0], case[1]))