# use probability[score]
class IOISureWinner:
    def probability(self, scoreNeeded, subtasks, p):
        cur_prob = [1] + [0 for _ in range(scoreNeeded)]
        for i, subtask in enumerate(subtasks):
            next_prob = [0 for _ in range(scoreNeeded + 1)]
            for j, prob in enumerate(cur_prob):
                next_prob[min(scoreNeeded, j + subtask)] += prob * p[i] / 100.0
                next_prob[j] += prob * (1 - p[i] / 100.0)
            # print(next_prob)
            cur_prob = list(next_prob)
        return cur_prob[-1]