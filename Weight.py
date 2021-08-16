print('Hello, welcome to Weight Calculator')
weight = float(input('Input weight here: '))
ty_pe = input('(K)g  or  (L)bs?: ')

if ty_pe.lower() == 'K':
    converted = weight / 0.45
    print('Weight in Lbs: ' + str(converted))

else:
    converted_ = weight * 0.45
    print('Weight in K: ' + str(converted_))

