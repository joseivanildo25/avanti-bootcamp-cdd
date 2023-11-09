#!/usr/bin/env python
# coding: utf-8

# In[49]:


import pandas as pd
import seaborn as sns


# In[50]:


df = sns.load_dataset('tips')


# In[51]:


df


# In[24]:


## Dicionário de dados ##


# In[46]:


df_dict = pd.DataFrame([
    {
    "variavel": "total_bill",
    "descricao": "total da conta",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    },
    {
    "variavel": "tip",
    "descricao": "gorgeta",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    },
    {
    "variavel": "sex",
    "descricao": "sexo",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "smoker",
    "descricao": "fumante",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "day",
    "descricao": "dia da semana",
    "tipo": "qualitativa",
    "subtipo": "ordinal"
    },
    {
    "variavel": "time",
    "descricao": "hora do pagamento",
    "tipo": "qualitativa",
    "subtipo": "ordinal"
    },
    {
    "variavel": "size",
    "descricao": "capacidade da mesa",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    }
]
)

df_dict


# In[25]:


## Estatística dos dados ##


# In[30]:


df_dict.query('tipo == "qualitativa"').variavel.to_list()


# In[31]:


df[['sex', 'smoker', 'day', 'time']].mode()


# In[32]:


df_dict.query('tipo == "quantitativa"').variavel.to_list()


# In[35]:


df.describe()


# In[ ]:


## descrição das variáveis qualitativa ##


# In[45]:


qualitative_vars = ['sex', 'smoker', 'day', 'time']

for variavel in qualitative_vars:
    valores_unicos = df[variavel].unique()
    for valor in valores_unicos:
        print(f"{variavel} - {valor}")
        subamostra = df[df[variavel] == valor]
        display(subamostra.describe())
        print("="*100)


# In[53]:


## Segundo conjunto de dados ##


# In[ ]:


ti = sns.load_dataset('titanic')


# In[52]:


ti


# In[ ]:


## Dicionário de dados ##


# In[62]:


ti_dict = pd.DataFrame([
    {
    "variavel": "survived",
    "descricao": "sobrevivente?",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    },
    {
    "variavel": "pclass",
    "descricao": "classe do passageiro",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    },
    {
    "variavel": "sex",
    "descricao": "sexo",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "age",
    "descricao": "idade",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    },
    {
    "variavel": "sibisp",
    "descricao": "numero de irmão/conjuges a bordo",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    },
    {
    "variavel": "parch",
    "descricao": "numero de pais/filhos a bordo",
    "tipo": "quantitativa",
    "subtipo": "discreta"
    },
    {
    "variavel": "fare",
    "descricao": "tarifa paga",
    "tipo": "quantitativa",
    "subtipo": "continua"
    },
    {
    "variavel": "embarked",
    "descricao": "onde embarcou?",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "class",
    "descricao": "classe do passageiro",
    "tipo": "qualitativa",
    "subtipo": "ordinal"
    },
    {
    "variavel": "who",
    "descricao": "homem ou mulher",
    "tipo": "qualitativa",
    "subtipo": "nomial"
    },
    {
    "variavel": "adult_male",
    "descricao": "homem adulto?",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "deck",
    "descricao": "area",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "embark_town",
    "descricao": "onde embarcou",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "alive",
    "descricao": "vivo?",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    },
    {
    "variavel": "alone",
    "descricao": "sozinho?",
    "tipo": "qualitativa",
    "subtipo": "nominal"
    }
]
)

ti_dict


# In[ ]:


## Estatística dos dados ##


# In[63]:


ti_dict.query('tipo == "qualitativa"').variavel.to_list()


# In[64]:


ti[['sex',
 'embarked',
 'class',
 'who',
 'adult_male',
 'deck',
 'embark_town',
 'alive',
 'alone']].mode()


# In[65]:


ti_dict.query('tipo == "quantitativa"').variavel.to_list()


# In[66]:


ti.describe()


# In[ ]:


## descrição das variáveis qualitativa ##


# In[68]:


qualitative_vars = ['sex',
 'embarked',
 'class',
 'who',
 'adult_male',
 'deck',
 'embark_town',
 'alive',
 'alone']

for variavel in qualitative_vars:
    valores_unicos = ti[variavel].unique()
    for valor in valores_unicos:
        print(f"{variavel} - {valor}")
        subamostra = ti[ti[variavel] == valor]
        display(subamostra.describe())
        print("="*100)


# In[ ]:




