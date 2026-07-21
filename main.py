import os
import discord
import asyncio
import time
from flask import Flask
from threading import Thread
from discord.ext import commands

# ===== WEB (Railway) =====
app = Flask(__name__)

@app.route("/")
def home():
    return "OK", 200

def run_web():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def start_web():
    Thread(target=run_web, daemon=True).start()

start_web()

# ===== DISCORD (commands.Bot) =====
# Usamos commands.Bot para suporte nativo a Cogs e extensões
bot = commands.Bot(command_prefix="?", self_bot=True)

# ===== CONFIG =====
prefix = "?"
start_time = time.time()

# 🔥 LISTA DE IDS PERMITIDOS
ALLOWED_IDS = [
    932012274569338981,
    1473488490795896997, 
    569633804537430036, 
    932011766651703358
]

status_manual = False

# ===== STATUS ROTATIVO =====
async def rotacao_status():
    await bot.wait_until_ready()
    i = 0

    while True:
        try:
            if status_manual:
                await asyncio.sleep(5)
                continue

            atividades = [
                discord.Activity(type=discord.ActivityType.playing, name="Arena Breakout"),
                discord.Activity(type=discord.ActivityType.playing, name="Arena Breakout"),
                discord.Activity(type=discord.ActivityType.playing, name="Arena Breakout")
            ]

            await bot.change_presence(
                status=discord.Status.dnd,
                activity=atividades[i % len(atividades)]
            )

            i += 1
            await asyncio.sleep(10)

        except Exception as e:
            print("Erro status:", e)
            await asyncio.sleep(5)

# ===== FUNÇÃO PARA CARREGAR COGS =====
async def load_extensions():
    if os.path.exists("./cogs"):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                cog_name = f"cogs.{filename[:-3]}"
                try:
                    await bot.load_extension(cog_name)
                    print(f"📦 Cog carregada: {cog_name}")
                except Exception as e:
                    print(f"❌ Erro ao carregar {cog_name}: {e}")

# ===== EVENTOS =====
@bot.event
async def on_ready():
    print(f"🟢 Logado como {bot.user} | ID: {bot.user.id}")
    await load_extensions()
    bot.loop.create_task(rotacao_status())

# ===== HANDLER DE COMANDOS MANUAIS =====
async def handle_command(message):
    global status_manual

    content = message.content.strip()

    # 🔒 PERMISSÃO (SEM MENSAGEM DE ERRO)
    if message.author.id != bot.user.id and message.author.id not in ALLOWED_IDS:
        return

    # Processa comandos registrados nas Cogs
    await bot.process_commands(message)

    # ===== EVAL =====
    if content.startswith(f"{prefix}eval"):
        if message.author.id not in ALLOWED_IDS:
            return

        codigo = content[len(f"{prefix}eval"):].strip()

        if not codigo:
            await message.channel.send("Sem código.")
            return

        import io
        import contextlib
        import traceback

        if codigo.startswith("```"):
            codigo = "\n".join(codigo.split("\n")[1:-1])

        stdout = io.StringIO()

        try:
            exec_code = "async def _exec(message, client):\n"
            for linha in codigo.split("\n"):
                exec_code += f"    {linha}\n"

            local_vars = {}
            exec(exec_code, globals(), local_vars)

            with contextlib.redirect_stdout(stdout):
                resultado = await local_vars["_exec"](message, bot)

            saida = stdout.getvalue()

            resposta = "✅ Código executado com sucesso!\n"

            if saida:
                if len(saida) > 1900:
                    saida = saida[:1900] + "\n... (cortado)"
                resposta += f"📤 Saída:\n```py\n{saida}\n```"

            if resultado is not None:
                resultado_str = str(resultado)
                if len(resultado_str) > 1900:
                    resultado_str = resultado_str[:1900] + "\n... (cortado)"
                resposta += f"\n📥 Retorno:\n```py\n{resultado_str}\n```"

            if not saida and resultado is None:
                resposta += "ℹ️ Nenhuma saída foi produzida."

            await message.channel.send(resposta)

        except Exception:
            erro = traceback.format_exc()
            if len(erro) > 1900:
                erro = erro[:1900] + "\n... (cortado)"
            await message.channel.send(
                f"❌ Erro ao executar:\n```py\n{erro}\n```"
            )

    # ===== setstatus =====
    elif content.startswith(f"{prefix}setstatus"):
        try:
            args = content.split()

            if len(args) < 2:
                await message.channel.send("Uso: ?setstatus online/dnd/idle/invisible")
                return

            status_map = {
                "online": discord.Status.online,
                "idle": discord.Status.idle,
                "dnd": discord.Status.dnd,
                "invisible": discord.Status.invisible
            }

            status_arg = args[1].lower()

            if status_arg in status_map:
                status_manual = True
                await bot.change_presence(status=status_map[status_arg])
                await message.channel.send(f"Status: {status_arg}")
            else:
                await message.channel.send("Status inválido")

        except Exception as e:
            await message.channel.send(f"Erro: {e}")

    # ===== resetstatus =====
    elif content.startswith(f"{prefix}resetstatus"):
        status_manual = False
        await message.channel.send("Status automático ativado")

    # ===== say =====
    elif content.startswith(f"{prefix}say"):
        try:
            corpo = content[len(f"{prefix}say"):].strip()
            
            if not corpo:
                return

            args = corpo.split(" ", 1)
            
            if args[0].isdigit() and len(args[0]) >= 17:
                canal_id = int(args[0])
                canal = bot.get_channel(canal_id)
                
                if canal:
                    texto_para_enviar = args[1] if len(args) > 1 else "..."
                    await canal.send(texto_para_enviar)
                else:
                    await message.channel.send(corpo)
            else:
                await message.channel.send(corpo)

        except Exception as e:
            print(f"Erro no say: {e}")

# ===== LISTENERS DE MENSAGENS =====
@bot.event
async def on_message(message):
    await handle_command(message)

@bot.event
async def on_message_edit(before, after):
    if after.author.id == bot.user.id:
        return

    await handle_command(after)

# ===== RUN =====
token = os.environ.get("TOKEN")

if not token:
    raise Exception("TOKEN não definido nas variáveis de ambiente")

bot.run(token)
        
