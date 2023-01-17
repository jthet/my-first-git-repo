


words = []

with open('words','r') as infile:
    for i in range(10,20,2):
        print(infile.readline().strip('\n'))

'''
my_shapes = ['circle', 'heart', 'triangle', 'square']

with open('my_shapes.txt', 'w') as f:
    for shape in my_shapes:
        f.write( f'{shape}\n' )

'''