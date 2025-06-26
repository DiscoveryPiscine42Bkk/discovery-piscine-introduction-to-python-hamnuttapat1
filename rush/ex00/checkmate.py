def checkmate(board):
    board = [list(row) for row in board.strip().split('\n')]
    n = len(board) #Vertical row
    m = len(board[0]) #Horizontal column นอน

    #Find king
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'K':
                king_pos = (i, j)
    ki, kj = king_pos

    #Pawn 
    for di, dj in [(1, -1), (1, 1)]:
        ni, nj = ki + di, kj + dj #ni, nj king check pawn left down and right down
        if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == 'P':#check range of ni and nj still in board range or not. if found P mean king attacked by pawn (success)
            print("Success")
            return

    # Bishop/Queen 
    for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        ni, nj = ki + di, kj + dj 
        while 0 <= ni < n and 0 <= nj < m:
            if board[ni][nj] == 'B' or board[ni][nj] == 'Q':
                print("Success")
                return
            if board[ni][nj] != '.':#If it found Rook then exit
                break
            ni += di
            nj += dj
            #move 4 side in x pattern till out of range then stop

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
            #move 4 side in + pattern till out of range
    print("Fail")