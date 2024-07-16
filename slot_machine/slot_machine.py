# A slot machine that a user is going to bet on either one, two or three lines
# If they won we are goin to multiply their bet by the value of the lines they chose
# Add the amount won to their balance nd allow them to keep playing until they decide to cash out and quit, or run outof money
import random


MAX_LINE=3
MIN_BET=1
MAX_BET=100

ROWS = 3
COLS = 3

symbols_item = {
    "😍":9,
    "🤑":7,
    "😎":8
}

symbols_value = {
    "😍":10,
    "🤑":30,
    "😎":8
}

def game(balance):
    lines = get__number_of_lines()
    # Check if  user has enough balance to bet
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You don't have enough balance to continue playing. Your balance is: ${balance}, you need at least ${total_bet}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Your total amount is ${total_bet}")

    slot = get_slot_spin(COLS,ROWS,symbols_item)
    get_slot_machine(slot)

    winnings, winning_lines = check_winnings(slot, lines, bet, symbols_value)
    print(f"You won: ${winnings}")
    print(f"You won on ", *winning_lines)

    return winning_lines-total_bet

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol]*bet
    return winnings


def get_slot_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def get_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1 :
                print(column[row], end=" | ")
            else:
                print(column[row])


# Deposit amount to play the game
def deposit():
    while True:
        amount = input("What amount are you depositing? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("This is not a valid amount")
        else:
            print("Enter a number")
    return amount

# Get the number of lines to bet on
def get__number_of_lines():
    while True:
        lines = input(f"Enter number of lines from 1-{MAX_LINE} lines: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINE:
                break
            else:
                print("Enter a number between the range given")
        else:
            print("Invalid! Enter only numbers within the specific range given")
    return lines

# Get Bet Function
def get_bet():
    while True:
        bet = input("What amount are you betting? $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a number between {MIN_BET}-{MAX_BET}")
        else:
            print("Invalid value! Enter a number between the range given")
    return bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is ${balance}")
        spin = input("Press 'Enter' to play again or 'q' to quit")
        if spin == "q":
            break
        balance +=game(balance)
    
        print(f"You left with ${balance}")
main()