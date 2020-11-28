
from flask import Flask, request, json
from controllers.user import ControllerUser

userController = ControllerUser()


class Routes:
    def create(self, req):
        response = userController.save(req)
        return response

    def remove(self, req):
        response = userController.remove(req)
        return response

    def query(self, req):
        response = userController.query(req)
        return response
