import pandas as pd
import json
from pathlib import Path

def converter_xlsx_para_json():
    """Converte os arquivos XLSX com múltiplas planilhas para JSONs separados por mês."""
    
    arquivos = ['servidores.xlsx', 'contratados.xlsx']
    
    for arquivo in arquivos:
        nome_base = arquivo.replace('.xlsx', '')
        caminho = Path(arquivo)
        
        if not caminho.exists():
            print(f"⚠️  Arquivo {arquivo} não encontrado!")
            continue
        
        print(f"\n📂 Processando {arquivo}...")
        
        # Lê todas as planilhas do arquivo
        xlsx = pd.ExcelFile(arquivo)
        
        for planilha in xlsx.sheet_names:
            print(f"   📄 Planilha: {planilha}")
            
            # Lê a planilha
            df = pd.read_excel(xlsx, sheet_name=planilha)
            
            # Converte para JSON
            dados = df.to_dict(orient='records')
            
            # Formata o nome do arquivo JSON (ex: servidores_01-2026.json)
            nome_json = f"{nome_base}_{planilha}.json"
            
            with open(nome_json, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=2, default=str)
            
            print(f"   ✅ Criado: {nome_json} ({len(dados)} registros)")
    
    print("\n✨ Conversão concluída!")

if __name__ == "__main__":
    converter_xlsx_para_json()
