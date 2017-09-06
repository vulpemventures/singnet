from aiopg.sa import create_engine

from sqlalchemy_utils import drop_database, database_exists, create_database

from sn_agent.database import DatabaseSettings


def prepare_database(delete_existing: bool) -> bool:
    """
    (Re)create a fresh database and run migrations.

    :param delete_existing: whether or not to drop an existing database if it exists
    :return: whether or not a database has been (re)created
    """
    settings = DatabaseSettings()
    db_url = settings.URL

    if database_exists(db_url):
        if delete_existing:
            print('dropping database as it already exists...')
            drop_database(db_url)
        else:
            print('database already exists, skipping')
            return False
    else:
        print('database does not yet exist')

    print('creating database...')

    create_database(db_url)

    engine = create_engine(db_url)
    print('creating tables from model definition...')
    Base.metadata.create_all(engine)
    engine.dispose()
    return True


if __name__ == "__main__":
    print(prepare_database(False))
