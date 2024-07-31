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

% 高斯消元法求解线性方程组
x_gaussian = gaussianElimination(A, b)


% 高斯消元法函数实现
function x = gaussianElimination(A, b)
    n = size(A, 1);
    
    % 增广矩阵
    Ab = [A, b];
    
    % 步骤1：消元过程
    for k = 1:n-1
        for i = k+1:n
            factor = Ab(i,k) / Ab(k,k);
            Ab(i, k+1:end) = Ab(i, k+1:end) - factor * Ab(k, k+1:end);
            Ab(i, k) = 0;
        end
    end
    
    % 步骤2：回代过程
    x = zeros(n, 1);
    x(n) = Ab(n,n+1) / Ab(n,n);
    
    for i = n-1:-1:1
        x(i) = (Ab(i,n+1) - Ab(i,i+1:n)*x(i+1:n)) / Ab(i,i);
    end
end
