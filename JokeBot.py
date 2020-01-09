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
reddit = praw.Reddit(client_id='', 
                    	 client_secret='', 
                    	 user_agent='', 
                   	  	 username='', 
                   	     password='')
print('Logging in...')
#telegran BotAPI authentication handler and command resolution
#add api key to initialise the updater
updater = Updater('')
dp = updater.dispatcher
#handler to send a joke 
dp.add_handler(CommandHandler('joke', tellJoke))
dp.add_handler(CommandHandler('start', keyboard))
#start polling
updater.start_polling()
updater.idle()




