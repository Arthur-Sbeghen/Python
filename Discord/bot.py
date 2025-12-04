import discord
import random
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix="!quack ", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

@bot.command()
async def ola(ctx):
    await ctx.send(f"Olá, {ctx.author.name}! AHDAHDAHWDHADHAHDA")

@bot.command()
async def quack(ctx):
    await ctx.send("Quack! 🦆")

@bot.command()
@commands.has_permissions(change_nickname=True)
async def apelidagem(ctx, *, apelido):
    guild = ctx.guild
    alterados = 0

    await ctx.send(f"Alterando apelidos para: **{apelido}**...")

    for member in guild.members:
        
        if member.bot or member == ctx.guild.me:
            continue

        try:
            await member.edit(nick=apelido)
            await asyncio.sleep(0.2)
            alterados += 1
        except discord.Forbidden:
            await ctx.send(f"❌ Não tenho permissão para alterar o apelido de {member.mention}... 🦆")
            continue
        except discord.HTTPException:
            continue

    await ctx.send(f"✅ Apelidos alterados com sucesso. Total de membros alterados: {alterados} 🦆")

@bot.command()
@commands.has_permissions(change_nickname=True)
async def desapelidagem(ctx):
    guild = ctx.guild
    alterados = 0

    await ctx.send(f"Removendo apelidos...")

    for member in guild.members:
        
        if member.bot or member == ctx.guild.me:
            continue

        try:
            await member.edit(nick=None)
            await asyncio.sleep(0.2)
            alterados += 1
        except discord.Forbidden:
            continue
        except discord.HTTPException:
            continue

    await ctx.send(f"✅ Apelidos alterados com sucesso. Total de membros alterados: {alterados} 🦆")

@bot.command()
async def curiosidade(ctx, membro: discord.Member = None):

    if membro is None:
        await ctx.send("🔍 Você precisa mencionar alguém para compartilhar uma curiosidade! Exemplo: `!quack curiosidade @Fulano`")
        return

    if membro == bot.user:
        await ctx.send("🤖 Sabia que eu sou feito de código e curiosidades? Aqui vai uma para você!")
        return

    curiosidades = [
        "🦑 **Lulas-gigantes** têm olhos do tamanho de bolas de basquete!",
        "🌌 **A Via Láctea** tem um buraco negro supermassivo no seu centro!",
        "🐜 **Formigas** não têm pulmões - respiram através de pequenos orifícios no corpo!",
        "🍫 **Chocolate** era usado como moeda pelos Astecas!",
        "🦈 **Tubarões** existem há mais de 400 milhões de anos - são mais antigos que dinossauros!",
        "💡 **A luz** leva 8 minutos para viajar do Sol até a Terra!",
        "🐝 **Abelhas** conseguem reconhecer rostos humanos!",
        "🌊 **O oceano** contém cerca de 20 milhões de toneladas de ouro dissolvido!",
        "🦉 **Corujas** podem girar a cabeça em quase 270 graus!",
        "⚡ **Raios** são 5 vezes mais quentes que a superfície do Sol!",
        "🐬 **Golfinhos** dão nomes uns aos outros com assovios únicos!",
        "🍯 **Mel** nunca estraga - arqueólogos encontraram mel com 3.000 anos ainda comestível!",
        "🦒 **As línguas das girafas** podem medir até 50 cm de comprimento!",
        "🧩 **O cérebro humano** pode gerar cerca de 70.000 pensamentos por dia!",
        "🐙 **Polvos** têm três corações e sangue azul!",
        "🌎 **A Rússia** tem 11 fusos horários diferentes!",
        "🦇 **Morcegos** são os únicos mamíferos que podem voar!",
        "🎵 **Música** pode afetar seus batimentos cardíacos e pressão arterial!",
        "🐢 **Tartarugas** podem respirar através do traseiro!",
        "🚀 **Estação Espacial Internacional** dá uma volta na Terra a cada 90 minutos!"
    ]

    indice_aleatorio = random.randint(0, len(curiosidades) - 1)
    curiosidade_escolhida = curiosidades[indice_aleatorio]
    
    mensagem = f"{membro.mention} {curiosidade_escolhida} 📚"

    await ctx.send(mensagem)

@bot.command()
async def reagir(ctx, mensagem_id: int, emoji: str):
    """Reage a uma mensagem específica pelo ID"""
    try:
        mensagem = await ctx.channel.fetch_message(mensagem_id)
        await mensagem.add_reaction(emoji)
        await ctx.send(f"✅ Reagido à mensagem {mensagem_id} com {emoji}", delete_after=3)
    except discord.NotFound:
        await ctx.send("❌ Mensagem não encontrada! Verifique o ID.")
    except discord.HTTPException:
        await ctx.send("❌ Emoji inválido ou não encontrado!")

@bot.command()
async def rpg_do_cellbit(ctx, membro: discord.Member = None):
    await ctx.send(f'{membro.mention}: "Ai, eu assisto o rpg do Cellbit 🤓☝!"')

usuarios_vigiados = set()

@bot.command()
async def anunciar(ctx, membro: discord.Member = None):
    if membro is None:
        await ctx.send("❌ Você precisa mencionar alguém! Exemplo: `!anunciar @usuário`")
        return
    
    if membro.id in usuarios_vigiados:
        await ctx.send("❌ Este usuário já está sendo anunciado")
        return
    
    if membro == bot.user:
        await ctx.send("Eu já anuncio minhas próprias mensagens! Quack! 🦆")
        return
    
    usuarios_vigiados.add(membro.id)
    await ctx.send(f"📢 Agora vou anunciar quando {membro.mention} mandar mensagens!")

@bot.command()
async def silenciar(ctx, membro: discord.Member = None):
    if membro is None:
        await ctx.send("❌ Você precisa mencionar alguém! Exemplo: `!silenciar @usuário`")
        return
    
    if membro.id in usuarios_vigiados:
        usuarios_vigiados.remove(membro.id)
        await ctx.send(f"🔇 Parei de anunciar {membro.mention}")
    else:
        await ctx.send("❌ Este usuário não está sendo anunciado")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.author.id in usuarios_vigiados:
        await message.reply(f"{message.author.mention} QQQQQQUUUUUUUUAAAAAAAAAAAAACCCCCCCKKKKKKKKKK! 🦆🦆🦆")

    await bot.process_commands(message)


bot.run("aaaa")