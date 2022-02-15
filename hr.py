#A payrollSystem class that processes payroll:

# In hr.py

class PayrollSystem:
    def calculate_payroll(self, employees):
        print('Calculating Payroll')
        print('===================')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            if employee.address:
                print('- Sent to:')
                print(employee.address)
            print('')
            

class SalaryPolicy:
    def __init__(self,weekly_salary):
        
        self.weekly_salary=weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary



class HourlyPolicy:
    def __init__(self,hours_worked,hour_rate):
        
        self.hour_worked =hours_worked
        self.hour_rate =hour_rate


    def calculate_payroll(self):
        return self.hour_worked *self.hour_rate


class CommisionPolicy(SalaryPolicy):
    def __init__(self,weekly_salary,commision):
        super().__init__(weekly_salary)
        self.commision=commision

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commision




