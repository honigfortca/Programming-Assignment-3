# Programming-Assignment-3
Steps for reproducing my [Christine Honigfort's] results:

1. To begin, first download Oracle VirtualBox to faciliate your virtual machine. You will need to restart your laptop after downloading this before you can use the VM (or at least I needed to).
3. Next, search online for Ubuntu 16.04.7 LTS (Xenial Xerus). This is preferable over newer versions of Ubuntu because it automatically comes with python version 2.7. Download this version of Ubuntu (64-bit) so that it can be added as the operating system in your virtual machine. 
4. Use the blue button labeled "new" in VirtualBox to add Ubuntu 16.04.7 and set up your "Programming Assignment 3" in your VM.
5. Use https://github.com/StanfordSNR/pantheon/ to clone pantheon and follow the indicated setup procedure.
6. Test that pantheon works by typing "src/wrappers/pcc.py receiver 5555" in one terminal and typing "src/wrappers/pcc.py sender 127.0.0.1 5555" in another terminal to see if the server and receiver connect and report SendRate, RTT, CWnd, PktSndPeriod, RecvACK, and RecvNAK.
7. Read the steps on http://mahimahi.mit.edu/. First, download all of the depedencies one by one that are listed on the site. Next type in the following commands (downloading any additional depedencies that are mentioned in error statements)
           git clone https://github.com/ravinet/mahimahi
           cd mahimahi
           ./autogen.sh
           ./configure
            make
            sudo make install
   7. Use the command mv to move mahimahi into pantheon/src/wrappers.
