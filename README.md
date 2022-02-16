# Wireless-Sound-Control-AI

This project enables us to alter the device volume without using any device like mouse or keyboard keys.
This is done by using open source libraries like opencv , pycaw
Using opencv we are getting live feed from the device camera which we feed into the algorithim 
Using MediaPipe we will then recognize the finger land-mark points , in which the land-mark of thumb and index finger 
we then calculate the distance between thumb and index using pythagoras theorem
With the pycaw library we get acess to device volume control where we take the min and max value which we will 
adjust with ratio of distance between choosen finger landmarks 
