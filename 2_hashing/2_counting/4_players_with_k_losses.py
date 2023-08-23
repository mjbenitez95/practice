# You are given an integer array matches where matches[i] = [winneri, loseri] 
# indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.

# The values in the two lists should be returned in increasing order.

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.

TEST_CASES = [
    [[[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]], [[1,2,10],[4,5,7,8]]],
    [[[2,3],[1,3],[5,4],[6,4]], [[1,2,5,6],[]]],
]

def players_with_n_losses(matches):
    zero_loss_players = []
    one_loss_players = []

    losses = {}

    for match in matches:
        if match[0] not in losses:
            losses[match[0]] = 0
        if match[1] not in losses:
            losses[match[1]] = 0

        losses[match[1]] += 1

    for player, num_losses in losses.items():
        if num_losses == 0:
            zero_loss_players.append(player)
        elif num_losses == 1:
            one_loss_players.append(player)

    return [sorted(zero_loss_players), sorted(one_loss_players)]

if __name__ == "__main__":
    for case in TEST_CASES:
        print(players_with_n_losses(case[0]) == case[1])