#CONTOH KASUS
#   Skrip ini mensimulasikan lintasan gerak parabola untuk 3 sudut elevasi berbeda
#   ($\theta = 30^\circ, 45^\circ, 60^\circ$) dengan kecepatan awal $v_0 = 25\text{ m/s}$.

import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# 1. PARAMETER FISIKA INTI
# ==========================================
v0 = 25.0              # Kecepatan awal (m/s)
g = 9.81               # Percepatan gravitasi bumi (m/s^2)
sudut_list = [30, 45, 60]  # Variasi sudut elevasi (derajat)

# Menyiapkan kanvas grafik
plt.figure(figsize=(9, 5))

print("=== HASIL PERHITUNGAN GERAK PARABOLA ===")

for theta_deg in sudut_list:
    # Konversi sudut dari derajat ke radian
    theta_rad = np.radians(theta_deg)
    
    # Waktu total penerbangan (saat posisi vertikal y = 0)
    t_total = 2 * v0 * np.sin(theta_rad) / g
    
    # Membuat diskritisasi waktu t dari 0 sampai t_total (200 titik)
    t = np.linspace(0, t_total, 200)
    
    # Persamaan Kinematika Gerak 2D
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * (t**2)
    
    # Perhitungan parameter puncak dan jangkauan maksimum
    h_max = (v0**2 * (np.sin(theta_rad)**2)) / (2 * g)
    r_max = (v0**2 * np.sin(2 * theta_rad)) / g
    
    # Tampilkan ringkasan di Terminal VS Code
    print(f"Sudut {theta_deg}° | t_total: {t_total:.2f} s | h_max: {h_max:.2f} m | R_max: {r_max:.2f} m")
    
    # Plot lintasan posisi y(x)
    plt.plot(x, y, label=f"θ = {theta_deg}° R = {r_max:.1f} m | H = {h_max:.1f} m | T = {t_total:.1f} s")


# ==========================================
# 2. ESTETIKA & DEKORASI GRAFIK
# ==========================================
plt.title("Simulasi Gerak Parabola - Fisika Dasar 1", fontsize=13, fontweight='bold')
plt.xlabel("Jarak Horizontal x (meter)", fontsize=11)
plt.ylabel("Ketinggian Vertikal y (meter)", fontsize=11)
plt.axhline(0, color='black', linewidth=1.2)  # Garis permukaan tanah
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')
plt.tight_layout()

# Menampilkan jendela grafik
plt.show()