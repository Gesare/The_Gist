import os


class Config:
    """
    General configuration parent class
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://mzaza:password@localhost/blog'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


class ProdConfig(Config):
    """
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class TestConfig(Config):
    """
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """
    pass


class DevConfig(Config):
    """
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    """

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
