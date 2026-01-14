class Company:
    company_name = ""

    @classmethod
    def set_company(cls, name):
        cls.company_name = name

    @classmethod
    def get_company(cls):
        return f"Моя компания называется - {cls.company_name}"

name = input()
company = Company
company.set_company(name)
print(company.get_company())
