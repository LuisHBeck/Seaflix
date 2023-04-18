from connection import cursor


def read_user():
    read_user_info = f'SELECT * from users'

    cursor.execute(read_user_info)
    result = cursor.fetchall()

    return result


def read_movie():
    read_movie_info = f'SELECT * from movies'

    cursor.execute(read_movie_info)
    result = cursor.fetchall()

    return result


def search_user(id_user):
    user_search = f'SELECT * from users WHERE idUsers= {id_user}'

    cursor.execute(user_search)
    result = cursor.fetchall()

    return result

