# coding: utf8

from spacy.tokenizer import Tokenizer

# from spacy.vocab import Vocab
# import itertools
from spacy import load
import random
from uuid import uuid4

# Old stop_word removal step
# for content in doc:
#     filtered_sentence = ""
#     for word in area.split():
#         lexeme = nlp.vocab[word]
#         if not lexeme.is_stop:
#             filtered_sentence += f"{word} "
#     result.append(filtered_sentence.strip())


def generate_random_object(doc_areas, doc_habilidades):
    # Generate a spacy doc containing a random amount of
    # areas and habilidades on the same string
    # Instead of making a vector matching alg, just made it compare a string
    # with the whole content

    qtd = random.randint(1, len(doc_areas))
    areas = []
    habilidades = []
    for i in range(qtd):
        area = random.choice(doc_areas)
        habilidade = random.choice(doc_habilidades)
        if area not in areas:
            areas.append(area)
        if habilidade not in habilidades:
            habilidades.append(habilidade)
    areas.extend(habilidades)
    return nlp(" ".join(areas))


def remove_stopwords_and_create_doc(_list):
    result = []
    docs = [nlp(item) for item in _list]
    for item in docs:
        sentence = []
        for token in item:
            if token.text in nlp.Defaults.stop_words:
                continue
            sentence.append(token.text)
        result.append(" ".join(sentence))
    return result

# Loading large portuguese model
nlp = load("pt_core_news_lg")

# Appending custom set of stop_words
stop_words = set(
    """
    de a o que e do da em um para é com não uma os no se na por mais as dos como mas foi ao ele das tem à
    seu sua ou ser quando muito há nos já está eu também só pelo pela até isso ela entre era depois sem mesmo
    aos ter seus quem nas me esse eles estão você tinha foram essa num nem suas meu às minha têm numa pelos
    elas havia seja qual será nós tenho lhe deles essas esses pelas este fosse dele tu te vocês vos lhes meus minhas
    teu tua teus tuas nosso nossa nossos nossas dela delas esta estes estas aquele aquela aqueles aquelas isto aquilo
    estou está estamos estão estive esteve estivemos estiverames tava estávamos estavames tivera estivéramos esteja
    """.split()
)

# Some definitions
areas = [
    "Análise de Algoritmos e Complexidade de Computação",
    "Programação de Computadores",
    "Engenharia de Software",
    "Banco de Dados",
    "Sistemas de Informação",
    "Hardware",
    "Inteligência Artificial",
    "Interação Humano Computador",
    "Sistemas Operacionais",
    "Computação Gráfica",
    "Redes de Computadores",
    "Segurança",
    "Solos",
    "Fitossanidade",
    "Fitotecnia",
    "Floricultura, Parques e Jardins",
    "Engenharia Rural",
    "Economia, administração e extensão rural",
    "Ecologia dos Animais",
    "Genética, Melhoramento e Reprodução Animal",
    "Nutrição e Alimentação",
    "Pastagem e Forragicultura",
    "Produção Animal",
]

habilidades = [
    "Visual Studio Code",
    "Frontend",
    "Python",
    "Django",
    "Java",
    "C",
    "Javascript",
    "Typescript",
    "React",
    "Elixir",
    "PostgreSQL",
]

# add stop words
nlp.Defaults.stop_words |= stop_words

# Create a list containing doc objects and removing stop_words
doc_areas = remove_stopwords_and_create_doc(areas)
doc_habilidades = remove_stopwords_and_create_doc(habilidades)

# Generate random content for the position
vaga = generate_random_object(doc_areas, doc_habilidades)

pessoas = []

# Generate random amount of candidates and its contents
qtd_pessoas = random.randint(5, 20)
for i in range(qtd_pessoas):
    obj = {"string": generate_random_object(doc_areas, doc_habilidades)}
    obj["id"] = uuid4()
    pessoas.append(obj)


# Create a similarities dict to add a pessoa uuid as key and the similarity 
# with the position as value
similarities = {}
for pessoa in pessoas:
    pessoa_id, string = pessoa["id"], pessoa["string"]
    similarities[pessoa_id] = vaga.similarity(string)

print(similarities)