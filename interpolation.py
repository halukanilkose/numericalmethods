import numpy
import matplotlib.pyplot as plt
import pandas

dataName                   = input("Please enter the name of the document:")
data                       = numpy.loadtxt("{}.txt".format(dataName))
firstVariable              = data [:,0]
secondVariable             = data [:,1]


firstVariableName          = input("First Variable Label: ")
secondVariableName         = input("Second Variable Label: ") 

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.plot(firstVariable, secondVariable, linestyle='-', color='red')
plt.xlabel('{}'.format(firstVariableName),fontweight="bold")
plt.ylabel('{}'.format(secondVariableName),fontweight="bold")
plt.xlim([0,40])
plt.ylim([0,12])
plt.savefig("UninterpolatedData.png",dpi=1500)
plt.show()


interpolationInterval      = float(input("Please enter the interpolation interval for the data: "))
lastValue                  = firstVariable [-1] + 1 - (firstVariable[-1] % 1)
firstValue                 = firstVariable [0] - (firstVariable[0] % 1)
firstVariableInterpolation = numpy.arange(firstValue,lastValue+interpolationInterval,interpolationInterval)
interpolatedData           = []


i = 0
while i<len(firstVariableInterpolation):
    interpolatedData.append(numpy.interp(firstVariableInterpolation[i],firstVariable,secondVariable))
    i+=1



plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.plot(firstVariableInterpolation, interpolatedData, linestyle='-', color='red')
plt.xlabel('{}'.format(firstVariableName),fontweight="bold")
plt.ylabel('{}'.format(secondVariableName),fontweight="bold")
plt.xlim([0,40])
plt.ylim([0,12])
plt.savefig("InterpolatedData.png",dpi=1500)
plt.show()


firstVariableOutput        = pandas.Series(numpy.round(firstVariableInterpolation,2))
secondVariableOutput       = pandas.Series(numpy.round(interpolatedData,2))
data                       = pandas.concat([firstVariableOutput,secondVariableOutput],axis=1)
data.to_excel("interpolatedData.xlsx",header=["{}".format(firstVariableName),"{}".format(secondVariableName)],index=None)
