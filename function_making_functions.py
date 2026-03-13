# A function that builds functions

def constructor(color, size):
    print('>>> constructor color:', color, "size:", size)

    def repeater():
        print('### repeater color:', color, "size:", size)

    print('<<< exit constructor')
    return repeater
    
red_xl = constructor('red', 'xl')
pink_sm = constructor('green', 'sm')

for i in range(0,4):
    red_xl()
    pink_sm()


