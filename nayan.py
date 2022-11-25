# Creating employee class
class employee:
    def _init_(self, name, weeklyhours, rate,overtimeRate,weeklytaxcredit):
        self.name=name
        self.weeklyhours=weeklyhours
        self.rate=rate
        self.overtimeRate=overtimeRate
        self.weeklytaxcredit=weeklytaxcredit

    def computeWeeklyPay(self, hours):
        compute = (hours*self.rate)+(hours+self.overtimeRate)
        return compute
    
    def computeTax(self, grossPay):
        tax=(0.4*grossPay)-self.weeklytaxcredit
        return tax
    
    


        

    