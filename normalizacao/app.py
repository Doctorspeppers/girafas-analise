import MySQLdb
import re

def removeAcento(letraComAcento):
    acentos = {
            "Á":"A",
            "À":"A",
            "Â":"A",
            "Ã":"A",
            "Ó":"O",
            "Ò":"O",
            "Ô":"O",
            "Õ":"O",
            "Í":"I",
            "Ì":"I",
            "Î":"I",
            "É":"E",
            "È":"E",
            "Ê":"E",
            "Ú":"U",
            "Ù":"U",
            "Û":"U"
            }

    for acento,letra in acentos.items():
        if str.isupper(letraComAcento) == False:
            if acento == str.upper(letraComAcento):
                return str.lower(letra)
        if acento == str.upper(letraComAcento):
            return letra
    return letraComAcento

regioes = {
    "AC":"NORTE",
    "AL":"NORTE",
    "AP":"NORTE",
    "AM":"NORTE",
    "BA":"NORDESTE",
    "CE":"NORDESTE",
    "DF":"CENTRO",
    "ES":"SUDESTE",
    "GO":"CENTRO",
    "MA":"NORDESTE",
    "MT":"CENTRO",
    "MS":"CENTRO",
    "MG":"SUDESTEs",
    "PA":"NORTE",
    "PB":"NORDESTE ",
    "PR":"SUL",
    "PE":"NORDESTE",
    "PI":"NORDESTE",
    "RJ":"SUDESTE",
    "RN":"NORDESTE",
    "RS":"SUL",
    "RO":"NORTE",
    "RR":"NORTE",
    "SC":"SUL",
    "SP":"SUDESTE",
    "SE":"NORDESTE",
    "TO":"NORTE"
}


estados = {
    "acre":"AC",
    "alagoas":"AL",
    "amapá":"AP",
    "amazonas":"AM",
    "bahia":"BA",
    "ceara":"CE",
    "distrito federal":"DF",
    "espírito santo":"ES",
    "goias":"GO",
    "maranhão":"MA",
    "mato grosso":"MT",
    "mato grosso do sul":"MS",
    "minas gerais":"MG",
    "para":"PA",
    "paraiba ":"PB",
    "parana":"PR",
    "pernambuco":"PE",
    "piaui":"PI",
    "rio de Janeiro":"RJ",
    "rio grande do norte":"RN",
    "rio grande do sul":"RS",
    "rondonia":"RO",
    "roraima":"RR",
    "santa catarina":"SC",
    "sao paulo":"SP",
    "sergipe":"SE",
    "tocantins":"TO"
}


cnx = MySQLdb.connect(
    host="localhost",
    user="root",
    password="",
    database="girafas"
)

cursor = cnx.cursor()

cursor.execute("SELECT id,cidade FROM franquias")

infos = cursor.fetchall()

infoNorm = {}

for info in infos:

        infoNorm[info[0]] = str.upper(info[1])

for id,cidade in infoNorm.items():
    cursor.execute("UPDATE franquias SET  cidade='"+cidade+"' WHERE id="+str(id))




cursor.execute("SELECT id,estado FROM franquias")

infos = cursor.fetchall()

for info in infos:
    estado = ""
    if len(info[1]) != 2:
        for x in info[1]:
            estado += removeAcento(str.lower(x))
        estado = estados[estado]
    else:
        estado = info[1]
    regiao = regioes[estado]
    
    cursor.execute("UPDATE franquias SET regiao='"+regiao+"', estado='"+estado+"' WHERE id="+str(info[0]))





cursor.execute("SELECT id,regiao,cep FROM franquias")

infos = cursor.fetchall()

cnx.commit()
prog = re.compile("\d{5}-(\d){3}")
for info in infos:
    if prog.match(info[1]) != None:
        print(prog.match(info[1]))
        cursor.execute("UPDATE franquias SET regiao='"+info[2]+"', cep='"+info[1]+"' WHERE id="+str(info[0]))



cnx.commit()