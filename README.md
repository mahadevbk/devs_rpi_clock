# devs_rpi_clock
A Raspberry clock with weather information from openweathermap and ipgeolocation.io

Head to openweathermap and get your free API Key
Head to ipgeolocation.io and get your fee API Key
Edit the file dev_rpi_clock.py and enter your API keys, Edit your location and unit preferences.

Note : The script with throw up an error if the API Keys are not entered.

Edit the screen resolution as per the resolution of your screen. In the file, the default resolution is 320 x 240 for wave share 3.2" TFT.
You can change the Background and Foreground colours as per your preference. In the file the default is a White Text over a Blue Background.
You can edit the Text sizes for each individual element #comments have been added to show where the text size needs to be edited.

Save the file dev_rpi_clock.py in the home folder of your Raspberry Pi.

To autolaunch the clock upon startup, goto the autostart folder by entering "cd /home/pi/.config/autostart"
Make a file dev_rpi_clock.desktop by entering 'nano dev_rpi_clock.desktop'
Paste the lines below :
[Desktop Entry]
Type=Application
Name=Clock
Exec=/usr/bin/python3 /home/pi/dev_rpi_clock.py
press Ctrl+X to exit and press Y to save the file.

Once you restart your Pi, the Clock should autostart.
