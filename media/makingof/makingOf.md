# Diário de Bordo: Making Of - Portfólio Pessoal

Este documento regista o processo de conceção, modelação e tomada de decisão para a aplicação de Portfólio Académico desenvolvida em Django.

---

## Registos do Trabalho em Papel
*Os registos visuais de suporte a este documento (fotografias do caderno e esquemas) encontram-se na pasta `/media/makingof/` do repositório.*

### 1. Identificação de Entidades e Atributos Versão 1 (Imagem `Modelacao/entidadesV1`)
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

## Modelação de Dados e Relações Versão 1 (Imagem `Modelacao/realacoesEntidadesV1`)

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

## Modelação de Dados e Relações Versão 2 (Imagem `Modelacao/realacoesEntidadesV2`)
* **Projeto (1:N) Contribuidor:** Um projeto pode conter um ou mais contribudores 
* **TFCS (1:N) Contribuidor:** Um TFC pode conter um ou mais contribudores

---

## Atributos Entidades Versão 1 (Imagem `Modelacao/atributosEntidadesV1`)
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

## Atributos Entidades Versão 2 (Imagem `Modelacao/atributosEntidadesV2`)
* **Contribuidor:** Nome

---

## Justificação de Decisões de Modelação 
## ⚖️ Justificações das Decisões de Modelação (Mínimo 2 por Entidade)

### 1. Licenciatura
* **Decisão:** Inclusão do atributo `ECTS`.
    * **Justificação:** Após analisar o site da lusofona decidi inserir os ECTS do Curso.
* **Decisão:** Atributo `Formato` (Presencial/Híbrido).
    * **Justificação:** Contextualiza o regime de ensino.

### 2. Unidade Curricular (UC)
* **Decisão:** Atributo `Ano`.
    * **Justificação:** Essencial para organizar a cronologia do curso.
* **Decisão:** Atributos  e `Semestre`.
    * **Justificação:** Essencial para organizar a cronologia do curso.

### 3. Docentes (Entidade Adicional)
* **Decisão:** Criação de entidade independente (em vez de texto na UC).
    * **Justificação:** Evita redundância de dados (Normalização), permitindo atualizar os dados de um docente (como a foto ou link) em apenas um local, afetando todas as UCs associadas.
* **Decisão:** Link para a `Página Pessoal(Link do Linkedin)`.
    * **Justificação:** Estabelece credibilidade ao docente na qual os recrutadores possam ver os docentes por detrás do ensino de uma determinada UC.

### 4. Projetos
* **Decisão:** Atributo `Conceitos`.
    * **Justificação:** Complemento sobre o aprendizado ao longo do projeto.
* **Decisão:** Atributos `Github` e `Video`.
    * **Justificação:** São as provas materiais de competência técnica que complementam a documentação do projeto.

### 5. Tecnologias
* **Decisão:** Atributo `Classificação/Nível`.
    * **Justificação:** Permite distinguir ferramentas que domino bem como as que não domino tanto.
* **Decisão:** Relação `ManyToMany` com Projetos e TFCs.
    * **Justificação:** Cria um sistema de filtros dinâmico: ao clicar numa tecnologia (ex: Django), o site mostra automaticamente todos os trabalhos onde essa ferramenta foi aplicada.

### 6. TFCs
* **Decisão:** Atributo `Destaque` (Booleano).
    * **Justificação:** Permite controlar a visibilidade na Homepage, para garantir que o trabalho de maior relevância tenha mais visibilidade.
* **Decisão:** Atributo `Palavras-chave`.
    * **Justificação:** Melhora a organização por temas e facilita a pesquisa rápida por áreas de especialização.

### 7. Formações
* **Decisão:** Atributos `Ano Início` e `Ano Fim`.
    * **Justificação:** Permite gerar uma linha do tempo profissional clara, distinguindo o percurso académico atual de formações complementares anteriores.
* **Decisão:** Relação com `Tecnologias`.
    * **Justificação:** Complementa a informação acerca de uma formação em especifico para mostrar as tecnologias que foram adquiridas.

### 8. Competências
* **Decisão:** Atributo `Nível`.
    * **Justificação:** Serve para quantificar as minhas competências.
* **Decisão:** Separação entre  `Descrição`.
    * **Justificação:** A descrição permite detalhar.

### 9. Áreas (Entidade Adicional)
* **Decisão:** Criação de entidade separada para `Áreas`.
    * **Justificação:** Permite agrupar os projetos/TFCs por áreas.
* **Decisão:** Relação `1:N` com TFCs.
    * **Justificação:** Organiza os trabalhos finais por domínios de especialização.

### 10. Contribuidor (Entidade Adicional - Versão 2)
* **Decisão:** Criação da entidade `Contribuidor`.
    * **Justificação:** Permite apresentar a equipa por detrás do trabalho associando pessoas e dar credibilidade ás pessoas envolvidas.
* **Decisão:** Distinção entre `Autor` e `Contribuidor`.
    * **Justificação:** Separa a responsabilidade principal  da colaboração técnica.

### 11. Making Of (Obrigatório)
* **Decisão:** Atributo `Uso AI`.
    * **Justificação:** Serve para documentar como as ferramentas de IA auxiliaram na estruturação e no desenvolvimento do projeto.
* **Decisão:** Atributo `Erros/Correções`.
    * **Justificação:** Serve para demonstrar erros e correções sobre os erros ao longo do desenvolvimento do projeto.


## Ajustes na modelação bem como as suas decisões 

### Versão 1
* **Decisão 1 (Imagem: `Decisoes/Decisao_1`) Criação da entidade "Docentes":**  Após ler o enunciado e verificar de uma forma geral conclui que , um uma unidade curricular pode ter mais que um professor e que um professor pode dar mais que uma unidade curricular, então para evitar repetições criei a entidade "Docentes" na qual permite-me associar múltiplos professores a uma UC, incluindo a sua foto e link para a página pessoal.  
* **Decisão 2 (Imagem: `Decisoes/Decisao_2`) Criação da entidade "Áreas":**  Após verificar o ficheiro **JSON** dos TFCs verifiquei que pode haver TFCs com as mesmas áreas então para evitar repetições de dados acabei por criar esta entidade para associar multiplas áreas a múltiplos TFCs.


### Versão 2
* **Decisão 3 (Imagem: `Decisoes/Decisao_3`) Criação da entidade "Contribuidor" e relação com projetos e TFCS:** Após alguma revisão da minha parte optei por criar a entidade 'Contribuidor' pois um projeto ou um TFC podem ter um ou mais contribudores , e esses mesmos contribudores podem estar presentes em vários projetos/TFCs esta ideia vêm do Linkedin (`Ideias/ideiaContribuidor`) (Com esta decisão foi alterado a modelação entre entidades representação em imagem: `Modelacao/realacoesEntidadesV2`e `Modelacao/atributosEntidadesV2`)

* **Decisão 4 (Imagem: `Decisoes/Decisao_4`) Manter o atributo 'Autor' na entidade 'Projeto' e 'TFC': ** Optei por manter o campo Autor e a relação Contribuidores em separado para distinguir a autoria principal da colaboração secundária. O Autor é o dono do projeto, enquanto os Contribuidores são a equipa que auxiliou no desenvolvimento.
