from connection import cursor, data_base


def creat_user(name, age, email, plan, type, id):
    insert_user = f'''INSERT INTO users(user_name, user_age, user_email, user_plan, user_type, user_id)
    values
    ('{name}', {age}, '{email}', '{plan}', '{type}', {id})'''

    cursor.execute(insert_user)
    data_base.commit()


def creat_movie(name, description, plan, classification):
    insert_movie = f'''INSERT INTO movies(movie_name, movie_desc, movie_plan, movie_class)
        values
        ('{name}', '{description}', '{plan}', {classification})'''

    cursor.execute(insert_movie)
    data_base.commit()
