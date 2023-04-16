import datetime


class Logger:

    log_file_name = ""

    def __init__(self, file_name="fakebook.log"):
        self.log_file_name = file_name

    def log(self, level="INFO", message=""):
        log_file = open(self.log_file_name, "a")
        log_file.write("{}] {}] {}\n".format(
            datetime.datetime.now(),
            level,
            str(message)
        ))
        log_file.flush()

    def log_request(self, request):
        self.log("======================== REQUEST ==============================")
        self.log("Method : "+str(request.method))
        self.log("POST : "+str(request.POST))
        self.log("GET : "+str(request.GET))
        self.log("===================== END REQUEST =============================")
