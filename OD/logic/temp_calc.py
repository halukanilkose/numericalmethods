# logic/temp_calc.py

class TempPhysics:
    @staticmethod
    def calculate_outlet_temp(inputs):
        """
        Q = m_dot * cp * delta_t formülünden t_out çeker.
        """
        try:
            v_dot_lpm = inputs['v_dot_lpm']
            rho = inputs['rho']
            cp = inputs['cp']
            Q = inputs['Q']
            t_in = inputs['t_in']

            # Debi dönüşümü: LPM -> m^3/s
            # 1 LPM = (1/1000) / 60 m^3/s
            v_dot_m3s = (v_dot_lpm * 0.001) / 60.0
            
            # Kütlesel Debi: m_dot = v_dot * rho
            m_dot = v_dot_m3s * rho
            
            if m_dot == 0 or cp == 0:
                return None, "Kütlesel debi veya Cp sıfır olamaz."

            # Q = m_dot * cp * delta_t  =>  delta_t = Q / (m_dot * cp)
            delta_t = Q / (m_dot * cp)
            
            t_out = t_in + delta_t
            
            return t_out, None

        except Exception as e:
            return None, str(e)