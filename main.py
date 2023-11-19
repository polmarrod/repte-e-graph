actualtemp = 0
maxtemp = 0
def on_forever():
    global actualtemp, maxtemp
    actualtemp = input.temperature()
    if actualtemp > maxtemp:
        maxtemp = actualtemp
    led.plot_bar_graph(actualtemp, maxtemp)
basic.forever(on_forever)