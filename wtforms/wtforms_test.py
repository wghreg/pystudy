#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import time
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop

from wtforms.fields import IntegerField, StringField, DateField
from wtforms.validators import DataRequired
from wtforms_tornado import Form

'''
https://pypi.org/project/wtforms-tornado/
form提交验证框架
'''
class UserForms(Form):
    userid = IntegerField(validators=[DataRequired()])
    username = StringField(validators=[DataRequired()])
    passwd = StringField(validators=[DataRequired()])
    createDate = DateField(validators=[DataRequired()], default=time.time())


class UserHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        form = UserForms(self.request.arguments)
        if form.validate():
            self.write(str(form.data['userid'] + form.data['username']))
        else:
            self.set_status(404)
            self.write("" % form.errors)

application = Application([
    (r'/', UserHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    IOLoop.instance().start()