bind = "0.0.0.0:8000"
pidfile = "/home/box/web/gunicorn/gunicorn.pid"
accesslog = "/home/box/web/gunicorn/access.log"
errorlog = "/home/box/web/gunicorn/error.log"
pythonpath = "/home/box/web/ask"
daemon = False
worker = 5
timeout = 60
