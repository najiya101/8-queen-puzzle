from django.shortcuts import render

def index(request):
    board = [[0 for _ in range(8)] for _ in range(8)]
    queens_positions = [(0, 0), (1, 2), (2, 4), (3, 6), (4, 1), (5, 3), (6, 5), (7, 7)]  # Example positions
    attacking_positions = set()

    # Mark attacking positions
    for row, col in queens_positions:
        for i in range(8):
            attacking_positions.add(f"{row},{i}")  # Horizontal
            attacking_positions.add(f"{i},{col}")  # Vertical
        for i in range(8):
            if 0 <= row + i < 8 and 0 <= col + i < 8:
                attacking_positions.add(f"{row + i},{col + i}")  # Diagonal
            if 0 <= row + i < 8 and 0 <= col - i < 8:
                attacking_positions.add(f"{row + i},{col - i}")  # Diagonal
            if 0 <= row - i < 8 and 0 <= col + i < 8:
                attacking_positions.add(f"{row - i},{col + i}")  # Diagonal
            if 0 <= row - i < 8 and 0 <= col - i < 8:
                attacking_positions.add(f"{row - i},{col - i}")  # Diagonal

    # Convert queen positions to strings for easy comparison
    queens_positions_str = [f"{row},{col}" for row, col in queens_positions]

    context = {
        'queens_positions': queens_positions_str,
        'attacking_positions': attacking_positions,
        'row_indices': range(8),
        'col_indices': range(8),
    }
    return render(request, 'index.html', context)
