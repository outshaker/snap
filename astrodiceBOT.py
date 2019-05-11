import threading
from time import sleep
from plurk_bot import PlurkBot, now_str, Logger


def chk_friend_handler(bot, alertLog):
    # print('chk friend')
    bot.check_notify_and_add_friend(alertLog)
    global chk_friend
    chk_friend = threading.Timer(60, chk_friend_handler, [bot, alertLog])
    chk_friend.start()

def check_keyword_handler(bot, replyLog, plurkLog):
    # print('chk keyword')
    bot.timeline_detect(replyLog, plurkLog)
    global chk_keyword
    chk_keyword = threading.Timer(60, check_keyword_handler, [bot, replyLog, plurkLog])
    chk_keyword.start()

global chk_keyword
global chk_friend
bot = PlurkBot()
alertLog = Logger('alertLog')
replyLog = Logger('replyLog')
plurkLog = Logger('plurkLog')
chk_friend_handler(bot, alertLog)
check_keyword_handler(bot, replyLog, plurkLog)

while True:
    try:
        # print('mainLoop')
        sleep(1)
    except KeyboardInterrupt:
        chk_friend.cancel()
        chk_keyword.cancel()
        del chk_friend
        del chk_keyword
        del bot
        break
