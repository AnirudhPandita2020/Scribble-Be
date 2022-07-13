"""
Utility file for Scribble
"""
from pydantic import BaseSettings
from passlib.context import CryptContext


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = ".env"


setting = Settings()


class PasswordManager(object):

    def __int__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hashPassword(self, password: str):
        return self.pwd_context.hash(password)

    def verifyPassword(self, password: str, givenpassword: str):
        return self.pwd_context.verify(password, givenpassword)
