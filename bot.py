import discord
import os
import random

# array that stores all quotes, feel free to pull quotes from an api or create a database
quotes = [
    '“حين ينتهي الحُب، أدرِكْ أنه لم يَكُن حُبًّا. الحُب لابدَّ أن يُعاش، لا أن يُتَذَكَّر.”\n“When love ends, know it wasn’t really love. Love must be lived, not remembered.”',
    '“حُرّيتي أن أكون كما لا يريدون لي أن أكون.”\n“My freedom is to be what they don’t want me to be.”',
    '“لرُبّما القمر ليس جميلًا إلا لأنه بعيد.”\n“Maybe the moon is beautiful only because it is far.”',
    '“على هذه الأرضِ ما يَسْتَحِقُّ الحياة.”\n“We have on this land what makes life worth living.”',
    '“الجميلاتُ هُنَّ الفقيرات، كالوردِ في ساحَةِ المَعْرَكة.”\n“The beautiful ones are the poor ones, like roses in the battlefield.”',
    '“وأقولُ لِنَفْسي: سِيَطْلَعُ من عَتْمتي قمر.”\n“And I tell myself: a moon will rise from my darkness.”',
    '“سأحلُم، لا لأصلح أي معنى خارجي. بل كي أُرَمِّم داخلي المَهْجور.”\n“I will dream, not to fix any external meaning. Rather, to restore my deserted interior.”',
    '“إذا أردتَ أن تستيقظ سعيدًا في الصباح، فاعرفْ مع من تتحدث ليلًا.”\n“If you want to wake up happy in the morning, know who you talk to at night.”',
    '“احْذرْ قلبك، لا تُدَلِّلـهُ أكثر مما ينبغي، ولا تهملهُ أكثر مما يستحق.”\n“Beware of your heart, do not spoil it more than it should, and do not neglect it more than it deserves.”',
    '“الحُبُّ ليسَ ما تَقوله الشفاه، بل ما تَفعله الأفعال.”\n“Love is not what lips say, but what actions do.”',
]

# function that takes a string and removes everything after the second heart emoji
def remove_after_second_heart(text):
  parts = text.split('💖')
  if len(parts) > 2:
    result = '💖'.join(parts[:2]) + '💖'
    return result.strip()
  else:
    return text.strip()


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return


  # Forward messages starting with 💖 from a specific user
  if message.author.id == 432610292342587392 and message.content.startswith( # Mudae's author id
      '💖'):
    stored = remove_after_second_heart(message.content)
    channel_id =   # Replace with your actual 18-digit channel ID, this will be the channel where you want to send claim messages to
    channel = client.get_channel(channel_id)
    if channel is not None:
      await channel.send(stored)
    else:
      print(f"Channel with ID {channel_id} not found.")



  # Handle $qotd command
  if message.content.startswith('$qotd'):
    quote = random.choice(quotes)
    await message.channel.send(quote)


client.run(os.getenv('TOKEN')) # Replace with your actual bot token