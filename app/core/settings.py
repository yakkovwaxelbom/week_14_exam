from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_HOST: str = '127.0.0.1'
    MYSQL_PORT: str = '3306'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = 'pass'
    MYSQL_DATABASE: str = 'week_14_exam'


setting = Settings() 
