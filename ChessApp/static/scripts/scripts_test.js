let start_position = function(reversed_board){
            if (reversed_board == "true"){
                let chessboard = document.querySelector(".chessboard img");
                chessboard.src = "/static/images/clear_board_reversed.jpg";
            }

            if (reversed_board == "true"){
                black_position_top = "87%";
                white_position_top = "0%";
            } else {
                black_position_top = "0%";
                white_position_top = "87%";
            }

            let rook_black1 = document.querySelector("#rook_black1");
            rook_black1.style.left = "0%";
            rook_black1.style.top = black_position_top;

            let knight_black1 = document.querySelector("#knight_black1");
            knight_black1.style.left = "12%";
            knight_black1.style.top = black_position_top;

            let bishop_black1 = document.querySelector("#bishop_black1");
            bishop_black1.style.left = "24.5%";
            bishop_black1.style.top = black_position_top;

            let queen_black = document.querySelector("#queen_black");
            queen_black.style.left = "37%";
            queen_black.style.top = black_position_top;

            let king_black = document.querySelector("#king_black");
            king_black.style.left = "49.5%";
            king_black.style.top = black_position_top;

            let bishop_black2 = document.querySelector("#bishop_black2");
            bishop_black2.style.left = "62%";
            bishop_black2.style.top = black_position_top;

            let knight_black2 = document.querySelector("#knight_black2");
            knight_black2.style.left = "74.5%";
            knight_black2.style.top = black_position_top;

            let rook_black2 = document.querySelector("#rook_black2");
            rook_black2.style.left = "87%";
            rook_black2.style.top = black_position_top;


            let rook_white1 = document.querySelector("#rook_white1");
            rook_white1.style.left = "0%";
            rook_white1.style.top = white_position_top;

            let knight_white1 = document.querySelector("#knight_white1");
            knight_white1.style.left = "12%";
            knight_white1.style.top = white_position_top;

            let bishop_white1 = document.querySelector("#bishop_white1");
            bishop_white1.style.left = "24.5%";
            bishop_white1.style.top = white_position_top;

            let queen_white = document.querySelector("#queen_white");
            queen_white.style.left = "37%";
            queen_white.style.top = white_position_top;

            let king_white = document.querySelector("#king_white");
            king_white.style.left = "49.5%";
            king_white.style.top = white_position_top;

            let bishop_white2 = document.querySelector("#bishop_white2");
            bishop_white2.style.left = "62%";
            bishop_white2.style.top = white_position_top;

            let knight_white2 = document.querySelector("#knight_white2");
            knight_white2.style.left = "74.5%";
            knight_white2.style.top = white_position_top;

            let rook_white2 = document.querySelector("#rook_white2");
            rook_white2.style.left = "87%";
            rook_white2.style.top = white_position_top;

            let colors = ['black', 'white'];
            for (let i=1; i<9; i++){
                colors.forEach(function(color){
                    let div = document.createElement("div");
                    div.setAttribute("class", "element2");
                    let id = "pawn_" + color + i;
                    div.setAttribute("id", id);
                    div.setAttribute("onclick", "move(id)");
                    div.setAttribute("onmousedown", "moving(id)");
                    div.style.left = 12.5 * (i - 1) +"%";

                    if ((color == 'white' && reversed_board == "true") || (color == 'black' && reversed_board != "true"))
                        div.style.top = "12%";
                    else div.style.top = "75%";

                    let image = document.createElement("img");
                    if (color == 'white')
                        image.src = "/static/images/pawn_white.png";
                    else image.src = "/static/images/pawn_black.png";
                    image.setAttribute("class", "piece");

                    div.appendChild(image);
                    let chessboard = document.querySelector(".chessboard")
                    chessboard.appendChild(div);
                })
            }
        }

let update_piece_position = function(response){
                        response = JSON.parse(response);
                        //console.log("response: ");
                        //console.log(response);
                        elem.style.left = response['coordinate_x'] * 60 + "px";
                        elem.style.top = response['coordinate_y'] * 60 + "px";
                        if (response['piece_to_delete'] != "empty_square"){
                            let piece_to_delete = document.querySelector("#" + response['piece_to_delete']);
                            board.removeChild(piece_to_delete);
                        }
                        if (response['castling_coordinate_x']){
                            let rook = document.querySelector("#" + response['castling_rook']);
                            rook.style.left = response['castling_coordinate_x'] * 60 + "px";
                            rook.style.top = response['castling_coordinate_y'] * 60 + "px";
                        }
                        if (response['promotion'][0]){
                            let div = document.querySelector("#" + response['promotion'][1]);
                            let img = div.querySelector(".piece");
                            div.id = response['promotion'][2]
                            img.src = "/static/images/queen_white.png";
                            img.src = "/static/images/queen_" + response['promotion'][3] + ".png";
                        }
                        if (response['move_has_made']){
                            //let all_moves = response['all_moves'];
                            //let last_move = all_moves.at(-1);
                            let last_move = response['last_move']
                            let moves_div = document.querySelector(".moves");
                            if (response['piece_color'] == "black"){
                                let move_div = document.createElement("div");
                                move_div.innerHTML += last_move + "<br>";
                                move_div.setAttribute("id", last_move);
                                move_div.setAttribute("move_counter", response['move_counter']);
                                move_div.setAttribute("piece_color", response['piece_color']);
                                move_div.setAttribute("onclick", "click_on_move(this.getAttribute('id'), \
                                        this.getAttribute('move_counter'), this.getAttribute('piece_color'))");
                                moves_div.appendChild(move_div);
                                move_div.style.left = "70px";
                                move_div.style.top = 25 * (response['move_counter'] - 1) + "px";
                            }
                            else{
                                let move_div = document.createElement("div");
                                move_div.innerHTML += last_move;
                                move_div.setAttribute("id", last_move);
                                move_div.setAttribute("move_counter", response['move_counter']);
                                move_div.setAttribute("piece_color", response['piece_color']);
                                move_div.setAttribute("onclick", "click_on_move(this.getAttribute('id'), \
                                        this.getAttribute('move_counter'), this.getAttribute('piece_color'))");
                                moves_div.appendChild(move_div);
                                move_div.style.top = 25 * (response['move_counter'] - 1) + "px";
                            }
                            //let i = 0;
                            //all_moves.forEach(function(move){
                                //i += 1;
                                //document.querySelector(".moves").innerHTML += move;
                                //if (i % 2 == 0){
                                    //document.querySelector(".moves").innerHTML += 'qqq';
                                //}
                            //});
                            //document.querySelector(".moves").innerHTML = response['all_moves'];
                        }
                    }

let moving = function(id){
    // console.log(id);
    let board = document.querySelector(".chessboard");
    let board_coordinates = board.getBoundingClientRect();
    let elem = document.querySelector("#" + id);
    let old_coordinates = elem.getBoundingClientRect()
    elem.setAttribute("old_coordinates_x", Math.round((old_coordinates.x - board_coordinates.x) / 60))
    elem.setAttribute("old_coordinates_y", Math.round((old_coordinates.y - board_coordinates.y) / 60))
    elem.style.zIndex = "10";
}