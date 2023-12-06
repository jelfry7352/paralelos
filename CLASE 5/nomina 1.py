class Nomina:

 def Afp(self,sb):

    return sb * 0.07


 def Ars(self,sb):

    return sb * 0.02

 def TotalDesc(self,afp, ars):

    return afp + ars

 def SueldoNeto (self,sb,td):

    return sb - td


n= Nomina()
sueldo = float(input("Entra Sueldo Base :"))
afp= n.Afp(sueldo)
ars= n.Ars(sueldo)
descuentos = n.TotalDesc(afp, ars)
sn = n.SueldoNeto(sueldo,descuentos)

print("Afp         :(10.2f)",format(afp))
print("Ars         :(10.2f)",format(ars))
print("Descuentos  :(10.2f)",format(descuentos))
print("SueldoNeto  :(10.2f)",format(sn))


