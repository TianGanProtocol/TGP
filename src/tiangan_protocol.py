"""
TianGan Protocol V1.0 Core Algorithm
Author: 黄裳 / TIANGANPROTOCOL
License: CC BY-NC 4.0
"""

TIAN_GAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]  # 天干，场态，Z10
DI_ZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]  # 地支，相位，Z12
JIA_ZI = [f"{tg}{dz}" for tg in TIAN_GAN for dz in DI_ZHI][:60]  # 六十甲子，Z60

def phase_to_stem(phase_deg: float) -> str:
    """将相位角（度）映射为天干场态。每36°一个天干。"""
    idx = int(phase_deg % 360 // 36) % 10  # 36 = 360 / 10
    return TIAN_GAN[idx]

def phase_to_branch(phase_deg: float) -> str:
    """将相位角（度）映射为地支相位。每30°一个地支。"""
    idx = int(phase_deg % 360 // 30) % 12  # 30 = 360 / 12
    return DI_ZHI[idx]

def jiazi_mapping(tg_deg: float, dz_deg: float) -> str:
    """
    核心耦合公式：将天干角度和地支角度映射到唯一的六十甲子。
    公式: (10 * dz_idx + 12 * tg_idx) % 60
    这是 ℤ₁₂ × ℤ₁₀ → ℤ₆₀ 同态的数学实现。
    """
    tg_idx = int(tg_deg % 360 // 36) % 10
    dz_idx = int(dz_deg % 360 // 30) % 12
    jiazi_idx = (10 * dz_idx + 12 * tg_idx) % 60
    return JIA_ZI[jiazi_idx]

if __name__ == "__main__":
    # 验证核心映射
    print("验证核心映射:")
    print(f"jiazi_mapping(36, 30) -> {jiazi_mapping(36, 30)}")  # 应输出：甲子
    print(f"jiazi_mapping(252, 210) -> {jiazi_mapping(252, 210)}")  # 应输出：庚午
