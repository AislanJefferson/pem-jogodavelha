def criaConexaoServ(ip,porta):

    hostConn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    hostConn.bind((ip,porta))

    hostConn.listen(1)

    return hostConn



def enviarDadosStr(conexao, dado):

    return conexao.send(str(dado).encode('utf-8'))



def receberDadosStr(conexao,tamanho):

    return conexao.recv(tamanho).decode('utf-8')


def retornaIP():

    """Função que retorna o endereço IP da maquina onde está executando. O import do pacote

    micropython.fcntl foi ignorado no código e pode dar erro. Tem que ser instalado e pelo

    que vi só é possivel via comandos linux."""

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    return socket.inet_ntoa(fcntl.ioctl(

        s.fileno(),

        0x8915,  # SIOCGIFADDR

        struct.pack('256s', 'eth0'[:15])

        )[20:24])


