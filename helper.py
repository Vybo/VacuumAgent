import  error_messages


def character_to_coordinate(character):
    if character.isalpha():
        return ord(character.lower()) - ord('a')
    else:
        error_messages.wrong_coordinate(character)
        return False


def chess_coordinate_to_x(coordinate):
    return character_to_coordinate(coordinate[0:1])


def chess_coordinate_to_y(coordinate):
    try:
        if len(coordinate) == 3:
            return int(coordinate[1:3])-1
        elif len(coordinate) == 2:
            return int(coordinate[1:2])-1
        else:
            return False
    except ValueError:
        error_messages.wrong_coordinate(coordinate)
        return False


def coordinate_to_chess(coordinate):
    return chr(coordinate+ord('a'))