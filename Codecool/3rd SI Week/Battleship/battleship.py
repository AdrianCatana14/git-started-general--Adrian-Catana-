import string
import sys
import os
import time
import ai_algorithm

# Selecteaza cate turnuri avem
def choose_turn_limit():
    while True:
        limit = input("""Please choose a turn limit between 5-50!\n""")
        if limit.isnumeric():
            if limit in (str(x) for x in range(4, 51)):
                return int(limit)
            else:
                print(f"\nInvalid input! The chosen {limit} limit is not available!\n")
        else:
            print("\nPlease provide a number between 5-50!\n")

# Selecteaza modul
def choose_mode():
    ai_mode = False
    mode = input("\nPlease choose mode: 1. Single player, 2. Multiplayer: \n")
    while mode not in ["1", "2"]:
        print("Invalid input!")
        mode = input("\nPlease choose mode: 1. Single player, 2. Multiplayer: \n")
    if mode == "1":
        ai_mode = True
    return ai_mode

# returneaza size-ul mapei in functie de input
def choose_size():
    size = None
    while size not in range(5, 10):
        size = input("Please choose the size of the table: 5 to 9 \n")
        if size == "quit":
            sys.exit()
        try:
            size = int(size)
            if size not in range(5, 10):
                print("\nWrong size! Please choose from 5 to 9! \n")
                continue
        except ValueError:
            print("\nPlease choose from 5 to 9! \n")

    return size

# returneaza tabla in functie de input
def init_table(size):
    table = []
    for _ in range(size):
        table.append(["O" for _ in range(size)])
    return table

# printeaza tabla
def print_table(table):
    abc = list(string.ascii_uppercase)
    print(f"\n  {' '.join([str(num + 1) for num in range(len(table))])}")
    for index, row in enumerate(table):
        print(f"{abc[index]} {' '.join(row)}")

# returneaza coordonatele pe randuri si coloane
def ask_valid_input(table, board):
    rows = list(string.ascii_uppercase)
    columns = [str(num) for num in range(len(table) + 1)]
    row, col = (-1, -1)
    while (row, col) == (-1, -1):
        coordinates = input("\nPlease give me the coordinates! \n")
        if coordinates == "quit":  # quit
            sys.exit()
        if not coordinates:
            continue
        coordinates = list(coordinates)
        coordinates[0] = coordinates[0].upper()
        if (
            len(coordinates) == 2
            and coordinates[0].upper() in rows[: len(table)]
            and coordinates[1] in columns
        ):
            row = rows.index(coordinates[0])
            col = int(coordinates[1]) - 1
        else:
            print("\nInvalid coordinates!\n")
    return row, col

# returneaza tipul si dimensiunea navei
def select_ship(table, ship_type, board, ai_mode, player):
    ship_types = {3: "Cruiser", 2: "Destroyer"}
    ship_lenght = {v: k for k, v in ship_types.items()}
    if not ai_mode or (ai_mode and player == 1):
        orientation = 0
        while orientation not in [1, 2]:
            orientation = input(
                f"""\nChoose orientation for your {ship_types[ship_type]} (lenght:{ship_lenght[ship_types[ship_type]]}): 
                1 - Horizontal,     2 - Vertical \n"""
            )
            try:
                orientation = int(orientation)

            except ValueError:
                print("\nInvalid orientation!\n")
                continue

    if ai_mode and player == 2:
        row, col, orientation = ai_algorithm.place_ships(table)
    else:
        row, col = ask_valid_input(table, board)
    ship = []
    for i in range(int(ship_type)):
        if orientation == 1:
            new_position = (row, col + i)
            ship.append(new_position)
        else:
            new_position = (row + i, col)
            ship.append(new_position)

    return ship

# returneaza vecinii navei
def generate_neighbors(row, col, table):
    neighbors = [
        (row - 1, col),  # top neighbor
        (row, col + 1),  # right neighbor
        (row + 1, col),  # bottom neighbor
        (row, col - 1),  # left neighbor
    ]
    new_neighbors = []
    for pos in neighbors:
        if (0 <= pos[0] < len(table)) and (0 <= pos[1] < len(table)):
            new_neighbors.append(pos)
    return new_neighbors

# verifica imprejurimile navei
def validate_ship(table, ship_type, board, select_ship, ai_mode, player):
    ship = select_ship(table, ship_type, board, ai_mode, player)
    while ship[-1][0] >= len(table) or ship[-1][1] >= len(table):
        if not ai_mode or (ai_mode and player == 1):
            print("\nYou can't place your ship in the unexplored area!\n")
            print_table(table)
        ship = select_ship(table, ship_type, board, ai_mode, player)
    is_valid = True
    for element in ship:
        row = element[0]
        col = element[1]
        if table[row][col] == "O":
            neigh = generate_neighbors(row, col, table)
            for el in neigh:
                if table[el[0]][el[1]] == "O":
                    is_valid = is_valid and True
                else:
                    is_valid = False
        else:
            is_valid = False

    return is_valid, ship

# amplaseaza nava daca spatiul este liber si daca nu sunt vecini in jur
def put_ship(table, ship_type, board, select_ship, ai_mode, player):
    is_valid, ship = validate_ship(
        table, ship_type, board, select_ship, ai_mode, player
    )
    if is_valid:
        for element in ship:
            row = element[0]
            col = element[1]
            table[row][col] = "X"
        return table, is_valid, ship
    else:
        if not ai_mode or (ai_mode and player == 1):
            print("\nAnother ship is dangerously close!\n")
        return table, is_valid, ship

# returneaza o noua tabla pentru amplasarea noului jucator
def wait_for_another_player(size):
    time.sleep(1)
    os.system("cls || clear")
    print("Next ship's placement phase.")
    new_table = init_table(size)
    return new_table

# returneaza tabla afisata cu nave si o lista cu barcile 
def put_all_ships(table, size, board, ai_mode, player, select_ship):
    if ai_mode and player == 2:
        print("\nNow AI is setting the coordinates for its ships!\n")
        time.sleep(1)
    count_ships = 0
    ships_list = []
    ship_type = 2
    while count_ships != size // 2:
        if not ai_mode or (ai_mode and player == 1):
            print_table(table)
        table, is_valid, ship = put_ship(
            table, ship_type, board, select_ship, ai_mode, player
        )
        ships_list.append(ship)
        if is_valid:
            count_ships += 1
            if ship_type == 2:
                ship_type = 3
            else:
                ship_type = 2
    if not ai_mode or (ai_mode and player == 1):
        print_table(table)
    return table, ships_list

# returneaza coordonatele pentru shooting phase
def shooting_phase(player, table, board, ships_list, ai_mode, ask_valid_input):
    row, col = ask_valid_input(table, board)
    if table[row][col] == "O":
        board[row][col] = "\033[31mM\033[0m"
        if not ai_mode or (ai_mode and player == 1):
            print("\n\033[31mYou've missed! Refilling...\033[0m\n")
        else:
            print("\n\033[31mAI has missed! Refilling...\033[0m\n")
    elif board[row][col] != "O":
        if not ai_mode or (ai_mode and player == 1):
            print("This coordinate has been already tried!")
        return shooting_phase(
            player, table, board, ships_list, ai_mode, ask_valid_input
        )
    elif table[row][col] == "X":
        board[row][col] = "\033[33mH\033[0m"
        if not ai_mode or (ai_mode and player == 1):
            print("\n\033[33mEnemy's shield is down!\033[0m\n")
        else:
            print("\n\033[33mAI hit your ship!\033[0m\n")

    for ship in ships_list:
        is_ship_shink = 0
        for place in ship:
            if board[place[0]][place[1]] == "\033[33mH\033[0m":
                is_ship_shink += 1

        if is_ship_shink == len(ship):
            for place in ship:
                board[place[0]][place[1]] = "\033[32mS\033[0m"
            if not ai_mode or (ai_mode and player == 1):
                print(
                    "\n\033[32mYou've destroyed one of the enemy's ships!\033[0m\n"
                )
            else:
                print("\n\033[32mAI've destroyed one of your ships!\033[0m\n")
            return board
        else:
            continue

    return board

# returneaza tablele pentru player1 si player 2
def display_boards(board_player1, board_player2, player):
    board1 = board_player1.copy()
    board2 = board_player2.copy()
    print("\nStatus maps:\n")
    if player == 1:
        print("Yours        Enemy's")
    else:
        print("Enemy's      Yours")
    abc = list(string.ascii_uppercase)
    boards = (board1, board2)
    for board in boards:
        for index, row in enumerate(board):
            board[index] = str(abc[index] + " " + " ".join(row))

        first_line = str("  " + " ".join([str(num + 1) for num in range(len(board))]))
        board.insert(0, first_line)

    for line1, line2 in zip(board1, board2):
        print(f"{line1}  {line2}")


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

# rreturneaza functia de castig
def is_won(board, table, player):
    flat_board = flatten_list(board)
    flat_table = flatten_list(table)
    if flat_board.count("\033[32mS\033[0m") == flat_table.count("X"):
        return player
    return ""


def shooting_turns(
    player, table_player, board_player, ships_list, ai_mode, ask_valid_input
):
    print(f"Player {player}'s turn:\n")
    board_player = shooting_phase(
        player, table_player, board_player, ships_list, ai_mode, ask_valid_input
    )
    winner = is_won(board_player, table_player, player)
    return board_player, winner


def main():
    ai_mode = choose_mode()
    winner = ""
    size = choose_size()
    limit = choose_turn_limit()
    table1 = init_table(size)
    board_player1 = init_table(size)
    board_player2 = init_table(size)
    player = 1
    table_player1, ships_player1 = put_all_ships(
        table1, size, board_player1, ai_mode, player, select_ship
    )
    if ai_mode:
        table2 = init_table(size)
        player = 2
        table_player2, ships_player2 = put_all_ships(
            table2, size, board_player1, ai_mode, player, select_ship
        )
    else:
        table2 = wait_for_another_player(size)
        player = 2
        table_player2, ships_player2 = put_all_ships(
            table2, size, board_player2, ai_mode, player, select_ship
        )
    time.sleep(1)
    os.system("cls || clear")
    time.sleep(1)
    print("All ships are in position and waiting for your orders!\n")
    time.sleep(1)

    player = 1
    display_boards(board_player1, board_player2, player)
    while limit != 0:
        time.sleep(1)
        print(f"\n\033[34mTurns left: {limit}\033[0m\n")
        if player == 1:
            board_player2, winner = shooting_turns(
                player,
                table_player2,
                board_player2,
                ships_player2,
                ai_mode,
                ask_valid_input,
            )
            display_boards(board_player1, board_player2, player)
            if winner != "":
                break
            player = 2
        elif player == 2:
            limit -= 1
            if ai_mode:
                board_player1, winner = shooting_turns(
                    player,
                    table_player1,
                    board_player1,
                    ships_player1,
                    ai_mode,
                    ai_algorithm.get_ai_shooting_coords,
                )
                time.sleep(2)
            else:
                board_player1, winner = shooting_turns(
                    player,
                    table_player1,
                    board_player1,
                    ships_player1,
                    ai_mode,
                    ask_valid_input,
                )
            display_boards(board_player1, board_player2, player)
            if winner != "":
                break
            player = 1

    if winner == "":
        print(
            "\nNo more turns left! It's a tie!\n"
        )
    else:
        print(f"\nCONGRATS! {winner} won the battle!\n")


if __name__ == "__main__":
    main()