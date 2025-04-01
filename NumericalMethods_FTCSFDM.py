import pandas
import numpy
import matplotlib.pyplot as plt


directionStep                 = 2*10**(-3)
length                        = 10*10**(-3)
directionVector               = pandas.Series(numpy.arange(0,length+directionStep,directionStep))
temperatureDisturbion         = []

i=0
while i<len(directionVector):
    temperatureDisturbion.append(16.67 * (1 - (directionVector[i]**2/length**2)) + 340.91)
    i+=1

temperatureDisturbion         = pandas.Series(temperatureDisturbion)

plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.plot(directionVector, temperatureDisturbion, linestyle='-', color='red', label='y = x^2')
plt.xlabel('Location [m]',fontweight="bold")
plt.ylabel('Temperature [°C]',fontweight="bold")
plt.xlim([0.000,0.010])
plt.ylim([330,360])
plt.savefig("steadyStateSolution.png", dpi=1500)
plt.close()

    
steadyStateResult = pandas.concat([directionVector,temperatureDisturbion.round(2)],axis=1).T
steadyStateResult.to_excel("steadyStateResult.xlsx",index=False,header=None)


thermalConductivity           = 30 
thermalDiffusitivity          = 5 * 10**(-6) 
thermalCapacity               = thermalConductivity / thermalDiffusitivity

heatGeneration                = 2 * 10 **(7)
solutionDuration              = 400
heatTransferCoefficient       = 1100
freeStreamTemperature         = 250

biotNumber                    = heatTransferCoefficient * directionStep / thermalConductivity
fourierNumber                 = 0.5 / (1 + biotNumber)
timeStep                      = fourierNumber * directionStep **2 / thermalDiffusitivity
checkingTimeStep              = solutionDuration % timeStep

if checkingTimeStep == 0: 
    timeStep = timeStep
else:
    timeStep = solutionDuration / (solutionDuration // timeStep + 1)

fourierNumber                 = (thermalDiffusitivity * timeStep) / (directionStep**2)
timeMatrix                    = numpy.arange(0, solutionDuration + timeStep,timeStep)


temperatureMatrix             = numpy.zeros((numpy.size(directionVector),numpy.size(timeMatrix)))
temperatureMatrix[:,0]        = temperatureDisturbion


j = 0
while j < len(timeMatrix)-1:
    temperatureMatrix[0,j+1] = fourierNumber * (2 * temperatureMatrix[1,j] + heatGeneration *directionStep**2 / thermalConductivity) +  (1 - 2* fourierNumber)*temperatureMatrix[0,j]
    
    i=1
    while i<len(directionVector)-1:
        temperatureMatrix[i,j+1] = (1-2*fourierNumber) * temperatureMatrix[i,j] + fourierNumber *(temperatureMatrix[i+1,j] + temperatureMatrix[i-1,j] + (heatGeneration * directionStep**2) / thermalConductivity )
        i+=1
    
    temperatureMatrix[-1,j+1] = (2*fourierNumber) * (temperatureMatrix[-2,j] + biotNumber * freeStreamTemperature + 0.5 * heatGeneration * directionStep**2 / thermalConductivity) + (1 - 2*fourierNumber-2*biotNumber*fourierNumber)*temperatureMatrix[-1,j]
    j+=1

temperatureMatrix = pandas.DataFrame(temperatureMatrix)
temperatureMatrix = temperatureMatrix.round(2)
temperatureMatrix = pandas.concat([pandas.Series(directionVector),temperatureMatrix],axis=1)
temperatureMatrix.to_excel("results.xlsx",header=[""]+timeMatrix.tolist(), index=False)


plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.plot(timeMatrix, temperatureMatrix.T[0][1:], linestyle='-', color='black')
plt.plot(timeMatrix, temperatureMatrix.T[5][1:], linestyle='-', color='red')
plt.xlabel('Time [s]',fontweight="bold")
plt.ylabel('Temperature [°C]',fontweight="bold")
plt.legend(["x=0.00 m","x=0.01 m"])
plt.xlim([0,400])
plt.ylim([320,480])
plt.savefig("transientSolution.png", dpi=1500)
plt.close()





