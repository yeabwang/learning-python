heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

print(len(heros))
heros.append('black panther')
print(heros)
heros.insert(heros.index('hulk'), 'black panther')
print(heros)
heros.insert(heros.index('thor'), 'doctor strange')
heros.remove('thor')
heros.remove('hulk')
print(heros)
print(sorted(heros))
for i in len(heros):
    for j in (i+1)