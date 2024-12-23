print('Welcome to the Cybersecurity Mission')
mission = input('Choose your mission (trace the hacker/secure the system): ')
if mission == 'trace the hacker':
    trace_action = input('Choose your strategy (track their IP/decode their message): ')
    if trace_action == 'track their IP':
        print('You caught the hacker. You Win!')
    elif trace_action == 'decode their message':
        print('The message was a trap. Game Over.')
elif mission == 'secure the system':
    secure_action = input('Choose your method (shut down the server/upgrade the firewall): ')
    if secure_action == 'shut down the server':
        print('The attack was stopped. You Win!')
    elif secure_action == 'upgrade the firewall':
        print('The hacker bypassed it. Game Over.')
