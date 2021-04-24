from sqlalchemy import create_engine
from sqlalchemy.orm import Session

#data_base_url = "postgresql://gmail:harshith@localhost/"


def get_engine(data_base_url, echo, max_overflow, pool_size):
    engine = create_engine(data_base_url, echo=echo, max_overflow=max_overflow,
                           pool_logging_name="database_pool", pool_size=pool_size)
    return engine


if __name__ == "__main__":
    # session
    with Session(engine) as session:
        print(session)
        print(session)
