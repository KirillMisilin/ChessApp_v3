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
            knight_black1.style.left = "12.5%";
            knight_black1.style.top = black_position_top;

            let ds_bishop_black = document.querySelector("#ds_bishop_black");
            ds_bishop_black.style.left = "25.0%";
            ds_bishop_black.style.top = black_position_top;

            let queen_black = document.querySelector("#queen_black");
            queen_black.style.left = "37.5%";
            queen_black.style.top = black_position_top;

            let king_black = document.querySelector("#king_black");
            king_black.style.left = "50.0%";
            king_black.style.top = black_position_top;

            let ls_bishop_black = document.querySelector("#ls_bishop_black");
            ls_bishop_black.style.left = "62.5%";
            ls_bishop_black.style.top = black_position_top;

            let knight_black2 = document.querySelector("#knight_black2");
            knight_black2.style.left = "75.0%";
            knight_black2.style.top = black_position_top;

            let rook_black2 = document.querySelector("#rook_black2");
            rook_black2.style.left = "87.5%";
            rook_black2.style.top = black_position_top;


            let rook_white1 = document.querySelector("#rook_white1");
            rook_white1.style.left = "0%";
            rook_white1.style.top = white_position_top;

            let knight_white1 = document.querySelector("#knight_white1");
            knight_white1.style.left = "12.5%";
            knight_white1.style.top = white_position_top;

            let ls_bishop_white = document.querySelector("#ls_bishop_white");
            ls_bishop_white.style.left = "25.0%";
            ls_bishop_white.style.top = white_position_top;

            let queen_white = document.querySelector("#queen_white");
            queen_white.style.left = "37.5%";
            queen_white.style.top = white_position_top;

            let king_white = document.querySelector("#king_white");
            king_white.style.left = "50.0%";
            king_white.style.top = white_position_top;

            let ds_bishop_white = document.querySelector("#ds_bishop_white");
            ds_bishop_white.style.left = "62.5%";
            ds_bishop_white.style.top = white_position_top;

            let knight_white2 = document.querySelector("#knight_white2");
            knight_white2.style.left = "75.0%";
            knight_white2.style.top = white_position_top;

            let rook_white2 = document.querySelector("#rook_white2");
            rook_white2.style.left = "87.5%";
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


let moving = function(id){
    // console.log(id);
    let elem = document.querySelector("#" + id);
    elem.style.zIndex = "10";
}