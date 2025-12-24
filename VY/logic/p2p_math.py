# logic/p2p_math.py

class P2PMath:
    @staticmethod
    def map_pixel_to_real(pixel_val, px_min, px_max, real_min, real_max):
        """
        Piksel koordinatını gerçek dünya koordinatına dönüştürür.
        Formül: Doğrusal Enterpolasyon (Linear Interpolation)
        """
        # Sıfıra bölünme hatasını önle
        if (px_max - px_min) == 0:
            return 0.0
            
        # Oransal hesap
        ratio = (pixel_val - px_min) / (px_max - px_min)
        real_val = real_min + ratio * (real_max - real_min)
        
        return real_val