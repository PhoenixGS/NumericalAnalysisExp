cnt = 0;
l = 0;
while cnt < 10
    r = l + 1;
    if besselj(0, l)*besselj(0, r) < 0
        fzerotx(@(x) besselj(0, x), [l, r])
        cnt = cnt + 1;
    end
    l = l + 1;
end