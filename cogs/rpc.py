import time
from pypresence import Presence
from pypresence.exceptions import DiscordNotFound, InvalidID


# ============================================================
# CONFIGURAÇÃO
# ============================================================

CLIENT_ID = "1535666837260607489"

# Nome EXATO do asset cadastrado no Developer Portal
ASSET = "crafttools_ae"

# Link do botão
CRAFTTOOLS_URL = "https://crafttools.com.br/"


# ============================================================
# CONFIGURAÇÃO DA PRESENÇA
# ============================================================

DETAILS = "Crafttools x AE"
STATE = "After Effects aberto"
LARGE_TEXT = "CraftTools x AE"

# Atualização da presença
UPDATE_INTERVAL = 15


# ============================================================
# RICH PRESENCE
# ============================================================

def conectar():

    try:
        rpc = Presence(CLIENT_ID)
        rpc.connect()

        print("🟢 Rich Presence conectado ao Discord.")
        return rpc

    except DiscordNotFound:
        print("❌ Discord Desktop não encontrado.")
        print("➡️ Abra o Discord Desktop antes de executar o rpc.py.")
        return None

    except InvalidID:
        print("❌ CLIENT_ID inválido.")
        return None

    except Exception as e:
        print(f"❌ Erro ao conectar ao Discord: {e}")
        return None


def iniciar_rpc():

    rpc = conectar()

    if rpc is None:
        return

    inicio = int(time.time())

    while True:

        try:

            rpc.update(
                details=DETAILS,
                state=STATE,

                large_image=ASSET,
                large_text=LARGE_TEXT,

                start=inicio,

                buttons=[
                    {
                        "label": "Conhecer CraftTools",
                        "url": CRAFTTOOLS_URL
                    }
                ]
            )

            print("🔵 Rich Presence atualizado.")

            time.sleep(UPDATE_INTERVAL)

        except KeyboardInterrupt:

            print("\n🔴 Rich Presence encerrado.")

            try:
                rpc.clear()
                rpc.close()
            except Exception:
                pass

            break

        except Exception as e:

            print(f"⚠️ Conexão perdida: {e}")
            print("🔄 Tentando reconectar...")

            try:
                rpc.close()
            except Exception:
                pass

            time.sleep(5)

            rpc = conectar()

            if rpc is None:
                print("❌ Não foi possível reconectar.")
                print("⏳ Tentando novamente em 10 segundos...")
                time.sleep(10)
                continue


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    iniciar_rpc()
