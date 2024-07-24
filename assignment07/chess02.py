import time
import asyncio
 
opponents = 24
pair = 30
judit_move = 0.1
opponent_move = 0.5

async def game(x):
    bord_start_time = time.perf_counter()
    for i in range(pair):
        await asyncio.sleep(judit_move)
        print(f"BOARD-{x} ({i+1}) Judit made a move.")
        await asyncio.sleep(opponent_move)
        print(f"BOARD-{x} ({i+1}) Opponent made move.")
        
    print(f"BOARD-{x+1} >>> Finished move in {round(time.perf_counter() - bord_start_time)} secs\n")
    return round(time.perf_counter() - bord_start_time)

async def main():

    start_time = time.perf_counter()
    bord_time = 0   

    tasks = [game(bord) for bord in range(opponents)]
    results = await asyncio.gather(*tasks)
    bord_time = sum(results)
    
    print(f"Board finished in {bord_time} secs.")
    print(f"Finished in {round(time.perf_counter() - start_time)} secs.")

asyncio.run(main())