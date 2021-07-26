<div>
<img align="left" src="./img/afit-logo.png" height="100" title="HILICS"><img align="right" src="./img/ccr-logo.png" height="100" title="HILICS">  
</div><br clear="all" /><br>





# ACE 2021 - Industrial Control Systems

## Introduction

Welcome to ICS security. Today you will explore a programmable logic controller that is controlling two simulated processes. The equipment you will be working with is representative of control devices you might find as part of a larger control system network. You will learn how to explore unknown control devices, configure proprietary software to interface with the controller, and use your access to manipulate the processes. In a real-world scenario, an adversary's attack will depend on their desired effect (e.g., equipment damage, process manipulation, etc.). 

## Schedule

	0830 - 0930:	Lecture
	0930 - 1000:	Intro/demo
	1000 - 1200:	Basic labs
	1200 - 1300:	Lunch
	1300 - 1330:	Discussion and/or questions
	1300 - 1530:	Advanced labs


## Equipment

Industrial control systems contain a wide variety of equipment and processes. This picture shows an example of a simple water system training platform. This system is expensive, takes up a significant amount of space and requires compressed air and water tanks. Thus, it is infeasible to build multiple platforms, and one system cannot be shared amongst 50 students.

<div align="center">
<img src="./img/water_system.png" width="500">
</div><br/>

Now, we could just hook up multiple programmable logic controllers and let you go to town, but it would not be realistic or interesting unless there was a process to control. That's why we built the [hardware-in-the-loop](https://en.wikipedia.org/wiki/Hardware-in-the-loop_simulation) industrial control system (HILICS) training platform. For specifics on the system, check out the [HILICS github page](https://github.com/sdunlap-afit/hilics).

<div align="center">
<img src="./img/hilics.png" width="500">
</div><br/>

Each HILICS kit contains a MicroLogix 1100 programmable logic controller to act as the target for attack and defense. A Raspberry Pi simulates the physical process and feeds inputs/outputs to/from the programmable logic controller. As far as the MicroLogix knows, it is operating a full-fledged industrial control system.

<div align="center">
<img src="./img/block_diagram.png" height="300">
</div><br/>


You will be working in your prearranged groups in breakout rooms. Each group will have access to one HILICS kit, accessible through the GECO VPN. To enable this virtual interface, the Raspberry Pis have noVNC installed; you will use a browser to access the noVNC interface to view and operate the process simulations. You should not try to attack the Raspberry Pi's VNC interface. 


<div align="center">
<img src="./img/hilics_kits.png" width="500">
</div><br/>


Each Raspberry Pi is directly connected to the MicroLogix 1100 via an Ethernet cable, and port-forwarding is used to route the necessary traffic through the Raspberry Pi to the MicroLogix. Thus, you will access both the VNC and the MicroLogix interfaces through the same IP address. This is representative of port-forwarding through a NATed router.

<div align="center">
<img src="./img/hilics_close.png" width="500">
</div><br/>


# Documentation and procedures

Read through the documentation in this order.

* [Network Information](./01_network.md)

* [Simulation Raspberry Pi vnc](./02_hilics_vnc.md)
* [PLC's web interface](./03_web_interface.md)
* [Setup RSLinx to connect to the PLC](./04_rslinx.md)
* [RSLogix background](./05_rslogix.md)
* [Retrieve the PLC's project file (Upload)](./06_upload.md)
* [Program the PLC (Download)](./07_download.md)
* [See the PLC in operation live (Go Online)](./08_online.md)


