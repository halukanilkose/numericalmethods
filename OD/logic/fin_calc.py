# logic/fin_calc.py
import math

class FinPhysics:
    @staticmethod
    def calculate_optimum_spacing(inputs):
        """
        Optimum Fin Boşluğu Hesaplar.
        Formül: s_opt = 2.659 * ( (L*mu*k) / (g*beta*cp*rho*dt) )^0.25 * (rho^-0.5)
        """
        try:
            L = inputs['L']
            mu = inputs['mu']
            k = inputs['k']
            g = inputs['g']
            beta = inputs['beta']
            cp = inputs['cp']
            rho = inputs['rho']
            dt = inputs['dt']

            # Pay (Numerator)
            num = L * mu * k
            
            # Payda (Denominator)
            den = g * beta * cp * dt
            
            if den == 0 or rho == 0:
                return None, "Sıfıra bölme hatası (Yoğunluk veya DT sıfır olamaz)."

            # Formül Uygulama
            term1 = math.pow(num / den, 0.25)
            term2 = math.pow(rho, -0.5) # rho üzeri -0.5 (veya 1/sqrt(rho))
            
            # Not: Orijinal kodda rho^-0.5 ayrı bir çarpım olarak verilmişti, aynen korundu.
            # Ancak fiziksel olarak genellikle Rayleigh sayısı içinde rho^2 olur. 
            # Senin koduna sadık kalındı.
            
            s_opt_m = 2.659 * term1 * term2
            s_opt_mm = s_opt_m * 1000.0
            
            return s_opt_mm, None

        except Exception as e:
            return None, str(e)