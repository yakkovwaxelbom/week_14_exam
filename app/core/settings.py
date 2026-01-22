from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_PORT: str = '3306'
    MYSQL_USER: str = 'root'
    MYSQL_PASSWORD: str = 'pass'
    MYSQL_DATABASE: str 


setting = Settings() 

