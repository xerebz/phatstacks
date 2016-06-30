# phatstacks
A few useful scripts for debugging Python performance on running processes. No code instrumentation required.
## Prerequisites
Depends on  [pyrasite](pyrasite.com).
<pre>pip install pyrasite</pre>
..which depends on gdb.
<pre>sudo apt install gdb</pre>
On Ubuntu, you'll also need to enable ptrace.
<pre>echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope</pre>

## Usage
Write the stacktrace of a running program to $HOME/stacktrace-PID.log
<pre>pyrasite PID /path/to/phatstacks.py</pre>
Start profiling a running program
<pre>pyrasite PID /path/to/profstart.py</pre>
End profiling and write cProfile output to $HOME/profile-PID.cprof
<pre>pyrasite PID /path/to/profend.py</pre>
View profiling output using RunSnakeRun or pstats
<pre>python -m pstats $HOME/profile-PID.cprof</pre>