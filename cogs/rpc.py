import time
from pypresence import Presence

# ============================================================
# DISCORD APPLICATION
# ============================================================

CLIENT_ID = "1535666837260607489"

# Asset que você já enviou no Developer Portal
ASSET = "crafttools_ae"

# Site do botão
SITE = "https://crafttools.com.br/"


# ============================================================
# RICH PRESENCE
# ============================================================

def main():

    print("🔄 Conectando ao Discord...")

    rpc = Presence(CLIENT_ID)
    rpc.connect()

    print("🟢 RPC conectado!")

    inicio = int(time.time())

    while True:

        try:

            rpc.update(
                details="Crafttools x AE",
                state="After Effects aberto",

                # Puxa o asset diretamente da Application
                large_image=ASSET,
                large_text="CraftTools x AE",

                # Contador
                start=inicio,

                # Botão
                buttons=[
                    {
                        "label": "Conhecer CraftTools",
                        "url": SITE
                    }
                ]
            )

            print("✅ Presença atualizada.")
            time.sleep(15)

        except KeyboardInterrupt:

            print("\n🔴 RPC encerrado.")

            try:
                rpc.clear()
                rpc.close()
            except:
                pass

            break

        except Exception as e:

            print(f"⚠️ Erro: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main()
