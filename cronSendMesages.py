from crontab import CronTab


def setReminder(hour, minute):
    cron = CronTab(user='root')
    job = cron.new(
        command='python -u "c:\Users\iwell\OneDrive\Desktop\proy\Whatsapp-Bot-Reminder-of-Magic-Hours\recordatorioHorasMagicas.py"')
    job.hour.on(hour)
    job.minute.on(minute)
    cron.write()


horasMagicas = {
    1: 11,
    2: 22,
    3: 33,
    4: 44,
    5: 55,
    11: 11,
    13: 11,
    14: 22,
    15: 33,
    16: 44,
    17: 55,
    23: 11
}

horasMagicasLista = horasMagicas.keys()

for hora in horasMagicasLista:
    setReminder(hora, horasMagicas[hora])
