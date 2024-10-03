import json
from django.shortcuts import render
from django.http import JsonResponse

# Initialize the board and counter
board = [[{'class': 'grey', 'has_queen': False} for _ in range(8)] for _ in range(8)]
counter = 0

def index(request):
    global board, counter
    return render(request, 'index.html', {'board': board})

def place_queen(request):
    global board, counter
    if request.method == 'POST':
        data = json.loads(request.body)
        i = data.get('i')
        j = data.get('j')

        if counter < 8 and not board[i][j]['has_queen']:
            board[i][j]['has_queen'] = True
            counter += 1
            
            # Mark invalid spaces
            for x in range(8):
                if x != j:  # Mark same row
                    board[i][x]['class'] = 'red'
                if x != i:  # Mark same column
                    board[x][j]['class'] = 'red'
            for x in range(1, 8):
                if (i + x) < 8 and (j + x) < 8:  # Mark diagonal down-right
                    board[i + x][j + x]['class'] = 'red'
                if (i - x) >= 0 and (j - x) >= 0:  # Mark diagonal up-left
                    board[i - x][j - x]['class'] = 'red'
                if (i + x) < 8 and (j - x) >= 0:  # Mark diagonal down-left
                    board[i + x][j - x]['class'] = 'red'
                if (i - x) >= 0 and (j + x) < 8:  # Mark diagonal up-right
                    board[i - x][j + x]['class'] = 'red'

            # Check for victory
            if counter == 8:
                message = "Congratulations you have solved the 8 Queen problem"
            else:
                message = None

            return JsonResponse({'board': board, 'counter': counter, 'message': message})
    
    return JsonResponse({'board': board, 'counter': counter})
