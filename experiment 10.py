class Slab:
    """Represents one income tax slab."""
    def __init__(self, lower, upper, rate):
        self.lower = lower
        self.upper = upper
        self.rate = rate          # e.g. 0.05 for 5%

    def tax_for(self, income):
        """Tax on the part of income that falls inside this slab."""
        if income <= self.lower:
            return 0
        amount_in_slab = min(income, self.upper) - self.lower
        return amount_in_slab * self.rate


class TaxCalculator:
    """Holds all slabs and calculates income tax."""
    STANDARD_DEDUCTION = 75000
    REBATE_LIMIT = 1200000
    CESS_RATE = 0.04

    def __init__(self):
        inf = float("inf")
        self.slabs = [
            Slab(0, 400000, 0.00),
            Slab(400000, 800000, 0.05),
            Slab(800000, 1200000, 0.10),
            Slab(1200000, 1600000, 0.15),
            Slab(1600000, 2000000, 0.20),
            Slab(2000000, 2400000, 0.25),
            Slab(2400000, inf, 0.30),
        ]

    def calculate_income_tax(self, annual_gross):
        taxable_income = annual_gross - self.STANDARD_DEDUCTION

        if taxable_income <= self.REBATE_LIMIT:   # rebate
            return 0

        tax = sum(slab.tax_for(taxable_income) for slab in self.slabs)
        tax += tax * self.CESS_RATE               # add cess
        return tax


class Employee:
    """Stores employee details (monthly salary components)."""
    def __init__(self, emp_id, name, basic, hra, allowances):
        self.emp_id = emp_id
        self.name = name
        self.basic = basic
        self.hra = hra
        self.allowances = allowances

    def monthly_gross(self):
        return self.basic + self.hra + self.allowances


class PayrollProcessor:
    """Creates the payslip for an employee."""
    PF_RATE = 0.12

    def __init__(self, tax_calculator):
        self.tax_calculator = tax_calculator

    def generate_payslip(self, emp):
        gross = emp.monthly_gross()
        pf = emp.basic * self.PF_RATE
        annual_tax = self.tax_calculator.calculate_income_tax(gross * 12)
        monthly_tax = annual_tax / 12
        net = gross - pf - monthly_tax

        print("=" * 35)
        print(f"PAYSLIP - {emp.name} (ID: {emp.emp_id})")
        print("=" * 35)
        print(f"Basic            : {emp.basic:>12,.2f}")
        print(f"HRA              : {emp.hra:>12,.2f}")
        print(f"Allowances       : {emp.allowances:>12,.2f}")
        print(f"Gross Salary     : {gross:>12,.2f}")
        print("-" * 35)
        print(f"PF Deduction     : {pf:>12,.2f}")
        print(f"Income Tax (mo.) : {monthly_tax:>12,.2f}")
        print("-" * 35)
        print(f"NET SALARY       : {net:>12,.2f}")
        print("=" * 35)


# ---------- Main program ----------
if __name__ == "__main__":
    calculator = TaxCalculator()
    payroll = PayrollProcessor(calculator)

    e_id=int(input("enter id of employee : "))
    e_name=input("Enter name of employee : ")
    e_basic=int(input("Enter Basics : "))
    e_Hra=int(input("Enter Hra : "))
    e_Allow=int(input("Enter Allowances : "))



    emp1 = Employee(e_id,e_name, basic=e_basic, hra=e_Hra, allowances=e_Allow)
    payroll.generate_payslip(emp1)