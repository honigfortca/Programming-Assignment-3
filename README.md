# Programming-Assignment-3
Steps for reproducing my [Christine Honigfort's] results:

1. To begin, first download Oracle VirtualBox to faciliate your virtual machine. You will need to restart your laptop after downloading this before you can use the VM (or at least I needed to).
3. Next, search online for Ubuntu 16.04.7 LTS (Xenial Xerus). This is preferable over newer versions of Ubuntu because it automatically comes with python version 2.7. Download this version of Ubuntu (64-bit) so that it can be added as your operating system in your virtual machine. 
4. Use the blue button labeled "new" in VirtualBox to add Ubuntu 16.04.7 and set up your "Programming Assignment 3" VM.
5. Use https://github.com/StanfordSNR/pantheon/ to clone pantheon and follow the indicated setup procedure.
6. Test that pantheon works by typing "src/wrappers/pcc.py receiver 5555" in one terminal and typing "src/wrappers/pcc.py sender 127.0.0.1 5555" in another terminal to see if the server and receiver connect and report SendRate, RTT, CWnd, PktSndPeriod, RecvACK, and RecvNAK.
7. Read the steps on http://mahimahi.mit.edu/. First, download all of the depedencies one by one that are listed on the site. Next type in the following commands (downloading any additional depedencies that are mentioned in error statements):
           git clone https://github.com/ravinet/mahimahi
           cd mahimahi
           ./autogen.sh
           ./configure
            make
            sudo make install
8. Use the command mv to move mahimahi into pantheon/src/wrappers.
9. Download the following schemes: Copa, TCP Cubic, and Sprout.
10. Use "sudo pip2 install numpy==1.15.0" to install numpy from the root folder (to navigate to the root type "su" and then enter your password).
11. Use "sudo apt-get install python-matplotlib" to install matplotlib from the root.
12. Create the file christine_trace_high_bandwidth_low_latency.py (the code for this file can be found in this github).
13. Use the linux command "python christine_trace_high_bandwidth_low_latency.py>christine_trace_high_bandwidth_low_latency.trace" to create the trace file from the python file.
14. Use the linux command "src/experiments/test.py local --runtime 60 --schemes "copa cubic sprout"  --uplink-trace src/experiments/christine_trace_high_bandwidth_low_latency.trace --downlink-trace src/experiments/christine_trace_high_bandwidth_low_latency.trace --append-mm-cmds "mm-delay 10"".
15. Create the file christine_trace_low_bandwidth_high_latency.py (the code for this file can be found in this github).
16. Use the linux command "python christine_trace_low_bandwidth_high_latency.py>christine_trace_low_bandwidth_high_latency.trace" to create the trace file from the python file.
17. Use the linux command "src/experiments/test.py local --runtime 60 --schemes "copa cubic sprout"  --uplink-trace src/experiments/christine_trace_low_bandwidth_high_latency.trace --downlink-trace src/experiments/christine_trace_low_bandwidth_high_latency.trace --append-mm-cmds "mm-delay 100"".
18. View and analyze the generated reports.
 
