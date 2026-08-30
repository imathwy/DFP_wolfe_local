# 开放问题：三次连续可微目标函数上的经典 DFP 是否全局收敛？

## 1. 问题背景

考虑经典 Davidon–Fletcher–Powell（DFP）方法的逆 Hessian 形式：

\[
d_k=-H_k\nabla f(x_k),\qquad
x_{k+1}=x_k+\alpha_k d_k,
\]

其中 \(H_0\succ0\)，并使用标准 DFP 更新公式生成 \(H_{k+1}\)。假设每个正步长
\(\alpha_k\) 均满足标准 Wolfe 条件；更强地，可以要求标准 strong Wolfe 条件

\[
f(x_{k+1})
\le f(x_k)+c_1\alpha_k\nabla f(x_k)^Td_k,
\]

\[
\left|\nabla f(x_{k+1})^Td_k\right|
\le c_2\left|\nabla f(x_k)^Td_k\right|,
\qquad 0<c_1<c_2<1.
\]

现有反例已经证明：即使 \(f\in C^2(\mathbb R^2)\) 全局一致强凸，且

\[
\frac12I\preceq\nabla^2f(x)\preceq\frac32I,
\]

经典 DFP 在满足 strong Wolfe 条件的合法步长序列下仍可能不全局收敛；具体而言，
可以有

\[
\|\nabla f(x_k)\|\longrightarrow G_\infty>0.
\]

参见本仓库的 [`main-new.tex`](./main-new.tex) 以及论文
[A counterexample to global convergence of classical DFP under the standard strong Wolfe conditions](https://arxiv.org/abs/2608.21708)。

## 2. 核心开放问题

> **开放问题（\(C^3\)-DFP 全局收敛问题）.**  是否存在维数 \(n\ge2\)、函数
> \(f\in C^3(\mathbb R^n)\)、常数 \(0<m\le M<\infty\)、初始点
> \(x_0\)、初始矩阵 \(H_0\succ0\)，以及一列正步长 \((\alpha_k)\)，使得：
>
> 1. \(mI\preceq\nabla^2f(x)\preceq MI\) 对所有 \(x\in\mathbb R^n\) 成立；
> 2. 经典 DFP 迭代对所有 \(k\) 均良定义；
> 3. 每一步均满足固定参数 \(0<c_1<c_2<1\) 的标准 strong Wolfe 条件；
> 4. 但 DFP 仍不全局收敛，例如
>    \[
>    \liminf_{k\to\infty}\|\nabla f(x_k)\|>0?
>    \]

最具体的起点是固定常用参数，例如

\[
c_1=\frac14,\qquad c_2=\frac34,
\]

并首先研究二维情形。若这样的例子存在，则 \(C^2\) 反例可以升级到 \(C^3\)；
若不存在，则需要证明：在上述假设下，任意满足 strong Wolfe 条件的合法 DFP 步长序列
都满足

\[
\|\nabla f(x_k)\|\longrightarrow0.
\]

也可以提出较弱的原始版本：只要求 weak Wolfe 条件时，\(C^3\) 是否足以保证全局收敛？
strong Wolfe 版本更适合作为首要问题，因为它对反例提出了更强要求。

## 3. 当前已知结论与必须避免的误解

当前论文只构造并证明了一个全局 \(C^2\) 的目标函数。论文明确把“是否存在比
\(C^2\) 更光滑的类似反例”留作开放问题。因此目前可以确认的是：

- 当前给出的具体函数不是一个已经证明的 \(C^3\) 反例；
- 当前局部 bump 插值方法不能直接升级为 \(C^3\)；
- 这并不意味着已经证明了“\(C^3\) 反例不存在”；
- 是否存在完全不同的 \(C^3\) 反例，或者 \(C^3\) 是否蕴含经典 DFP 全局收敛，仍未解决。

换言之，下面两个命题必须严格区分：

1. **关于当前构造：** 当前轨道和插值具有明显的正则性瓶颈，不能简单平滑化为
   \(C^3\) 而保持全部规定的 DFP 数据。
2. **关于所有可能构造：** 尚无结论排除另一种满足三阶兼容条件的非收敛轨道和目标函数。

## 4. 为什么当前构造自然停在 \(C^{2,1/2}\) 尺度？

当前构造在第 \(j\) 个两步周期中使用小参数 \(\epsilon_j\to0\)，其基本空间尺度为

\[
r_j=\epsilon_j^2.
\]

插值支撑半径满足

\[
\rho_k\asymp\epsilon_j^2,
\]

而需要插入的梯度修正满足 \(\|a_k\|=O(\epsilon_j^3)\)。相邻两步的数据表明，
每个周期中至少有一个修正具有 \(\Theta(\epsilon_j^3)\) 的大小。对局部函数

\[
\psi_k(z)=
\chi\!\left(\frac{z-x_k}{\rho_k}\right)
a_k^T(z-x_k),
\]

缩放关系给出

\[
\|D^2\psi_k\|\asymp
\frac{\|a_k\|}{\rho_k}
\asymp\epsilon_j,
\]

以及在非退化子序列上

\[
\|D^3\psi_k\|\asymp
\frac{\|a_k\|}{\rho_k^2}
\asymp\epsilon_j^{-1}.
\]

因此 Hessian 在大小约为 \(\epsilon_j^2\) 的距离上发生大小约为
\(\epsilon_j\) 的变化，而

\[
\epsilon_j=(\epsilon_j^2)^{1/2}.
\]

这表明当前构造的自然临界正则性是

\[
\nabla^2f\in C^{0,1/2},
\qquad\text{即}\qquad f\in C^{2,1/2},
\]

而不应期待 \(\nabla^2f\) 是 Lipschitz 连续的。三阶导数的尺度还会在极限圆附近
发散，所以该 bump 构造不能产生全局 \(C^3\) 函数。

论文目前正式证明的是 \(C^2\)，并未把“恰为 \(C^{2,1/2}\)”写成独立定理。
把上述尺度论证补成严格的上、下 Hölder 估计，是一个重要且相对明确的第一步。

## 5. 一个更强的中间问题：当前轨道是否根本不允许 \(C^3\) 插值？

当前两步循环采用的 secant 矩阵在各自的移动正交基下具有形式

\[
A_1(\epsilon)=
\begin{pmatrix}1&\epsilon\\ \epsilon&1\end{pmatrix},
\qquad
A_2(\epsilon)=
\begin{pmatrix}1&-2\epsilon\\ -2\epsilon&1\end{pmatrix}.
\]

两条相邻线段的空间尺度及其间距为 \(O(\epsilon^2)\)，但相应混合 secant 分量
之间存在 \(\Theta(\epsilon)\) 的变化。若 Hessian 是 \(\alpha\)-Hölder 连续的，
则这种变化原则上只能是

\[
O\bigl((\epsilon^2)^\alpha\bigr)=O(\epsilon^{2\alpha}).
\]

与 \(\Theta(\epsilon)\) 比较，临界指数正好是 \(\alpha=1/2\)。这提示下列可单独解决的
中间问题：

> **轨道兼容性问题.** 证明当前规定的点、函数值和梯度数据不存在
> \(C^{2,\alpha}\) 插值，其中 \(\alpha>1/2\)；特别地，不存在保持同一条精确 DFP
> 轨道的 \(C^3\) 目标函数。

这里需要比较的是实际 secant 方程在共同法向—切向坐标中的分量，而不能仅比较
辅助矩阵 \(A_1\) 和 \(A_2\) 的算子范数。完成这一点将说明正则性障碍来自轨道数据
本身，而不只是所选 cutoff 函数不够巧妙。

## 6. 解决主问题的两条可能路线

### 路线 A：证明 \(C^3\) 下全局收敛

因为一致强凸性把相关水平集限制在有界区域内，\(f\in C^3\) 意味着 Hessian 在该区域
上局部 Lipschitz，且 Lipschitz 常数可以取为一致常数。可能的目标是利用这一额外估计
证明：

- 相邻 secant 商不能以当前反例中的速度交替振荡；
- DFP 逆 Hessian 近似的退化与无限总旋转不能同时发生；或
- strong Wolfe 条件与 Hessian Lipschitz 性共同迫使某个势函数下降，从而推出
  \(\liminf_k\|\nabla f(x_k)\|=0\)，再进一步得到完整极限为零。

困难在于：已有带 Hessian Lipschitz 假设的条件收敛定理通常还使用修改后的线搜索、
精确线搜索、步长可和性或其他附加条件；它们不能直接推出标准 Wolfe 条件下的结论。

### 路线 B：构造新的 \(C^3\) 反例

新的构造必须从轨道层面满足三阶 Whitney 兼容性，而不能只在最后更换一个更光滑的
cutoff。可能需要：

- 让相邻 secant 数据的变化降到与空间距离同阶，即把当前
  \(\Theta(\epsilon)\) 对 \(O(\epsilon^2)\) 的失配消除；
- 增加周期长度、状态变量或空间维数，使产生无限旋转的效应累积，同时使局部 Hessian
  变化保持 Lipschitz；
- 重新选择衰减律，使“梯度模长变化可和”与“旋转角不可和”仍能同时成立；
- 直接构造兼容的二阶 jet，再用 \(C^3\) Whitney 延拓，而不是只规定函数值和梯度后
  使用互不相交的局部 bump。

## 7. 建议优先验证的三个子问题

1. **临界正则性定理：** 严格证明论文中的具体目标函数属于 \(C^{2,1/2}\)，但不属于
   任何 \(C^{2,\alpha}\)，\(\alpha>1/2\)。
2. **固定轨道不可能性：** 不依赖具体 bump，证明当前规定的 DFP endpoint jets 不存在
   \(C^3\) 实现。
3. **Lipschitz-Hessian 动力学：** 确定 Hessian Lipschitz 条件是否排除所有具有
   “梯度模长变化可和、基向量总旋转不可和”特征的 DFP 非收敛轨道，还是只排除当前
   两步构造。

前两个子问题即使不能解决主开放问题，也会准确刻画现有反例的最优正则性，并解释
为什么从 \(C^2\) 升级到 \(C^3\) 需要新的数学机制，而不是技术性的平滑处理。

## 8. 一句话版本

> 经典 DFP 在一致强凸的 \(C^2\) 目标函数和标准 strong Wolfe 条件下可以不全局收敛；
> 现有反例的 Hessian 呈现临界的 \(1/2\)-Hölder 尺度。若进一步要求目标函数属于
> \(C^3\)，是否仍存在反例，还是 Hessian 的局部 Lipschitz 性足以恢复全局收敛？

