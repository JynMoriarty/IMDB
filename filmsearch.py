import streamlit as st
import pymongo
from streamlit_extras.no_default_selectbox import selectbox
import numpy as np
client = pymongo.MongoClient("mongodb://localhost:27017/")
movies = client.Scraping.Movies


a = movies.find()
all_titles = ['']
genr = ['']
actors = ['']
scor = ['']
float=np.arange(8,9.2,0.1)
scor = ['8.0' , '8.1', '8.2', '8.3', '8.4', '8.5', '8.6', '8.7', '8.8', '8.9', '9.0' ,'9.1','9.2']
for elt in a :
    all_titles.append(elt['title'])
    if elt['genre'] not in genr :
        genr.append(elt['genre'])
    if elt['acteurs'][0] not in actors:
        actors.append(elt['acteurs'][0])

Questions = ['Question 1 : Quel est le film le plus long ?','Question 2 : Quels sont les 5 films les mieux notés ?','Question 3 : Dans combien de films a joué Morgan Freeman ? Tom Cruise ?','Question 4 : Quels sont les 3 meilleurs films d’horreur ? Dramatique ? Comique ?','Question 5 : Parmi les 100 films les mieux notés, quel pourcentage sont américains ? Français ?','Question 6 : Quel est la durée moyenne d’un film en fonction du genre ?']

# brief = st.selectbox('Brief',Questions)
# if brief :


title = st.selectbox('Top 250 des FOAT',all_titles, format_func=lambda x:'Entrez un titre de film' if x == '' else x)
genre = st.selectbox('Choissisez un genre ',genr)
acteur = st.selectbox('Choissisez un acteur/des acteurs',actors)

query ={}
   
   
if title :
    query['title'] = title
    results = movies.find(query)

    i=0



    for result in results:
        link = movies.find({'genre': result['genre']}).sort('score',-1).limit(6)
        

        st.write(result['title'])
        st.image(result['image'], width = 400) 
        st.write(result['genre'])
        """DESCRIPTION : """
        st.write(result['description'])
        var = result['title']

        st.write('Film à voir : ')
        
        cols = st.columns(5)

        for elt in link :

            if var != elt['title']:
                
                cols[i] : st.write(str(i+1)+'.'+ elt['title']+ '('+str(elt['score'])+')')
                cols[i].image(elt['image'],use_column_width=True)
                i+=1
    

elif genre :


    query['genre'] = genre
    results = movies.find(query).sort('score',-1)
   
    

    st.write("Results:")

    for result in results:
        
        

        st.write(result['title']+ '(' + str(result['score'])+')')
        st.image(result['image'], width = 400) 
        """DESCRIPTION : """
        st.write(result['description'])
elif acteur:
    query['acteurs'] = acteur
    results = movies.find({'acteurs': acteur}).sort('score',-1)
   


    st.write("Results:")

    for result in results:
        
        

        st.write(result['title'] + 'genre : '+ str(result['genre']) + ' (' + str(result['score']) + ')'  )
        st.image(result['image'], width = 400) 
        
        """DESCRIPTION : """
  
        st.write(result['description'])



# score= st.select_slider('Choissisez le score du film', scor)
# if query['title'] not in all_titles:
    #     query = {}
    # if genre:
    #     query["genre"] = genre
    #     if query["genre"] not in genr:
    #         query = {}
    #     else :
    #         query['acteurs'] = acteur

 # if title == 'Entrez un titre de film' :
    #     query['score']= score
    # else :




                



