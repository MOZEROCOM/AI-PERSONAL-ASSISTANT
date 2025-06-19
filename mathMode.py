# mathMode.py
from speak import speak
from listen import listen
import math
import re


def mathMode():
    
    speak("Entering math mode. You can say things like 'calculate 3 plus 5', 'sine of 30', or 'log of 1000'. Say 'exit math mode' when you're done.")

    while True:
        response = listen()
        if "exit" in response or "leave" in response or "stop math mode" in response:
            speak("Exiting math mode.")
            break


        try:
            if "calculate" in response:
               speak("Okay, let me do the math.")
               # Replace words with symbols
               equation = response.replace("calculate", "")
               equation = equation.replace("plus", "+")
               equation = equation.replace("minus", "-")
               equation = equation.replace("times", "*")
               equation = equation.replace("divided by", "/")
               equation = equation.replace("divided", "/")
               equation = equation.strip()


               # Extract just numbers and symbols
               match = re.findall(r"[\d\.\+\-\*/\(\)]+", equation)
               clean_expression = "".join(match)
               try:
                   result = eval(clean_expression)
                   speak(f"The answer is {result}")
               except:
                   speak("Sorry, I couldn't calculate that.")


            elif "sine of" in response or "sign of"in response:
                value = response.split("sine of")[-1].strip()
                angle = float(value)
                result = math.sin(math.radians(angle))
                speak(f"The sine of {angle} degrees is {round(result, 5)}")


            elif "cosine of" in response or "co sign of":
                value = response.split("cosine of")[-1].strip()
                angle = float(value)
                result = math.cos(math.radians(angle))
                speak(f"The cosine of {angle} degrees is {round(result, 5)}")


            elif "tangent of" in response or"tanjant of"in response:
                value = response.split("tangent of")[-1].strip()
                angle = float(value)
                result = math.tan(math.radians(angle))
                speak(f"The tangent of {angle} degrees is {round(result, 5)}")


            elif "log of" in response:
                value = response.split("log of")[-1].strip()
                number = float(value)
                if number <= 0:
                    speak("I can't take the log of a non-positive number.")
                else:
                    result = math.log10(number)
                    speak(f"The log base 10 of {number} is {round(result, 5)}")

                    
        except ValueError:
            speak("I couldn't understand the number. Please try again.")
        except Exception:
            speak("Something went wrong with the calculation.")