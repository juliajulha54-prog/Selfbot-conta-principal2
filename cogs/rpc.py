import time
from pypresence import Presence
from pypresence.exceptions import DiscordNotFound, InvalidID

# ============================================================
# CONFIGURAÇÃO
# ============================================================

# ID da sua aplicação criada no Discord Developer Portal
CLIENT_ID = "1535666837260607489"

# Nome do asset enviado para:
# Discord Developer Portal > sua aplicação > Rich Presence > Art Assets
ASSET = "crafttools_ae"

# Link que será aberto pelo botão "Conhecer CraftTools"
CRAFTTOOLS_URL = "https://crafttools.com.br/"


# ============================================================
# RICH PRESENCE
# ============================================================

def iniciar_rpc():

    rpc = Presence(CLIENT_ID)

    try:
        rpc.connect()
        print("🟢 Rich Presence conectado ao Discord.")

    except DiscordNotFound:
        print("❌ Discord Desktop não encontrado.")
        print("Abra o Discord Desktop e execute o rpc.py novamente.")
        return

    except InvalidID:
        print("❌ CLIENT_ID inválido.")
        return

    inicio = int(time.time())

    while True:
        try:

            rpc.update(
                details="Crafttools x AE",

                state="After Effects aberto",

                large_image=ASSET,
                large_text="CraftTools x AE",

                start=inicio,

                buttons=[
                    {
                        "label": "Conhecer CraftTools",
                        "url": CRAFTTOOLS_URL
                    }
                ]
            )

            print("🔵 Rich Presence atualizado.")

            # Atualiza a cada 15 segundos
            time.sleep(15)

        except KeyboardInterrupt:
            print("\n🔴 Rich Presence encerrado.")

            try:
                rpc.clear()
                rpc.close()
            except:
                pass

            break

        except Exception as e:
            print("⚠️ Erro no Rich Presence:", e)
            time.sleep(10)


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    iniciar_rpc()
