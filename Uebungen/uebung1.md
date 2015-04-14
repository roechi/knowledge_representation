In [1]: obst = ['Apfel', 'Birne', 'Orange']

In [2]: obst
Out[2]: ['Apfel', 'Birne', 'Orange']

In [3]: for x in obst:
   ...:     print(x + ' zu verkaufen')
   ...:     
Apfel zu verkaufen
Birne zu verkaufen
Orange zu verkaufen

In [4]: obstpreise = {'Apfel' : 2.5, 'Birne' : 3., 'Orange' : 2.75}

In [5]: obstpreise
Out[5]: {'Apfel': 2.5, 'Birne': 3.0, 'Orange': 2.75}

In [18]: for item in obstpreise.items():
    print(item[0] + ' zu verkaufen für ' + str(item[1]) + ' Euro pro Kilo')
   ....:     
Orange zu verkaufen für 2.75 Euro pro Kilo
Apfel zu verkaufen für 2.5 Euro pro Kilo
Birne zu verkaufen für 3.0 Euro pro Kilo

In [17]: S {[x**2 for x in range(10)}

In [18]: S
Out[18{[0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

In [19]: V = [2**x for x in range(12)]

In [20]: V
Out[20]: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

In [22]: M = {x for x in S if x % 2 == 0}

In [23]: M
Out[23]: {0, 4, 16, 36, 64}

strings = ['Some String', 'Art', 'Music',
  'Artificial Intelligence']

In [33]: strings = [x.lower() for x in strings]

In [34]: strings
Out[34]: ['some string', 'art', 'music', 'artificial intelligence']