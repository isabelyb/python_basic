from bokeh.plotting import figure, output_file, show


if __name__ == '__main__':
    output_file('correcaminos.html')
    fig = figure()

    """Aqui puedes graficar el seguimiento de la presencia del 
       Gran Correcaminos (Geococcys californianus)
       en la reserva Dictionary Hills"""


    total_vals = int(input('De cuantos dias quieres hacer seguimiento? '))
    x_vals = list(range(total_vals))
    y_vals = []

    for x in x_vals:
        val = int(input(f'individuos avistados en el dia {x}:  '))
        y_vals.append(val)

    fig.line(x_vals, y_vals, line_width=2)
    show(fig)
