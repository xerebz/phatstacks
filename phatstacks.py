import sys, traceback, os

home = os.path.expanduser("~")
pid = os.getpid()
output = os.path.join(home,"stacktrace-%s.log"%(pid))
for thread, frame in sys._current_frames().items():
    with open(output, "w") as f:
        traceback.print_stack(frame, file=f)
