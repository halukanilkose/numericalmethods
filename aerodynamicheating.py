import numpy
import pandas
import math
import json


trajectoryDataName            = input("Please enter the name of the document: ") 
trajectoryData                = pandas.read_excel("{}.xlsx".format(trajectoryDataName))

with open("variables.txt", "r") as dosya:
    variable                  = json.load(dosya)


headerList                    = list(trajectoryData.columns.values)
timeDomain                    = trajectoryData[headerList[0]]
mach                          = trajectoryData[headerList[1]]
altitude                      = trajectoryData[headerList[2]]

freeStreamTemperature         = []
freeStreamPressure            = []
freeStreamDensity             = []
freeStreamDynamicViscosity    = []
freeStreamThermalConductivity = []


i=0
while i<len(altitude):
    if altitude[i] < 11000:
        freeStreamTemperature.append(15.04 - 0.00649 * altitude[i])
        freeStreamPressure.append(101.29 * ((freeStreamTemperature[i] + 273.15) /288.08) ** (5.256))
    elif 11000 <= altitude[i] <=25000:
        freeStreamTemperature.append(-56.46)
        freeStreamPressure.append(22.65 * math.exp(1.73 - 0.000157 * altitude[i]))
    else:
        freeStreamTemperature.append(-131.21 + 0.00299 * altitude[i])
        freeStreamPressure.append(2.488 * ((freeStreamTemperature[i] + 273.15) / 216.6) ** (-11.388))
    
    freeStreamDensity.append(freeStreamPressure[i] / (0.2869 * (freeStreamTemperature[i] + 273.15))) 
    freeStreamThermalConductivity.append(1.993 * 10 **(-3) * (freeStreamTemperature[i] + 273.15) ** (1.5) / (freeStreamTemperature[i] + 273.15 + 112))
    freeStreamDynamicViscosity.append(1.458 * 10 **(-6) * (freeStreamTemperature[i] + 273.15) ** (1.5) / (freeStreamTemperature[i] + 273.15 + 110.4) )    
    
    
    i+=1

freeStreamPressure          = (pandas.Series(freeStreamPressure) * 1000).tolist()
freeStreamTemperature       = (pandas.Series(freeStreamTemperature) + 273.15).tolist()


location                    =  variable["location"]
flightDuration              =  variable["flightDuration"]
timeStep                    =  variable["timeStep"]
timeMatrix                  =  numpy.arange(0,flightDuration+timeStep,timeStep) 


thermalConductivity          =  variable["materialProperties"]["thermalConductivity"]
density                      =  variable["materialProperties"]["density"]
specificHeat                 =  variable["materialProperties"]["specificHeat"]
thermalDiffusivity           =  thermalConductivity / (density * specificHeat)

thickness                    =  variable["thickness"]
directionStep                =  variable["directionStep"]
directionMatrix              =  numpy.arange(0,thickness+directionStep,directionStep)
FourierNumber                =  thermalDiffusivity * timeStep / directionStep ** 2

gasConstant                  = 287.05
specificHeatRatio            = 1.4
stefanBolztmanConstant       = 5.67 * 10 **(-8)
emissivity                   = variable["materialProperties"]["emissivity"]

temperatureMatrix            =  numpy.zeros((numpy.size(directionMatrix),numpy.size(timeMatrix)))
initialCondition             =  273.15 + variable["initialCondition"]
temperatureMatrix[:,0]       =  initialCondition
heatTransferCoefficient      =  []
heatFlux                     =  []
stabilityCriteria            =  []


i = 0
while i<len(timeMatrix)-1:
    interpolatedFreeStreamMach            = numpy.interp(timeMatrix[i],timeDomain,mach)
    interpolatedFreeStreamDensity         = numpy.interp(timeMatrix[i],timeDomain,freeStreamDensity)
    interpolatedFreeStreamTemperature     = numpy.interp(timeMatrix[i],timeDomain,freeStreamTemperature)
    interpolatedFreeStreamPressure        = numpy.interp(timeMatrix[i],timeDomain,freeStreamPressure)

    freeStreamSonicVelocity               = (specificHeatRatio *  gasConstant * interpolatedFreeStreamTemperature) ** (0.5)
    freeStreamVelocity                    = freeStreamSonicVelocity * interpolatedFreeStreamMach
    
    if interpolatedFreeStreamMach <= 1 :
        localStagnationPressure           = interpolatedFreeStreamPressure * ( 1 + (( specificHeatRatio - 1 ) / 2 ) * interpolatedFreeStreamMach**2)**(specificHeatRatio / (specificHeatRatio - 1))
    else:
        freeStreamStagnationPressure      = interpolatedFreeStreamPressure * ( 1 + (( specificHeatRatio - 1) / 2 ) * interpolatedFreeStreamMach**2)**(specificHeatRatio / (specificHeatRatio - 1))
        localStagnationPressure           = freeStreamStagnationPressure   * ((( specificHeatRatio + 1 ) / 2 * interpolatedFreeStreamMach**2) / (1 + (specificHeatRatio - 1 ) / 2 * interpolatedFreeStreamMach**2))**(specificHeatRatio/(specificHeatRatio-1)) * (2 * specificHeatRatio / (specificHeatRatio + 1) * interpolatedFreeStreamMach**2 - (specificHeatRatio - 1) / (specificHeatRatio + 1)) ** (1 / (1 - specificHeatRatio))
    
    dynamicPressure                       = 0.5 * interpolatedFreeStreamDensity * freeStreamVelocity **2
    maximumPressureCoefficient            = (localStagnationPressure - interpolatedFreeStreamPressure) / dynamicPressure
    localPressure                         = dynamicPressure * maximumPressureCoefficient * math.sin(0) ** 2 + interpolatedFreeStreamPressure
    localMachNumber                       = (((localStagnationPressure / localPressure) ** ((specificHeatRatio - 1) / specificHeatRatio ) - 1 ) * ( 2 / (specificHeatRatio-1))) ** (0.5)
    localStagnationTemperature            = interpolatedFreeStreamTemperature * ( 1 + (specificHeatRatio - 1) / 2 * interpolatedFreeStreamMach **2)
    localTemperature                      =  localStagnationTemperature / ( 1 + (specificHeatRatio - 1) / 2 * localMachNumber **2)
    
    airDynamicViscosity                 = 1.458 * 10 ** (-6) * (localTemperature) ** (3/2) / (localTemperature+ 110.4)
    airThermalConductivity              = 1.993 * 10 ** (-3) * localTemperature ** (1.5) / (localTemperature + 112)
    airSpecificHeat                     = -1 * 10 **(-7) * (localTemperature) ** (3) + 0.0003 * localTemperature **(2) - 0.047 * localTemperature + 991.75
    airPrandtlNumber                    = airDynamicViscosity * airSpecificHeat / airThermalConductivity
    airReynoldsNumber                   = interpolatedFreeStreamDensity * freeStreamSonicVelocity * location / airDynamicViscosity
    
    if airReynoldsNumber <= 5 * 10 **5 :
        recoveryFactor   = airPrandtlNumber ** (1/2)
    else:
        recoveryFactor   = airPrandtlNumber ** (1/3)
    
    
    adiabaticWallTemperature            = localTemperature * ( 1  + (specificHeatRatio - 1) / 2 * localMachNumber **2)
    
    referenceTemperature                = localTemperature + 0.5 * (temperatureMatrix[0,i]- localTemperature) + 0.22 * (adiabaticWallTemperature - localTemperature)
    referenceDensity                    = localPressure / (gasConstant * referenceTemperature)
    referenceDynamicViscosity           = (1.458 * 10 ** (-6) * (referenceTemperature) ** (3/2)) / (referenceTemperature + 110.4)
    referenceThermalConductivity        = 1.993 * 10 ** (-3) * (referenceTemperature) ** (3/2) / (referenceTemperature + 112)
    referenceSpecificHeat               = -1 * 10 **(-7) * (referenceTemperature) ** (3) + 0.0003 * referenceTemperature **(2) - 0.047 * referenceTemperature + 991.75
    
    
    localSonicVelocity                  = (specificHeatRatio * gasConstant * localTemperature) ** (0.5)
    localVelocity                       = localSonicVelocity * localMachNumber
    
    referenceReynoldsNumber             = (referenceDensity * localVelocity * location) / (referenceDynamicViscosity)
    referencePrandtlNumber              = referenceDynamicViscosity * referenceSpecificHeat / referenceThermalConductivity
    
    if referenceReynoldsNumber <= 5 * 10 **(5):
        localNusseltNumber              = 0.332 * referenceReynoldsNumber ** (1/2) * referencePrandtlNumber ** (1/3)    
    else:
        localNusseltNumber              = 0.0296 * referenceReynoldsNumber ** (4/5) * referencePrandtlNumber ** (1/3)
    
    heatTransferCoefficient.append( localNusseltNumber * referenceThermalConductivity / location)
    heatFlux.append(heatTransferCoefficient[i] * (adiabaticWallTemperature - temperatureMatrix[0,i]))
    
    temperatureMatrix[0,i+1] = temperatureMatrix[0,i] + ( 2 * heatFlux[i] * timeStep ) / (directionStep * density * specificHeat) - 2 * ( thermalConductivity * timeStep) / (density * specificHeat * directionStep**2) * (temperatureMatrix[0,i]-temperatureMatrix[1,i])
        
    j = 1
    while j < len(directionMatrix)-1:
        temperatureMatrix[j,i+1] = (1-2*FourierNumber) * temperatureMatrix[j,i] + FourierNumber * (temperatureMatrix[j+1,i] + temperatureMatrix[j-1,i])
        j+=1
            
    temperatureMatrix[len(directionMatrix)-1,i+1] = temperatureMatrix[len(directionMatrix)-1,i] - ( 2 * timeStep * thermalDiffusivity / directionStep** 2 ) * (temperatureMatrix[len(directionMatrix)-1,i] - temperatureMatrix[len(directionMatrix)-2,i])
     
    i+=1


postProcessTimeFrequency     = 1 
postProcessLength            = int(postProcessTimeFrequency / timeStep)
heatFlux.append(0)
heatTransferCoefficient.append(0)


time                         = []
skinTemperatureData          = []
innerWallData                = []
heatFluxData                 = []
referenceHTCData             = []


i = 0
while i<=len(timeMatrix):
    time.append(timeMatrix[i])
    skinTemperatureData.append(temperatureMatrix[0,i]-273.15)
    innerWallData.append(temperatureMatrix[-1,i]-273.15)
    heatFluxData.append(heatFlux[i])
    referenceHTCData.append(heatTransferCoefficient[i])
    i+=postProcessLength
    
    

time                         = pandas.Series(time)
skinTemperatureData          = pandas.Series(skinTemperatureData)
innerWallData                = pandas.Series(innerWallData)
heatFluxData                 = pandas.Series(heatFluxData)
referenceHTCData             = pandas.Series(referenceHTCData)

data                         = pandas.concat([time,skinTemperatureData,innerWallData,heatFluxData,referenceHTCData],axis=1)
header                       = ["Time[s]","Outer Wall Temperature[°C]","Inner Wall Temperature[°C]","Heat Flux[W/m\u00b2]","HTC[W/m\u00b2K]"]
data.to_csv("data.txt",index=None, sep="," , header= header)

    


