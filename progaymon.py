import asyncio
import httpx
import time

async def get_pokemon_names_with_ability(client, url, ability_name):
    start_time = time.perf_counter()
    print(f'{time.ctime()} - Fetching {ability_name} from {url}')
    
    resp = await client.get(url)
    ability_data = resp.json()
    
    pokemon_names = [pokemon['pokemon']['name'] for pokemon in ability_data['pokemon']]
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    print(f'{time.ctime()} - Completed fetching {ability_name}. Time taken: {elapsed_time} seconds')
    
    return pokemon_names, elapsed_time

async def get_abilities_pokemon_names():
    async with httpx.AsyncClient() as client:
        urls = {
            "battle-armor": "https://pokeapi.co/api/v2/ability/battle-armor",
            "speed-boost": "https://pokeapi.co/api/v2/ability/speed-boost"
        }

        tasks = [asyncio.create_task(get_pokemon_names_with_ability(client, url, ability)) for ability, url in urls.items()]
        
        results = await asyncio.gather(*tasks)
        
        names_dict = {ability: names for ability, (names, _) in zip(urls.keys(), results)}
        times_dict = {ability: elapsed_time for ability, (_, elapsed_time) in zip(urls.keys(), results)}
        
        return names_dict, times_dict

async def index():
    start_time = time.perf_counter()
    
    abilities_pokemon_names, times_taken = await get_abilities_pokemon_names()
    
    end_time = time.perf_counter()

    for ability, names in abilities_pokemon_names.items():
        print(f"\nจำนวน Pokemon ที่มีความสามารถ {ability} ({len(names)} total):")
        for name in names:
            print(f"- {name}")
    
    print("\nเวลาในการรันสำหรับแต่ละความสามารถ:")
    for ability, time_taken in times_taken.items():
        print(f"- {ability}: {time_taken:.4f} seconds")
    
    print(f"\n{time.ctime()} - Asynchronous fetch completed. Total time taken: {end_time - start_time} seconds")

if __name__ == '__main__':
    asyncio.run(index())
