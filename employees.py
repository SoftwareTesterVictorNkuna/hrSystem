from hr import (
    
    SalaryPolicy,
    CommisionPolicy,
    HourlyPolicy
    
)

from productivity import (
    ManagerRole,
    SecretaryRole,
    SalesRole,
    FactoryRole
)
class Employee:
    def __init__(self,id,name):
        self.id =id
        self.name=name
        self.address=None

class Manager(Employee,ManagerRole,SalaryPolicy):
    def __init__(self,id,name,weekly_salary):
        super ().__init__(id,name)
        self.weekly_salary =weekly_salary
        
    
        
class Secretary(Employee,SecretaryRole,SalaryPolicy):
    def __init__(self,id,name,weekly_salary):
        SalaryPolicy.__init__(self,weekly_salary)
        super().__init__(id,name)
        
    
        
class SalesPerson(Employee,SalesRole,CommisionPolicy):
    def __init__(self,id,name,weekly_salary,commision):
        CommisionPolicy.__init__(self,weekly_salary,commision)
        super().__init__(id, name)


class FactoryWorker(Employee,FactoryRole,HourlyPolicy):
    def __init__(self, id, name,hours_worked,hour_rate):
        HourlyPolicy.__init__(self,hours_worked,hour_rate)
        super().__init__(id, name)


class TemporarySecretary(Employee, SecretaryRole,HourlyPolicy):

    def __init__(self, id, name,hours_worked,hour_rate):
        HourlyPolicy.__init__(self,hours_worked,hour_rate)
        super().__init__(id, name)