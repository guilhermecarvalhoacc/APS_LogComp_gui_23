
Trabalho soma(x::Int, y::Int)::Int
  Devolva x + y
FIM

# v2.3 testing
x_1::Int
x_1 = 2
x_1 = soma(1, x_1)

x_1 = Leia()
SoSe ((x_1 > 1) && !(x_1 < 1)) 
  x_1 = 3
SeNumFor 
  
  x_1 = (-20+30)*4*3/40 # teste de comentario
  
FIM
Amostre(x_1)
x_1 = Leia()
SoSe ((x_1 > 1) && !(x_1 < 1))
  x_1 = 3
SeNumFor
  x_1 = (-20+30)*12/40
FIM
Amostre(x_1)
ArrochaEnquanto ((x_1 > 1) || (x_1 == 1)) 
  x_1 = x_1 - 1
  Amostre(x_1)
FIM

#RESPOSTA ESPERADA 3,3,2,1,0