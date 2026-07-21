import asyncio
from discord.ext import commands

class MensagensCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Adicione quantas mensagens quiser na lista
        self.lista_mensagens = [
            "Não pode falar um "A" aqui que é ban, KKKKKKKKKKK por isso que tá falido aí, server de merda, Morgan é outro fudidozinho que nunca vai crescer, com pc de 100k de reais e edita uma bosta, eu edito mais que ele pelo AM
aí se junta com um viado depressivo e gordo igual o ntz que ficava falando "aí pq eu existo?" "krl tropa tô triste" ficava botando bio no Discord falando "minha vida é uma bosta e isso me basta" e nem adianta negar pq todo mundo aqui sabe que é vdd, rtz vc é uma vergonha para sua família, uma decepção.
aproveita que vc é depressivo e gordo e se corta logo para se matar , só assim vc morre logo e para de causar terremotos na terra seu gordo de merda.
e não apaga as mensagens não sua puta. se apagar vai mostrar o quanto vc é depressivo e fracassado....
isso vale pra tu também Morgan, o  viadinho dos EUA KKKKKKKKKKKKK, vergonhoso sua crise de depressão e querer me passar posse do server de 1k de membros, servidor de Discord é assim seu jumento, uma hora vai desanimar, mas apagar é burrice.....
olha isso KKKKKKKKKKKKKKKK misericórdia que nojo de vcs mn, dois depressivo KKKKKKKKKKKKKKKK https://cdn.discordapp.com/attachments/1528821092397875280/1528867199412863057/Screenshot_20260207-2154382.jpg?ex=6a5fdc09&is=6a5e8a89&hm=f1ff33cc92e002f3da9e797f8b95b6fd849988f0f3511609f3fafb26d7586a0c& 
"busco atenção" depressivo do krl, implorando por msg de macho https://cdn.discordapp.com/attachments/1528821092397875280/1528867348675563652/Screenshot_20260720-1742302.jpg?ex=6a5fdc2c&is=6a5e8aac&hm=894487a76be5713e18f1818a0293aac39ca748cfa47ca1e4d65ae33ca6c3acae&
se até o Morgan sente vergonha dele pq eu não vou sentir? KKKKKKKKKK que nojo desse depressivo fudido https://cdn.discordapp.com/attachments/1528821092397875280/1528869685615923272/Screenshot_20260720-1757422.jpg?ex=6a5fde5a&is=6a5e8cda&hm=fdc9305d396b40b86ba87f48e34bfdde414a18731c5ab4b82c59d3df498d6033&"
        ]

    @commands.command(name="enviar")
    async def enviar(self, ctx):
        # Apaga a mensagem do comando para manter a conversa limpa
        try:
            await ctx.message.delete()
        except Exception:
            pass

        for msg in self.lista_mensagens:
            await ctx.send(msg)
            await asyncio.sleep(1) # Intervalo de 1 segundo entre envios

async def setup(bot):
    await bot.add_cog(MensagensCog(bot))
    
