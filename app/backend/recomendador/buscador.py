import tmdbsimple as tmdb
import requests


url = "https://api.themoviedb.org/3/movie/"
url_img = "https://image.tmdb.org/t/p/original"
url_imdb = "https://www.imdb.com/title/"

headers = {
    "accept": "application/json",
    "Authorization": "Header"
}

tmdb.API_KEY = 'TU_API_KEY'

search = tmdb.Search()


def listar_ids(pelis):
    ids = []

    if len(pelis) > 0:
        for p in pelis:
            if not len(p) > 100:
                response = search.movie(query=p)
            if response['total_results'] > 0:
                ids.append(response['results'][0]['id'])

    return ids


def sacar_datos_pelis(pelis):
    ids = listar_ids(pelis)
    datos = []

    for i in ids:
        response = requests.get(
            f"{url}/{i}?language=es-ES", headers=headers, timeout=3)

        print(response)

        if response.status_code == 200:
            data = response.json()
            show_data = {"nombre": data['title'], "sinopsis": data['overview'],
                         "poster": "", "anyo": data["release_date"][0:4], "IMDB": ""}

            if data['imdb_id'] is None:
                show_data['IMDB'] = ""
            else:
                show_data['IMDB'] = f"{url_imdb}{data['imdb_id']}"

            if data['poster_path'] is None:
                show_data['poster'] = ""
            else:
                show_data['poster'] = f"{url_img}{data['poster_path']} "

            datos.append(show_data)

    return datos
