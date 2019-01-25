# Information-Gathering-Tool


* Reconnaissance is a systematic attempt to locate, 
  gather, identify and record information about the target.

* Attackers extract information such as live machines, port, 
  port status, OS details, device type, system uptime to launch attack. 

* IGT is a tool developed using Python to perform some basic 
  information gathering and hacking methodologies like pinging, 
  footprinting of information like operating system details, port scanning, 
  performing flooding attacks, etc. using the utilities and commands provided by KALI LINUX.

* It provides its users with an easy GUI to execute the same

IGT is a software, developed with Python, which runs on Linux Platforms. It performs basic Information gathering (Reconnaissance), which is the first step of the hacking methodology, which uses the pre-loaded Nmap package at the backend. Along with performing reconnaissance, the feature of performing DOS attack and Smurf Flooding attack on a target machine has also been included, which uses the Hping3 package at the backend. Other than this, IGT provides the user with the System Information such as Kernel Version, BIOS information, Memory details, etc. of their own system. 

This tool has been created on Python 3.0 platform in combination of Kali Linux utilities  that work in backend. This tool has been beneficial to its non-technical users as its simple GUI and awk commands have excluded the unnecessary information.

The tools like Nmap have been used in backend for port scanning which gives the basic results port state, Os detection, Service Version etc. The hping3 tool helps to perform DOS attack on the target.

This tools works as stepping stone to all the Ethical Hackers as gathered information will help them to then exploit their target, which is the second stage of Hacking Methodology.    

The main purpose of developing this software was to release the user from the complexities of memorizing the commands and typing them in the terminal. IGT provides a friendly GUI to perform these tasks. Additionally, the tool gives the user filtered outputs, i.e. the user gets only the specific and necessary information shown in the output panel. Whereas, in the Command Line, it becomes hectic to search for the desired information in the midst of a lengthy output.
