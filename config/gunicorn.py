import multiprocessing

bind = "0.0.0.0:8000"
# workers = multiprocessing.cpu_count() * 2 + 1
workers = 1
errorlog = 'config/error.log'
infolog = 'config/info.log'
accesslog = 'config/access.log'