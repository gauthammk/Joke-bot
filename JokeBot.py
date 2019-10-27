import praw
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram import ReplyKeyboardMarkup

#get the jokes from the subreddit r/Jokes
def getJokes():
	randomJoke = reddit.subreddit('dadjokes').random()
	return randomJoke.title + '\n\n' + randomJoke.selftext

#print out a joke as a response to the user's message on Telegram
def tellJoke(bot, update):
	#bot.send_chat_action(chat_id=chat_id, action=telegram.ChatAction.TYPING)
	update.message.reply_text(getJokes())

def keyboard(bot, update):
	chat_id = update.message.chat_id
	menu_keyboard = [['/joke']]
	menu_markup = ReplyKeyboardMarkup(menu_keyboard, one_time_keyboard=False, resize_keyboard=True)
	bot.send_message(chat_id=chat_id, text='Hit \\joke', reply_markup=menu_markup)


#initialse the reddit access token for the api key
reddit = praw.Reddit(client_id='AZfYZhZ_qLKECw', 
                    	 client_secret='P5SY1iiHI49nqpDmcO5nsivQJjQ', 
                    	 user_agent='Joke', 
                   	  	 username='i_amgmk', 
                   	     password='ga_mbat0015')
print('Logging in...')
#Telegran BotAPI authentication handler and command resolution
updater = Updater('1041100217:AAH1zNDAG6uBa5JTnETHe8qUEvBIl0Nb71k')
dp = updater.dispatcher
#handler to send a joke 
dp.add_handler(CommandHandler('joke', tellJoke))
dp.add_handler(CommandHandler('start', keyboard))
#start polling
updater.start_polling()
updater.idle()




