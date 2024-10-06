from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def is_safe(board, row, col):
    # Check the row
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_n_queens(board, col):
    if col >= len(board):
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_n_queens(board, col + 1):
                return True

            board[i][col] = 0  # Backtrack

    return False

def get_solution(request):
    board = [[0 for _ in range(8)] for _ in range(8)]
    if solve_n_queens(board, 0):
        solution = [row.index(1) for row in board]
        return JsonResponse(solution, safe=False)
    else:
        return JsonResponse({'error': 'No solution found'})
