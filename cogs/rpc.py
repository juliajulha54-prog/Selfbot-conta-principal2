import time
from pypresence import Presence

CLIENT_ID = "1535666837260607489"
ASSET = "crafttools_ae"
SITE = "https://crafttools.com.br/"

rpc = None
inicio = int(time.time())


def iniciar_rpc():
    global rpc

    try:
        rpc = Presence(CLIENT_ID)
        rpc.connect()

        rpc.update(
            details="Crafttools x AE",
            state="After Effects aberto",
            large_image=ASSET,
            large_text="CraftTools x AE",
            start=inicio,
            buttons=[
                {
                    "label": "Conhecer CraftTools",
                    "url": SITE
                }
            ]
        )

        print("🟢 Rich Presence conectado.")

    except Exception as e:
        print(f"❌ Erro no Rich Presence: {e}")


def setup(bot):
    iniciar_rpc()
