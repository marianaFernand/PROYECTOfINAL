import json

data_pelicula= """{"Title":"Rojo","Year":"2018","Rated":"N/A","Released":"12 Jul 2019","Runtime":"109 min","Genre":"Drama, Mystery, Thriller","Director":"Benjamín Naishtat","Writer":"Benjamín Naishtat","Actors":"Claudio Martínez Bel, Mara Bestelli, Alfredo Castro, Rudy Chernicoff","Plot":"Set in Argentina during the mid-1970s, Benjamín Naishtat's hypnotic drama follows a successful lawyer whose picture-perfect life begins to unravel when a private detective comes to his seemingly quiet small town and starts asking questions","Language":"Spanish","Country":"Argentina, Brazil, France, Netherlands, Germany, Belgium, Switzerland","Awards":"N/A","Poster":"https://m.media-amazon.com/images/M/MV5BN2RkNDAwZDgtZDBhNC00ZTVkLTgzMWItMzhiOTJiMGM3Yzk5XkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"6.4/10"},{"Source":"Rotten Tomatoes","Value":"96%"},{"Source":"Metacritic","Value":"75/100"}],"Metascore":"75","imdbRating":"6.4","imdbVotes":"679","imdbID":"tt8956390","Type":"movie","DVD":"N/A","BoxOffice":"N/A","Production":"DistriB Films","Website":"N/A","Response":"True"}"""
pelicula = json.loads(data_peli)


