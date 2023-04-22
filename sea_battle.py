#todo: Реализовать игровую механику морского боя.
# 1. Система в случайном порядке расставляет 10 однопалубных кораблей в игровом поле 10x10
# 2. Между караблями при расстановке должно соблюдаться правило пустых полей.
# 3. Игра заканчивается при 20 промахах.

#todo:
#   Для задачи task12.py "Морской бой", написать Save game. Пользователь может прервать игру и сохраниться, затем продолжить либо выйти.
#   Предусмотереть возможность восстановить игру из заранее сохраненного состояния. Сохранение произвести в файл по имени.

import os
import random

import yaml

NAME_FILE_SAVE = "saved_game.sbs"

field = []
rows = []
cols = []
allowed_miss_count = 0
ship_count = 0

cell_type = {"EMPTY":0, "SHIP":1, "CRUSH":2, "BROKEN":3, "BUSY": 4}

lock_cell_near_ship = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def generate_empty_field(size):
    ret_field = []

    rows = list(range(1, size+1))
    cols = list(map(chr, range(ord("A"), ord("A") + size)))

    for iy in range(0, size):
        ret_field.append([])
        for ix in range(0, size):
            ret_field[iy].append(cell_type["EMPTY"])

    return rows, cols, ret_field

def install_ships(ship_count):
    global field
    count = 0
    while count < ship_count:
        y = random.randrange(0, len(field))
        x = random.randrange(0, len(field[y]))
        if allow_install_ship(x, y) == True:
            count += 1
            install_ship(x, y)

def allow_install_ship(x, y):
    if cell_in_field(x, y) == False: return False
    return get_field_cell(x, y) == cell_type['EMPTY']

def install_ship(x, y):
    set_field_cell(x, y, cell_type['SHIP'])
    cells_busy = list(map(lambda offset: (y + offset[1], x + offset[0]), lock_cell_near_ship))
    for cell in cells_busy:
        set_field_cell(cell[1], cell[0], cell_type['BUSY'])

def get_field_cell(x, y):
    global field
    return field[y][x]

def set_field_cell(x, y, cell):
    global field
    if(cell_in_field(x, y)):
        field[y][x] = cell

def cell_in_field(x, y):
    global field
    if y < 0: return False
    if y >= len(field): return False
    if x < 0: return False
    if x >= len(field[y]): return False
    return True

def draw_field():
    global field, rows, cols
    letter_map = "    "
    letter_map_under = "    "
    for letter in cols:
        letter_map += " "+letter+" "
        letter_map_under += "---"
    print(letter_map)
    print(letter_map_under)
    for line, number in zip(field, rows):
        str_field = str(number).rjust(2) + " |"
        for cell in line:
            cell_show = "░"
            match(cell):
                case 0:
                    cell_show = "░"
                case 1:
                    cell_show = "░"
                case 2:
                    cell_show = "o"
                case 3:
                    cell_show = "X"
                case 4:
                    cell_show = "░"
            str_field += " "+cell_show+" "
        print(str_field)

def shoot(row, col):
    is_hit = False
    try:
        x = cols.index(col)
        y = rows.index(int(row))
        new_cell = 2
        match(get_field_cell(x, y)):
            case 0:
                new_cell = 2
            case 1:
                is_hit = True
                new_cell = 3
            case 2:
                new_cell = 2
            case 3:
                new_cell = 3
            case 4:
                new_cell = 2
        set_field_cell(x, y, new_cell)
    except:
        print("Invalid coordinates")
    return is_hit

def check_command(command):
    global allowed_miss_count, ship_count
    match(command.lower()):
        case "save":
            save_game()
        case "load":
            load_game()
        case _:
            return False
    return True

def init_game():
    global field, rows, cols, allowed_miss_count, ship_count
    rows, cols, field = generate_empty_field(10)
    allowed_miss_count = 10
    ship_count = 10
    install_ships(ship_count)

def start_game():
    global allowed_miss_count, ship_count
    end_game = False
    win = False
    while(not end_game):
        draw_field()
        print("Осталось %d промахов" % allowed_miss_count)

        try:
            row = input("Номер строки: ")
            if(check_command(row)): continue

            col = input("Буква столбца: ")
            if(check_command(col)): continue
        except KeyboardInterrupt:
            print("Bye!")
            break

        if not shoot(row, col.upper()):
            allowed_miss_count -= 1
        else:
            ship_count -= 1

        if(allowed_miss_count == 0):
            end_game = True
            break

        if(ship_count == 0):
            end_game = True
            win = True
            break

    if(win):
        print("вы победили")
    else:
        print("Вы проиграли")

def serialize_game():
    global field, allowed_miss_count, ship_count
    return {"field": field, "miss": allowed_miss_count, "ships": ship_count}

def deserialize_game(object):
    global field, allowed_miss_count, ship_count
    field = object['field']
    allowed_miss_count = object['miss']
    ship_count = object['ships']

def save_game():
    game_state = serialize_game()
    with open(NAME_FILE_SAVE, "w") as file:
        yaml.dump(game_state, file)

def load_game():
    with open(NAME_FILE_SAVE, "r") as file:
        data = yaml.safe_load(file)
        deserialize_game(data)


def main():
    init_game()
    start_game()

main()


