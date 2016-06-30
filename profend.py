import cProfile
import os
if hasattr(cProfile, 'pr'):
    cProfile.pr.disable()
    home = os.path.expanduser("~")
    pid = os.getpid()
    outfile = os.path.join(home,"profile-%s.cprof" % pid)
    cProfile.pr.dump_stats(outfile)
