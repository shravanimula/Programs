def adding_msg(display):
    def inner_fun(name):
        if name=='bbbb':
            print("hello",name)
        else:
            display(name)

    return inner_fun

@adding_msg
def display(name):
    print("hello",name,"good morning")

display('aaaa')
display('bbbb')
display('ccc')
