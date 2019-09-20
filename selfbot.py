import asyncio
import discord
import data

client = discord.Client()

#Resets the text files' counter values

def reset():
    data.counter1 = 0
    data.counter2 = 0
    data.counter3 = 0
    data.counter_public_1 = 0
    data.counter_public_2 = 0
    data.counter_public_3 = 0
    data.counter_private_1 = 0
    data.counter_private_2 = 0
    data.counter_private_3 = 0
    data.wronggone1 = 0
    data.wronggone2 = 0
    data.wronggone3 = 0
    data.weight_time = 1
    data.game_in_session = False
    update_data()

#Opens text file to update data whenever new results are found

def update_data():
    file1 = open('data/num1.txt', 'w')
    file2 = open('data/num2.txt', 'w')
    file3 = open('data/num3.txt', 'w')
    file4 = open('data/gamerunning.txt', 'w')

    file1.write(str(data.counter1))
    file2.write(str(data.counter2))
    file3.write(str(data.counter3))
    file4.write(str(int(data.game_in_session)))

    file1.close()
    file2.close()
    file3.close()
    file4.close()

#This is the command that triggers the selfbot to start it's 10 second scan of the surveyed channels
@client.event
async def on_message(message):

    if message.content.startswith('+hq') and message.channel.id == data.command_channel:

        if data.game_in_session == True:
            return
        data.game_in_session = True
        update_data()

    if data.game_in_session and message.channel.id in data.input_hq_private:
        if message.content == '1' or message.content == '1apg' or message.content == '1 apg':
            data.counter_private_1 += 10
        elif message.content == '1?' or message.content == '?1':
            data.counter_private_1 += 5
        elif message.content == 'cnf1' or message.content == '1cnf' or message.content == '1 cnf':
            data.counter_private_1 += 15
        elif message.content == '2' or message.content == '2apg' or message.content == '2 apg':
            data.counter_private_2 += 10
        elif message.content == '2?' or message.content == '?2':
            data.counter_private_2 += 5
        elif message.content == 'cnf2' or message.content == '2cnf' or message.content == '2 cnf':
            data.counter_private_2 += 15
        elif message.content == '3' or message.content == '3apg' or message.content == '3 apg':
            data.counter_private_3 += 10
        elif message.content == '3?' or message.content == '?3':
            data.counter_private_3 += 5
        elif message.content == 'cnf3' or message.content == '3cnf' or message.content == '3 cnf':
            data.counter_private_3 += 15

    if data.game_in_session and message.channel.id in data.input_hq_public:
        if message.content == '1' or message.content == '1apg' or message.content == '1 apg':
            data.counter_public_1 += 10
        elif message.content == '1?' or message.content == '?1':
            data.counter_public_1 += 5
        elif message.content == '1q' or message.content == 'q1':
            data.counter_public_1 += 100
        elif message.content == '1x' or message.content == 'x1':
            data.wronggone1 = 1
        elif message.content == 'cnf1' or message.content == '1cnf' or message.content == '1 cnf':
            data.counter_public_1 += 15
        elif message.content == '2' or message.content == '2apg' or message.content == '2 apg':
            data.counter_public_2 += 10
        elif message.content == '2?' or message.content == '?2':
            data.counter_public_2 += 5
        elif message.content == '2q' or message.content == 'q2':
            data.counter_public_2 += 100
        elif message.content == '2x' or message.content == 'x2':
            data.wronggone2 = 1
        elif message.content == 'cnf2' or message.content == '2cnf' or message.content == '2 cnf':
            data.counter_public_2 += 15
        elif message.content == '3' or message.content == '3apg' or message.content == '3 apg':
            data.counter_public_3 += 10
        elif message.content == '3?' or message.content == '?3':
            data.counter_public_3 += 5
        elif message.content == '3q' or message.content == 'q3':
            data.counter_public_3 += 100
        elif message.content == '3x' or message.content == 'x3':
            data.wronggone3 = 1
        elif message.content == 'cnf3' or message.content == '3cnf' or message.content == '3 cnf':
            data.counter_public_3 += 15

    data.counter1 = data.weight_time * (data.counter_public_1 + data.weight * data.counter_private_1)
    data.counter2 = data.weight_time * (data.counter_public_2 + data.weight * data.counter_private_2)
    data.counter3 = data.weight_time * (data.counter_public_3 + data.weight * data.counter_private_3)

    if data.wronggone1 == 1:
        data.counter1 = 0
    if data.wronggone2 == 1:
        data.counter2 = 0
    if data.wronggone3 == 1:
        data.counter3 = 0

    update_data()

#Prints when the client is started and ready for usage

@client.event
async def on_ready():
    print('Bot Client is ready!')
    data.init()
    update_data()
    reset()

#This sets the 10 second timer for the search to happen

async def second_counter():
    while not client.is_closed:
        await asyncio.sleep(1)
        if data.game_in_session == True:
            await asyncio.sleep(7)
            # added 12 sec for test
            #await asyncio.sleep(20)
            data.weight_time = 2
            await asyncio.sleep(3)
            data.game_in_session = False
            reset()
            update_data()

client.loop.create_task(second_counter())
client.run(data.self_bot_token, bot=False)
