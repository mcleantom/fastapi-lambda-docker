from mangum import Mangum
from MyApp import api

handler = Mangum(app=api)
