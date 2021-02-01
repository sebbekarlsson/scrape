from scrape.import_utils import run_import

import scrape.db_utils as db
import getpass


DB_USER = input('database user: ')
DB_PASSWORD = getpass.getpass('database password: ')
DB_IP = input('database IP: ')
DB_NAME = input('database name: ')

# connect to DB
engine, session = db.connect(DB_USER, DB_PASSWORD, DB_IP, DB_NAME)

# start program
if __name__ == '__main__':
    # create tables if not exist
    db.create_tables(engine)

    # run import job (scrape site and put data in DB)
    run_import(session)
