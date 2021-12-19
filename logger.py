import datetime

def logger(f):
    filename = "log.txt"

    def log(dt, name, args, result):
        s = dt.date().__str__() + " " + dt.time().__str__() + " " + name \
            + args.__str__() + " => " + str(result) + "\n"
        with open(filename, "a") as file:
            file.write(s)

    def f2(*args, **kwargs):
        dt = datetime.datetime.now()
        result = f(*args, **kwargs)
        log(dt, f.__name__, args, result)
        return result

    return f2
