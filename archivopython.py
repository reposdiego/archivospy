## Se almacena un texto en una variable.
txt = '''R is a programming language and software environment for statistical computing 
and graphics supported by the R Foundation for Statistical Computing.[3] The R language 
is widely used among statisticians and data miners for developing statistical software[4] 
and data analysis.[5] Polls, surveys of data miners, and studies of scholarly literature 
databases show that R's popularity has increased substantially in recent years.[6]
'''

## Se verifica el contenido.
print(txt)

open("file/wiki.txt", "w").write(txt)


y=open("file/wiki.txt", "r").read(txt)
print(y)

"index" "name" "value"
1 "A" 3.03
2 "B" 5.14
3 "C" 0.4
4 "D" 1.13
5 "E" 8.25
