import time 

opponents = 24
pair = 30
judit_move = 0.09
opponent_move = 0.91

def game(x):
    board_start_time = time.perf_counter()
    for i in range(pair):
        time.sleep(judit_move)
        print(f"BOARD{x+1} - Judit move.({i+1})")
        
        time.sleep(opponent_move)
        print(f"BOARD{x+1} - Opponent move.({i+1})")
        
    print(f"BOARD{x+1} >>> Finished move in {round(time.perf_counter() - board_start_time)} secs\n")
    return round(time.perf_counter() - board_start_time)

if __name__ == "__main__":
    start_time = time.perf_counter()
    board_time = 0
    for board in range(opponents):
        board_time += game(board)
    
    print(f"Board exhibition finished in {board_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")
