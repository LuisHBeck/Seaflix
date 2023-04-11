from connection import cursor, data_base


def modify_user(x, y, z):
    update_user = f'UPDATE movies SET {x} = "{y}" WHERE idmovies = {z}'

    cursor.execute(update_user)
    data_base.commit()


def modify_movie(x, y, z):
    update_movie = f'UPDATE users SET {x} = "{y}" WHERE idUsers = {z}'

    cursor.execute(update_movie)
    data_base.commit()
