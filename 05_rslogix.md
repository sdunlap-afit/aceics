
# RSLogix Micro (aka, RSLogix 500)

RSLogix (RS stands for Rockwell Software) is the programming "IDE" used for writing control code for Rockwell Automation PLCs. You will use this software to interface with the PLC and accomplish various tasks. In my experience, RSLogix is among the easiest to work with and is a great starting point for learning PLC programming. That said, it is still confusing and poorly designed (just like all ICS software).

## Background

Most ICS programming software costs thousands of dollars for each license (although adversaries can pirate copies). Rockwell has different versions of RSLogix for their various families of PLCs. The MicroLogix series (MicroLogix 1100, 1400, etc.) use RSLogix 500. The larger CompactLogix and ControlLogix series use RSLogix 5000, which has been renamed to Studio 5000. Not only do you have to buy a license for the specific software, but there are different versions of RSLogix for each major firmware revision (e.g., versions 16, 17, 18, 19...), so you have to have the license to match the firmware version of your target PLC. If that wasn't annoying enough, if you find yourself exploring an ICS network, it is very common to come across multiple brands of control devices (e.g., Seimens, Rockwell, GE, etc.), each having their own programming software. 

In my opinion, the most valuable trait you can develop is the ability to come into an unknown system and just start learning how it works. This requires a degree of confidence and a lack of intimidation or fear. No matter how large or complicated the system, you can eventually break it down into bite-size chunks.


## Terminology

For some reason, in ICS, simple terminology such as "download" and "upload" are completely backward. Here are a few terms and definitions to help clear things up. These terms and their meanings are pretty much standard across control systems. 

* **Project file** - a file containing all of the configuration and programming for a device/PLC.

* **Download** - send a project file from the programming software to the PLC (like I said, backward).

* **Upload** - retrieve a project file (the source code) from a PLC to the programming software. Most PLCs have this feature, although the retrieved project file will most likely lack comments and other metadata.

* **Online** - the programming software maintains an active network connection to monitor the state of the programming. This is used for debugging, troubleshooting or temporarily monitoring a PLC in operation. You will use this mode to figure out how the code works and make sure that your code works as expected.

* **PLC Mode** - most PLCs have a physical key (like a tractor key) that lets the operators change the mode of the PLC between these three options:

    * **Run mode** - the PLC is running the project file, controlling a process and limits the activities you can do. For example, you cannot download a project file while the PLC is in Run mode.

    * **Program mode** - the PLC is idle (not controlling the process) and you are free to download a project file.

    * **Remote mode** - this allows you to remotely (i.e., over the network) switch between Run mode and Program mode. Your PLCs should be in Remote mode. 100% of the PLCs I have looked at on Shodan have been in this mode.


