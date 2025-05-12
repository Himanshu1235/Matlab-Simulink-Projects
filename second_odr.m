K=1
figure
hold on
for a=[0,0.5,1.2,1]
    num=[K*K]
    den = [1 2*a*K K*K];
    G2=tf(num, den)
    xlim([0 300])
    plot(step(G2))
end
grid on
legend('a=0', 'a=0.5', 'a=1.2', 'a=1')
xlabel('Time(sec)')
ylabel('Response')
grid on