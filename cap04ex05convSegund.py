def converter_segundos(segundos):

    horas = segundos // 60**2
    minutos = (segundos % 60**2) // 60
    seg = (segundos % 60**2) % 60

    print(f'São {horas} horas, {minutos} minutos e {seg} segundos.')

converter_segundos(8563)
converter_segundos(3268)
converter_segundos(10589)
converter_segundos(7598)
converter_segundos(4589)


