import logging
import os

HERE = os.path.dirname(os.path.realpath(__file__))


class DbConfig:
    db_user = os.environ.get('POSTGRES_USER', 'test')
    db_password = os.environ.get('POSTGRES_PASSWORD', 'test')
    db_host = os.environ.get('POSTGRES_HOST', '192.168.216.81')
    db_name = os.environ.get('POSTGRES_DB',)
    db_port = os.environ.get('POSTGRES_PORT', 5433)
    main_database_url = "postgresql://{}:{}@{}:{}/{}".format(
        db_user,
        db_password,
        db_host,
        db_port,
        db_name
    ) if db_name else None
    test_database_ur = 'sqlite:///{}/practice_database.db'.format(HERE)
    database_url = main_database_url or test_database_ur
