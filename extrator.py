import re
import os

def extract_netflix_ids(input_file, output_file):
    """
    Extrai todos os NetflixId de um arquivo de texto e salva em outro arquivo
    """
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        netflix_ids = []
        
        lines = content.split('\n')
        for line in lines:
            if '.netflix.com' in line and '\t' in line:
                parts = line.split('\t')
                if len(parts) >= 7 and parts[5] == 'NetflixId' and parts[6].strip():
                    netflix_id = 'NetflixId=' + parts[6].strip()
                    
                    if netflix_id not in netflix_ids:
                        netflix_ids.append(netflix_id)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for netflix_id in netflix_ids:
                f.write(netflix_id + '\n')
        
        print(f"[+] {len(netflix_ids)} NetflixId extraidos e salvos em '{output_file}'")
        return len(netflix_ids)
        
    except FileNotFoundError:
        print(f"[-] Arquivo '{input_file}' nao encontrado")
        return 0
    except Exception as e:
        print(f"[-] Erro: {e}")
        return 0

def main():
    print("Netflix ID Extractor")
    print("=" * 30)
    
    input_file = "cookies.txt"
    output_file = "cookies_extraidos.txt"
    
    if not os.path.exists(input_file):
        print(f"[-] Arquivo '{input_file}' nao encontrado")
        print(f"[*] Arquivos no diretorio atual:")
        for file in os.listdir('.'):
            if file.endswith('.txt'):
                print(f"   - {file}")
        return
    
    count = extract_netflix_ids(input_file, output_file)
    
    if count > 0:
        print(f"\n[+] Extracao concluida!")
        print(f"[*] Total de NetflixId encontrados: {count}")
        print(f"[*] Arquivo de saida: {output_file}")
        
        try:
            with open(output_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()[:5]
                print(f"\n[*] Primeiros {len(lines)} resultados:")
                for i, line in enumerate(lines, 1):
                    print(f"   {i}. {line.strip()}")
        except:
            pass
    else:
        print("[-] Nenhum NetflixId encontrado")

if __name__ == "__main__":
    main()
