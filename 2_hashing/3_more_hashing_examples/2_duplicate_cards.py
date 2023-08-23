# Given an integer array cards, find the length of the shortest 
# subarray that contains at least one duplicate. If the array has 
# no duplicates, return -1.

TEST_CASES = [
    [[1,2,3,4,5,5,3,5], 2],
    [[1,2,3,4,5,3,7,8,5], 4],
    [[1,2,3,4,5,3,7,8,5], 4],
    [[1,2,3,4,5,6], -1],
    [[1,1,3,4,5,6,5], 2],
]

def duplicate_cards_sliding_window(cards):
    left = 0
    ans = -1

    cards_seen = {}

    for right in range(len(cards)):
        card = cards[right]
        if card not in cards_seen:
            cards_seen[card] = 0

        cards_seen[card] += 1

        while cards_seen[card] == 2:
            subarr_len = right - left + 1
            if ans == -1:
                ans = subarr_len
            else:
                ans = min(ans, subarr_len)

            cards_seen[cards[left]] -= 1
            left += 1

    return ans

# reframe as, what is the shortest distance between two duplicates?
def duplicate_cards_hashing(cards):
    ans = float('inf')
    cards_indices = {}

    for index, card in enumerate(cards):
        if card not in cards_indices:
            cards_indices[card] = []

        cards_indices[card].append(index)

    for card in cards_indices:
        arr = cards_indices[card]
        for i in range(len(arr) - 1):
            ans = min(ans, arr[i+1] - arr[i] + 1)

    return ans if ans < float('inf') else -1


if __name__ == "__main__":
    for case in TEST_CASES:
        print(duplicate_cards_sliding_window(case[0]) == case[1], duplicate_cards_hashing(case[0]) == case[1])
