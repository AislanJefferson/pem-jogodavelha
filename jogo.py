def criaConexaoServ(ip,porta):

    hostConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    hostConn.bind((ip,porta))

    hostConn.listen(1)

    return hostConn



def enviarDadosStr(conexao, dado):

    return conexao.send(str(dado).encode('utf-8'))



def receberDadosStr(conexao,tamanho):

    return conexao.recv(tamanho).decode('utf-8')
