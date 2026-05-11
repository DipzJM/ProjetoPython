import os
from django.core.files import File
import portfolio.models as portfolio_models

def executar_migracao(modelo_nome, campo_nome, pasta_fallback):
    # Verifica se o modelo existe no seu models.py
    if not hasattr(portfolio_models, modelo_nome):
        print(f"⚠️  Modelo '{modelo_nome}' não encontrado no models.py. A saltar...")
        return

    modelo = getattr(portfolio_models, modelo_nome)
    print(f"\n>>> Migrando {modelo_nome} (campo: {campo_nome})...")
    
    # Caminho exato do seu workspace
    pasta_base_media = "/workspaces/ProjetoPython/media/"
    
    objetos = modelo.objects.all()
    sucesso = 0

    for obj in objetos:
        campo = getattr(obj, campo_nome, None)
        
        # Se o campo não existir (ex: tentámos 'foto' mas é 'imagem')
        if campo is None:
            print(f"  ❌ Erro: O modelo {modelo_nome} não tem o campo '{campo_nome}'")
            break

        if campo and campo.name:
            nome_ficheiro = os.path.basename(campo.name)
            
            # Tentamos o caminho guardado na BD
            caminho_final = os.path.join(pasta_base_media, campo.name)
            
            # Se não existir, tentamos na pasta que vimos na imagem
            if not os.path.exists(caminho_final):
                caminho_final = os.path.join(pasta_base_media, pasta_fallback, nome_ficheiro)

            if os.path.exists(caminho_final):
                try:
                    with open(caminho_final, 'rb') as f:
                        # O save=True envia para o Cloudinary automaticamente
                        campo.save(nome_ficheiro, File(f), save=True)
                    sucesso += 1
                    print(f"  ✅ {nome_ficheiro} migrado com sucesso!")
                except Exception as e:
                    print(f"  ❌ Erro ao enviar {nome_ficheiro}: {e}")
            else:
                print(f"  ❌ Ficheiro não encontrado no disco: {caminho_final}")

    print(f"Concluído {modelo_nome}: {sucesso} migrados.")

def migrar_tudo():
    # CONFIGURAÇÃO ATUALIZADA SEGUNDO O TEU MODELS.PY
    # (Nome do Modelo, Nome do Campo Real, Pasta no disco)
    config = [
        ('Tecnologia', 'logo', 'tecnologias'),     
        ('Docente', 'foto', 'docentes'),         
        ('Projeto', 'imagem', 'projetos'),        
        ('UnidadeCurricular', 'imagem', 'ucs'),     
        ('MakingOf', 'foto', 'making_of'),        
        ('TFC', 'imagem', 'tfcs'),          
    ]

    for mod, camp, pasta in config:
        executar_migracao(mod, camp, pasta)

if __name__ == "__main__":
    migrar_tudo()