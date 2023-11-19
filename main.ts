let actualtemp = 0
let maxtemp = 0
basic.forever(function on_forever() {
    
    actualtemp = input.temperature()
    if (actualtemp > maxtemp) {
        maxtemp = actualtemp
    }
    
    led.plotBarGraph(actualtemp, maxtemp)
})
