# logic/atmosphere.py
import math

class AtmospherePhysics:
    g0 = 9.80665
    R = 287.0528
    GAMMA = 1.4
    BETA = 1.458e-6
    S_CONST = 110.4

    @staticmethod
    def get_atmosphere_layers():
        return [
            (11000.0, -0.0065), (20000.0,  0.0), (32000.0,  0.0010),
            (47000.0,  0.0028), (51000.0,  0.0), (71000.0, -0.0028),
            (86000.0, -0.0020)
        ]

    @staticmethod
    def calculate(altitude_input, unit, temp_offset_k):
        altitude_m = 0.0
        if unit == "m": altitude_m = altitude_input
        elif unit == "km": altitude_m = altitude_input * 1000.0
        elif unit == "ft": altitude_m = altitude_input * 0.3048
        
        if altitude_m < -5000 or altitude_m > 86000:
            return None, f"Hesaplama aralığı dışı!\nGirilen: {altitude_m:.1f} m\nİzin verilen: -5000 m ile 86000 m arası."

        current_h = 0.0
        current_T = 288.15
        current_P = 101325.0
        T_std = current_T
        P_std = current_P

        if altitude_m < 0:
            lapse_rate = -0.0065
            T_std = current_T + lapse_rate * altitude_m
            base = T_std / current_T
            power = -AtmospherePhysics.g0 / (lapse_rate * AtmospherePhysics.R)
            P_std = current_P * (base ** power)
        else:
            layers = AtmospherePhysics.get_atmosphere_layers()
            for layer_end_h, lapse_rate in layers:
                if altitude_m <= layer_end_h:
                    delta_h = altitude_m - current_h
                    if lapse_rate == 0.0:
                        T_std = current_T
                        P_std = current_P * math.exp((-AtmospherePhysics.g0 * delta_h) / (AtmospherePhysics.R * current_T))
                    else:
                        T_std = current_T + lapse_rate * delta_h
                        P_std = current_P * ((T_std / current_T) ** (-AtmospherePhysics.g0 / (lapse_rate * AtmospherePhysics.R)))
                    break
                else:
                    delta_h = layer_end_h - current_h
                    if lapse_rate == 0.0:
                        next_P = current_P * math.exp((-AtmospherePhysics.g0 * delta_h) / (AtmospherePhysics.R * current_T))
                        next_T = current_T
                    else:
                        next_T = current_T + lapse_rate * delta_h
                        next_P = current_P * ((next_T / current_T) ** (-AtmospherePhysics.g0 / (lapse_rate * AtmospherePhysics.R)))
                    current_h = layer_end_h
                    current_T = next_T
                    current_P = next_P
                    T_std = current_T
                    P_std = current_P

        T_final = T_std + temp_offset_k
        if T_final <= 0: return None, "Sıcaklık mutlak sıfıra ulaştı."
        
        rho = P_std / (AtmospherePhysics.R * T_final)
        speed_of_sound = math.sqrt(AtmospherePhysics.GAMMA * AtmospherePhysics.R * T_final)
        viscosity = (AtmospherePhysics.BETA * (T_final ** 1.5)) / (T_final + AtmospherePhysics.S_CONST)

        return {
            "alt_m": altitude_m, "temp_k": T_final, "pressure": P_std,
            "density": rho, "sound_speed": speed_of_sound, "viscosity": viscosity
        }, None