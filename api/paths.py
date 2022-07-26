from api.route import Route

@Route(path="/func1")
def random_name(eg):
    return eg

@Route("/big")
def function2(eg):
    return eg + eg + eg

# defaults to function name if left blank
@Route()
def small(eg=1):
    return int(eg) + int(eg)
