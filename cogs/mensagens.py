import asyncio
from discord.ext import commands

class MensagensCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Primeira lista de mensagens
        self.lista_1 = [
            'não pode falar um "A" aqui que é ban, KKKKKKKKKKK por isso que tá falido aí, server de merda, Morgan é outro fudidozinho que nunca vai crescer, com pc de 100k de reais e edita uma bosta, eu edito mais que ele pelo AM',
            'aí se junta com um viado depressivo e gordo igual o ntz que ficava falando "aí pq eu existo?" "krl tropa tô triste" ficava botando bio no Discord falando "minha vida é uma bosta e isso me basta" e nem adianta negar pq todo mundo aqui sabe que é vdd, rtz vc é uma vergonha para sua família, uma decepção.',
            "aproveita que vc é depressivo e gordo e se corta logo para se matar , só assim vc morre logo e para de causar terremotos na terra seu gordo de merda.", 
"e não apaga as mensagens não sua puta. se apagar vai mostrar o quanto vc é depressivo e fracassado....",
"isso vale para tu também Morgan, o  viadinho dos EUA KKKKKKKKKKKKK, disse que tinha medo de mulher, vergonhoso sua crise de depressão e querer me passar posse do server de 1k de membros, servidor de Discord é assim seu jumento, uma hora vai desanimar, mas apagar é burrice....." ]
        
        # Segunda lista de mensagens (agora alinhada corretamente dentro do __init__)
        self.lista_2 = [
            "olha isso KKKKKKKKKKKKKKKK , q de vcs mn https://cdn.discordapp.com/attachments/1474439026315366402/1529154576450588752/Screenshot_20260207-2154382.jpg?ex=6a60e7ad&is=6a5f962d&hm=caebff789adece49470f80ad7f894685089756cc1f4df96a94b7c4520a990307& https://cdn.discordapp.com/attachments/1528821092397875280/1528869685615923272/Screenshot_20260720-1757422.jpg?ex=6a60871a&is=6a5f359a&hm=4ca0bc6e8efc2b7f39fcdc7caa465403e525adeb9afc95765551df8e780ce749& https://cdn.discordapp.com/attachments/1528821092397875280/1528867348675563652/Screenshot_20260720-1742302.jpg?ex=6a6084ec&is=6a5f336c&hm=a7edf6713c2fbc131e5920e2c859d2543c933fa6b67fb56ade7abd4ad620f189&"
        ]

    @commands.command(name="enviar")
    async def enviar(self, ctx):
        # Apaga a mensagem que chamou o comando
        try:
            await ctx.message.delete()
        except Exception:
            pass

        # Unifica as duas listas de mensagens
        todas_as_mensagens = self.lista_1 + self.lista_2

        # Envia cada mensagem com um intervalo de tempo
        for msg in todas_as_mensagens:
            await ctx.send(msg)
            await asyncio.sleep(1) # Intervalo de 1 segundo entre envios


async def setup(bot):
    await bot.add_cog(MensagensCog(bot))
    
