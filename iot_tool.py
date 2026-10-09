# iot_tool.py
# Collaborative engineering automation and embedded systems computation toolkit
import math

def print_banner():
    print("==========================================================")
    print("=== IoT & Embedded Systems Engineering Toolkit v1.0   ===")
    print("==========================================================")


# ====================================================================
# DEVELOPER ZONE: STUDENTS MUST WRITE CODE EXCLUSIVELY INSIDE THEIR FUNCTION
# ====================================================================

def calculate_variant_1():
    print("\n[Variant 1: Servomotor Control Systems]")
    a = float(input("Введіть кут повороту ротора "))
    b = float(input("Введіть кутову швидкість "))
    t = a/b
    print (t)
    pass


def calculate_variant_2():
    print("\n[Variant 2: Analog-to-Digital Conversion]")
    # DEVELOPER 2: Read 10-bit ADC and Vref = 5.0. Calculate V = (ADC / 1023) * Vref.
    # Apply bitwise left shift ADC << 2. Validate sensor marking, list of voltages.
    pass


def calculate_variant_3():
    print("\n[Variant 3: Battery Pack Monitoring]")
    # DEVELOPER 3: Read capacity E and power P. Calculate t = E / P.
    # Perform bitwise OR between integer E and P. Reverse LiFePO4 string, cell voltages.
    pass


def calculate_variant_4():
    print("\n[Variant 4: Stress and Strain Calculation]")
    # DEVELOPER 4: Read force F and area A. Mechanical stress sigma = F / A.
    # Apply bitwise right shift F >> 1. Material grade string and component strains.
    pass


def calculate_variant_5():
    print("\n[Variant 5: Unmanned Aerial Vehicle Telemetry]")
    # DEVELOPER 5: Read altitude H and vertical speed Vz. Calculate t = H / Vz.
    # Perform bitwise XOR between H and Vz. Validate $GPGGA telemetry string, active sensors.
    pass


def calculate_variant_6():
    print("\n[Variant 7: Robot Kinematics Drive Calculation]")
        # DEVELOPER 7: Read gear ratio i and motor RPM Nin.
        # Output shaft Nout = Nin / i. Apply bitwise left shift Nin << 3. Manipulator link string.
    pass


def calculate_variant_7():
    print("\n[Variant 7: Robot Kinematics Drive Calculation]")
    # DEVELOPER 7: Read gear ratio i and motor RPM Nin.
    i = float(input('Enter gear ratio:'))
    N_in = float(input('Enter motor RPM:'))
    # Output shaft Nout = Nin / i. Apply bitwise left shift Nin << 3. Manipulator link string.
    N_out = N_in / i
    bit_shift = int(N_in) << 3 

    print(f'Output shaft: {N_out}')
    print(f'Bitwise left shift: {bit_shift}')
    pass


def calculate_variant_8():
        #1
        P, Q = map(float, input("Введіть тиск та витрату рідини: ").split())
        W = (P * Q) / 600
        Y = int(P) | int(Q)
        print("Гідравлічна потужність:",W)
        print("Побітова операція OR:",Y)
        #2
        a = input("Введіть код діагностики: ")
        i = "DTC" in a
        m = a.find("_")
        print("Чи починається з DTC:",i)
        print("Частина коду:",a[:m])
        #3
        s = list(map(float, input("Введіть список показань температури: ").split()))
        s = s[1:]
        s = s + [float(18)]
        s_max = max(s)
        s_min = min(s)
        T = s_min, s_max
        print("Список:",s)
        print("Граничні значення:",T)
        #4
        c = {"cylinder_id":6767,"stroke_lenght":1809,"fluid_tags":["Wow","wow","woW","WoW","Wow"]}
        f = set(c["fluid_tags"])
        o = ("CONTAMINATED" not in f) and (c["stroke_lenght"]>=200)
        print("Множина унікальних специфікацій:",f)
        print("Перевірка логічної умови:",o)


def calculate_variant_9():
    print("\n[Variant 9: Climate Control and Ventilation Systems]")
    # DEVELOPER 9: Read heater power (P) and runtime (t). Thermal energy Q = P * t.
    # Perform bitwise XOR between power and time. PLC_HVAC controller identifier string.
    pass


def calculate_variant_10():
    print("\n[Variant 10: Orientation and Navigation Systems (IMU)]")
    # DEVELOPER 10: Read Ax, Ay, Az. Total acceleration A = sqrt(Ax^2 + Ay^2 + Az^2).
    # Apply bitwise right shift Az >> 2. Raw data ACC:X=... string, Euler angles.
    pass


def calculate_variant_11():
    print("\n[Variant 11: BLDC Motor Control Systems]")
    # DEVELOPER 11: Read PWM duty cycle (DUTY) and supply voltage Vdc. Vphase = (DUTY/100)*Vdc.
    # Perform bitwise AND between integer DUTY and 0b11110000. Hall sensors state string.
    pass


def calculate_variant_12():
    print("\n[Variant 12: Optical Encoder Data Acquisition]")
    PPR, N = map(int, input('Введіть частоту та кількість сигналів: ').split(' '))

    print(f'Кількість повних обертів: {N // PPR}')
    print(f'Залишковий кут у імпульсах: {N % PPR}')

    print(f'Зсунута кількість сигналів: {N << 1}')


def calculate_variant_13():
    print("\n[Variant 13: Industrial Modbus RTU Network]")
    # DEVELOPER 13: Read 16-bit Modbus register value R.
    # Split into High and Low bytes, print both in binary format.
    pass


# ====================================================================
# MAIN EXECUTION MODULE (TEAM LEAD UNCOMMENTS DURING INTEGRATION)
# ====================================================================
if __name__ == "__main__":
    print_banner()
    
    # calculate_variant_1()
    # calculate_variant_2()
    # calculate_variant_3()
    # calculate_variant_4()
    # calculate_variant_5()
    # calculate_variant_6()
    # calculate_variant_7()
    # calculate_variant_8()
    # calculate_variant_9()
    # calculate_variant_10()
    # calculate_variant_11()
    # calculate_variant_12()
    # calculate_variant_13()
