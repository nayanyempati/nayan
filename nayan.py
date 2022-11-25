# Creating employee class
class employee:
    def __init__(self, name, weeklyhours, rate,overtimeRate,weeklytaxcredit):
        self.name=name
        self.weeklyhours=weeklyhours
        self.rate=rate
        self.overtimeRate=overtimeRate
        self.weeklytaxcredit=weeklytaxcredit

    def computeWeeklyPay(self, hours):
        compute = (hours*self.rate)+(4*self.overtimeRate)
        return compute

    def computeTax(self, grossPay):
        tax=(0.4*grossPay)-self.weeklytaxcredit
        return tax
    
data=employee('nayan',35,11,15,70)

computeWeeklyPay=data.computeWeeklyPay(35)
computeTax = data.computeTax(computeWeeklyPay)

print("Weekly Pay: "+str(computeWeeklyPay)+" and compute tax: "+ str(computeTax))
    
