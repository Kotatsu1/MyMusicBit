# import discord
# from discord.ext import commands

# class AiView(discord.ui.View):

#     def __init__(self, ctx):
#         super().__init__()
#         self.ctx = ctx

#     @discord.ui.button(label="Start recording", style=discord.ButtonStyle.green)
#     async def button_start(self, button, interaction: discord.Interaction):
#         await interaction.response.send_message('Started recording')
#         await listen(self.ctx)

#     @discord.ui.button(label="Stop recording", style=discord.ButtonStyle.red)
#     async def button_end(self, button, interaction: discord.Interaction):
#         await interaction.response.send_message('Stopped recording')
#         await stop(self.ctx)