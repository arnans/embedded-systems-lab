"""Generate the Lab 1 schematics (placeholders until redrawn in EasyEDA).

Shared pins (decided 18 Nov 2026): kit ESP32 and Wokwi use LED = GPIO23, button = GPIO4.
The GoGo CM (ESP32-S3) has its LED on IO6 and the big button (U6) on IO4, with R22 5.1k + C11 100nF.

    python tools/lab1_schematics.py      # writes images/lab1-*.png
"""
import os
import matplotlib
matplotlib.use("Agg")
import schemdraw
import schemdraw.elements as elm

OUT = os.path.join(os.path.dirname(__file__), "..", "images")
schemdraw.config(fontsize=13, lw=1.6, font="Tahoma")  # Tahoma has Thai glyphs


def esp32(d, pins, label="ESP32 DevKit", at=None, right=()):
    """A box with the named GPIO pins (left side unless listed in `right`); returns the element."""
    ic = elm.Ic(pins=[elm.IcPin(name=p, side="right" if p in right else "left") for p in pins],
                edgepadW=1.6, pinspacing=1.6,
                label=label, lblofst=0.3, lblloc="top")
    return d.add(ic.at(at) if at is not None else ic)


def save(d, name):
    path = os.path.join(OUT, name)
    d.save(path, dpi=130)
    print("wrote", os.path.normpath(path))


def button_circuit(d, start, r_pull, label_pull, series=None, cap=None, analyzer=False, extra=""):
    """Pull-up button circuit ending at `start` (the GPIO pin), drawn to the left."""
    d.move_from(start)
    line = d.add(elm.Line().left(1.2))
    node = line.end
    d.add(elm.Dot())
    # pull-up to 3V3
    d.push()
    d.add(elm.Resistor().up().label(label_pull, loc="bottom"))
    d.add(elm.Vdd().label("3V3"))
    d.pop()
    if cap:
        d.push()
        d.add(elm.Line().left(1.8))
        d.add(elm.Dot())
        d.push()
        d.add(elm.Capacitor().down().label(cap, loc="bottom"))
        d.add(elm.Ground())
        d.pop()
        if series:
            d.add(elm.Resistor().left().label(series))
        d.add(elm.Button().left().label("SW"))
        d.add(elm.Line().down(1.0))
        d.add(elm.Ground())
        d.pop()
    else:
        d.push()
        d.add(elm.Line().left(1.8))
        if series:
            d.add(elm.Resistor().left().label(series))
        d.add(elm.Button().left().label("SW"))
        d.add(elm.Line().down(1.0))
        d.add(elm.Ground())
        d.pop()
    if analyzer:
        d.push()
        d.add(elm.Line().down(2.4))
        d.add(elm.Dot(open=True).label("Logic Analyzer CH0\n(GND ต่อร่วมกับวงจร)", loc="bottom"))
        d.pop()
    return node


# --- Breadboard sheet ---------------------------------------------------------------
with schemdraw.Drawing(show=False) as d:   # 04: button on GPIO4 (10k pull-up) + LED on GPIO23
    ic = esp32(d, ["GPIO4", "GPIO23"], right=("GPIO23",))
    button_circuit(d, ic.GPIO4, "R2\n10kΩ", "R2 10kΩ")
    d.move_from(ic.GPIO23)
    d.add(elm.Line().right(1.2))
    d.add(elm.Resistor().down().label("R1 1kΩ", loc="bottom"))
    d.add(elm.LED().down().label("LED", loc="bottom"))
    d.add(elm.Ground())
    save(d, "lab1-breadboard-04.png")

with schemdraw.Drawing(show=False) as d:   # 07: logic analyzer on the button pin
    ic = esp32(d, ["GPIO4"])
    button_circuit(d, ic.GPIO4, "R2\n10kΩ", "R2 10kΩ", analyzer=True)
    save(d, "lab1-breadboard-07.png")

with schemdraw.Drawing(show=False) as d:   # 08: RC debounce (33k series + 100nF) on the button pin
    ic = esp32(d, ["GPIO4"])
    button_circuit(d, ic.GPIO4, "R2\n10kΩ", "R2 10kΩ", series="R3 33kΩ", cap="C1\n100nF", analyzer=True)
    save(d, "lab1-breadboard-08.png")

# --- CM sheet (on-board parts, from the EasyEDA netlist) ---------------------------
with schemdraw.Drawing(show=False) as d:   # CM LED: IO6 -> R23 1k -> LED2 (red) -> GND
    ic = esp32(d, ["IO6"], label="ESP32-S3 (บอร์ด CM)")
    d.move_from(ic.IO6)
    d.add(elm.Line().left(1.2))
    d.add(elm.Resistor().down().label("R23 1kΩ", loc="bottom"))
    d.add(elm.LED().down().label("LED2 (แดง)", loc="bottom"))
    d.add(elm.Ground())
    save(d, "lab1-cm-led.png")

with schemdraw.Drawing(show=False) as d:   # CM button: R22 5.1k pull-up, C11 100nF to GND, U6 to GND, IO4
    ic = esp32(d, ["IO4"], label="ESP32-S3 (บอร์ด CM)")
    d.move_from(ic.IO4)
    d.add(elm.Line().left(1.2))
    d.add(elm.Dot())
    d.push()
    d.add(elm.Resistor().up().label("R22 5.1kΩ", loc="bottom"))
    d.add(elm.Vdd().label("3V3"))
    d.pop()
    d.add(elm.Line().left(1.8))
    d.add(elm.Dot())
    d.push()
    d.add(elm.Capacitor().down().label("C11\n100nF", loc="bottom"))
    d.add(elm.Ground())
    d.pop()
    d.add(elm.Line().left(3.2))
    d.add(elm.Button().down().label("U6\n(Run / Stop)", loc="top", ofst=0.4))
    d.add(elm.Ground())
    save(d, "lab1-cm-button.png")
