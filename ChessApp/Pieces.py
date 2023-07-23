import re


board_dict = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h"}


class Piece:
    def __init__(self, name, position):
        self.name = name
        if re.search("black", name):
            self.color = "black"
        else:
            self.color = "white"
        self.position = position
        # self.position_alt = [board_dict[str(position[0])], 8 - position[1]]
        self.has_not_moved = True
        self.has_taken = False
        self.name_alt = ""

    def get_position_alt(self, position=None):
        position = self.position.copy() if not position else position
        return [board_dict[str(position[0])], 8 - position[1]]

    def get_position(self):
        pass

    def is_right_move(self, new_position):
        pass


class Rook(Piece):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.name_alt = "R"

    def is_right_move(self, new_position):
        if self.position[0] == new_position[0] or self.position[1] == new_position[1]:
            return True
        return False


class Knight(Piece):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.name_alt = "Kn"

    def is_right_move(self, new_position):
        if [abs(self.position[0] - new_position[0]), abs(self.position[1] - new_position[1])] == [2, 1] \
                or [abs(self.position[1] - new_position[1]), abs(self.position[0] - new_position[0])] == [2, 1]:
            # if abs(self.position[0] - new_position[0]) == 2 and abs(self.position[1] - new_position[1]) == 1
            return True
        return False


class Bishop(Piece):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.name_alt = "B"

    def is_right_move(self, new_position):
        if abs(self.position[0] - new_position[0]) == abs(self.position[1] - new_position[1]):
            return True
        return False


class Queen(Piece):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.name_alt = "Q"

    def is_right_move(self, new_position):
        if abs(self.position[0] - new_position[0]) == abs(self.position[1] - new_position[1]) \
                or (self.position[0] == new_position[0] or self.position[1] == new_position[1]):
            return True
        return False


class King(Piece):
    def __init__(self, name, position):
        super().__init__(name, position)
        self.name_alt = "K"

    def is_right_move(self, new_position):
        if abs(self.position[0] - new_position[0]) < 2 and abs(self.position[1] - new_position[1]) < 2 \
                or (self.position[1] == new_position[1] and (new_position[0] == 2 or new_position[0] == 6)
                    and self.has_not_moved):
            return True
        return False


class Pawn(Piece):
    def __init__(self, name, position):
        super().__init__(name, position)

    def is_right_move(self, new_position):
        if (abs(self.position[0] - new_position[0]) < 2
            and self.position[1] - new_position[1] == 1 and self.color == "white") \
                or (abs(self.position[0] - new_position[0]) < 2 and self.position[1] - new_position[1] == -1
                    and self.color == "black") \
                or (self.position[0] == new_position[0] and self.has_not_moved and self.position[1] == 1
                    and new_position[1] == 3) \
                or (self.position[0] == new_position[0] and self.has_not_moved and self.position[1] == 6
                    and new_position[1] == 4):
            return True
        return False


class EmptySquare:
    def __init__(self):
        self.name = "empty_square"
        self.color = "empty"
        self.position = None
        self.has_not_moved = True
        self.has_taken = True
