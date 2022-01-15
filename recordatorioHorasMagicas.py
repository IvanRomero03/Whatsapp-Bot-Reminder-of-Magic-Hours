import time
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6c181e01332055220e0940113d80e89b"
# Your Auth Token from twilio.com/console
auth_token = "5d7359a7af252f0f35c82ea94c967f6e"

client = Client(account_sid, auth_token)

horasminutos = {
    1: 11,
    2: 22,
    3: 33,
    4: 44,
    5: 55,
    11: 11
}


def printBarritaCargando(segundos):
    segundosCargados = 1
    segundosPorCargar = segundos - 1
    # hacer una barra de carga que se actualize cada segundo
    for i in range(segundos):
        print("\r" + "Esperando: " +
              "[" + "#"*segundosCargados + "·"*segundosPorCargar + "]", end="")
        segundosCargados += 1
        segundosPorCargar -= 1
        time.sleep(1)
    print("\r")


while(True):
    localtime = time.localtime()
    horasNotables = horasminutos.keys()
    print(localtime)
    if(localtime.tm_hour % 12 in horasNotables):
        if(localtime.tm_min == horasminutos[localtime.tm_hour % 12]):
            mensaje = localtime.tm_hour % 12 + ":" + localtime.tm_min
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                to='whatsapp:+5216461617687',
                body=mensaje
            )
            print(message.sid)
            time.sleep(3600)
        else:
            print("No es hora de recordatorio")
            printBarritaCargando(30)
    else:
        print("no hora notables")
        printBarritaCargando(60)
