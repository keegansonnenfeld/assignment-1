#calculating momentem
def Momentum(m, v):
    return (float(m) * float(v))

#calc energy
def KineticEnergy(m, v):
    return (float(m) * float(v) * float(v))

#inputs
M = input("enter the Mass :")

V = input("enter the Velocity :")



print(" the momentum is " + str(Momentum(M, V)),"kg*m/s",)

print(" the kinetic energy is " + str(KineticEnergy(M, V)),"jules",)