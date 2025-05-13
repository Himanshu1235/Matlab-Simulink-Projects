num = [5];
den = [1 1];
G1 = tf(num,den)
figure
hold on
for K = [1,2,5,10,20];
    Closed_loop_System = feedback(K*G1,1);
    plot(step(Closed_loop_System));
end
legend('K=1', 'K=2', 'K=5', 'K=10','K=20');
title('Closed loop response')
xlabel('Time(sec)');
ylabel('Response');
grid on