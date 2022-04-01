from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Pilimg server."
    app_version: str = "0.1"
    admin_email: str = "wujiocean@gmail.com"


settings = Settings()
