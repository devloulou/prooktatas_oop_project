import psycopg2 as postgres

## python logging

# ETL folyamatot szeretnék majd fejelszteni, és az ETL folyamat működéséhez akarunk
# egy modul-t fejleszteni

# ETL - Extract Transform Load -> gyakorlatilag az adat adatbázisba való integrálásának egy módszerét jelenti
# legyen adatbázisban logolva a folyamat
# újrafuttattható legyen minden része: 
# ősfeltöltés -> a meglévő adatok tömeges, egyszeri feldolgozása
# az objektumok létrehozása is történjen pythonból
# maga az etl-hez szükséges funkciók lefejlesztése

class PostgresHandler:

    movies_table = 'movies'
    movie_meta_table = 'movie_meta'
    log_table = 'movie_meta_log'

    cre_movies_table = f"""
        CREATE TABLE {movies_table} (
            id serial primary key,
            search_meta_id int,
            movie_name varchar(100) ,
            creation_date date DEFAULT now()
        )
    """

    cre_movie_meta = f"""
    create table {movie_meta_table} (id serial primary key,
        movie_id int,
        adult boolean,
        backdrop_path varchar(32),
        original_language varchar(2),
        original_title varchar(7),
        overview varchar(244),
        popularity decimal(2, 1),
        poster_path varchar(32),
        release_date date,
        title varchar(7),
        video boolean,
        vote_average decimal(1, 1),
        vote_count int,
        poster_folder_path varchar(250),
        creation_date date default now(),
        constraint movie_id_fk
        foreign key (movie_id)
        references movies(id)
        on delete cascade
        )
    """
    cre_log_table = f"""
    create table {log_table} (
        id serial primary key,
        process_name varchar(250),
        status varchar(50),
        error_message varchar(4000),
        creation_date date default now()
        )
    """

    check_table = """
    select count(*) from information_schema.tables t 
        where t.table_name = '{table_name}'
        and t.table_schema = 'public'
    """

    insert_movies = f"""
    insert into {movies_table} (search_meta_id, movie_name) values (%s, %s) returning id;
    """

    insert_movie_meta = f"""
    insert into {movie_meta_table} (movie_id,
        adult,
        backdrop_path,
        original_language,
        original_title,
        overview,
        popularity,
        poster_path,
        release_date,
        title,
        video,
        vote_average,
        vote_count,
        poster_folder_path) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """

    def __init__(self):
        pass

    def get_connection(self):
        return postgres.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port=5432,
            database="postgres"
            )

    def etl_log(self, process_name, status, error_message=''):
        # itt is hibára futhat az execute, majd ezt is le kellene kezelni
        conn = self.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(f"insert into {self.log_table} (process_name, status, error_message)\
                values ('{process_name}', '{status}', '{error_message}')")
        except Exception as e:
            conn.rollback()
            print(str(e))
        finally:
            conn.commit()
            cursor.close()
            conn.close()

    def create_database_objects(self):
        conn = self.get_connection()
        cursor = conn.cursor()

        # meg kell nézni, hogy létezik e az adott tábla: ha létezik dobjuk el
        # hozzuk létre

        cursor.execute(self.check_table.format(table_name=self.movies_table))

        if cursor.fetchone()[0]:
            cursor.execute(f'drop table {self.movies_table} cascade')
            conn.commit()

        cursor.execute(self.check_table.format(table_name=self.movie_meta_table))

        if cursor.fetchone()[0]:
            cursor.execute(f'drop table {self.movie_meta_table}')
            conn.commit()

        cursor.execute(self.check_table.format(table_name=self.log_table))

        if cursor.fetchone()[0]:
            cursor.execute(f'drop table {self.log_table}')
            conn.commit()

        cursor.execute(self.cre_movies_table)
        cursor.execute(self.cre_movie_meta)
        cursor.execute(self.cre_log_table)

        # ide kell majd egy log bejegyzés

        conn.commit()
        cursor.close()
        conn.close()
        # bármelyik fenti adatbázis művelet hibára futhat, és ezt le kellene kezelni

        self.etl_log(process_name='create_database_objects', status='OK')

    def insert_movie_meta(self, params):
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(self.insert_movie_meta, params)

        conn.commit()
        cursor.close()
        conn.close()

    def insert_movie(self, params:tuple):
        conn = self.get_connection()
        cursor = conn.cursor()

        # kell egy insert a movies tálába -> vissza kell kérnem az insertált Id-t
        #  kell egy insert a movie_meta táblába

        cursor.execute(self.insert_movies, params)
        print(cursor.fetchone()[0])

        # és amikor  a feldolgozás kész van, akkor egy OK log
        conn.commit()
        cursor.close()
        conn.close()
    
    def delete_record(self):
        pass

    def update_record(self):
        pass

if __name__ == '__main__':
    test = PostgresHandler()

    # conn = test.get_connection()
    # cursor = conn.cursor()

    # cursor.execute('select 11')
    # print(cursor.fetchone()[0])

    #test.create_database_objects()
    params = (666, 'Jóban rosszban')
    test.insert_movie(params)