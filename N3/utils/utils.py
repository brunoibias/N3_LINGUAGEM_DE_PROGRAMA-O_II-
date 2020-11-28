""" regex """
import re


class Utils:
    def validar_cpf(self, cpf):
        if len(cpf) != 14:
            return False
        elif cpf == '000.000.000-00' or cpf == '111.111.111-11' or cpf == '222.222.222-22' or cpf == '333.333.333-33' or cpf == '444.444.444-44' or cpf == '555.555.555-55' or cpf == '666.666.666-66' or cpf == '777.777.777-77' or cpf == '888.888.888-88' or cpf == '999.999.999-99':
            return False
        else:
            return True

    def validar_email(self, email):
        return re.search(r'^[\w]+@[\w]+\.[\w]{2,4}', email) != None
