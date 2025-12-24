# logic/pao_props.py

class PAOPhysics:
    # Kullanıcıdan gelen PAO Veri Tablosu
    # Format: (Sıcaklık [°C], Viskozite [mm2/s], Yoğunluk [g/cm3], Özgül Isı [kJ/kgK], İletkenlik [W/mK])
    DATA_TABLE = [
        (-40, 249.3, 0.851, 2.010, 0.164),
        (-20,  53.9, 0.832, 2.072, 0.162),
        ( 10,  12.5, 0.804, 2.167, 0.157),
        ( 25,  7.67, 0.790, 2.214, 0.155),
        ( 30,  6.52, 0.785, 2.229, 0.154),
        ( 40,  5.00, 0.775, 2.261, 0.152),
        ( 60,  3.22, 0.750, 2.330, 0.150),
        ( 85,  2.11, 0.733, 2.418, 0.146)
    ]

    @staticmethod
    def interpolate(x, x1, x2, y1, y2):
        """Lineer İnterpolasyon Formülü"""
        return y1 + (x - x1) * (y2 - y1) / (x2 - x1)

    @classmethod
    def calculate(cls, temp_c):
        table = cls.DATA_TABLE
        
        # Sınır değer kontrolleri (Clamping)
        if temp_c <= table[0][0]:
            return cls._format_res(table[0])
        if temp_c >= table[-1][0]:
            return cls._format_res(table[-1])

        # Tablo içinde arama ve interpolasyon
        for i in range(len(table) - 1):
            t1, v1, d1, cp1, k1 = table[i]
            t2, v2, d2, cp2, k2 = table[i+1]
            
            if t1 <= temp_c <= t2:
                visc = cls.interpolate(temp_c, t1, t2, v1, v2)
                dens = cls.interpolate(temp_c, t1, t2, d1, d2)
                cp   = cls.interpolate(temp_c, t1, t2, cp1, cp2)
                cond = cls.interpolate(temp_c, t1, t2, k1, k2)
                
                return {
                    "viscosity": visc,
                    "density": dens * 1000,      # g/cm3 -> kg/m3 dönüşümü
                    "specific_heat": cp * 1000,  # kJ/kgK -> J/kgK dönüşümü
                    "thermal_k": cond
                }

    @staticmethod
    def _format_res(res_tuple):
        return {
            "viscosity": res_tuple[1],
            "density": res_tuple[2] * 1000,      # g/cm3 -> kg/m3
            "specific_heat": res_tuple[3] * 1000, # kJ/kgK -> J/kgK
            "thermal_k": res_tuple[4]
        }