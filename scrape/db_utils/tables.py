from sqlalchemy import Column, Integer, String, MetaData, Table


def table_exists(engine, tablename):
    return engine.dialect.has_table(engine, tablename)


def create_tables(engine):
    if table_exists(engine, 'posts'):
        # table already exists. exit function.
        return

    # we need this to create table
    meta = MetaData()

    # define table structure
    Table(
           'posts', meta,
           Column('id', Integer, primary_key=True),
           Column('link', String(200)),
           Column('text', String(200)),
    )

    # finally, create table
    meta.create_all(engine)
