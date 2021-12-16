 params = (666, 'Alien','Alien')

    test.insert_movie(params)
    test.insert_movie(params)
    test.insert_movie(params)
    test.insert_movie(params)

    conn = test.get_connection()
    cursor = conn.cursor()

    cursor.execute('select * from movies')

       data = cursor.fetchall()