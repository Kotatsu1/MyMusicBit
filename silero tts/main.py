import discord
from discord.ext import commands
from silero import sound_ai
from stt import recognition
import subprocess
import os


bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())

class AiView(discord.ui.View):

    def __init__(self, ctx):
        super().__init__()
        self.ctx = ctx

    @discord.ui.button(label="Start recording", style=discord.ButtonStyle.green)
    async def button_start(self, button, interaction: discord.Interaction):
        await interaction.response.send_message('Started recording')
        await listen(self.ctx)

    @discord.ui.button(label="Stop recording", style=discord.ButtonStyle.red)
    async def button_end(self, button, interaction: discord.Interaction):
        await interaction.response.send_message('Stopped recording')
        await stop(self.ctx)


@bot.command()
async def ai(ctx):
    view = AiView(ctx)
    await ctx.send(view=view)


@bot.command()
async def join(ctx):
    vc = ctx.message.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await vc.connect()

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("not in a voice channel!")



async def get_answer(ctx, text):
    vc = ctx.message.author.voice.channel
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice == None:
        await vc.connect()
    try:
        link = sound_ai(text)
        ctx.voice_client.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source=link))
    except Exception as ex:
        await ctx.send(ex)



@bot.command()
async def listen(ctx):
    if ctx.voice_client:
        ctx.voice_client.start_recording(discord.sinks.WaveSink(), callback, ctx)
    else:
        await ctx.send("not in a voice channel!")


async def callback(sink: discord.sinks, ctx):
    for user_id, audio in sink.audio_data.items():
        if user_id == ctx.author.id:
            audio: discord.sinks.core.AudioData = audio
            
            if os.path.exists('mono.wav'):
                os.remove('mono.wav')
            with open('stereo.wav', "wb") as f:
                f.write(audio.file.getvalue())

            subprocess.call(["ffmpeg", "-i", 'stereo.wav', "-map_channel", "0.0.0", 'mono.wav'])

            text = recognition()
            ctx.voice_client.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source='on_ready.wav'))
            await get_answer(ctx, text)
            

@bot.command()
async def stop(ctx):
    ctx.voice_client.stop_recording()

@bot.command()
async def repeat(ctx):
    ctx.voice_client.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source='stereo.wav'))


@bot.command()
async def mic_test(ctx):
    if ctx.voice_client:
        ctx.voice_client.start_recording(discord.sinks.WaveSink(), mic_test_callback, ctx)
        await ctx.send("started testing...")
    else:
        await ctx.send("not in a voice channel!")


async def mic_test_callback(sink: discord.sinks, ctx):
    for user_id, audio in sink.audio_data.items():
        if user_id == ctx.author.id:
            audio: discord.sinks.core.AudioData = audio

            with open('mic_test.wav', "wb") as f:
                f.write(audio.file.getvalue())

@bot.command()
async def mic_stop(ctx):
    ctx.voice_client.stop_recording()
    await ctx.send("stopped testing")
    ctx.voice_client.play(discord.FFmpegPCMAudio(executable='ffmpeg.exe', source='mic_test.wav'))


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

bot.run('')