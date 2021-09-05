import mysql.connector
from mysql.connector import Error
from time import sleep


con = mysql.connector.connect(
    host='', 
    database='', 
    user='',
    password=''
)


cursor = con.cursor()


def desconectarBD(cursor):
    if con.is_connected():
        cursor.close()
        con.close()
        print('\nConexão ao MySQL encerrada.')


def inserirTenistas():
    print('Inserindo 5 novos tenistas ao banco de dados...')
    sleep(0.5)
    comandoSQL = """
                    INSERT INTO `tenis`.`tenista`
                    (id,nome,apelido,ano_nasc,cidade_nascimento,cidade_moradia,esta_ativo,id_padrinho)
                    VALUES
                    (8,'Abílio','Ab',1995,'Maceió','Santos',1,3),
                    (9,'Joel','Jô',1987,'Maceió','Florianópolis',1,1),
                    (10,'Francisco','Chico',1998,'Fortaleza','Madrid',1,4),
                    (11,'Emili','Mili',2001,'Vitória','Barcelona',1,2),
                    (12,'Jorge','Apelido',1999,'Barcelona','Sevilha',1,5);
                    """
    cursor.execute(comandoSQL)
    con.commit()
    print(cursor.rowcount, 'Registros inseridos na tabela!')
    sleep(0.5)


def removerDadosTorneio():
    print('\nRemovendo dados do torneio Arapiraca Open e a participação dos tenistas...')
    sleep(0.5)
    comandoSQL = """
                    DELETE FROM tenis.torneio WHERE id = 5;
                    """
    cursor.execute(comandoSQL)
    con.commit()
    print(cursor.rowcount, 'Registro removido da tabela!')
    sleep(0.5)


def jogadoresAtivos():
    print('\nLista dos jogadores ativos:\nnome apelido ano_nasc')
    sleep(0.5)
    comandoSQL = """
                    SELECT nome, apelido, ano_nasc FROM tenis.tenista WHERE esta_ativo = 1;
                    """
    cursor.execute(comandoSQL)
    linhas = cursor.fetchall()
    for linha in linhas:
        print(linha)
    sleep(0.5)


def rolandGarros():
    print('\nLista dos jogadores que disputaram Roland Garros:\nnome idade')
    sleep(0.5)
    comandoSQL = """
                    SELECT DISTINCT nome, 2021 - ano_nasc AS idade FROM tenis.tenista, tenis.participar WHERE id = id_tenista AND id_torneio = 4;
                    """
    cursor.execute(comandoSQL)
    linhas = cursor.fetchall()
    for linha in linhas:
        print(linha)
    sleep(0.5)


def torneiosJogador():
    print('\nQuantidade de torneios disputados por cada jogador:\nnome torneios_disputados')
    sleep(0.5)
    comandoSQL = """
                    SELECT nome, count(nome) AS 'torneios disputados' FROM tenis.tenista, tenis.participar WHERE id = id_tenista GROUP BY nome;
                    """
    cursor.execute(comandoSQL)
    linhas = cursor.fetchall()
    for linha in linhas:
        print(linha)
    sleep(0.5)


def consultas():
    while True:
        consulta = int(input('\n1 - Consultar tenistas.'
                            '\n2 - Consultar torneios.'
                            '\n3 - Consultar participação.'
                            '\n4 - Voltar.\n'))

        if consulta == 1:
            comandoSQL = """
                            SELECT * FROM tenis.tenista;
                            """
            cursor.execute(comandoSQL)
            linhas = cursor.fetchall()
            print('id nome apelido ano_nasc cidade_nascimento cidade_moradia esta_ativo id_padrinho')
            for linha in linhas:
                print(linha)

        elif consulta == 2:
            comandoSQL = """
                            SELECT * FROM tenis.torneio;
                            """
            cursor.execute(comandoSQL)
            linhas = cursor.fetchall()
            print('id nome local')
            for linha in linhas:
                print(linha)

        elif consulta == 3:
            comandoSQL = """
                            SELECT * FROM tenis.participar ORDER BY id_torneio;
                            """
            cursor.execute(comandoSQL)
            linhas = cursor.fetchall()
            print('id_tenista id_torneio ano premio foi_finalista foi_campeao')
            for linha in linhas:
                print(linha)

        elif consulta == 4:
            break


if con.is_connected():
    while True:
        option = int(input('\n1 - Consultas.'
                            '\n2 - Inserir 5 novos tenistas.'
                            '\n3 - Remover dados do torneio Arapiraca Open.'
                            '\n4 - Relatórios dos jogadores ativos.'
                            '\n5 - Jogadores que disputaram Roland Garros.'
                            '\n6 - Torneios disputados por cada jogador.'
                            '\n7 - Desconectar.\n'))
        
        if option == 1:
            consultas()

        elif option == 2:
            inserirTenistas()

        elif option == 3:
            removerDadosTorneio()

        elif option == 4:
            jogadoresAtivos()

        elif option == 5:
            rolandGarros()

        elif option == 6:
            torneiosJogador()

        elif option == 7:
            desconectarBD(cursor)
            break
