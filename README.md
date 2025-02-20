# MicroHeartbeat
A very simple graphical application written in Python which periodically pings a given DNS address, logging and timestamping results to user's home directory. The script may be easily modified to ping an address of your choice. Pings are sent in groups of five at ten second intervals.

The script will now automatically parse the log file for you, recording any incidents of packet loss in packetloss.log which can also be found in your home directory. Each line in packetloss.log corresponds to the above mentioned ten second period.

Intended as a basic, user-friendly solution for tracking packet loss, server uptimes and what have you.

Note for Windows users: The executable is currently only working under Linux. I recommend grabbing the latest version of Python 3 from the Windows Store, downloading the script and executing it directly if you'd like to use this utility on Win 10 or 11.

Looking for the log file?

Linux Users: /home/YourUserHere/

Windows Users: C:/Users/YourUserHere/
