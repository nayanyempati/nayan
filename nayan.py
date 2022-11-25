#https://github.com/nayanyempati/nayan/commits/main/nayan.py

# Creating employee class
class employee:
    def __init__(self, name, weeklyhours, rate,overtimeRate,weeklytaxcredit):
        self.name=name
        self.weeklyhours=weeklyhours
        self.rate=rate
        self.overtimeRate=overtimeRate
        self.weeklytaxcredit=weeklytaxcredit

    def computeWeeklyPay(self, hours):
        if(self.overtimeRate<0):
            return "Overtime cannot be negative"
        compute = (hours*self.rate)+(4*self.overtimeRate)
        if(compute <0):
            #Returing 0 if weekly pay is negative
            return 0
        else:  
            return compute

    def computeTax(self, grossPay):
        tax=(0.4*grossPay)-self.weeklytaxcredit
        if(tax<0):
            # Returing 0 if tax is negative
            return 0
        return tax
    
data=employee('nayan',35,11,15,70)

computeWeeklyPay=data.computeWeeklyPay(35)
computeTax = data.computeTax(computeWeeklyPay)

print("Weekly Pay: "+str(computeWeeklyPay)+" and compute tax: "+ str(computeTax))






        

