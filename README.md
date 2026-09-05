# Latihan-Python 
**Penggunaan Python dalam mengonversi rumus matematika dan fisika menjadi grafik 2D.**

-- Simulasi Lintasan Gerak Parabola 3 Sudut Elevasi. --

_//Parameter awal_
Sudut lintasan yaitu theta = 30 deg, 45 deg, 60 deg
Kecepatan awal v0 = 25 m/s
Konstanta Gravitasi g = 9.81 m/s^2

_//Konversi sudut khusus Python karena penggunaan NumPy_
1. 30 deg = rad 1/6 pi
2. 45 deg = rad 1/4 pi
3. 60 deg = rad 1/3 pi

_//Inisiasi rumus persamaan GLB dan GLBB_
a. GLB : x = v0 * cos(theta_rad) * t
b. GLBB : y = v0 * sin(theta_rad) * t - 1/2 * g * t_squared
