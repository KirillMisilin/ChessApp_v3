from .Pieces import *
from .models import Game as Gamedb, Move
import copy


class Game:

    def __init__(self, player_white='Boba', player_black='Biba'):
        self.player_white = player_white
        self.player_black = player_black

        self.gamedb = Gamedb(player_white_username=self.player_white, player_black_username=self.player_black)
        self.gamedb.save()

        self.rook_black1 = Rook("rook_black1", [0, 0])
        self.rook_black2 = Rook("rook_black2", [7, 0])
        self.knight_black1 = Knight("knight_black1", [1, 0])
        self.knight_black2 = Knight("knight_black2", [6, 0])
        self.bishop_black1 = Bishop("bishop_black1", [2, 0])
        self.bishop_black2 = Bishop("bishop_black2", [5, 0])
        self.king_black = King("king_black", [4, 0])
        self.queen_black = Queen("queen_black", [3, 0])
        self.pawn_black1 = Pawn("pawn_black1", [0, 1])
        self.pawn_black2 = Pawn("pawn_black2", [1, 1])
        self.pawn_black3 = Pawn("pawn_black3", [2, 1])
        self.pawn_black4 = Pawn("pawn_black4", [3, 1])
        self.pawn_black5 = Pawn("pawn_black5", [4, 1])
        self.pawn_black6 = Pawn("pawn_black6", [5, 1])
        self.pawn_black7 = Pawn("pawn_black7", [6, 1])
        self.pawn_black8 = Pawn("pawn_black8", [7, 1])

        self.rook_white1 = Rook("rook_white1", [0, 7])
        self.rook_white2 = Rook("rook_white2", [7, 7])
        self.knight_white1 = Knight("knight_white1", [1, 7])
        self.knight_white2 = Knight("knight_white2", [6, 7])
        self.bishop_white1 = Bishop("bishop_white1", [2, 7])
        self.bishop_white2 = Bishop("bishop_white2", [5, 7])
        self.king_white = King("king_white", [4, 7])
        self.queen_white = Queen("queen_white", [3, 7])
        self.pawn_white1 = Pawn("pawn_white1", [0, 6])
        self.pawn_white2 = Pawn("pawn_white2", [1, 6])
        self.pawn_white3 = Pawn("pawn_white3", [2, 6])
        self.pawn_white4 = Pawn("pawn_white4", [3, 6])
        self.pawn_white5 = Pawn("pawn_white5", [4, 6])
        self.pawn_white6 = Pawn("pawn_white6", [5, 6])
        self.pawn_white7 = Pawn("pawn_white7", [6, 6])
        self.pawn_white8 = Pawn("pawn_white8", [7, 6])

        self.empty_square = EmptySquare()

        self.number_of_white_queens = 1
        self.number_of_black_queens = 1

        self.current_position = self.get_start_position3()

        self.black_pieces = [piece[0] for piece in self.current_position]
        self.black_pawns = [pawn[1] for pawn in self.current_position]
        self.white_pieces = [piece[7] for piece in self.current_position]
        self.white_pawns = [pawn[6] for pawn in self.current_position]

        self.current_black_pieces = [piece for piece in self.black_pieces if not piece.has_taken]
        self.current_black_pawns = [pawn for pawn in self.black_pawns if not pawn.has_taken]
        self.current_white_pieces = [piece for piece in self.white_pieces if not piece.has_taken]
        self.current_white_pawns = [pawn for pawn in self.white_pawns if not pawn.has_taken]

        self.white_to_move = True
        self.move_counter = 0
        self.move_has_made = False

        self.board_dict = {"0": "a", "1": "b", "2": "c", "3": "d", "4": "e", "5": "f", "6": "g", "7": "h"}
        self.board_dict_inv = {value: key for key, value in self.board_dict.items()}

        self.response = None

    def get_response(self):
        return self.response

    def get_start_position3(self):
        return [[self.rook_black1, self.pawn_black1, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white1, self.rook_white1],
                [self.knight_black1, self.pawn_black2, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white2, self.knight_white1],
                [self.bishop_black1, self.pawn_black3, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white3, self.bishop_white1],
                [self.queen_black, self.pawn_black4, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white4, self.queen_white],
                [self.king_black, self.pawn_black5, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white5, self.king_white],
                [self.bishop_black2, self.pawn_black6, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white6, self.bishop_white2],
                [self.knight_black2, self.pawn_black7, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white7, self.knight_white2],
                [self.rook_black2, self.pawn_black8, self.empty_square, self.empty_square,
                 self.empty_square, self.empty_square, self.pawn_white8, self.rook_white2]]

    def print_current_position(self):
        return [self.current_position[i][j].name for i in range(0, 8) for j in range(0, 8)]

    def print_current_coordinates(self):
        return [self.current_position[i][j].position for i in range(0, 8) for j in range(0, 8)]

    def update_taken_pieces(self):
        self.current_black_pieces = [piece for piece in self.black_pieces if not piece.has_taken]
        self.current_black_pawns = [pawn for pawn in self.black_pawns if not pawn.has_taken]
        self.current_white_pieces = [piece for piece in self.white_pieces if not piece.has_taken]
        self.current_white_pawns = [pawn for pawn in self.white_pawns if not pawn.has_taken]

    def path_is_empty(self, piece_object, new_position):
        vector = [new_position[0] - piece_object.position[0], new_position[1] - piece_object.position[1]]
        vector_norm = [int((vector[0] / abs(vector[0])) if vector[0] != 0 else 0),
                       int((vector[1] / abs(vector[1])) if vector[1] != 0 else 0)]
        for i in range(1, max(abs(vector[0]), abs(vector[1]))):
            coordinates_to_check = [piece_object.position[0] + vector_norm[0] * i,
                                    piece_object.position[1] + vector_norm[1] * i]
            if type(self.current_position[coordinates_to_check[0]][coordinates_to_check[1]]) is not EmptySquare:
                return False
        return True

    def is_check(self, king, new_position):
        if king.color == "white":
            self.current_position[king.position[0]][king.position[1]] = self.empty_square
            for black_piece in self.current_black_pieces:
                if self.can_make_move(black_piece, new_position):
                    self.current_position[king.position[0]][king.position[1]] = king
                    return True
            self.current_position[king.position[0]][king.position[1]] = king
            for black_piece in self.current_black_pawns:
                if self.can_make_move(black_piece, new_position):
                    return True
        else:
            self.current_position[king.position[0]][king.position[1]] = self.empty_square
            for white_piece in self.current_white_pieces:
                if self.can_make_move(white_piece, new_position):
                    return True
            self.current_position[king.position[0]][king.position[1]] = king
            for white_piece in self.current_white_pawns:
                if self.can_make_move(white_piece, new_position):
                    return True
        self.current_position[king.position[0]][king.position[1]] = king
        return False

    def update_current_position(self, piece_object, new_position):  # фигура со старой позицией, новая позиция фигуры
        piece_object = self.__getattribute__(piece_object.name)
        self.current_position[piece_object.position[0]][piece_object.position[1]] = self.empty_square
        piece_object.position = [new_position[0], new_position[1]]
        self.current_position[piece_object.position[0]][piece_object.position[1]] = piece_object
        piece_object.has_not_moved = False
        self.current_black_pieces = [self.current_position[j][i] for i in range(0, 8) for j in range(0, 8)
                                     if (type(self.current_position[j][i]) in {Rook, Knight, Bishop, Queen, King}
                                         and self.current_position[j][i].color == "black")]
        self.current_white_pieces = [self.current_position[j][i] for i in range(0, 8) for j in range(0, 8)
                                     if (type(self.current_position[j][i]) in {Rook, Knight, Bishop, Queen, King}
                                         and self.current_position[j][i].color == "white")]
        self.current_black_pawns = [self.current_position[j][i] for i in range(0, 8) for j in range(0, 8)
                                    if (type(self.current_position[j][i]) is Pawn
                                        and self.current_position[j][i].color == "black")]
        self.current_white_pawns = [self.current_position[j][i] for i in range(0, 8) for j in range(0, 8)
                                    if (type(self.current_position[j][i]) is Pawn
                                        and self.current_position[j][i].color == "white")]

    def can_make_move(self, piece_object, new_position):
        # проверка на возможность такого хода на пустой доске
        if piece_object.is_right_move([new_position[0], new_position[1]]):
            # проверка на то, что на пути нет других фигур
            if type(piece_object) is Knight or self.path_is_empty(piece_object, [new_position[0], new_position[1]]):
                # свою фигуру есть нельзя
                if piece_object.color != self.current_position[new_position[0]][new_position[1]].color:
                    piece_to_delete = self.current_position[new_position[0]][new_position[1]]

                    if type(piece_object) is Pawn:
                        if (piece_to_delete.name == "empty_square" and piece_object.position[0] == new_position[0]) \
                                or (piece_to_delete.name != "empty_square"
                                    and piece_object.position[0] != new_position[0]):
                            return True
                        else:
                            return False

                    if type(piece_object) is King:
                        if new_position[0] == 2 and type(self.current_position[0][piece_object.position[1]]) is Rook \
                                and self.current_position[0][piece_object.position[1]].has_not_moved \
                                and type(self.current_position[3][piece_object.position[1]]) is EmptySquare \
                                and type(self.current_position[2][piece_object.position[1]]) is EmptySquare \
                                and type(self.current_position[1][piece_object.position[1]]) is EmptySquare \
                                and not self.is_check(piece_object, [4, piece_object.position[1]]) \
                                and not self.is_check(piece_object, [3, piece_object.position[1]]) \
                                and not self.is_check(piece_object, [2, piece_object.position[1]]):
                            return True

                        elif new_position[0] == 6 and type(self.current_position[7][piece_object.position[1]]) is Rook \
                                and self.current_position[7][piece_object.position[1]].has_not_moved \
                                and type(self.current_position[6][piece_object.position[1]]) is EmptySquare \
                                and type(self.current_position[5][piece_object.position[1]]) is EmptySquare \
                                and not self.is_check(piece_object, [4, piece_object.position[1]]) \
                                and not self.is_check(piece_object, [5, piece_object.position[1]]) \
                                and not self.is_check(piece_object, [6, piece_object.position[1]]):
                            return True

                        elif (new_position[0] == 2 or new_position[0] == 6) and piece_object.has_not_moved:
                            return False
                    return True
        return False

    def make_move(self, request):
        piece_to_delete = self.empty_square
        castling_rook = self.empty_square
        castling_position = [None, None]
        promotion = [False, None, None]
        if type(request) is list:
            coordinate_x = int(request[2][0])
            coordinate_y = int(request[2][1])
            piece_object = self.__getattribute__(request[0])
        elif type(request) is dict:
            coordinate_x = int(request['coordinate_x'])
            coordinate_y = int(request['coordinate_y'])
            piece = request['piece']
            piece_object = self.__getattribute__(piece)
        else:
            coordinate_x = int(request.POST['coordinate_x'])  # новые координаты
            coordinate_y = int(request.POST['coordinate_y'])  # новые координаты
            piece = request.POST['piece']
            piece_object = self.__getattribute__(piece)

        old_piece_position = piece_object.position.copy()
        old_piece_has_not_moved = piece_object.has_not_moved
        old_current_position = copy.deepcopy(self.current_position)
        old_current_white_pieces = copy.deepcopy(self.current_white_pieces)
        old_current_black_pieces = copy.deepcopy(self.current_black_pieces)
        old_current_white_pawns = copy.deepcopy(self.current_white_pawns)
        old_current_black_pawns = copy.deepcopy(self.current_black_pawns)

        if (self.white_to_move and piece_object.color == "white") \
                or (not self.white_to_move and piece_object.color == "black"):

            can_make_move = self.can_make_move(piece_object, [coordinate_x, coordinate_y])
            if can_make_move:
                if type(piece_object) is King and piece_object.has_not_moved:
                    if coordinate_x == 2:
                        castling_rook = self.current_position[0][piece_object.position[1]]
                        castling_position = [3, piece_object.position[1]]
                        self.update_current_position(castling_rook, [3, piece_object.position[1]])  # обновление ладьи
                    if coordinate_x == 6:
                        castling_rook = self.current_position[7][piece_object.position[1]]
                        castling_position = [5, piece_object.position[1]]
                        self.update_current_position(castling_rook, [5, piece_object.position[1]])  # обновление ладьи
                if type(piece_object) is Pawn and (coordinate_y == 0 or coordinate_y == 7):
                    self.__dict__["number_of_" + piece_object.color + "_queens"] += 1
                    queen_name = "queen_" + piece_object.color + \
                                 str(self.__getattribute__("number_of_" + piece_object.color + "_queens"))
                    self.__setattr__(queen_name, Queen(queen_name, piece_object.position))
                    piece_object.has_taken = True
                    promotion = [True, piece_object.name, queen_name, piece_object.color]
                    piece_object = self.__dict__[queen_name]

                piece_to_delete = self.current_position[coordinate_x][coordinate_y]
                piece_to_delete.has_taken = True
                self.update_taken_pieces()
                self.update_current_position(piece_object, [coordinate_x, coordinate_y])
            if self.is_check(self.king_white if piece_object.color == "white" else self.king_black,
                             self.king_white.position if piece_object.color == "white"
                             else self.king_black.position):
                piece_object.position = old_piece_position.copy()
                piece_object.has_not_moved = old_piece_has_not_moved
                self.current_position = copy.deepcopy(old_current_position)
                piece_to_delete = self.empty_square
                castling_rook = self.empty_square
                castling_position = [None, None]
                promotion = [False, None, None]
                self.current_white_pieces = copy.deepcopy(old_current_white_pieces)
                self.current_black_pieces = copy.deepcopy(old_current_black_pieces)
                self.current_white_pawns = copy.deepcopy(old_current_white_pawns)
                self.current_black_pawns = copy.deepcopy(old_current_black_pawns)

            if old_piece_position != piece_object.position:  # ход сделан
                self.white_to_move = not self.white_to_move

        if old_piece_position != piece_object.position:
            self.move_has_made = True
            if not self.white_to_move:
                self.move_counter += 1
        else:
            self.move_has_made = False

        is_check = self.is_check(self.king_white if piece_object.color == "black" else self.king_black,
                                 self.king_white.position if piece_object.color == "black" else self.king_black.position)

        response = {
            'piece': piece_object.name,
            'piece_color': piece_object.color,
            'coordinate_x': piece_object.position[0],
            'coordinate_y': piece_object.position[1],
            'piece_to_delete': piece_to_delete.name,
            'castling_rook': castling_rook.name,
            'castling_coordinate_x': castling_position[0],
            'castling_coordinate_y': castling_position[1],
            'promotion': promotion,
            'is_check': is_check,
            'old_position': old_piece_position,
            'move_counter': self.move_counter,
            'move_has_made': self.move_has_made
        }
        return response

    def save_in_db(self, response):
        if self.move_has_made:
            piece_object = self.__getattribute__(response['piece'])
            old_position_alt = piece_object.get_position_alt(response['old_position'])
            takes_str = "" if response['piece_to_delete'] == "empty_square" else "X"
            is_check = "+" if response['is_check'] else ""
            promotion = "=Q" if response['promotion'][0] else ""
            move = piece_object.name_alt + old_position_alt[0] + str(old_position_alt[1]) + takes_str \
                   + str(piece_object.get_position_alt()[0]) + str(piece_object.get_position_alt()[1]) \
                   + promotion + is_check
            Move(move_counter=self.move_counter, piece=piece_object.name,
                 old_position=str(response['old_position'][0]) + str(response['old_position'][1]),
                 new_position=str(response['coordinate_x']) + str(response['coordinate_y']),
                 who_to_move="white" if not self.white_to_move else "black",
                 move=move, game_id=self.gamedb.id).save()

    def data_from_db_move(self, db_move):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        pieces_db_names = {'R': 'rook', 'B': 'bishop', 'Q': 'Queen', 'K': 'king'}
        if db_move[0] in letters:
            piece = "pawn"
            old_position = db_move[0] + db_move[1]
            new_position = db_move[2] + db_move[3] if db_move[2] != 'X' else db_move[3] + db_move[4]
        elif db_move[0] + db_move[1] == "Kn":
            piece = "knight"
            old_position = db_move[2] + db_move[3]
            new_position = db_move[4] + db_move[5] if db_move[4] != 'X' else db_move[5] + db_move[6]
        else:
            piece = pieces_db_names[db_move[0]]
            old_position = db_move[1] + db_move[2]
            new_position = db_move[3] + db_move[4] if db_move[3] != 'X' else db_move[4] + db_move[5]
        old_position = [int(self.board_dict_inv[old_position[0]]), 8 - int(old_position[1])]
        new_position = [int(self.board_dict_inv[new_position[0]]), 8 - int(new_position[1])]
        return [piece, old_position, new_position]

    def run(self, request):
        response = self.make_move(request)
        self.save_in_db(response)

        all_moves = []
        moves_from_db = Move.objects.filter(game_id=self.gamedb.id)
        for move in moves_from_db:
            all_moves.append(move.move)
        response.update({'all_moves': all_moves})
        if moves_from_db.last():
            response.update({'last_move': moves_from_db.last().move})
        self.response = response
        return response

    def get_position_from_db(self, request):
        target_move = Move.objects.get(game_id=request.POST['game_id'],
                                       move=request.POST['last_move'],
                                       who_to_move=request.POST['piece_color'],
                                       move_counter=request.POST['move_counter'])
        moves_from_db = Move.objects.filter(game_id=request.POST['game_id'], move_counter__lte=target_move.move_counter)
        game2 = Game()
        piece_names_to_delete = []
        for move in moves_from_db:
            prepared_move = [move.piece, [int(move.old_position[0]), int(move.old_position[1])],
                              [int(move.new_position[0]), int(move.new_position[1])]]
            response = game2.make_move(prepared_move)
        pieces = []
        for piece in game2.black_pieces + game2.black_pawns + game2.white_pieces + game2.white_pawns:
            pieces.append([piece.name, piece.position, piece.has_taken])
        return pieces


# game = Game("Biba", "Boba")
