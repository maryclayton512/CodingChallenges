#Name: Mary Clayton
#Date: 7/10/2022
#Purpose: Waveform Generator

#INPUT
#Import time library
import time
#Global Variables
MaxY = 40
NumCycles = 10
Step = 4
PlotSymbol = "o"
EmptySymbol = " "

for y in range(NumCycles):
    for waveheight in range(0, MaxY, Step):
        line = ""
        #Pad a string with spaces
        #Put a "*" at the desired height
        #First loop ascends
        for i in range(MaxY):
            if i == waveheight:
                line += PlotSymbol
            else:
                line += EmptySymbol
        print(line)
        time.sleep(0.05)

        #this loop descends
        for waveheight in range(0, MaxY, Step):
            line = ""
            for i in range(MaxY):
                if i == MaxY - waveheight - 1:
                    line += PlotSymbol
                else:
                    line += EmptySymbol
            print(line)
            time.sleep(0.10)
