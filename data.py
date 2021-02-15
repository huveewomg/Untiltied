import time
import sys

toolbar_width = 20
tool_width_exit = 25

print('Welcome')
print('Water is starting')


# code below are progress bar for bootup screen 
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) #


for i in range(toolbar_width):
    time.sleep(0.1)
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar

print('This is a simple application to find if your plant is a good condition.')


from decimal import Decimal as D

minDegree = D(20.0) 
minHumidity  = int(50) 
minIntensity = int(1) 
minMoisture = int(1) 

maxDegree = D(30)    #Temperature celcius
maxHumidity = int(60) #Humidity in air r/h
maxIntensity = int(100) #light intensity 
maxMoisture = int(100) #soil moisture 

print('How many degree is it? [in degree celcius]')
Degree = input('')
Degree = D(Degree)

print('How high is the humidity?')
Humidity = input('')
Humidity = int(Humidity)

print('How intense is the sun?')
Intensity = input('')
Intensity = int(Intensity)

print('How wet is the soil?')
Moisture = input('')
Moisture = int(Moisture)




#user input value
if Degree < minDegree:
    print('For Temperature: it is too cool for now!')
elif Degree > maxDegree:
    print('For Temperature: is slighty high')
elif Degreec >= minDegree <=maxDegree:
    print('For Temperature: is suitable to water')

if Humidity < minHumidity:
    print('For Humidity: The weather is dry!')
elif Humidity > maxHumidity:
    print('For Humidity: Is too wet')    
elif Humidity >= minHumidity < maxHumidity:
    print('For Humidity: Is a right Humidity') # test)
             
if Intensity < minIntensity:
    print('For Light Intensity: The sunlight is low!')
elif Intensity > maxIntensity:
    print('For Light Intensity: The sun is too strong')    
elif Intensity >= minIntensity <= maxIntensity:
    print('For Light Intensity: Right amount of light')
    
if Moisture < minMoisture:
    print('For Soil Moisture: It is dried and you should water your plant.')
elif Moisture > maxMoisture:
    print('For Soil Moisture: is too wet')
elif Moisture >= minMoisture <=maxMoisture:
    print('For Soil Moisture: Is not too wet nor too dry so dont water too much!')







#end boot
sys.stdout.write("[%s]" % (" " * tool_width_exit)) #ending
sys.stdout.flush()
sys.stdout.write("\b" * (tool_width_exit+1)) # return to start of line, after '['

for i in range(tool_width_exit):
    time.sleep(0.10) # Little fast than the loading bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("]\n") # this ends the progress bar    











    

    







