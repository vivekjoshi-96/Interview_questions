"""" A ride in an Amusement park starts at the ground level. it moves either up or down.
Write a program to count the number of sinks. A raise is defined as a move above ground from start position
followed by any string of moves up or down until the ride reaches the start position again.
A sink is defined as a move below ground from start position
followed by any string of moves up or down until the ride reaches the start position again.
"""


def main():
    moves = 'HLLHHHHLLLLLHHHHHHLLLLLLLLHHHHLLHH'
    curr_pos = 0
    sinks = 0
    for letter in moves:
        if letter == 'H':
            curr_pos += 1
        elif letter == 'L':
            curr_pos -= 1
            if curr_pos == -1:
                sinks += 1
        else:
            print("Invalid string")
            exit()
    print(sinks)


main()
