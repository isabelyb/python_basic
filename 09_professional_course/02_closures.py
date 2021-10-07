def make_repeater_of(n):  ##  scope global
    def repeater(string):  ## Función anidada
        assert type(string) == str, 'Solo puedes repetir cadenas'   ## Confirmar que solo se reciben strings
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)  ## asignación de n
    print(repeat_5('Hola '))

    repeat_10 = make_repeater_of(10)
    print(repeat_10('Isa '))


if __name__ == '__main__':
    run()