# player event-trigger system

from queue import Queue
from time import sleep
from random import choice, randint
import threading

class Dispatcher():
    def __init__(self):
        self._inbox = Queue()
        self._outbox = Queue()
        self._recvSet = set() # {"start","update"} # input
        self._sub = {} # {"start":startEventHandler, "update":updateEventHandler}

    def regist(self, ev, hdlr):
        if ev not in self._recvSet:
            self._recvSet |= {ev}
        self._sub[ev] = hdlr
        print("[info] regist event: %s, handler: %s" % (ev,hdlr))

    def unregist(self, ev):
        if ev in self._recvSet:
            del self._sub[ev]
            self._recvSet -= {ev}
            print("[info] unregist event: %s" % ev)

    def eventLoop(self):
        while True:
            r = self._inbox.get() # block=True
            if type(r) is str and r in self._recvSet:
                cmd = r
                print("[info] event %s" % cmd)
                self._sub[cmd]()
            elif type(r) is list and r[0] in self._recvSet:
                cmd, args = r[0], r[1]
                print("[info] event %s %s" % (cmd,args))
                self._sub[cmd](args)
            else: # unsupported event
                print("[warm] unsupported event")

    def send(self, cmd, *args):
        if args:
            self._outbox.put([cmd,args]) # with args
        else:
            self._outbox.put(cmd) # no arg
        return

class PlayerCtrl():
    def __init__(self, dispatcher):
        self._ACTIVE = threading.Event()
        self._dispatcher = dispatcher

    def send(self, cmd, *args):
        print("[info] Ctrl: send %s, %s" % (cmd,args))
        self._dispatcher.send(cmd, *args)

    def action(self):
        print("[info] Ctrl cmd: action")
        cmds = ["creature_card","spell_card","weapon_card","char_ability","creature_attack","char_attack"]
        self.send("action",choice(cmds))

    def end(self):
        print("[info] Ctrl cmd: end")
        self.send("end")
        self._ACTIVE.clear()

    def eventLoopTest(self, n=None, interval=None): # test
        while True:
            print("[info] Ctrl: event loop wait signal")
            self._ACTIVE.wait()
            while self._ACTIVE.is_set():
                print("[info] Ctrl: simulation for one round")
                if n is None: n=randint(1,10) # 1-10 cmd
                if interval is None: interval=10+randint(1,20) # 10-30 sec
                t = interval / n
                print("[info] Ctrl: action_n=%d interval_t=%.1fs" % (n,t))
                for i in range(n):
                    if self._ACTIVE.is_set():
                        self.action()
                        sleep(t)
                    else:
                        print("[erro] Ctrl: player is inactive")
                        break
                self.end()

    # TODO creat a true event loop
    # TODO implement timeout force end
    def startEventHandler(self):
        print("[info] Ctrl EventHandler: start")
        self._ACTIVE.set()

    def forcedEndEventHandler(self):
        print("[info] Ctrl EventHandler: forced end")
        self._ACTIVE.clear()

class PlayerModel():
    def __init__(self):
        self._ENV = {}

    # TODO CRUD, creat, read, update, delete
    def updateEventHandler(self, *args):
        print("[info] Model EvnetHandler: Update")
        print(args) # test
        
    # TODO implement draw card

def startTest(dispatcher):
    print("test start event")
    sleep(1)
    dispatcher._inbox.put("start")

def updateTest(dispatcher):
    print("test update event")
    sleep(1)
    dispatcher._inbox.put("update")

def forceEndTest(dispatcher):
    print("test forceEnd event")
    sleep(1)
    dispatcher._inbox.put("start")
    sleep(10)
    dispatcher._inbox.put("forceEnd")

# Test create object and regist event
# def foo(): print("foo")
# def bar(): print("bar")
# msgr = Dispatcher()
# msgr.regist("start",foo)
# msgr.regist("update", bar)

msgr = Dispatcher()
pctrl = PlayerCtrl(msgr)
pmodl = PlayerModel()
msgr.regist("start",pctrl.startEventHandler)
msgr.regist("update", pmodl.updateEventHandler)
msgr.regist("forceEnd", pctrl.forcedEndEventHandler)

t = threading.Thread(target = msgr.eventLoop)
t.start()

t2 = threading.Thread(target = pctrl.eventLoopTest)
t2.start()

startTest(msgr)
updateTest(msgr)
forceEndTest(msgr)
