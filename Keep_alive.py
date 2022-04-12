  role = discord.utils.get( member.guild.roles , id=role_id) # name = "otaku"
  await member.add_roles( role )
  channel = client.get_channel(channel_id)
  await channel.send('Congrats {0.mention}.\nYou have been assigned the role of Otaku.'.format(member))
 
@client.event
async def on_reaction_add(reaction, user):
  msg = reaction.message
  await msg.add_reaction(reaction.emoji)
 
keep_alive()
client.run(my_secret)
 
# TO BE ADDED
# 1. display about me of mentioned user/author
# 2. play audio and video
# 3. Whatsapp and Discord chatbot
# 4. Chrome Extension
 
 
from flask import Flask
from threading import Thread
 
app = Flask('')
 
@app.route('/')
def home():
  return ("Hello. I am alive!")
 
def run():
  app.run(host='0.0.0.0', port=8080)
 
def keep_alive():
  t = Thread(target = run)
  t.start()