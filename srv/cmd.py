from srv.apiHandler import testConnect

def command_test():
    return 'testing some stuff'

def command_math():
    a = 5
    b = 10
    c = a + b
    return str(c)

def command_api():
    apiout = testConnect()
    return apiout

def command_help():
    return 'The following commands are allowed by our bot. (!help, !math, !test)'

def comman_suicide():
    return '/me believes that suicide is not a solution to a temporary problem. Please contact 1(800)273-8255 if you need to talk.'

