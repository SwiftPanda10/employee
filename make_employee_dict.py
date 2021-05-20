# Author: Samuel Bennett
# Date: 5/19/2021
# Description: Function creates employee dictionary that stores and connects name, employee id,salary, and email

class Employee:
    __emp_name = ''
    __emp_id = ''
    __emp_sal = 0
    __emp_mail = ''

    def __init__(self, name, id, sal, email):
        self.__emp_name = name
        self.__emp_id = id
        self.__emp_sal = sal
        self.__emp_mail = email

    def get_name(self):
        return self.__emp_name

    def get_id_number(self):
        return self.__emp_id

    def get_salary(self):
        return self.__emp_sal

    def get_mail_address(self):
        return self.__emp_mail


def make_employee_dict(names, ids, sals, emails):
    diction = {}
    for i in range(len(names)):
        emp = Employee(names[i], ids[i], sals[i], emails[i])
        diction[ids[i]] = emp
    return diction


emp_names = ["Jean", "Kat", "Pomona"]
emp_ids = ["100", "101", "102"]
emp_sals = [30, 35, 28]
emp_emails = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
result = make_employee_dict(emp_names, emp_ids, emp_sals, emp_emails)

print(result["100"].get_name())
