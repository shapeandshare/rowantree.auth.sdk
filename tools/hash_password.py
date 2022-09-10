"""
python -m tools.hash_password
"""

from dotenv import load_dotenv

# load locally defined environmental variables
load_dotenv(dotenv_path="env/.env.offline")  # take environment variables from .env.

from src.rowantree.auth.sdk import get_password_hash, verify_password

if __name__ == "__main__":
    password: str = "secret"
    hashed_password: str = get_password_hash(password=password)
    verified: bool = verify_password(plain_password=password, hashed_password=hashed_password)
    print(password)
    print(verified)
    print(hashed_password)
