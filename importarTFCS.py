import os
import django
import json
import sys

# Garante que o Django encontra as configurações do projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetoPython.settings')
django.setup()

from portfolio.models import TFC, Tecnologia, Area, Docente

def importar_tfcs(ficheiro_json):
    if not os.path.exists(ficheiro_json):
        print(f"O ficheiro {ficheiro_json} não foi encontrado.")
        return

    with open(ficheiro_json, 'r', encoding='utf-8') as f:
        try:
            dados = json.load(f)
        except json.JSONDecodeError:
            print("❌ O ficheiro JSON não tem a formatação correta.")
            return

    contador_sucesso = 0

    for item in dados:
        titulo = item.get('titulo', 'Sem Título')
        autor_raw = item.get('autor', 'Autor Desconhecido')
        curso = item.get('curso', 'N/A')
        resumo = item.get('resumo', '')
        palavras_chave = item.get('palavras_chave', '')
        tfc, created = TFC.objects.get_or_create(
            titulo=titulo,
            defaults={
                'autor': autor_raw,
                'curso': curso,
                'ano': 2025,
                'resumo': resumo,
                'palavras_chave': palavras_chave,
            }
        )

        if created:
            print(f"A importar: {titulo}")
            
            # Relacionar as áreas
            areas_raw = item.get('areas')
            if areas_raw:
                lista_areas = [a.strip() for a in areas_raw.replace(';', ',').split(',')]
                for nome_area in lista_areas:
                    if nome_area:
                        area, _ = Area.objects.get_or_create(nome=nome_area)
                        tfc.areas.add(area)

            # Relacionar as tecnologias
            tecs_raw = item.get('tecnologias')
            if tecs_raw:
                lista_tecs = [t.strip() for t in tecs_raw.replace(';', ',').split(',')]
                for nome_tec in lista_tecs:
                    if nome_tec:
                        tec, _ = Tecnologia.objects.get_or_create(nome=nome_tec)
                        tfc.tecnologias.add(tec)

            # Relacionar os orientadores (Docentes)
            docs_raw = item.get('orientador')
            if docs_raw:
                lista_docs = [d.strip() for d in docs_raw.replace(';', ',').split(',')]
                for nome_docente in lista_docs:
                    if nome_docente:
                        docente, _ = Docente.objects.get_or_create(nome=nome_docente)
                        tfc.docentes_orientadores.add(docente)
            
            contador_sucesso += 1
        else:
            print(f"(Já existe): {titulo}")

    print(f"\nImportação concluída! {contador_sucesso} TFCs adicionados.")

if __name__ == "__main__":
    importar_tfcs('data/tfcs_2025.json')