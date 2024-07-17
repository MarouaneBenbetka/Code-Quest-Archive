n, m = map(int, input().split())


server_name = {}
for _ in range(n):
    server, ip = input().split()
    server_name[ip] = server

for _ in range(m):
    server, ip = input().split()
    ip = ip[:-1]

    print(f'{server} {ip}; #{server_name[ip]}')
