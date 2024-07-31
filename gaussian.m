% ���Է�����ʾ����
% 2x + y - z = 8
% -3x - y + 2z = -11
% -2x + y + 2z = -3

% ϵ������ A
A = [2, 1, -1;
    -3, -1, 2;
    -2, 1, 2];

% �Ҳೣ������ b
b = [8; -11; -3];

% ��˹��Ԫ��������Է�����
x_gaussian = gaussianElimination(A, b)


% ��˹��Ԫ������ʵ��
function x = gaussianElimination(A, b)
    n = size(A, 1);
    
    % �������
    Ab = [A, b];
    
    % ����1����Ԫ����
    for k = 1:n-1
        for i = k+1:n
            factor = Ab(i,k) / Ab(k,k);
            Ab(i, k+1:end) = Ab(i, k+1:end) - factor * Ab(k, k+1:end);
            Ab(i, k) = 0;
        end
    end
    
    % ����2���ش�����
    x = zeros(n, 1);
    x(n) = Ab(n,n+1) / Ab(n,n);
    
    for i = n-1:-1:1
        x(i) = (Ab(i,n+1) - Ab(i,i+1:n)*x(i+1:n)) / Ab(i,i);
    end
end
