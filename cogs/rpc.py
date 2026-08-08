import asyncio
import threading
import time

from discord.ext import commands

from pypresence import Presence


# ============================================================
# CONFIGURAÇÃO
# ============================================================

CLIENT_ID = "1535666837260607489"

# Asset criado no Discord Developer Portal
ASSET = "crafttools_ae"

# Link do botão
CRAFTTOOLS_URL = "https://crafttools.com.br/"


# ============================================================
# TEXTOS DA PRESENÇA
# ============================================================

DETAILS = "Crafttools x AE"
STATE = "After Effects aberto"
LARGE_TEXT = "CraftTools x AE"


# ============================================================
# CONFIGURAÇÕES
# ============================================================

UPDATE_INTERVAL = 15

rpc = None
rpc_thread = None
rpc_running = False


# ============================================================
# FUNÇÃO DO RPC
# ============================================================

def rpc_worker():
    global rpc
    global rpc_running

    rpc_running = True

    inicio = int(time.time())

    print("🔵 Iniciando Rich Presence...")

    try:

        rpc = Presence(CLIENT_ID)

        print("🔵 Tentando conectar ao Discord RPC...")

        rpc.connect()

        print("🟢 Rich Presence conectado!")

        while rpc_running:

            try:

                rpc.update(
                    details=DETAILS,
                    state=STATE,

                    # Asset da Application
                    large_image=ASSET,
                    large_text=LARGE_TEXT,

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

                print("🟢 Rich Presence atualizado.")

            except Exception as e:

                print(
                    f"⚠️ Erro ao atualizar Rich Presence: {e}"
                )

                # Tenta reconectar
                try:
                    rpc.close()
                except Exception:
                    pass

                time.sleep(5)

                try:

                    rpc = Presence(CLIENT_ID)
                    rpc.connect()

                    print("🟢 RPC reconectado!")

                except Exception as reconnect_error:

                    print(
                        f"❌ Falha ao reconectar RPC: "
                        f"{reconnect_error}"
                    )

                    time.sleep(10)

            time.sleep(UPDATE_INTERVAL)

    except Exception as e:

        print(
            f"❌ Erro no Rich Presence: {e}"
        )

    finally:

        try:

            if rpc is not None:

                rpc.clear()
                rpc.close()

        except Exception:
            pass

        rpc_running = False

        print("🔴 Rich Presence encerrado.")


# ============================================================
# COG
# ============================================================

class RPC(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

        self.thread = None

    async def start_rpc(self):

        global rpc_thread

        # Evita iniciar duas vezes
        if rpc_thread is not None and rpc_thread.is_alive():

            print("⚠️ Rich Presence já está rodando.")

            return

        print("🚀 Criando thread do Rich Presence...")

        rpc_thread = threading.Thread(
            target=rpc_worker,
            daemon=True
        )

        rpc_thread.start()

        self.thread = rpc_thread

    def stop_rpc(self):

        global rpc_running

        rpc_running = False

        print("🛑 Parando Rich Presence...")

    @commands.Cog.listener()
    async def on_ready(self):

        print(
            "🔵 Cog RPC carregada. "
            "Iniciando Rich Presence..."
        )

        await self.start_rpc()

    def cog_unload(self):

        self.stop_rpc()


# ============================================================
# SETUP
# ============================================================

async def setup(bot):

    await bot.add_cog(RPC(bot))

    print("📡 Cog carregada: cogs.rpc")
