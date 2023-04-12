from connection import cursor, data_base


def delete_user(x):
    user_delete = f'DELETE FROM users WHERE idUsers = {x}'

    cursor.execute(user_delete)
    data_base.commit()


def delete_movie(x):
    movie_delete = f'DELETE FROM movies WHERE idmovies = {x}'

    cursor.execute(movie_delete)
    data_base.commit()

