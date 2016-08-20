from flask import Flask
app = Flask(__name__)
app.config.from_object('foghornw.default_settings')
app.config.from_envvar('FOGHORNW_SETTINGS')

import foghornw.views
import foghornw.routes
