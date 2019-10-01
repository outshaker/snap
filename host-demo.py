from queue import Queue
from time import sleep
from random import choice, randint
import threading
from threading import Event

class CmdPack():
    def __init__(self, cmd, *args):
        self.pack = [cmd,args]
    def __str__(self):
        cmd, args = self.pack[0], self.pack[1]
        if len(args):
            return "'%s', %s" % (cmd, str(args))
        else:
            return "'%s'" % cmd
    def getCmd(self):
        return self.pack[0]
    def getArgs(self):
        return self.pack[1]

class GameCtrl():
    def __init__(self): # TODO add player
        self._pipes_from = [Queue(),Queue()]
        self._pipes_to = [Queue(),Queue()]
        self._actived = [Event(), Event()]
        self._cmds = ["action","end"]
        self._next = Event() # signal for turn next player
        self._gameOver = Event() # signal for game over

        self.p1_loop = threading.Thread(target=self.playerLoop, args=[0])
        self.p2_loop = threading.Thread(target=self.playerLoop, args=[1])
        self.p1_loop.start()
        self.p2_loop.start()

    def send(self, pid, cmdPack):
        print("[info] GameCtrl.send(p%d, %s) " % (pid,cmdPack))
        self._pipes_to[pid].put(cmdPack)

    def update(self,pid, *args):
        self.send(pid, CmdPack("update",*args))

    def recvTestCmd(self, pid, cmdPack): # test
        # print("[test] GameCtrl.recvTestCmd(%s) " % cmdPack) # debug
        self._pipes_from[pid].put(cmdPack)

    def actionEventHandler(self, pid, *args):
        # TODO comlete it
        if len(args):
            print("[info] action_event_handler: pid=%d args=%s " % (pid,str(args)))
        else:
            print("[info] action_event_handler: pid=%d " % pid)
        # rule system check and make result
        # update game status
        other_pid = (pid+1) % 2
        self.update(other_pid, *args)

    def endEventHandler(self, pid):
        print("[info] end_event_handler: pid=%d " % pid)
        self._actived[pid].clear()
        self._next.set()

    def forceEndEventHandler(self, pid):
        print("[info] forceEnd_event_handler: pid=%d " % pid)
        self._actived[pid].clear()
        self._next.set()
        
    def setGameOver(self):
        self._gameOver.set()

    def playerActionTest(self, pid): # test
        print("[test] playerAction waiting pid=%d " % pid)
        self._actived[pid].wait()
        print("[test] playerAction_start pid=%d " % pid)
        n = randint(1,5) # cmd
        t = randint(5,10) / n # sec
        print("[test] playerAction pid=%d n=%d t=%.1fs " % (pid,n,t))
        
        # TODO add more action
        cmds = ["action" for i in range(n)]
        cmds.append("end")
        print("[test] playerAction cmds=%s " % str(cmds))
        for cmd in cmds:
            if self._actived[pid].is_set():
                self.recvTestCmd(pid,CmdPack(cmd))
                sleep(t)
            else:
                print("[erro] playerAction_end pid=%d " % pid)
                return
        print("[test] playerAction_end pid=%d " % pid)
        # sleep(1) # wait signal off

    def playerLoop(self, pid): # run on thread, controled by signal
        while True:
            print("[info] playerLoop waiting pid=%d " % pid)
            self._actived[pid].wait()
            print("[info] playerLoop_start pid=%d " % pid)
            while self._actived[pid].is_set():
                cmdPack = self._pipes_from[pid].get() # block=True
                print("[info] GameCtrl.recv(p%d, %s) " % (pid, cmdPack))
                cmd, args = cmdPack.getCmd(), cmdPack.getArgs()
                # TODO add more
                if cmd is "action":
                    self.actionEventHandler(pid,*args)
                elif cmd is "end":
                    self.endEventHandler(pid)
                else:
                    print("[warm] playerLoop: unsupported_cmd %s " % cmd)
            print("[info] playerLoop_end pid=%d " % pid)

    def playerTurn(self, pid):
        print("[info] playerTurn_start pid=%d " % pid)
        print("[debug] playerTurn: clear _next pid=%d " % pid)
        self._next.clear()

        self.send(pid, "start")
        print("[debug] playerTurn: set _actived pid=%d " % pid)
        self._actived[pid].set() # turn on loop

        self.update(pid, "draw_card")

        forceEnd_countDown = threading.Timer(7, self.forceEndEventHandler, [pid])
        # player_loop = threading.Thread(target=self.playerLoop, args=[pid])
        # player_loop.start()
        player_action_tester = threading.Thread(target=self.playerActionTest, args=[pid])
        player_action_tester.start()
        forceEnd_countDown.start()

        self._next.wait()
        forceEnd_countDown.cancel() # end, cancel timer
        print("[info] playerTurn_end pid=%d " % pid)

    def gameLoop(self):
        print("[info] gameLoop_start ")
        self._gameOver.clear()
        gameOver_countDown = threading.Timer(22, self.setGameOver) # test
        gameOver_countDown.start()
        active_pid = 0 # first active player
        while self._gameOver.is_set() is False:
            self.playerTurn(active_pid)
            active_pid = (active_pid+1) % 2 # change player
            print("[info] gameLoop: change_player pid=%d " % active_pid)
        print("[info] gameLoop_end ")

g = GameCtrl()
# g.playerTurn(0)
g.gameLoop()
