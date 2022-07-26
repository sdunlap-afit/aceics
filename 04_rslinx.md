
# RSLinx setup

RSLinx is proprietary software that acts as a communications gateway for PLCs. The programming software (RSLogix 500 in our case) uses RSLinx to access individual PLCs, so you have to configure RSLinx first. Once it is configured, simply leave it running in the background.

# Instructions

1. Select "RSLinx Classic" from the Windows start menu.

<div align="center">
<img src="./img/rslinx1.png" width="150">
</div><br/>

2. Once it loads, select "Communications >> Configure Drivers...". In the resulting window, select "Ethernet devices" from the dropdown, then click "Add New...". Leave the default name, and clock "OK".

You can now enter your IP address or shortly below.

<div>
<img align="left" src="./img/rslinx_1_b.png" height="300">
<img align="right" src="./img/rslinx_1_c.png" height="300">  
</div><br clear="all" /><br>


3. Click on the "RSWho" button, and you should see two drivers under "Workstation". Right-click on the AB_ETH driver and select "Configure Driver". 


<div>
<img align="left" src="./img/rslinx1_5.png" height="300">
<img align="right" src="./img/rslinx2.png" height="300">  
</div><br clear="all" /><br>



4. If you haven't already, enter your IP address into a Station and click "OK".

<div align="center">
<img src="./img/rslinx3.png" width="500">
</div><br/>

5. Wait. RSLinx will automatically scan your IP address and will show the device info. This takes a little while. Make sure "Autobrowse" is selected.

<div align="center">
<img src="./img/rslinx4.png" width="500">
</div><br/>

6. If you waited a couple minutes and RSLinx still fails to connect, let me know and I can take a look. I will be monitoring all the PLCs, so I should see if one goes offline. We do have backups, so if one kit fails, I can assign you another kit.

<div align="center">
<img src="./img/rslinx5.png" width="500">
</div><br/>

