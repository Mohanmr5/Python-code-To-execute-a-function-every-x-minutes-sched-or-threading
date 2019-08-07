import sched, time

app  = Flask(__name__)

s = sched.scheduler(time.time, time.sleep)
def do_something(sc): 
    insertPost()
    
    #you can edit it for your x seconds and x minutes
    #s.enter(60 (seconds), 1(Minutes), do_something, (sc,))

    s.enter(60, 1, do_something, (sc,))

s.enter(60, 1, do_something, (s,))
s.run()


