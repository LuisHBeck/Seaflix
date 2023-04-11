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
