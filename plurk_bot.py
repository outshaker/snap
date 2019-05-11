from plurk_oauth import PlurkAPI
from random import randint
from datetime import datetime, timedelta, timezone
from time import time
import json

gmt8 = timezone(timedelta(hours=8))

def now():
    return int(time())
def ts2str(ts): # use for logging & human reading
    return datetime.fromtimestamp(ts,gmt8).strftime("%H:%M:%S %Y/%m/%d")
def ts2str_2(ts): # use for file name
    return datetime.fromtimestamp(ts,gmt8).strftime("%Y%m%d-%H%M%S")
def now_str(): # ts -> local time string
    return ts2str(now())
def dt2offset(dt): # to isoformat
    return dt.strftime("%Y-%m-%dT%H:%M:%S")
def ts2offset(ts): # to isoformat
    return datetime.utcfromtimestamp(ts).strftime("%Y-%m-%dT%H:%M:%S")

def ts2dt(ts): # to datetime, local time
    return datetime.fromtimestamp(ts,gmt8)
def offset2dt(offset): # isoformat to datetime, utc
    return datetime.strptime(offset, "%Y-%m-%dT%H:%M:%S")
def gmt2dt(gmtformat_str): # gmtformat to datetime
    # TODO: %Z <-> GMT
    return datetime.strptime(gmtformat_str, "%a, %d %b %Y %H:%M:%S GMT")
def gmt2offset(gmt):
    # datetime.strptime(gmt, "%a, %d %b %Y %H:%M:%S GMT").strftime("%Y-%m-%dT%H:%M:%S")
    return dt2offset(gmt2dt(gmt))
    
def dt2ts(dt): # to timestamp, utc
    return int(dt.timestamp())

def dice():
    r = lambda : randint(0,11)
    return r(), r(), r()
def dice2str(tpl):
    # planet / object / what
    planet = ['太陽', '月亮', '水星', '金星', '火星', '木星',
              '土星', '天王星', '海王星', '冥王星', '北交點', '南交點' ]
    planet2 = ['形象', '情緒', '聰明', '愛情', '衝動', '擴張',
               '壓力', '變革', '夢幻', '神秘', '今生', '前世']
    # star / form / how
    star = ["牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座",
            "天秤座", "天蠍座", "射手座", "摩羯座", "水瓶座", "雙魚座" ]
    star2 = ['熱情', '頑固', '多變', '念舊', '王者', '完美', '均衡', '愛恨', '自由', '嚴肅', '新知', '博愛']
    # house / field / where
    house = ["1宮", "2宮", "3宮", "4宮", "5宮", "6宮",
             "7宮", "8宮", "9宮", "10宮", "11宮", "12宮"]
    house2 = ["命宮(自我)", "財帛宮(財富)", "兄弟宮(手足/學習)", "田宅宮(家庭)", "子女宮(孩子/愛情)",
              "奴僕宮(工作/健康)", "夫妻宮(婚姻/合夥)", "疾厄宮(死亡/偏財)", "遷移宮(學歷/旅行)",
              "官祿宮(事業/地位)", "福德宮(朋友/社團)", "玄秘宮(潛能/秘密)"]

    x,y,z = tpl[0], tpl[1], tpl[2]
    head = '[%s][%s][%s] ' % (planet[x],star[y],house[z])
    tail = '%sx%sx%s' % (planet[x],star[y],house[z])
    return head+tail

def get_plurk_post_time(pk): # get post_time to datetime
    gmt_str = pk['posted']
    return gmt2dt(gmt_str)
   
class Logger:
    def __init__(self, name):
        file_name = name + '_%s.log' % ts2str_2(now())
        self.f = open(file_name, 'w', encoding='utf8', errors='ignore')
        self.log('%s, log_start' % now_str())
    def log(self, s):
        print(s)
        self.f.write(s+'\n')
    def __del__(self):
        self.log('%s, log_end' % now_str())
        self.f.close()
    def close(self):
        self.f.close()
        
class PlurkBot:
    def __init__(self):
        self.startTime = datetime.now(gmt8)
        self.p = PlurkAPI()
        self.p.authorize()
        if self.p.is_authorized():
            print('%s, authorization completed' % now_str())
        else:
            raise RuntimeError('authorize fail')
       
    def getActive(self):
        return self.p.callAPI('/APP/Alerts/getActive')
    def addAsFriend(self, uid):
        return self.p.callAPI('/APP/Alerts/addAsFriend', {'user_id':uid})
    def poll_getPlurks(self, options):
        return self.p.callAPI('/APP/Polling/getPlurks', options)
    def responseAdd(self, plurkId, content, qualifier=':'):
        options={'plurk_id': plurkId, 'content': content, 'qualifier': qualifier}
        return self.p.callAPI('/APP/Responses/responseAdd', options)
        
    def check_notify_and_add_friend(self, logFile):
        t_str = now_str()
        alerts = self.getActive()
        logFile.log('%s, getActive, getAlert=%d' % (t_str, len(alerts)))
        for alert in alerts:
            print('notify type: %s' % alert['type'])
            if alert['type'] == 'friendship_request':
                uid = alert['from_user']['id']
                logFile.log('%s, addAsFriend, uid=%d' % (t_str, uid))
                self.addAsFriend(uid)
    
    def fetch_newer_plurks(self, offset, logFile, plurkFile): # start from offset to now, return plurks
        t_str = now_str()
        options = {'offset':offset, 'limit':'20', 'minimal_data':'true', 'minimal_user':'true'}
        data = self.poll_getPlurks(options) # offset = datetime.isoformat(timespec='seconds')
        ls = []
        for pk in data['plurks']:
            plurkFile.log('%s, %s, uid=%d, pkid=%d, %r' % (t_str, gmt2offset(pk['posted']), pk['user_id'], pk['plurk_id'], pk['content_raw']))
            ls.append(pk['plurk_id'])
        logFile.log('%s, Poll/getPlurks, %s, plurk=%d, pks=%s' % (t_str, offset, len(data['plurks']), ls))
        return data['plurks']

    # def fetch_period_plurks(self,dt1,dt2): # start from dt1 to dt2, return plurks
    #     loader = []
    #     dt = dt1
    #     while dt < dt2:
    #         pks = self.fetch_newer_plurks(dt2offset(dt),logFile,plurkFile)
    #         print('from %s, get %d plurk' % (dt2offset(dt), len(pks)))
    #         dt = get_plurk_post_time(pks[-1:]) # update last time
    #         print('last time in plurk: %s' % dt2offset(dt))
    #         if dt < dt2: # add all
    #             loader = loader + pks
    #         else: # overhead
    #             for pk in pks:
    #                 t = get_plurk_post_time(pk)
    #                 if t < dt2:
    #                     print('add plurk, plurkId=%d, postTime=%s' % (pk['plurk_id '], pk['posted']))
    #                     loader.append(pk)
    #                 else:
    #                     break
    #     print('get %d plurk' % len(loader))
    #     return loader

    def test_keywords(self, keywordList, string):
        for i in range(len(keywordList)):
            if keywordList[i] in string:
                return True, i+1
        return False, None
        
    def timeline_detect(self, logFile, plurkFile):
        pks = self.fetch_newer_plurks(ts2offset(now() - 62), logFile, plurkFile)
        keywordList = ['!占星骰', '！占星骰', '#召喚占星骰', '[召喚占星骰]', '召喚占星骰']
        for pk in pks:
            b, i = self.test_keywords(keywordList, pk['content_raw'])
            if b:
                print('has keyword')
                self.reply_astroDice(pk['plurk_id'], i, logFile)

    def reply_astroDice(self, plurkId, keywordId, logFile):
        tpl = dice()
        content = dice2str(tpl)
        logFile.log('%s, responseAdd, keyword=%d, pkid=%d, dice(%s)' % (now_str(), keywordId, plurkId, str(tpl)))
        self.responseAdd(plurkId, content)

