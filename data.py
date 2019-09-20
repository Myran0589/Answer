import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NjAyMjA1NDk0NDYzMTY4NTgy.XTNe0Q.Dn2YuivzioPpcq4l1CsRcNWf51w'
self_bot_token = 'NTQ5OTQwOTc3MTE3Mjk4NzA4.XSxtxA.p7sDLqU4kCjN240l7r7uCE-xXp0'

message = None
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '595300313930530833')

input_hq_private  = [
    "595300313930530833",
    "459842150323060736",
    "580198028950896640",
	    "513818250652680213",
	    "595639586726740049",
	    "568617830258442255",
	    "569420198717816852",
	    "591600008353021953",
	    "585285701671714826",
	    "595301050374815757",
	    "590471026899550208",
	    "589120764347678750",
	    "585682137202819101",
	    "590470896649502750",
	    "590182635653824542",
	    "589120764347678750",
	    "589516793350062100",
    "583796470394781696",
    "595301050374815757", # answers1
    "559442345674670082", #answers2
    '577486564402397194' #trivia-answers
]
input_hq_public = ['595301050374815757']
command_channel = '595301050374815757' #trivia-answers
admin_chat = '595301050374815757' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
