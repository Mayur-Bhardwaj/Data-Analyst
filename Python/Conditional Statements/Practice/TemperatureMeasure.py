# Develop a program that takes the temperature in celsius as input and classifies it based on the following criteria:
# temperature below 0 degree celsius should ;ablled as "Extreme cold, 
# temperature between 0 degree and 20 degree celsius as "Cold".
# temperature between  20 degree and 30 celsius as "Moderate".
# temperature between 30 degree celsius or above "Hot".
# If temperatue exceeds 45 degree, the program dhould display an additional warning, "Heatwave Alert!".
  
temperature = float(input("Please Enter the Temperature: "))

if (temperature < 0):
    print("Extreme Cold")
elif (temperature >=0 and temperature <= 20):
    print("Cold")
elif (temperature >20 and temperature <=30):
    print("Moderate")
elif (temperature > 30 and temperature <= 45):
    print("Hot")
elif (temperature > 45):
    print("HeatWave Alert !!")
else:
    print("Sorry!! You enter wrong Temperature Please Re-write Again.")

    