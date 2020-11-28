from flask import json


from config.config import ConfigDB
from utils.utils import Utils

database = ConfigDB()
utils = Utils()


class ControllerUser:
    def save(self, req):
        user = req.get_json()
        if user['nome'] == "":
            return json.dumps({"code": 400, "description": "Você não sabe seu nome?!", }), 400
        elif len(user['nome']) > 100:
            return json.dumps({"code": 400, "description": "Praque vc quer ter um nome com mais de 100 caracteres, acrevia isso!!", }), 400
        elif user['cpf'] == "":
            return json.dumps({"code": 400, "description": "Você nao tem cpf? seu inadimplente", }), 400
        elif user['email'] == "":
            return json.dumps({"code": 400, "description": "O e-mail, não vai por??", }), 400
        elif len(user['email']) > 400:
            return json.dumps({"code": 400, "description": "Pra que um email com mais de 400? faz outro o merda!", }), 400
        elif user['cpf'] != "":
            response = utils.validar_cpf(user['cpf'])
            if response == False:
                return json.dumps({"code": 400, "description": "Está fugindo da lei? que nao pode colocar um CPf real!", }), 400
            else:
                if user['email'] != "":
                    responseEmail = utils.validar_email(user['email'])
                    if responseEmail == False:
                        return json.dumps({"code": 400, "description": "Não inventa email, coloca um de verdade", }), 400
                    else:
                        return database.save(user)

    def remove(self, req):
        user = req.get_json()
        if user['cpf'] == None:
            return json.dumps({"code": 400, "description": "Este CPF nao é valido, da pra colocar o seu, ou ta se escondendo da policia?", }), 400
        else:
            return database.delete(user)

    def query(self, req):
        user = req.get_json()
        return database.query(user)
