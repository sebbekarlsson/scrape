from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect(user, password, host, dbname):
    # Connect to database
    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}/{dbname}',
        echo=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # return tuple with engine, session
    return engine, session
