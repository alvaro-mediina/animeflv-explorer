from utils import Queries as flv

# Simples

#Imprime las id's encontradas
def print_anime_id(query):
    anime_ids = flv.anime_ids(query)
    if len(anime_ids) > 0:
        print(f"\nSe encontraron {len(anime_id)} resultados:")
        for anime_id in anime_ids:
            print(f"\t- {anime_id}")

#Imprime los títulos encontrados
def print_titles(query):
    anime_list = flv.anime_titles(query)
    if len(anime_list) != 0:
        print(f"\nSe encontraron {len(anime_list)} resultados:")
        for anime in anime_list:
            print(f"\t- {anime}")
    else:
        print("No se encontraron resultados.")

 
def print_info(query):
    anime = flv.anime_info(query)
    print(f"\nInformación de {anime.title}:")

#Imprime los episodios encontrados:
def print_episodes(query):
    animes = flv.anime_search(query)
    for anime in animes:
        print(f"\nEpisodios de {anime.title}:")
        for episode in anime.episodes:
            print(f"  - {episode}")


#Menú
def print_menu():
    print("\nVer anime")
    print("-"*9)
    print("(1) Buscar un anime. ")
    print("(Otro) Salir.")
