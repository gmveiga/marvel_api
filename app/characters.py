from flask import Blueprint
import requests
import os
from dotenv import load_dotenv

load_dotenv()

characters_url = "https://gateway.marvel.com/v1/public/characters"
api_key = os.environ.get("PUBLIC_KEY")
ts = os.environ.get("TIMESTAMP")
hash_key = os.environ.get("HASH_KEY")

bp = Blueprint('characters',__name__)

# Quando acessar a rota princiapl, executa a função index
@bp.route("/")
def index():
    deadpool_id = 1009268
    spider_man_id = 1009610

    def get_character(id):
        params = {"apikey": api_key, "ts": 1, "hash": hash_key}
        response = requests.get(f"{characters_url}/{id}", params=params).json()
        return response["data"]["results"][0]

    characters = [
        get_character(deadpool_id),
        get_character(spider_man_id)
    ]

    return {'characters': characters}