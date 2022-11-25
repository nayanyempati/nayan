# Creating employee class
class employee:
    def __init__(self, name, weeklyhours, rate,overtimeRate,weeklytaxcredit):
        self.name=name
        self.weeklyhours=weeklyhours
        self.rate=rate
        self.overtimeRate=overtimeRate
        self.weeklytaxcredit=weeklytaxcredit

    def computeWeeklyPay(self, hours):
        compute = (hours*self.rate)+(hours+self.overtimeRate)
        print(compute)
        return compute

    def computeTax(self, grossPay):
        tax=(0.4*grossPay)-self.weeklytaxcredit
        print(tax)
        return tax
    
data=employee('nayan',35,11,15,70)
data.computeWeeklyPay(35)
    

        
