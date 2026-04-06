# Diário de Bordo: Making Of - Portfólio Pessoal

Este documento regista o processo de conceção, modelação e tomada de decisão para a aplicação de Portfólio Académico desenvolvida em Django.

---

## Registos do Trabalho em Papel
*Os registos visuais de suporte a este documento (fotografias do caderno e esquemas) encontram-se na pasta `/media/makingof/` do repositório.*

### 1. Identificação de Entidades e Atributos Versão 1 (Imagem `entidadesV1`)
Após a análise detalhada do enunciado e a consulta de referências (DEISI/Lusófona), identifiquei as entidades para o sistema:

* **Licenciatura**
* **Unidade Curricular (UC)**
* **Projetos**
* **Tecnologias**
* **TFCs**
* **Formações**
* **Competências**
* **Making Of**

#### Entidades Adicionais
1.  **Docentes**
2.  **Áreas**
---

## Modelação de Dados e Relações Versão 1 (Imagem `realacoesEntidadesV1`)

No desenho do **Diagrama Entidade-Relação (ER)**, foram definidas as seguintes relações:

* **Licenciatura (1:N) UC:** Uma licenciatura agrega várias disciplinas.
* **UC (1:N) Projeto:** Os projetos nascem dentro do contexto de uma disciplina na qual numa disciplina podemos ter mais que um projeto.
* **Projeto (N:N) Tecnologia:** Um projeto utiliza várias ferramentas; uma tecnologia é aplicada em diversos projetos.
* **Tecnologia (N:N) Competência:** O domínio de certas tecnologias alimenta competências específicas.
* **Docente (N:N) UC:** Uma unidade curricular pode ter mais que um professor e um professor pode dar mais que uma unidade curricular.
* **Formação (N:N) Tecnologias:** Cursos/Certificações oferecem conhecimento em novas tecnologias
* **TFCS (1:N) Áreas:** Um TFCS pode conter mais de uma área.
* **Docente (N:N) TFCS:** Um TFC pode conter ser orientado por mais que um docente, bem como, um docente pode orientar mais que um TFC.
* **TFCS (N:N) Tecnologias:** Um TFC pode conter mais que uma tecnologia, bem como, uma tecnologia pode estar em mais que um TFC.

## Modelação de Dados e Relações Versão 2 (Imagem `realacoesEntidadesV2`)
* **Projeto (1:N) Contribuidor:** Um projeto pode conter um ou mais contribudores 
* **TFCS (1:N) Contribuidor:** Um TFC pode conter um ou mais contribudores

---

## Atributos Entidades Versão 1 (Imagem `atributosEntidadesV1`)
* **Licenciatura:** Nome;Apresentação;Objetivos;NºSemestres;Formato;ECTS;Competências Adquiridas
* **Unidade Curricular:** Nome;Ano;Semetre;ECTS;Imagem
* **Docentes:** Nome;Foto;Página Pessoal
* **Projetos:** Titulo;Conceitos;Curso;Autor;Descrição;Imagem;Github;Video;  
* **Áreas:** Nome
* **Tecnologias:** Nome;Logo;WebSite;classificação;Descrição
* **TFCs:** Titulo;Palavras_chave;Autor;Curso;Imagem;Ano;Resumo;Destaque;Relatório;
* **Formações:** Titulo;Instituição;Ano Inicio;Ano Fim
* **Competências:** Nome;Descrição;Nivel
* **makingof:** Uso AI;DataRegisto;Fase;DescriçãoOpção;Decisões;Erros/Correções;Foto;    

## Atributos Entidades Versão 2 (Imagem `atributosEntidadesV2`)
* **Contribuidor:** Nome

---

## Justificação de Decisões de Modelação Versão 1

### Entidades Adicionais 
* **Decisão 1 (Imagem: `Decisao_1`) Criação da entidade "Docentes":**  Após ler o enunciado e verificar de uma forma geral conclui que , um uma unidade curricular pode ter mais que um professor e que um professor pode dar mais que uma unidade curricular, então para evitar repetições criei a entidade "Docentes" na qual permite-me associar múltiplos professores a uma UC, incluindo a sua foto e link para a página pessoal.  
* **Decisão 2 (Imagem: `Decisao_2`) Criação da entidade "Áreas":**  Após verificar o ficheiro **JSON** dos TFCs verifiquei que pode haver TFCs com as mesmas áreas então para evitar repetições de dados acabei por criar esta entidade para associar multiplas áreas a múltiplos TFCs.


## Justificação de Decisões de Modelação e Identificação de Entidades Versão 2
* **Decisão 3 (Imagem: `Decisao_3`) Criação da entidade "Contribuidor" e relação com projetos e TFCS:** Após alguma revisão da minha parte optei por criar a entidade 'Contribuidor' pois um projeto ou um TFC podem ter um ou mais contribudores , e esses mesmos contribudores podem estar presentes em vários projetos/TFCs esta ideia vêm do Linkedin (`ideiaContribuidor`) (Com esta decisão foi alterado a modelação entre entidades representação em imagem: `realacoesEntidadesV2`e `atributosEntidadesV2`)

* **Decisão 4 (Imagem: `Decisao_4`) Manter o atributo 'Autor' na entidade 'Projeto' e 'TFC': ** Optei por manter o campo Autor e a relação Contribuidores em separado para distinguir a autoria principal da colaboração secundária. O Autor é o dono do projeto, enquanto os Contribuidores são a equipa que auxiliou no desenvolvimento.
