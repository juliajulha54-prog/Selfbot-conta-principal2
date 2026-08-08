import os
import time
import requests
from pypresence import Presence

CLIENT_ID = "1535666837260607489"

# URL RAW da imagem no GitHub
IMAGE_URL = "https://raw.githubusercontent.com/SEU_USUARIO/SEU_REPOSITORIO/main/assets/crafttools.png"

IMAGE_PATH = "crafttools.png"


def baixar_imagem():
    print("🔵 Baixando imagem do GitHub...")

    response = requests.get(IMAGE_URL, timeout=15)
    response.raise_for_status()

    with open(IMAGE_PATH, "wb") as arquivo:
        arquivo.write(response.content)

    print("🟢 Imagem baixada!")


def main():
    baixar_imagem()

    rpc = Presence(CLIENT_ID)

    print("🔵 Conectando ao Discord Desktop...")
    rpc.connect()

    print("🟢 Conectado!")

    inicio = int(time.time())

    rpc.update(
        details="Crafttools x AE",
        state="After Effects aberto",

        # IMPORTANTE:
        # isto NÃO aceita IMAGE_PATH nem IMAGE_URL.
        # O Discord exige uma asset key da Application.
        large_image="crafttools_ae",
        large_text="CraftTools x AE",

        start=inicio,

        buttons=[
            {
                "label": "Conhecer CraftTools",
                "url": "https://crafttools.com.br/"
            }
        ]
    )

    print("🟢 Rich Presence enviada!")

    while True:
        time.sleep(15)


if __name__ == "__main__":
    main()
