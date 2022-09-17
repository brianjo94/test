import random

def play():
    user = input("r for rock, p for paper, s for scissors ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"
    
    if is_win(user, computer):
        return "You won"

    return "you lost"


   
def is_win(player, opponent):
    """# r > s , p > r, s > p"""
    """return true if player wins"""
    if (player == 's' and opponent == 'p') or (player == 'r' and opponent == 's') or (player == 'p' and opponent =='r'):
        return True

print(play())
print("thanks for playing")