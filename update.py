from connection import cursor, data_base


def modify_user(user_id, name, age, email, plan, u_type):
    update_user = f'UPDATE users SET user_name="{name}", user_age={age}, user_email="{email}", user_plan="{plan}", user_type="{u_type}"  WHERE idUsers = {user_id}'

    cursor.execute(update_user)
    data_base.commit()


def modify_movie(x, y, z):
    update_movie = f'UPDATE movies SET {x} = "{y}" WHERE idmovies = {z}'

    cursor.execute(update_movie)
    data_base.commit()
