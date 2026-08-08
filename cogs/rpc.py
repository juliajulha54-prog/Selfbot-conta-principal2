import os
import time
import requests

from pypresence import Presence
from pypresence.exceptions import DiscordNotFound, InvalidID


# ============================================================
# CONFIGURAÇÃO
# ============================================================

CLIENT_ID = "1535666837260607489"

# URL RAW da imagem no GitHub
IMAGE_URL = (
    "https://raw.githubusercontent.com/"
    "juliajulha54-prog/"
    "Selfbot-conta-principal2/"
    "3dfa67645daf07122ac494d10a603038c70c2cfa/"
    "crafttools_ae_512.png"
)

IMAGE_PATH = "crafttools_ae_512.png"

# Asset criado no Discord Developer Portal
ASSET = "crafttools_ae"

CRAFTTOOLS_URL = "https://crafttools.com.br/"


# ============================================================
# DOWNLOAD DA IMAGEM
# ============================================================

def baixar_imagem():

    print("🔵 Baixando imagem do GitHub...")

    try:

        response = requests.get(
            IMAGE_URL,
            timeout=15
        )

        response.raise_for_status()

        # Verifica se realmente recebeu uma imagem
        content_type = response.headers.get(
            "Content-Type",
            ""
        )

        if not content_type.startswith("image/"):
            print(
                "⚠️ O GitHub não retornou uma imagem."
            )

            print(
                f"Content-Type recebido: {content_type}"
            )

            return False

        with open(IMAGE_PATH, "wb") as arquivo:
            arquivo.write(response.content)

        tamanho = os.path.getsize(IMAGE_PATH)

        print(
            f"🟢 Imagem baixada: {IMAGE_PATH}"
        )

        print(
            f"📦 Tamanho: {tamanho} bytes"
        )

        return True

    except requests.RequestException as e:

        print(
            f"❌ Erro ao baixar a imagem: {e}"
        )

        return False


# ============================================================
# CONECTAR AO DISCORD
# ============================================================

def conectar_discord():

    print(
        "🔵 Procurando Discord Desktop..."
    )

    try:

        rpc = Presence(CLIENT_ID)

        rpc.connect()

        print(
            "🟢 Discord RPC conectado!"
        )

        return rpc

    except DiscordNotFound:

        print(
            "❌ Discord Desktop não encontrado."
        )

        print(
            "➡️ Abra o Discord Desktop nesta mesma máquina."
        )

        return None

    except InvalidID:

        print(
            "❌ CLIENT_ID inválido."
        )

        return None

    except Exception as e:

        print(
            f"❌ Erro ao conectar ao Discord: {e}"
        )

        return None


# ============================================================
# ATUALIZAR PRESENÇA
# ============================================================

def atualizar_rpc(rpc, inicio):

    rpc.update(

        # Texto principal
        details="Crafttools x AE",

        # Texto abaixo
        state="After Effects aberto",

        # Asset da Application
        large_image=ASSET,

        # Texto ao passar o mouse na imagem
        large_text="CraftTools x AE",

        # Contador
        start=inicio,

        # Botão
        buttons=[
            {
                "label": "Conhecer CraftTools",
                "url": CRAFTTOOLS_URL
            }
        ]
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 55)
    print("        CRAFTTOOLS x AE — RICH PRESENCE")
    print("=" * 55)

    # --------------------------------------------------------
    # Baixar imagem
    # --------------------------------------------------------

    baixar_imagem()

    print()

    # --------------------------------------------------------
    # Conectar Discord
    # --------------------------------------------------------

    rpc = conectar_discord()

    if rpc is None:

        input(
            "\nPressione ENTER para sair..."
        )

        return

    # --------------------------------------------------------
    # Tempo inicial
    # --------------------------------------------------------

    inicio = int(time.time())

    print(
        "🔵 Enviando Rich Presence..."
    )

    try:

        while True:

            try:

                atualizar_rpc(
                    rpc,
                    inicio
                )

                print(
                    "🟢 Rich Presence atualizada!"
                )

                print(
                    "   ├─ Crafttools x AE"
                )

                print(
                    "   ├─ After Effects aberto"
                )

                print(
                    "   ├─ Asset: crafttools_ae"
                )

                print(
                    "   └─ Contador ativo"
                )

                print()

                # Atualiza a cada 15 segundos
                time.sleep(15)

            except Exception as e:

                print(
                    f"⚠️ Erro na Rich Presence: {e}"
                )

                print(
                    "🔄 Tentando reconectar..."
                )

                try:
                    rpc.close()
                except Exception:
                    pass

                time.sleep(5)

                rpc = conectar_discord()

                if rpc is None:

                    time.sleep(10)

                    continue

                try:

                    atualizar_rpc(
                        rpc,
                        inicio
                    )

                except Exception as e:

                    print(
                        f"❌ Não foi possível atualizar: {e}"
                    )

    except KeyboardInterrupt:

        print(
            "\n🔴 Rich Presence encerrada pelo usuário."
        )

        try:

            rpc.clear()
            rpc.close()

        except Exception:
            pass

        print(
            "🟢 Discord RPC desconectado."
        )


# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    main()
