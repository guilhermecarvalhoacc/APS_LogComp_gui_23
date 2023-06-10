import sys

TT_INT		  = 'INT'
TT_PLUS       = 'PLUS'
TT_MINUS      = 'MINUS'
TT_MULT       = 'MULT'
TT_DIV        = 'DIV'
TT_OP         = 'OP'
TT_CP         = 'CP'
TT_OC         = 'OC'
TT_CC         = 'CC'
TT_EQUAL      = "EQUAL"
TT_VAR        = "IDENTIFIER"
TT_QL         = "QL"
TT_EE         = "EE"
TT_GT         = "GT"
TT_LT         = "LT"
TT_AND        = "e"
TT_OR         = "ou"
TT_NOT        = "nem"
TT_DOT        = "ponto"
TT_STR        = "Texto"
TT_VIR        = "virgula"
TT_DOISPONTOS = 'DOISPONTOS'
TT_EOF        = 'EOF'

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'


class Tokenizer:
    def __init__(self,source):
        self.source = source
        self.position = 0
        self.next = None
    
    def selectNext(self):
        lista_Reservadas = ["Amostre","Leia","SoSe","SeNumFor","ArrochaEnquanto","FIM","Int","Texto","Devolva","Trabalho"]
        while self.position < len(self.source) and self.source[self.position] == " ":
            self.position += 1

        if  self.position >= len(self.source):
            self.next = Token(TT_EOF,None)
        else:
            source = self.source
            caracter = source[self.position]

            if caracter.isalpha():
                variavel = self.make_identifier()
                if variavel in lista_Reservadas:
                    self.next = Token(variavel,variavel)
                else:
                    self.next = Token(TT_VAR,variavel)
                return self.next

            if caracter.isdigit():
                if source[self.position + 1].isalpha():
                    raise Exception("variavel invalida")
                else:
                    num = self.make_number()
                    self.next = Token(TT_INT,num)
                    return self.next

            elif caracter == "+":
                self.next = Token(TT_PLUS,None)
                self.position += 1
                return self.next
            
            elif caracter == "-":
                self.next = Token(TT_MINUS,None)
                self.position += 1
                return self.next

            elif caracter == "*":
                self.next = Token(TT_MULT,None)
                self.position += 1
                return self.next
            
            elif caracter == "/":
                self.next = Token(TT_DIV,None)
                self.position += 1
                return self.next

            elif caracter == "(":
                self.next = Token(TT_OP,None)
                self.position += 1
                return self.next

            elif caracter == ")":
                self.next = Token(TT_CP,None)
                self.position += 1
                return self.next
            elif caracter == "{":
                self.next = Token(TT_OC,None)
                self.position += 1
                return self.next

            elif caracter == "}":
                self.next = Token(TT_CC,None)
                self.position += 1
                return self.next

            elif caracter == "\n":
                self.next = Token(TT_QL,None)
                self.position += 1
                return self.next
            
            elif caracter == "=":
                if source[self.position + 1] == "=":
                    self.next = Token(TT_EE,None)
                    self.position += 2
                else:
                    self.next = Token(TT_EQUAL,None)
                    self.position += 1
                return self.next

            elif caracter == ">":
                self.next = Token(TT_GT,None)
                self.position += 1
                return self.next

            elif caracter == "<":
                self.next = Token(TT_LT,None)
                self.position += 1
                return self.next
            elif caracter == "&" and source[self.position + 1] == "&":
                self.next = Token(TT_AND,None)
                self.position += 2
                return self.next
            elif caracter == "|" and source[self.position + 1] == "|":
                self.next = Token(TT_OR,None)
                self.position += 2
                return self.next

            elif caracter == "!":
                self.next = Token(TT_NOT,None)
                self.position += 1
                return self.next

            elif caracter == ".":
                self.next = Token(TT_DOT,None)
                self.position += 1
                return self.next

            elif caracter == ":":
                if source[self.position + 1] == ":":
                    self.next = Token(TT_DOISPONTOS,None)
                    self.position += 2
                else:
                    raise Exception("Invalido")
                return self.next

            elif caracter == ",":
                self.next = Token(TT_VIR,None)
                self.position += 1
                return self.next


            elif caracter == '"':
                self.position += 1
                palavra = ""
                while (self.source[self.position] != '"'):
                    palavra += self.source[self.position]
                    self.position +=1 
                    if (self.position >= len(self.source)):
                        raise Exception("não fechou aspas")
                self.position += 1 
                self.next = Token(TT_STR,palavra)
                return self.next

            else:
                raise Exception("Invalido")

    def make_number(self):
        source = self.source
        num_str = ''
        while source[self.position] != None and source[self.position].isdigit():
            num_str += source[self.position]

            if (self.position == len(source) - 1):
                self.position += 1
                break

            self.position += 1


        return int(num_str)

    def make_identifier(self):
        source = self.source
        variavel = ''
        while source[self.position] != None and (source[self.position].isalpha() or source[self.position].isdigit() or source[self.position] == "_"):
            variavel += source[self.position]
            if (self.position == len(source) - 1):
                self.position += 1
                break

            self.position += 1

        return variavel



class Node:
    def __init__(self,value,children):
        self.value = value
        self.children = children

    def Evaluate(self,symbol_table):
        pass

class BinOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
        self.value = value
        self.children = children

    def Evaluate(self,symbol_table):
        filho_esquerda = self.children[0].Evaluate(symbol_table)[0]
        filho_direita = self.children[1].Evaluate(symbol_table)[0]
        
        tipo_esquerda = self.children[0].Evaluate(symbol_table)[1]
        tipo_direita = self.children[1].Evaluate(symbol_table)[1]



        if self.value == "+":
            if tipo_esquerda != tipo_direita:
                raise Exception("Tipos diferentes")
            return ((filho_esquerda + filho_direita), "Int")
        elif self.value == "-":
            if tipo_esquerda != tipo_direita:
                raise Exception("Tipos diferentes")
            return ((filho_esquerda - filho_direita),"Int")
        elif self.value == "*":
            if tipo_esquerda != tipo_direita:
                raise Exception("Tipos diferentes")
            return ((filho_esquerda * filho_direita),"Int")
        elif self.value == "/":
            if tipo_esquerda != tipo_direita:
                raise Exception("Tipos diferentes")
            return ((filho_esquerda // filho_direita), "Int")
        elif self.value == "==":
            return ((int(filho_esquerda == filho_direita)), "Int")
        elif self.value == "&&":
            return ((int(filho_esquerda and filho_direita)), "Int")
        elif self.value == "||":
            return ((int(filho_esquerda or filho_direita)), "Int")
        elif self.value == ">":
            return ((int(filho_esquerda > filho_direita)), "Int")
        elif self.value == "<":
            return ((int(filho_esquerda < filho_direita)), "Int")
        elif self.value == ".":
            return ((str(self.children[0].Evaluate(symbol_table)[0]) + str(self.children[1].Evaluate(symbol_table)[0])), "Texto")

class UnOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self,symbol_table):
        if self.value == "+":
            return (self.children[0].Evaluate(symbol_table)[0], "Int")
        elif self.value == "-":
            return (-self.children[0].Evaluate(symbol_table)[0], "Int")
        elif self.value == "!":
            return (not(self.children[0].Evaluate(symbol_table)[0]), "Int")


class IntVal(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self,symbol_table):
        return (self.value,"Int")

class NoOp(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self,symbol_table):
        pass


class Block(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self,symbol_table):
        for filho in self.children:
            if filho.__class__.__name__ == "ReturnNode":
                return filho.Evaluate(symbol_table)
            filho.Evaluate(symbol_table)
 
class EqualNode(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    
    def Evaluate(self,symbol_table):
        tipo = self.children[0].value
        no = self.children[1].Evaluate(symbol_table)
        symbol_table.set(tipo,(no[0],no[1]))

class IdentifierNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        return symbol_table.get(self.value)

class PrintNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        print(self.children[0].Evaluate(symbol_table)[0])

class SymbolTable:

    def __init__(self):
        self.table = {}

    def create(self,identifier: IdentifierNode, tupla):

        tipo = tupla[1]
        valor = tupla[0]

        if identifier in self.table.keys():
            raise Exception("ja declarada")

        if tipo == "Int":
            self.table[identifier] = (valor, tipo)
        elif tipo == "Texto":
            self.table[identifier] = (valor, tipo)


    def get(self,identifier):
        if identifier in self.table:
            return self.table[identifier]
        else:
            raise Exception("variable not found")

    def set(self,identifier,value):
        if identifier in self.table:
            if self.table[identifier][1] == value[1]:
                self.table[identifier] = value
            else:
                raise Exception("erro de tipo")
        else:
            self.table[identifier] = value



class FuncTable:
    table = {}
    def create(Identifier, pointer, type):
        if Identifier in FuncTable.table.keys():
            raise ValueError(f"Function already declared")
        FuncTable.table[Identifier] = (pointer, type)
    def get(identifier):
        if identifier in FuncTable.table:
            return FuncTable.table[identifier]
        else:
            raise Exception("variable not found")




class FuncDec(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def Evaluate(self, symbol_table):
        FuncTable.create(self.children[0].value, self, self.value)





class FuncCall(Node):
    def __init__(self, value, children):
        super().__init__(value, children)
    def Evaluate(self, symbol_table):
        argumentos = []
        new_func, type_func = FuncTable.get(self.value)
        new_ST = SymbolTable()
        for vardec in new_func.children[1]:
            argumentos.append(vardec.children[0].value)
            vardec.Evaluate(new_ST)

        if len(argumentos) != len(self.children):
            raise ValueError("Invalid number of argumentos")
        for i in range(len(argumentos)):
            new_ST.set(argumentos[i], self.children[i].Evaluate(symbol_table))
        ret = new_func.children[-1].Evaluate(new_ST)
        if type_func != ret[1]:
            raise ValueError(
                f"Cannot return {ret[1]} from function expecting {type_func}"
            )
        return ret

class ReturnNode(Node):
    def __init__(self, value, children):
        super().__init__(value, children)

    def Evaluate(self, symbol_table):
        return self.children[0].Evaluate(symbol_table)



class WhileNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        while(self.children[0].Evaluate(symbol_table)[0]):
            self.children[1].Evaluate(symbol_table)

class IfNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        if (self.children[0].Evaluate(symbol_table) == True):
            self.children[1].Evaluate(symbol_table)
        elif (len(self.children)) > 2:
            self.children[2].Evaluate(symbol_table)

class ReadNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        return (int(input()),"Int")


class VarDecNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        ident = self.children[0].value
        numero = self.children[1].value
        tipo_var = self.children[1].Evaluate(symbol_table)[1]
        symbol_table.create(ident, (numero, tipo_var))

class StringNode(Node):
    def __init__(self, value,children):
        super().__init__(value,children)
    
    def Evaluate(self,symbol_table):
        return (self.value,TT_STR)

class Parser():
    tokenizer = None
    @ staticmethod
    def parseRelExpression():
        resultado_exp = Parser.parseExpression()
        while (Parser.tokenizer.next.type == "EE" or Parser.tokenizer.next.type == "GT" or Parser.tokenizer.next.type == "LT" or Parser.tokenizer.next.type == "ponto"):
            tipo = Parser.tokenizer.next.type
            if tipo == "EE":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp("==",[resultado_exp,Parser.parseExpression()])
            elif tipo == "GT":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp(">",[resultado_exp,Parser.parseExpression()])
            elif tipo == "LT":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp("<",[resultado_exp,Parser.parseExpression()])
            elif tipo == "ponto":
                Parser.tokenizer.selectNext()
                resultado_exp = BinOp(".",[resultado_exp,Parser.parseExpression()])
        return resultado_exp

    @ staticmethod
    def parseExpression():
        resultado_Term = Parser.parseTerm()
        while (Parser.tokenizer.next.type == "MINUS" or Parser.tokenizer.next.type == "PLUS" or Parser.tokenizer.next.type == "ou"):
            tipo = Parser.tokenizer.next.type
            if tipo == "MINUS":
                Parser.tokenizer.selectNext()
                resultado_Term = BinOp("-",[resultado_Term,Parser.parseTerm()])
            elif tipo == "PLUS":
                Parser.tokenizer.selectNext()
                resultado_Term = BinOp("+",[resultado_Term,Parser.parseTerm()])
            elif tipo == "ou":
                Parser.tokenizer.selectNext()
                resultado_Term = BinOp("||",[resultado_Term,Parser.parseTerm()])
        return resultado_Term

    @ staticmethod
    def parseTerm():
        resultado_factor = Parser.parseFactor()
        while (Parser.tokenizer.next.type == "DIV" or Parser.tokenizer.next.type == "MULT" or Parser.tokenizer.next.type == "e"):
            tipo = Parser.tokenizer.next.type
            if tipo == "MULT":
                Parser.tokenizer.selectNext()
                resultado_factor = BinOp("*",[resultado_factor,Parser.parseFactor()])
            elif tipo == "DIV":
                Parser.tokenizer.selectNext()
                resultado_factor = BinOp("/",[resultado_factor,Parser.parseFactor()])
            elif tipo == "e":
                Parser.tokenizer.selectNext()
                resultado_factor = BinOp("&&",[resultado_factor,Parser.parseFactor()])
        return resultado_factor


    @ staticmethod
    def parseFactor():
        if Parser.tokenizer.next.type == "INT":
            reul_op = Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()
            return IntVal(reul_op,[])
        if Parser.tokenizer.next.type == "Texto":
            node_str = StringNode(Parser.tokenizer.next.value, TT_STR)
            Parser.tokenizer.selectNext()
            return node_str
            
        elif Parser.tokenizer.next.type == "IDENTIFIER":
            id_token = Parser.tokenizer.next.value
            identifier = IdentifierNode(Parser.tokenizer.next.value, [])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                call_node = FuncCall(id_token,[])
                Parser.tokenizer.selectNext()
                while Parser.tokenizer.next.type != "CP":
                    call_node.children.append(Parser.parseRelExpression())
                    if Parser.tokenizer.next.type == "virgula":
                        Parser.tokenizer.selectNext()
                Parser.tokenizer.selectNext()
                return call_node
            return identifier

        if Parser.tokenizer.next.type == "PLUS":
            Parser.tokenizer.selectNext()
            return UnOp("+",[Parser.parseFactor()])
        if Parser.tokenizer.next.type == "MINUS":
            Parser.tokenizer.selectNext()
            return UnOp("-",[Parser.parseFactor()])
        if Parser.tokenizer.next.type == "nem":
            Parser.tokenizer.selectNext()
            return UnOp("!",[Parser.parseFactor()])
        if Parser.tokenizer.next.type == "OP":
            Parser.tokenizer.selectNext()
            reul_op = Parser.parseRelExpression()
            if Parser.tokenizer.next.type == "CP":
                Parser.tokenizer.selectNext()
                return reul_op
            else:
                raise Exception("Não fechou parenteses")

        if Parser.tokenizer.next.type == "Leia":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type == "CP":
                    Parser.tokenizer.selectNext()    
                    return ReadNode([],[])  
        else:
            raise Exception("Invalido")

    @ staticmethod
    def parseBlock():
        node = Block("",[])
        while (Parser.tokenizer.next.type != "EOF"):
            child = Parser.parseStatement()
            node.children.append(child)
        Parser.tokenizer.selectNext()
        return node

    @ staticmethod
    def parseStatement():
        if Parser.tokenizer.next.type == "QL":
            Parser.tokenizer.selectNext()
            return NoOp("","")
        
        if Parser.tokenizer.next.type == "IDENTIFIER":
            node_identifier = IdentifierNode(Parser.tokenizer.next.value,[])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "EQUAL":
                Parser.tokenizer.selectNext()
                node_equal = EqualNode("",[node_identifier,Parser.parseRelExpression()])
                if Parser.tokenizer.next.type == "QL":
                    Parser.tokenizer.selectNext() 
                    return node_equal
                else:
                    raise Exception("Não terminou com quebra de linha")
            if Parser.tokenizer.next.type == "DOISPONTOS":
                Parser.tokenizer.selectNext()
                if Parser.tokenizer.next.type in ["Int", "Texto"]:
                    tipo = Parser.tokenizer.next.type
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "QL":
                        Parser.tokenizer.selectNext()
                        if tipo == "Int":
                            return VarDecNode(tipo,[node_identifier,IntVal(0,[])])
                        elif tipo == "Texto":
                            return VarDecNode(tipo,[node_identifier,StringNode("",TT_STR)])
                    elif Parser.tokenizer.next.type == "EQUAL":
                        Parser.tokenizer.selectNext()
                        resul_exp = Parser.parseRelExpression()
                        if Parser.tokenizer.next.type == "QL":
                            Parser.tokenizer.selectNext() 
                            node_dec = VarDecNode(tipo,[node_identifier,resul_exp])
                            return node_dec
                        else:
                            raise Exception("Não terminou com quebra de linha")
                

            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                call_node = FuncCall(node_identifier.value,[])
                while True:
                    call_node.children.append(Parser.parseRelExpression())
                    if Parser.tokenizer.next.type != "virgula":
                        raise Exception("Não terminou com virgula")
                    if Parser.tokenizer.next.type == "CP":
                        Parser.tokenizer.selectNext()
                        break
                    Parser.tokenizer.selectNext()
                return call_node
                    

        elif Parser.tokenizer.next.type  == "Trabalho":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "IDENTIFIER":
                raise Exception ("Error in function declaration")
            func_ident = IdentifierNode(Parser.tokenizer.next.value, [])
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type != "OP":
                raise Exception ("Error in function declaration")
            Parser.tokenizer.selectNext()
            func_argumentos = []
            if Parser.tokenizer.next.type != "CP":
                while True:
                    arg_ident = IdentifierNode(Parser.tokenizer.next.value, [])
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type != "DOISPONTOS":
                        raise Exception("Problema com dois pontos")
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type not in ["Int", "Texto"]:
                        raise Exception("Problem with argument type")
                    if Parser.tokenizer.next.type == "Int":
                        func_argumentos.append(VarDecNode(Parser.tokenizer.next.value, [arg_ident, IntVal(0,[])]))
                    elif Parser.tokenizer.next.type == "Texto":
                        func_argumentos.append(VarDecNode(Parser.tokenizer.next.value, [arg_ident, StringNode("",TT_STR)]))
                    Parser.tokenizer.selectNext()
                    if Parser.tokenizer.next.type == "CP":
                        break
                    if Parser.tokenizer.next.type != "virgula":
                        raise Exception("Problema com virgula")
                    Parser.tokenizer.selectNext()
            Parser.tokenizer.selectNext()  
            if Parser.tokenizer.next.type != "DOISPONTOS":
                raise Exception("Problema com dois pontos")
            Parser.tokenizer.selectNext()  
            if Parser.tokenizer.next.type not in ["Int", "Texto"]:
                raise Exception("Problem with return type")
            func_ret_type =  Parser.tokenizer.next.value
            Parser.tokenizer.selectNext()  
            if Parser.tokenizer.next.type != "QL":
                raise Exception("Prolem with quebra de linha")
            func_block = Block("",[])
            Parser.tokenizer.selectNext()
            while True:
                if Parser.tokenizer.next.type == "FIM":
                    break
                if Parser.tokenizer.next.type == "EOF":
                    raise Exception("Não fechou função")
                statement_val = Parser.parseStatement()
                func_block.children.append(statement_val)
            Parser.tokenizer.selectNext() 
            return_node = FuncDec(func_ret_type, [func_ident, func_argumentos, func_block])
            return return_node


        elif Parser.tokenizer.next.type == "Devolva":
            Parser.tokenizer.selectNext()
            return ReturnNode("Devolva", [Parser.parseRelExpression()])
            
        elif Parser.tokenizer.next.type == "Amostre":
            Parser.tokenizer.selectNext()
            if Parser.tokenizer.next.type == "OP":
                Parser.tokenizer.selectNext()
                node_print = PrintNode("Amostre",[Parser.parseRelExpression()])
                if Parser.tokenizer.next.type == "CP":
                    Parser.tokenizer.selectNext()

                    if Parser.tokenizer.next.type == "QL":
                        Parser.tokenizer.selectNext()
                        return node_print
                    else:
                        raise Exception("Não terminou com Ponto e Virgula")
                else:
                    raise Exception("Não fechou parenteses")
            else:
                raise Exception("Não abriu parenteses")
            
        elif Parser.tokenizer.next.type == "ArrochaEnquanto":
            Parser.tokenizer.selectNext()
            resul_rel = Parser.parseRelExpression()
            while_block = Block(None,[])
            if Parser.tokenizer.next.type == "QL":
                Parser.tokenizer.selectNext()
            while True:
                if Parser.tokenizer.next.type == "FIM":
                    Parser.tokenizer.selectNext()
                    break
                statement_val = Parser.parseStatement()
                while_block.children.append(statement_val)
                if Parser.tokenizer.next.type == "EOF":
                    raise Exception("Não fechou while")
            return WhileNode("ArrochaEnquanto",[resul_rel,while_block])


        elif Parser.tokenizer.next.type == "SoSe":
            Parser.tokenizer.selectNext()
            resul_rel = Parser.parseRelExpression()
            ifblock = Block(None,[])
            if Parser.tokenizer.next.type == "QL":
                Parser.tokenizer.selectNext()
            else:
                raise Exception("Não terminou com quebra de linha")
            while True:
                if Parser.tokenizer.next.type == "FIM":
                    Parser.tokenizer.selectNext()
                    break
                if Parser.tokenizer.next.type == "SeNumFor":
                    break
                statement_val = Parser.parseStatement()
                ifblock.children.append(statement_val)
            
            if Parser.tokenizer.next.type == "SeNumFor":
                Parser.tokenizer.selectNext()
                elseblock = Block(None,[])
                if Parser.tokenizer.next.type == "QL":
                    Parser.tokenizer.selectNext()
                while True:
                    if Parser.tokenizer.next.type == "FIM":
                        Parser.tokenizer.selectNext()
                        break
                    statement_val = Parser.parseStatement()
                    elseblock.children.append(statement_val)
                return IfNode("SoSe",[resul_rel,ifblock,elseblock])

            return IfNode("ArrochaEnquanto",[resul_rel,ifblock])

        else:
            return Parser.parseBlock()


    @ staticmethod
    def run(code):
        Parser.tokenizer = Tokenizer(code)
        Parser.tokenizer.selectNext()
        symboltable = SymbolTable()
        resultado_final = Parser.parseBlock()
        if Parser.tokenizer.next.type != "EOF":
            raise Exception("não consumiu até o fim")
        resultado_final.Evaluate(symboltable)


class PrePro:
    @staticmethod
    def filter(source):
        comentario = False
        texto_novo = ""
        for i in range(len(source)):
            if source[i] == "#":
                comentario = True
            if source[i] == "\n":
                comentario = False
            if comentario == False:
                texto_novo += source[i]
        texto_novo = texto_novo + "\n"

        linhas = texto_novo.splitlines()
        linhas_sem_branco = [linha for linha in linhas if linha.strip()]

        texto_sem_branco = '\n'.join(linhas_sem_branco) + '\n'
        
        return texto_sem_branco




def main(argv):
    file_name = argv[1]
    # file_name = "input.jl"
    with open(file_name, "r") as file:
        source = file.read()
        prepro = PrePro()
        param = prepro.filter(source)
        Parser.run(param)
        # parser = Parser()
        # resultado_main = parser.run(param)
        # resultado_main.Evaluate(symbol_table)

if __name__ == '__main__':
    main(sys.argv)