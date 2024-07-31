% 线性方程组示例：
% 2x + y - z = 8
% -3x - y + 2z = -11
% -2x + y + 2z = -3

% 系数矩阵 A
A = [2, 1, -1;
    -3, -1, 2;
    -2, 1, 2];

% 右侧常数向量 b
b = [8; -11; -3];

% LU分解法求解线性方程组
x_LU = LUSolver(A, b)

% LU分解法函数实现
function x = LUSolver(A, b)
    [L, U] = lu(A); % LU分解
    y = L \ b;      % 前向替代
    x = U \ y;      % 回代
end
