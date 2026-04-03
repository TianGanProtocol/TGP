# TianGan Protocol V1.0

**人类文明史上首个时空・场・对称统一系统**  
**The First Spacetime-Field-Symmetry Unified System in Human Civilization**

### An Ancient Chinese Unified Spacetime-Field Model via 360° Symmetry  
### 基于360°对称的古代宇宙时空场统一模型

**作者 Author**：黄裳 / TIANGANPROTOCOL  
**版本 Version**：V1.0（宇宙结构定论版 / Cosmic Structure Definitive Edition）  
**许可 License**：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 🚀 核心摘要 | Core Abstract

天干协议（TianGan Protocol）V1.0 是对古代中国干支体系的终极数理重构。我们首次运用**群论**、**规范场论**与**离散傅里叶变换**的现代框架，剥离了数千年的玄学外壳，将其严格定义为一套**纯数学、纯物理的宇宙时空场模型**。

TianGan Protocol V1.0 is the ultimate mathematical reconstruction of the ancient Chinese Heavenly Stems and Earthly Branches system. For the first time, we employ modern frameworks of **group theory**, **gauge field theory**, and **discrete Fourier transform** to strip away millennia of metaphysical interpretations, rigorously defining it as a **pure mathematical and physical model of cosmic spacetime-field**.

**核心原创洞察 | Core Original Insight**：定义**年、月为宇宙时空场基准模型**，揭示**日、时干支并非独立设定，而是由360°唯一基准递归切分生成**，从而实现了「基准场（年月）-微观场（日时）-宏观场（长周期）」的全域时空统一。

Define **year and month as the benchmark model of the cosmic spacetime-field**, revealing that **the daily and hourly stems-branches are not independently set but recursively segmented from the sole 360° benchmark**, thereby achieving the global unification of spacetime from **benchmark field (year/month) → micro field (day/hour) → macro field (long cycles)**.

**数学本质 | Mathematical Essence**：严格定义 **天干 = 频域场态 ($\mathbb{Z}_{10}$)**，**地支 = 时域相位 ($\mathbb{Z}_{12}$)**，其耦合必然映射到 **六十甲子 ($\mathbb{Z}_{60}$)**，形成一个最小完备的离散周期群系统，揭示了深植于该古老系统中的时频对偶与规范对称性。

Strictly define **TianGan (Heavenly Stems) = frequency-domain field states ($\mathbb{Z}_{10}$)**, **DiZhi (Earthly Branches) = time-domain phases ($\mathbb{Z}_{12}$)**. Their coupling inevitably maps to the **Sexagenary Cycle ($\mathbb{Z}_{60}$)**, forming a minimal complete discrete periodic group system, revealing the time-frequency duality and gauge symmetry deeply embedded in this ancient system.

---

## ⚙️ 核心特性 | Core Features

- **🎯 极简统一 | Minimalist Unification**：以 **360°周天为唯一基准**，用纯相位（地支）与纯场态（天干）耦合，统一描述四维时空。  
  Using the **360° celestial circle as the sole benchmark**, it couples pure phases (DiZhi) with pure field states (TianGan) to uniformly describe four-dimensional spacetime.

- **⚙️ 数学自洽 | Mathematical Self-Consistency**：基于循环群 $\mathbb{Z}_{12} \times \mathbb{Z}_{10} \to \mathbb{Z}_{60}$ 的完美同态，结构严谨，永不崩坏。  
  Based on the perfect homomorphism of cyclic groups $\mathbb{Z}_{12} \times \mathbb{Z}_{10} \to \mathbb{Z}_{60}$, the structure is rigorous and never collapses.

- **🔬 物理内核 | Physical Core**：暗合现代物理的时频对偶（傅里叶变换）、规范对称（规范场论）与振动模式（音律）。  
  Covertly aligns with modern physics concepts: time-frequency duality (Fourier transform), gauge symmetry (gauge field theory), and vibration modes (musical temperament).

- **📜 非玄学定位 | Non-Metaphysical Positioning**：所有结论基于数理推导与物理逻辑重构，不涉及任何命理玄学应用。  
  All conclusions are based on mathematical derivation and physical logic reconstruction, involving no metaphysical or fortune-telling applications.

---

## 📁 项目结构 | Project Structure
```
TianGan-Protocol/
├── README.md                           # 本文档 | This document
├── docs/
│   └── TianGan-Protocol-V1.0.md       # V1.0完整理论文档 | Complete theoretical documentation
├── src/
│   └── tiangan_protocol.py            # 核心映射算法实现 | Core mapping algorithm implementation
├── CONTRIBUTING.md                     # 贡献指南 | Contribution guidelines
├── CONTRIBUTOR.md                      # 贡献者声明 | Contributor declaration
└── LICENSE                             # CC BY-NC 4.0 许可证 | License
```
---

## 🚦 快速开始 | Quick Start

协议的核心是将任意时刻的年、月、日、时相位映射为唯一的“天地场时序队列”。以下Python片段展示了核心映射逻辑。

The core of the protocol is to map the phases of any given year, month, day, and hour into a unique “Heaven-Earth Field Temporal Queue.” The following Python snippet demonstrates the core mapping logic.

```python
# 核心思想：天干（场态）每36°一循环，地支（相位）每30°一循环
# Core idea: TianGan (field state) cycles every 36°, DiZhi (phase) cycles every 30°.
def get_stem(phase_deg: float) -> str:
    """根据相位角获取天干场态 | Get TianGan field state from phase angle."""
    STEMS = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
    idx = int(phase_deg % 360 // 36) % 10  # 36° = 360°/10
    return STEMS[idx]

def get_branch(phase_deg: float) -> str:
    """根据相位角获取地支相位 | Get DiZhi phase from phase angle."""
    BRANCHES = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
    idx = int(phase_deg % 360 // 30) % 12  # 30° = 360°/12
    return BRANCHES[idx]

# 示例：相位36°对应 甲子
# Example: Phase 36° corresponds to 甲子 (Jia-Zi)
print(f"{get_stem(36)}{get_branch(30)}")  # 输出: 甲子
```

完整实现、耦合公式 (10 * dz_idx + 12 * tg_idx) % 60 以及递归切分示例，请参见 src/tiangan_protocol.py。
For the complete implementation, the coupling formula (10 * dz_idx + 12 * tg_idx) % 60, and examples of recursive segmentation, please refer to src/tiangan_protocol.py.

## 📜 开源声明 | Open Source Statement

- **✅ 开源范围**
    
    **| What's Open Source**：本协议开源的**核心是数学模型、群论框架、物理诠释及实现算法**，旨在促进科学讨论与跨学科研究。
      
    The **core open-source components** are the mathematical model, group-theoretic framework, physical interpretation, and implementation algorithms, aimed at fostering scientific discussion and interdisciplinary research.
    
- **❌ 未开源/限制 | What's Not Open Source / Restrictions**：具体的命理推演、预测算法、商业级接口等衍生实践不属于本开源项目范畴。
      
    Specific fortune-telling derivations, prediction algorithms, commercial-grade interfaces, and other derivative practices are **not** part of this open-source project.
    
- **📄 许可证 | License**：本项目采用 **CC BY-NC 4.0** 许可证。您可以**自由分享、演绎**本作品，但必须**署名（作者：黄裳 / TIANGANPROTOCOL）**，且**不得用于任何商业目的**。
      
    This project is licensed under **CC BY-NC 4.0**. You are free to **share and adapt** the work, but you must **give appropriate credit (to Huang Shang / TIANGANPROTOCOL)** and **not use it for commercial purposes**.
    

---

## 🤝 欢迎共建 | Welcome to Contribute

本协议开源共建。若你认同 **“宇宙即结构”**，欢迎：  
This protocol is open for collaborative development. If you resonate with the idea that **“the universe is structure,”** you are welcome to:

- **Fork** 本仓库，提出改进建议。 | **Fork** this repository and suggest improvements.
- 提交 **Issue**，讨论公理的形式化或物理诠释。 | Submit an **Issue** to discuss the formalization of axioms or physical interpretations.
- 用你的领域知识（数学、物理、信号处理、复杂系统等）扩展或验证本协议。 | Use your expertise (mathematics, physics, signal processing, complex systems, etc.) to extend or validate the protocol.
- 参与后续版本（V1.x, V2.0）的生态构建。 | Participate in building the ecosystem for future versions (V1.x, V2.0).

详细贡献指南请见 CONTRIBUTING.md。  
For detailed contribution guidelines, please see CONTRIBUTING.md.

---

## 🗺️ 路线图 | Roadmap

- **V1.0 (当前 / Current)**：确立时空场统一模型的核心公理与群论骨架（宇宙结构定论）。  
    Establishes the core axioms and group-theoretic skeleton of the spacetime-field unification model (Cosmic Structure Definitive Edition).
    
- **V1.x (进行中 / In Progress)**：完善生态扩展规范，接纳社区周期序列扩展提案。  
    Refines ecosystem extension specifications and accepts community proposals for periodic sequence extensions.
    
- **V2.0 (规划中 / Planned)**：核心延伸「人与宇宙的关联」—— **人作为宇宙时空场的谐波共振腔**，实现“天人同构”的物理闭环。  
    Core extension explores **“the connection between humans and the cosmos”** — **humans as harmonic resonance cavities of the cosmic spacetime-field**, achieving a physical closed-loop of “cosmos-human isomorphism.”
    

---

## 👨‍💻 作者 | Author

**黄裳 / TIANGANPROTOCOL**  
天干协议（TianGan Protocol）V1.0 唯一原创设计者，完成本协议的全部数理建模、物理内核定义与核心洞察提出。
  
The sole original designer of TianGan Protocol V1.0, responsible for all mathematical modeling, physical kernel definition, and core insights of this protocol.
