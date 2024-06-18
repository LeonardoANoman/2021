import bs4 as bs
import urllib.request
import nltk
import spacy
nltk.download("rslp")
from spacy.matcher import PhraseMatcher
from IPython.core.display import HTML
from spacy.lang.pt.stop_words import STOP_WORDS
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud
import matplotlib.pyplot as plt

pln = spacy.load("pt")

documento = pln("Estou aprendendo rpocessamento de linguagem natural, em Curitiba")

for token in documento:
    print(token.text, token.pos_)

for token in documento:
    print(token.text, token.lemma_)

doc = pln("encontrei encontraram encontrarão encontrariam cursando curso crusei")
[token.lemma_ for token in doc]

stemmer = nltk.stem.RSLPStemmer()
stemmer.stem("aprender")

for token in documento:
  print(token.text, token.lemma_, stemmer.stem(token.text))

dados = urllib.request.urlopen('https://pt.wikipedia.org/wiki/Intelig%C3%AAncia_artificial')

dados = dados.read()

dados_html = bs.BeautifulSoup(dados, 'lxml')

paragrafos = dados_html.find_all('p')
len(paragrafos)

conteudo = ''
for p in paragrafos:
  conteudo += p.text

conteudo.lower()

pln = spacy.load('pt')

string = 'turing'
token_pesquisa = pln(string)


matcher = PhraseMatcher(pln.vocab)
matcher.add('SEARCH', None, token_pesquisa)

doc = pln(conteudo)
matches = matcher(doc)
texto = ''
numero_palavras = 50
doc = pln(conteudo)
matches = matcher(doc)

display(HTML(f'<h1>{string.upper()}</h1>'))
display(HTML(f"""<p><strong>Resultados encontrados:</strong> {len(matches)}</p>"""))
for i in matches:
  inicio = i[1] - numero_palavras
  if inicio < 0:
    inicio = 0
  texto += str(doc[inicio:i[2] + numero_palavras]).replace(string, f"<mark>{string}</mark>")
  texto += "<br /><br />"
display(HTML(f"""... {texto} ... """))

print(STOP_WORDS)
len(STOP_WORDS)

doc = pln(conteudo)
lista_token = []
for token in doc:
  lista_token.append(token.text)

print(lista_token)

sem_stop = []
for palavra in lista_token:
  if pln.vocab[palavra].is_stop == False:
    sem_stop.append(palavra)

print(sem_stop)

color_map = ListedColormap(['orange', 'green', 'red', 'magenta'])

cloud = WordCloud(background_color = 'white', max_words = 100, colormap=color_map)

cloud = cloud.generate(' '.join(sem_stop))
plt.figure(figsize=(15,15))
plt.imshow(cloud)
plt.axis('off')
plt.show()