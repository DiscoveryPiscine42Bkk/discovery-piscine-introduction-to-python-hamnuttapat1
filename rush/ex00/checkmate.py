def checkmate(board):
    board = [list(row) for row in board.strip().split('\n')]
    n = len(board)
    m = len(board[0])

    # Find king
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'K':
                king_pos = (i, j)
    ki, kj = king_pos

    # Pawn 
    for di, dj in [(1, -1), (1, 1)]:
        ni, nj = ki + di, kj + dj
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 'P':
            print("Success")
            return

    # Bishop/Queen 
    for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        ni, nj = ki + di, kj + dj
        while 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] == 'B' or board[ni][nj] == 'Q':
                print("Success")
                return
            if board[ni][nj] != '.':
                break
            ni += di
            nj += dj

    # Rook/Queen 
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = ki + di, kj + dj
        while 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] == 'R' or board[ni][nj] == 'Q':
                print("Success")
                return
            if board[ni][nj] != '.':
                break
            ni += di
            nj += dj

    print("Fail")