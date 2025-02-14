import os
from dotenv import load_dotenv

load_dotenv()

DATABASE: str = os.getenv("DATABASE", "test.db")
PASSWORD_SECRET_KEY: str = os.getenv("PASSWORD_SECRET_KEY", "")
CHECK_ENV: str = os.getenv("CHECK_ENV", "false")
# We will add stuff here

if isinstance(CHECK_ENV, str) and CHECK_ENV != "false":
    locals = locals().copy()
    for local_variable, value in locals.items():
        if value == "":
            raise ValueError(f"{local_variable} not set in .env")
