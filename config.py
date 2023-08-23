import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xd4\x80v!\x0e\xbe\xd1\x8e\x05T\xe8c\x18\x0fo\\'
    WTF_CSRF_SECRET_KEY = os.environ.get('WTM_CSRF_SECRET_KEY') or b'\xd4\x80v!\x0d\xbe\xd1\x8e\x05T\xe8c\x18\x0fo\\'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


class DevelopmentConfig(Config):
    DEBUG = True


class DockerConfig(ProductionConfig):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'docker': DockerConfig,
    'default': DevelopmentConfig
}
