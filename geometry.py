#geometry.py
from speak import speak     #imports the speak() function from speak.py
from listen import listen   #imports the listen() function from listen.py
import math

def geometry():
    speak("Which shape do you want to calculate?") #asks for shape
    shape = listen()

    if shape in ["square", "rectangle", "circle", "triangle", "parallelogram", "trapezium", "rhombus", "kite"]:
        speak("Do you want to calculate area or perimeter?")
        measure = listen()

        if shape == "square":
            speak("Enter the side length")
            side = float(listen())
            if measure == "area":
                speak(f"Area is {side * side}")
            elif measure == "perimeter":
                speak(f"Perimeter is {4 * side}")

        elif shape == "rectangle":
            speak("Enter length")
            l = float(listen())
            speak("Enter width")
            w = float(listen())
            if measure == "area":
                speak(f"Area is {l * w}")
            elif measure == "perimeter":
                speak(f"Perimeter is {2 * (l + w)}")

        elif shape == "circle":
            speak("Enter radius")
            r = float(listen())
            if measure == "area":
                speak(f"Area is {math.pi * r * r:.2f}")
            elif measure == "perimeter":
                speak(f"Circumference is {2 * math.pi * r:.2f}")

        elif shape == "triangle":
            if measure == "area":
                speak("Enter base")
                b = float(listen())
                speak("Enter height")
                h = float(listen())
                speak(f"Area is {0.5 * b * h}")
            elif measure == "perimeter":
                speak("Enter side A")
                a = float(listen())
                speak("Enter side B")
                b = float(listen())
                speak("Enter side C")
                c = float(listen())
                speak(f"Perimeter is {a + b + c}")

        elif shape == "parallelogram":
            speak("Enter base")
            b = float(listen())
            speak("Enter height")
            h = float(listen())
            if measure == "area":
                speak(f"Area is {b * h}")

        elif shape == "trapezium":
            speak("Enter base A")
            a = float(listen())
            speak("Enter base B")
            b = float(listen())
            speak("Enter height")
            h = float(listen())
            if measure == "area":
                speak(f"Area is {(0.5 * (a + b) * h)}")

        elif shape == "rhombus" or shape == "kite":
            speak("Enter diagonal 1")
            d1 = float(listen())
            speak("Enter diagonal 2")
            d2 = float(listen())
            if measure == "area":
                speak(f"Area is {(0.5 * d1 * d2)}")

    elif shape in ["cube", "cuboid", "sphere", "cylinder", "cone", "pyramid"]:
        speak("Do you want to calculate surface area or volume?")
        measure = listen()

        if shape == "cube":
            speak("Enter side length")
            a = float(listen())
            if measure == "surface area":
                speak(f"Surface area is {6 * a * a}")
            elif measure == "volume":
                speak(f"Volume is {a ** 3}")

        elif shape == "cuboid":
            speak("Enter length")
            l = float(listen())
            speak("Enter width")
            w = float(listen())
            speak("Enter height")
            h = float(listen())
            if measure == "surface area":
                sa = 2 * (l*w + l*h + w*h)
                speak(f"Surface area is {sa}")
            elif measure == "volume":
                speak(f"Volume is {l * w * h}")

        elif shape == "sphere":
            speak("Enter radius")
            r = float(listen())
            if measure == "surface area":
                speak(f"Surface area is {4 * math.pi * r * r:.2f}")
            elif measure == "volume":
                speak(f"Volume is {(4/3) * math.pi * r**3:.2f}")

        elif shape == "cylinder":
            speak("Enter radius")
            r = float(listen())
            speak("Enter height")
            h = float(listen())
            if measure == "surface area":
                sa = 2 * math.pi * r * (r + h)
                speak(f"Surface area is {sa:.2f}")
            elif measure == "volume":
                speak(f"Volume is {math.pi * r**2 * h:.2f}")

        elif shape == "cone":
            speak("Enter radius")
            r = float(listen())
            speak("Enter slant height")
            l = float(listen())
            speak("Enter height")
            h = float(listen())
            if measure == "surface area":
                sa = math.pi * r * (r + l)
                speak(f"Surface area is {sa:.2f}")
            elif measure == "volume":
                speak(f"Volume is {(1/3) * math.pi * r**2 * h:.2f}")

        elif shape == "pyramid":
            speak("Enter base side length")
            b = float(listen())
            speak("Enter height")
            h = float(listen())
            if measure == "volume":
                speak(f"Volume is {(1/3) * b * b * h}")
    
    else:
        speak("Shape not recognized. Please try again.")
