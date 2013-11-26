from kglobals import database_creator


def setup():
    database_creator.create_database()
    database_creator.initialize_database()


if __name__ == "__main__":
    setup()
