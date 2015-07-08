# the support of TC for python is just like shit...
class BichromeBoard:
    def ableToDraw(self, board):
        parity = None
        check = ''
        possible = True
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '?':
                    continue
                if parity == None:
                    parity = (i + j) % 2
                    check = board[i][j]
                    continue
                if ((i + j) % 2 == parity and board[i][j] != check or
                    (i + j) % 2 != parity and board[i][j] == check):
                    possible = False
                    break
        if possible:
            return 'Possible'
        return 'Impossible'

for board in ['W?W', '??B', '???'], ['W??W'], ['??'], ['W???', '??B?', 'W???', '???W'], ['W???', '??B?', 'W???', '?B?W'], ['B']:
    print(BichromeBoard().ableToDraw(board))
