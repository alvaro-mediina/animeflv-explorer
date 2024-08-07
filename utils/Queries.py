from animeflv import AnimeFLV

api = AnimeFLV()

#Busca el anime 
def anime_search(query):
    return api.search(query)

def anime_titles(query):
    animes = anime_search(query)
    return [anime.title for anime in animes]

def anime_ids(query):
    animes = anime_search(query)
    return [anime.id for anime in animes]