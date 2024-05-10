#!/usr/bin/env python
# coding: utf-8
# %% [markdown]
# ¡Hola!
# 
# Mi nombre es Tonatiuh Cruz. Me complace revisar tu proyecto hoy.
# 
# Al identificar cualquier error inicialmente, simplemente los destacaré. Te animo a localizar y abordar los problemas de forma independiente como parte de tu preparación para un rol como data-scientist. En un entorno profesional, tu líder de equipo seguiría un enfoque similar. Si encuentras la tarea desafiante, proporcionaré una pista más específica en la próxima iteración.
# 
# Encontrarás mis comentarios a continuación - **por favor no los muevas, modifiques o elimines**.
# 
# Puedes encontrar mis comentarios en cajas verdes, amarillas o rojas como esta:
# 
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Éxito. Todo está hecho correctamente.
# </div>
# 
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Observaciones. Algunas recomendaciones.
# </div>
# 
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Necesita corrección. El bloque requiere algunas correcciones. El trabajo no puede ser aceptado con comentarios en rojo.
# </div>
# 
# Puedes responderme utilizando esto:
# 
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante.</b> <a class="tocSkip"></a>

# # ¿Cuál es la mejor tarifa?
# 
# Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
# Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.

# ## Observaciones del proyecto.
# - Trabajar con la tabla plans para calcular la tarifa que le corresponde a cada usuarios. Estaba haciendo los calculos sin la ayuda de la tabla.
# - Redondear el consumo de gb hacia arriba; como lo hice con los minutos en llamadas
# - Donde usé el método groupby, usar el método pivot_table. Con el fin de ponerlo en practica y no se me olvidey corroborar la que la información calculada sea la misma tanto con groupby como con pivot_table.
# - Hacer la graficas con librerias seaborn (sns) y pandas (pd)
# - Corroborar que SI una los 4 dataframes agrupados calculados con las tablas.
# - Usar el método pivot_table. No usar gorupby ni agg, por ahora.
# - Declarar la unión de las tablas como merged_part1, merged_part2 & full_merged

# %%[markdown]
# ## Inicialización

# %%[markdown]

# Carga las librerías
import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
from scipy import stats as st
# Las liberías necesarias y que podría considerar para este proyecto.

# %%[markdown]
# ## Cargar datos

# %%[markdown]

# Carga los archivos de datos en diferentes DataFrames
calls = pd.read_csv('./megaline_calls.csv')
internet = pd.read_csv('./megaline_internet.csv')
messagges = pd.read_csv('./megaline_messages.csv')
plans = pd.read_csv('./megaline_plans.csv')
users = pd.read_csv('./megaline_users.csv')

# %%[markdown]
# Se cargaron las 5 tablas necesarias para llevar a acabo este proyecto.

# ## Preparar los datos

# [Los datos para este proyecto se dividen en varias tablas. Explora cada una para tener una comprensión inicial de los datos. Si es necesario, haz las correcciones requeridas en cada tabla.]

# ### Vizualación de los 5 tablas para asegurarnos que se cargaron correctamente y como están elaboradas.

# In[4]:


calls.head()


# In[5]:


internet.head()


# In[6]:


messagges.head()


# In[7]:


plans.head()


# In[8]:


users.head()

# %%[markdown]
# ### Calculamos la dimensión de las 5 tablas.
# Obervamos que no tiene valores nulos, por lo que no es necesario aplicar ningún método para tratar con valores nulos.

# In[9]:


calls.info()


# In[10]:


internet.info()


# In[11]:


messagges.info()


# In[12]:


plans.info()


# In[13]:


users.info()


# ### Filas duplicadas
# Calculamos en esta sección si en algunas de las tablas hay filas duplicadas. No hay ninguna fila duplicada con le que hay que lidiar.

# In[14]:


calls[calls.duplicated()]


# In[15]:


internet[internet.duplicated()]


# In[16]:


messagges[messagges.duplicated()]


# In[17]:


plans[plans.duplicated()]


# In[18]:


users[users.duplicated()]


# En esta sección se validaron que los datos se hayan cargado corectamente. Obervamos cuál es el cooumen de cada tabalas y lso valores no nulos que tiene. Al igual que los valores duplicados. El nombre de las columnas también parecen estar con un buen formato

# ## Tarifas

# %%[markdown]

# Imprime la información general/resumida sobre el DataFrame de las tarifas
plans.info()


# %%[markdown]


# Imprime una muestra de los datos para las tarifas
plans.sample()


# In[21]:


plans


# La tablas `plans` tiene una dimensión de 8 columnas x 2 filas, de las cuales no tienen ningún valor nulo. SIn embargo, podemo decir que si hay valores no adecuados, ya que  Megaline redondea los megabytes a gigabytes, y tenenos una columna, que es `mb_per_month_included` la cantidad de mb mensual que tienen los dos planes.  Por lo tanto se puede crear una columna llamada `gb_per_month_included` que muestra al conversión.

# ## Corregir datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[22]:


plans['gb_per_month_included'] = plans['mb_per_month_included'] / 1_024


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buen trabajo!! Es correcto considerar que 1024 megabytes son 1 gigabytes.
#     
# </div>

# <div class="alert alert-block alert-warning">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# 
# Te recomiendo usar la función de math.ceil() cuando redondeamos hacia arriba lo valores, dado que si lo que hacemos es transformalos a int solamente eliminamos la parte decimal y para este ejercicio debemos hacer el redondeo superior dado que se cobra el costo extra en cuanto se pasa de los límites.. 
# </div>

# In[23]:


plans


# Hicimos la conversión de megabytes a gigabytes

# ## Enriquecer los datos

# Lo que puede ser de mucha utilidad y que la tabla sea un poco mas específica es pasar la la columna `plan_name` como índice
#     y eliminar la la columna `mb_per_month_included` ya que ya no es necesaria. Al final solo me decidí por eliminar la columna `mb_per_month_included` y no pasar plan_name como índice. Debido a que puede hacerme util para unir dataframes si es necesario.

# In[24]:


#plans = plans.set_index('plan_name')
plans = plans.drop(columns=['mb_per_month_included'])


# In[25]:


plans


# ## Usuarios/as

# In[26]:


# Imprime la información general/resumida sobre el DataFrame de usuarios
users.info()


# In[27]:


# Imprime una muestra de datos para usuarios

users.sample(5)


# In[28]:


# users['churn_date'].value_counts(dropna=False)


# In[29]:


nan_values_churn_date = users['churn_date'].isna().sum()
f'Hay {nan_values_churn_date} en la columna churn_date'


# [Describe lo que ves y observas en la información general y en la muestra de datos impresa para el precio de datos anterior. ¿Hay algún problema (tipos de datos no adecuados, datos ausentes, etc.) que pudieran necesitar investigación y cambios adicionales? ¿Cómo se puede arreglar?]

# El df de `users` tiene una dimensión de 8 columnas x 500 filas. La única columna que tiene valores nulos es `churn_date` con 466; si el valor es ausente, la tarifa se estaba usando cuando fue extraída esta base de datos. La mayoría de las columnas son objetos y dos ellos, `reg_date` y `churn_date`, se pueden pasar a formato de fecha.

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[30]:


#users['churn_date'] = users['churn_date'].fillna(pd.NaT)


# In[31]:


users['reg_date'] = pd.to_datetime(users['reg_date'])
users['churn_date'] = pd.to_datetime(users['churn_date'],errors='coerce')


# <div class="alert alert-block alert-warning">
# <b>Comentario Revisor</b> <a class="tocSkip"></a>
# 
# En todos los casos en los que cambiamos el tipo de variable a datetime, te recomiendo agregar el argumento "format='%Y-%m-%d'" dentro de la función to_datetime(). De esta manera, puedes asegurarte siempre de que el formato de la fecha que deseas cambiar sea el que necesitas.
# </div>

# In[32]:


users.info()


# Para pasar a formato fecha en las dos columnas ya anteriormente mencionadas, primero tuve que convertir los valors NaN a NaT (not a time) con el método `fillna` y `atributo pd.NaT`.
# Nuavemente consulté la información general del df.

# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[33]:


users['full_name'] = users['first_name'] + ' ' + users['last_name']


# In[34]:


users = users.drop(columns='churn_date')


# In[35]:


users.sample(5)


# Lo que se me ocurrió a agregar es una columna que muestre el nombre completo y eliminar la columns `churn_date`.
# En todo los demás me parece que no es necesario hacer ningún otro cambio.

# <div class="alert alert-block alert-warning">
# <b>Comentario Revisor</b> <a class="tocSkip"></a>
# 
# Muy buena conclusión, pero a manera de complementar el análisis qué podríamos decir de los registros que no tienen valores en la variable churn_date?
# </div>

# ## Llamadas

# In[36]:


# Imprime la información general/resumida sobre el DataFrame de las llamadas
calls.info()


# In[37]:


# Imprime una muestra de datos para las llamadas
calls.sample(20,random_state=7659)


# <font color='blue'>
# Viendo la información general, no hay valores nulos. Sin embargo; observé que se registraron llamadas con una duración de 0.00 segundos. Usuarios colgaron a la velocidad de la luz justo en el momento en el que empezó el cronómetro de la llamada ¿Se cobran o no se cobran? Como es un registró tomaré que sí se cobran. Adicional, es algo que se debería aclarar con la empresa, bueno es no es nuestro análisis.
# Otro dato curioso que note es que el id de la llamada es un objeto debido al gión bajo (_)
#     </font>

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[38]:


#Redondeo hacia arriba
calls['duration'] = np.ceil(calls['duration'])


# In[39]:


#Sustuir lo valores 0 con 1
calls['duration'] = calls['duration'].where(~(calls['duration'] == 0),1)


# In[40]:


#Pasar a entero la columna duration
calls['duration'] = calls['duration'].astype('int')


# In[41]:


#Cambiar el formato a datetime la columna call_date
calls['call_date'] = pd.to_datetime(calls['call_date'])


# In[42]:


calls.sample(20,random_state=7659)


# In[43]:


calls.info()


# <font color='blue'>
# En la columna *duration*, para cambiar el valor de flotante a entero, se redonde hacia arriba los decimales y se sustituyeron los valores de 0 a 1.
# Posteriormente, cambié el formato fecha la columna *call_date*.
# Finalmente, corroboré nuevamente la información general para observar los cambios mencionados.
#     </font>

# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[44]:


#Dividimos el id para solo tener el numerod de la derecha
new_id = calls['id'].str.split('_', expand=True).rename(columns={1:'new_id'})['new_id']


# In[45]:


#Creo una nueva columna en calls
calls['id_call'] = new_id


# In[46]:


calls['id_call'] = calls['id_call'].astype('int')


# In[47]:


calls.info()


# In[48]:


#Funcion quitar el user_id y _
def split_id(data,column_name=''):
    return data.str.split('_', expand=True).rename(columns={1:column_name})[column_name]


# <font color='blue'>
# Lo que hice para poder enriquecer los datos es dividir el id de llamada. La fórmula para crear el id es: user_id + '_' + id_call. Aqui creamos una columna donde solo tenga el número que está después del guión bajo. La columna se llama id_call y no borramos la original; id. Además la columna id_call podemos convertirla a entero.
# Una observación es que esto debemos hacerlo en todo los dataframes, que tenga el id de esa forma asi que vamos a crear una función llamada split_id.
#     </font>

# ## Mensajes

# In[49]:


# Imprime la información general/resumida sobre el DataFrame de los mensajes
messagges.info()


# In[50]:


# Imprime una muestra de datos para los mensajes
messagges.sample(20,random_state=67598)


# <font color='blue'>
# La información es parecida a los dataframes anteriores. Hay una columna que se puede convertir en formato de fecha y crear una columna para el nuevo id de los mensajes.
#     </font>

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[51]:


messagges['message_date'] = pd.to_datetime(messagges['message_date'])


# In[52]:


messagges.sample(20,random_state=67598)


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[53]:


messagges['id_messagges'] = split_id(messagges['id'])
messagges['id_messagges'] = messagges['id_messagges'].astype('int')


# In[54]:


messagges.sample(5,random_state=67598)


# In[55]:


messagges.info()


# <font color='blue'>
# Como mencioné en un puntos anteriores, podemos crear una columna para tener un id mas claro. el nuevo id de mensajes es id_messages
#     </font>

# ## Internet

# In[56]:


# Imprime la información general/resumida sobre el DataFrame de internet
internet.info()


# In[57]:


# Imprime una muestra de datos para el tráfico de internet
internet.sample(12,random_state=76569)


# <font color='blue'>
# En este df, lo único considerable es crea el nuevo id sin el guión bajo, cambiar el formato fecha, y hacer la conversión de Megas a Gigas
#     </font>

# ### Corregir los datos

# [Corrige los problemas obvios con los datos basándote en las observaciones iniciales.]

# In[58]:


internet['session_date'] = pd.to_datetime(internet['session_date'])
internet['gb_used'] = internet['mb_used'] / 1_024
internet['id_internet'] = split_id(internet['id'])
internet['id_internet'] = internet['id_internet'].astype('int')


# In[59]:


internet.sample(12)


# ### Enriquecer los datos

# [Agrega factores adicionales a los datos si crees que pudieran ser útiles.]

# In[60]:


internet.info()


# <font color='blue'>
# Corroboramos la información general para asegurarnos de los cambios establecidos
#     </font>

# ## Estudiar las condiciones de las tarifas

# [Es sumamente importante entender cómo funcionan las tarifas, cómo se les cobra a los usuarios en función de su plan de suscripción. Así que te sugerimos imprimir la información de la tarifa para ver una vez más sus condiciones.]

# In[61]:


# Imprime las condiciones de la tarifa y asegúrate de que te quedan claras
plans


# <font color='blue'>
# La tabla plans (datos sobre las tarifas):
#  
# plan_name: nombre de la tarifa.
# usd_monthly_pay: pago mensual en dólares estadounidenses.
# minutes_included: minutos incluidos al mes (calls).
# messages_included: SMS incluidos al mes.
# gb_per_month_included: datos incluidos al mes (en gigabytes).
# usd_per_minute: precio por minuto tras exceder los límites del paquete (por ejemplo, si el paquete incluye 100 minutos, el operador cobrará el minuto 101).
# usd_per_message: precio por SMS tras exceder los límites del paquete.
# usd_per_gb: precio por gigabyte de los datos extra tras exceder los límites del paquete (1 GB = 1024 megabytes).
#     </font>

# ## Agregar datos por usuario
# 
# [Ahora que los datos están limpios, agrega los datos por usuario y por periodo para que solo haya un registro por usuario y por periodo. Esto facilitará mucho el análisis posterior.]

# In[62]:


# Calcula el número de llamadas hechas por cada usuario al mes. Guarda el resultado.
calls['month'] = calls['call_date'].dt.month #Extraer el mes de la columna call_date
# #con el método group_by
# grp_calls = calls.groupby(['user_id','call_date_month'])
# calls_per_user = grp_calls.count()[['id_call']].sort_values(by='id_call',ascending=False)
# calls_per_user
#con el método pivot_table
calls_per_user = pd.pivot_table(calls, values='id_call', 
               index=['user_id','month'], 
                aggfunc='count').sort_values(by='id_call',ascending=False).reset_index()
calls_per_user


# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
# Muy buen trabajo!! la función de pivot_table() es muy recomendable para hacer los códigos más eficientes.
#     
# </div>

# In[63]:


#Corroborando que los métodos usados se hicieron para los calculos correctos.
mask = "user_id == 1329 and month == 12"
calls.query(mask)['id_call'].count()


# In[64]:


# Calcula la cantidad de minutos usados por cada usuario al mes. Guarda el resultado.
# #con el método groupby
# grp_user_month = calls.groupby(['user_id','call_date_month'])
# min_used_monthly_per_user = grp_user_month.sum()[['duration']].sort_values(by='duration',ascending=False)
# min_used_monthly_per_user
#con el método pivot_table
min_used_monthly_per_user = pd.pivot_table(calls, 
               values='duration', 
               index=['user_id','month'], 
               aggfunc='sum').sort_values(by='duration',ascending=False).reset_index()
min_used_monthly_per_user


# In[65]:


#Corroborando que los métodos se hicieron para los calculos correctos.
mask = '(user_id == 1329) and (month == 12)'
calls.query(mask)["duration"].sum()


# In[66]:


#Corroborando de otra forma mi resultado anterior con el user_id 1267 y el mes de diciembre (12)
mask = '(user_id == 1267) and (month == 12)'
f'El usuario 1267 gastó {calls.query(mask)["duration"].sum()} minutos en el mes de diciembre.'


# In[67]:


#Calcula la cantidad de minutos usados por cada usuario al mes y  el número de llamadas hechas por cada usuario al mes en una sola linea.
grp = calls.groupby(['user_id','month'])
agg_dict = {'id_call':'count','duration':'sum'}
grp.agg(agg_dict)


# Nota adiconal: Me percaté que los calculos anteriores los podría haber hecho con el método `agg` con solo dos líneas de código

# In[68]:


# Calcula el número de mensajes enviados por cada usuario al mes. Guarda el resultado.
messagges['month'] = messagges['message_date'].dt.month
#con el método groupby
# grp = messagges.groupby(['user_id','message_date_month'])
# sent_msg_monthly_per_user = grp.count()['id_messagges'].sort_values(ascending=False)
# sent_msg_monthly_per_user
#Con pivot_table.
sent_msg_monthly_per_user = pd.pivot_table(messagges,
               values='id_messagges',
               index=['user_id','month'],
               aggfunc='count').sort_values(by='id_messagges',ascending=False).reset_index()
sent_msg_monthly_per_user


# In[69]:


#Corroborar de otra forma si la información de la parte superior es correcta
mask = "user_id == 1052 and month == 12"
f'El usuario 1052 gastó {messagges.query(mask)["id_messagges"].count()} mensajes durante el mes de diciembre'


# In[70]:


#Corroborar de otra forma si la información de la parte superior es correcta
mask = "(user_id == 1381) and (month == 10 or month == 11)"
f'El usuario 1381 gastó {messagges.query(mask)["id_messagges"].count()} mensajes durante el mes de octubre y noviembre'


# In[71]:


# Calcula el volumen del tráfico de Internet usado por cada usuario al mes. Guarda el resultado.
internet['month'] = internet['session_date'].dt.month

# #con el método groupby
# grp = internet.groupby(['user_id','session_date_month'])
# traffic_monthly_per_user = grp.sum()['gb_used']
# traffic_monthly_per_user.sort_values(ascending=False)


#Antes de la agrupación establecer la condición de que si alguien usa 1025 mb, se le cobrará 2 gb
internet['gb_used'].where(~(internet['gb_used']==(1025/1024)),np.ceil(internet['gb_used']))


#con pivot_table
traffic_monthly_per_user = pd.pivot_table(internet,
               values='gb_used',
               index=['user_id','month'],
              aggfunc='sum').sort_values(by='gb_used',ascending=False).reset_index()
traffic_monthly_per_user


# In[72]:


#Corroborar la información de otra forma.
mask = "user_id == 1379 and month == 12"
internet.query(mask)['gb_used'].sum()


# ### Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month

# In[73]:


# Fusiona los datos de llamadas, minutos, mensajes e Internet con base en user_id y month

#CAMBIAR ESTA PARTE!!!!!
#calls_per_user
#min_used_monthly_per_user
#sent_msg_monthly_per_user
#traffic_monthly_per_user


# In[74]:


#Primero, se cambia el nombre de la columnas para que el nombre se relacione con los datos.
calls_per_user = calls_per_user.rename(columns={'id_call':'calls_amount'})
min_used_monthly_per_user = min_used_monthly_per_user.rename(columns={'duration':'calls_duration'})
sent_msg_monthly_per_user = sent_msg_monthly_per_user.rename(columns={'id_messagges':'messages_amount'})
traffic_monthly_per_user = traffic_monthly_per_user.rename(columns={'id_internet':'used_gb'})


# In[75]:


calls_per_user.sample(5,random_state=748537)


# In[76]:


min_used_monthly_per_user.sample(5,random_state=748537)


# In[77]:


sent_msg_monthly_per_user.sample(5,random_state=748537)


# In[78]:


traffic_monthly_per_user.sample(5,random_state=748537)


# In[79]:


#Union de los dataframes

# calls_per_user_df = calls_per_user_df.reset_index()
# traffic_msg_monthly_per_user = \
# pd.concat([traffic_monthly_per_user_df,sent_msg_monthly_per_user_df],axis=1).reset_index()

#pd.concat([calls_per_user,min_used_monthly_per_user],axis=1)

#calls_per_user.merge(min_used_monthly_per_user,on='user_id')


# #### Union parte 1.
# En esta parte se unieron los df's `calls_per_user` y `min_used_monthly_per_user`.

# In[80]:


merge_part_1 = calls_per_user.merge(min_used_monthly_per_user,on=['user_id','month'],how='left')


# In[81]:


merge_part_1


# In[82]:


#Corroborando lo información de le hecho en al posterior
mask="user_id == 1000 and month == 12"
merge_part_1.query(mask)


# #### Union parte 2.
# 
# En esta sección se unierion `sent_msg_monthly_per_user` y `traffic_monthly_per_user`.

# In[83]:


merge_part_2 = sent_msg_monthly_per_user.merge(traffic_monthly_per_user,
                                               on=['user_id','month'],
                                               how='left')


# In[84]:


merge_part_2


# #### Union parte 3.
# 
# Unión de los df's `merge_part_1` y `merge_part_2`

# In[85]:


merge_part_3 = merge_part_1.merge(merge_part_2,
                                  on=['user_id','month'],
                                 how='left')


# In[86]:


merge_part_3


# #### Union parte 4.
# 
# unión de `merge_part_3` y `users`.

# In[87]:


users = users[['user_id','first_name',
       'last_name','age',
       'city','plan',]]


# In[88]:


full_merge = merge_part_3.merge(users,on=['user_id'],how='left')


# <div class="alert alert-block alert-warning">
# 
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
# Hola, José!! El número mágico al que buscamos llegar es 2293 cuando hacemos el merge. Considero que estas perdiendo registrados dado que para hacer el merge, entonces cuando hagamos el merge consdiera la forma "outer".
# </div>

# In[89]:


full_merge


# In[90]:


#Corroborar la información anterior
mask = "user_id == 1310"
merge_part_1.query(mask)


# In[91]:


#Corroborar la información anterior
mask = "user_id == 1052 and month == 12"
print(sent_msg_monthly_per_user.query(mask))
print(traffic_monthly_per_user.query(mask))


# #### Tarifa

# In[92]:


# Añade la información de la tarifa
plans.info()


# In[93]:


plans.describe()


# In[94]:


plans


# In[95]:


plans.loc[1,'usd_monthly_pay']     


# In[96]:


# Calcula el ingreso mensual para cada usuario
def plans_fee(row):
    
    plan = row['plan']
    calls_duration = row ['calls_duration']
    messages_amount = row['messages_amount']
    gb_used = row['gb_used']
    
    total_calls_duration = 0
    total_messages_amount = 0
    total_gb_used = 0
    
    if plan == 'surf':
        
        if (calls_duration > plans.loc[0,'minutes_included']):
            total_calls_duration = (calls_duration - plans.loc[0,'minutes_included']) * plans.loc[0,'usd_per_minute']
            
        if (messages_amount > plans.loc[0,'messages_included']):
            total_messages_amount = (messages_amount - plans.loc[0,'messages_included']) * plans.loc[0,'usd_per_message']
            
        if (gb_used > plans.loc[0,'gb_per_month_included']):
            total_gb_used = (gb_used - plans.loc[0,'gb_per_month_included']) * plans.loc[0,'usd_per_gb']
            
        return total_calls_duration + total_messages_amount + total_gb_used + plans.loc[0,'usd_monthly_pay']
    
    
    else:
        
        
        if (calls_duration > plans.loc[1,'minutes_included']):
             total_calls_duration = (calls_duration - plans.loc[1,'minutes_included']) * plans.loc[1,'usd_per_minute']
                
        if (messages_amount > plans.loc[1,'messages_included']):
            total_messages_amount = (messages_amount - plans.loc[1,'messages_included']) * plans.loc[1,'usd_per_message']
            
        if (gb_used > plans.loc[1,'gb_per_month_included']):
            total_gb_used = (gb_used - plans.loc[1,'gb_per_month_included']) * plans.loc[1,'usd_per_gb']
            
        return total_calls_duration + total_messages_amount + total_gb_used  + plans.loc[1,'usd_monthly_pay']     


# In[97]:


#calls_internet_msg_plan['total_fee'] = calls_internet_msg_plan.apply(plans_fee,axis=1)


# In[98]:


#calls_internet_msg_plan[calls_internet_msg_plan['plan'] == 'ultimate'].sample(20)


# In[99]:


full_merge['total_fee'] = full_merge.apply(plans_fee,axis=1)


# In[100]:


full_merge


# ## Estudia el comportamiento de usuario

# ### Llamadas

# In[101]:


#Compara la duración promedio de llamadas por cada plan y por cada mes. Traza un gráfico de barras para visualizarla.


# In[102]:


pd.pivot_table(full_merge,
               values=['calls_duration'],
               index=['month'],columns=['plan'],
              aggfunc='mean')


# In[103]:


pd.pivot_table(full_merge,
               values=['calls_duration'],
               index=['month'],columns=['plan'],
              aggfunc='mean').plot(kind='bar',
                                  title='Duración promedio de llamadas por cada plan y por cada mes',
                                  ylabel='llamadas promedio',
                                  xlabel='mes',
                                  legend=True,
                                  figsize=(10,8))
plt.legend(['surf','ultimate'],loc='lower right')
plt.grid(True)
plt.show()


# Al parecer los usuarios no hacen más llamadas si tienen un plan premium. Se comportan casi de la misma forma los usuarios que tienen el plan surf y ultimate. El único mes destacable es febrero.

# In[104]:


# Calcula la media y la varianza de la duración mensual de llamadas.
#media de la duración mensual de llamdas
media_duration_calls_montly = full_merge['calls_duration'].sum()/len(full_merge['month'].unique())


# In[105]:


agg_dict = {'calls_duration':'mean'}
grp = full_merge.groupby('month')
print(grp.agg(agg_dict))
media_duration_calls_montly = grp.agg(agg_dict).mean()

print("\n\nLa media de la duración mensual de llamadas es: {result:.2f}\n\n"
                                                      .format(result = media_duration_calls_montly.mean()))

print("La varianza de la duración mensual de llamadas es {result:.2f}\n\n"
                                                      .format(result = np.var(grp.agg(agg_dict)['calls_duration'])))


print(grp.agg(agg_dict).describe())


# In[106]:


# Traza un diagrama de caja para visualizar la distribución de la duración mensual de llamadas
grp.agg(agg_dict).boxplot(vert=False,
                         figsize=(10,5))
plt.title('Distribución de la duración mensual de llamadas')
plt.show()


# In[107]:


calls_duration_mean_surf = pd.pivot_table(full_merge,
               values='calls_duration',
               index=['month'],columns=['plan'],
              aggfunc='mean')['surf']
calls_duration_mean_ultimate = pd.pivot_table(full_merge,
               values='calls_duration',
               index=['month'],columns=['plan'],
              aggfunc='mean')['ultimate']


# In[108]:


print(calls_duration_mean_surf,'\n\n')

print(calls_duration_mean_ultimate)


print("\n\nLa media de la duración mensual de llamadas pertenecientes al plan surf es: {result:.2f}\n\n"
                                                      .format(result = calls_duration_mean_surf.mean()))

print("\n\nLa media de la duración mensual de llamadas pertenecientes al plan ultimate es: {result:.2f}\n\n"
                                                      .format(result = calls_duration_mean_ultimate.mean()))

print("\n\nLa varianza de la duración mensual de llamadas pertenecientes al plan surf es {result:.2f}\n\n"
                                                      .format(result = np.var(calls_duration_mean_surf)))

print("\n\nLa varianza de la duración mensual de llamadas pertenecientes al plan surf es {result:.2f}\n\n"
                                                      .format(result = np.var(calls_duration_mean_ultimate)))


# In[109]:


pd.pivot_table(full_merge,
               values='calls_duration',
               index=['month'],columns=['plan'],
              aggfunc='mean').boxplot(vert=False,
                                     figsize=(10,8))
plt.show()


# La media de la duración de llamadas mensual de cada plan están sesgados a la derecha o tienen asimetría negativa; por lo tanto la mediana es mayor que la media. (También implica que no importa el plan que tengan, los usuarios van a hacerer ciertos númeeros de llamadas que duren cierta cantidad específica) En función al plan, el comportamiento varía muy poco; solo algunos usuarios ultimate tienden a tener llamadas más largas.

# ### Mensajes

# In[110]:


# Comprara el número de mensajes que tienden a enviar cada mes los usuarios de cada plan
full_merge
pd.pivot_table(full_merge,
               values='messages_amount',
               index='month',
               columns='plan',
               aggfunc='count').plot(kind='bar',
                                  title='Mensajes enviados mensuales',
                                  ylabel='mensajes',
                                  xlabel='mes',
                                  legend=True,
                                    figsize=(10,8))
plt.legend(['surf','ultimate'],loc='upper left')
plt.grid(True)
plt.show()


# 
# De forma curiosa los usuarios que tienen un plan inferior suelen enviar más mensajes que los usuarios que tienen un mejor plan.

# ### Internet

# In[111]:


# Compara la cantidad de tráfico de Internet consumido por usuarios por plan
# pd.pivot_table(full_merge,
#                values='gb_used',
#                index='user_id',
#                columns='plan',
#                aggfunc='sum').mean().plot(kind='bar',
#                                           title='Promedio de cantidad de tráfico de Internet consumido por usuarios por plan')
# plt.show()


# In[112]:


data = pd.pivot_table(full_merge,
               values='gb_used',
               index='user_id',
               columns='plan',
               aggfunc='sum').mean()
plt.figure(figsize=(8, 8))
plt.title('Promedio de cantidad de tráfico de Internet consumido por usuarios por plan')
sns.barplot(data=data)
# width = 5
# height = 8
# sns.set(rc = {'figure.figsize':(width,height)})
# sns.Plot.layput(size=(5,8))
plt.legend(data.index)
plt
plt.show()


# 
# Haciendo la agrupación de el tráfico de internet por usuario por plan, me percaté que sería muy complicado hacer una gráfica con estos datos. Por lo que, a apartir de esa agrupación, calculé el promedio de tráfico que genera cada usuario según su plan.
# Parece que los usuarios ultimate no aprovechan el paquete que les ofrece de tráficod e internet según su plan en promedio.

# ## Ingreso

# [Del mismo modo que has estudiado el comportamiento de los usuarios, describe estadísticamente los ingresos de los planes.]

# In[113]:


plans


# In[114]:


plans.describe()


# In[115]:


#Graficar barras caunto gb ogrece cada plan
data = pd.pivot_table(plans,values='usd_monthly_pay',index='plan_name',aggfunc='sum')
sns.barplot(data=data)
plt.show()


# In[116]:


plt.figure(figsize=(20,8))
full_merge[full_merge['plan'] == 'surf']['total_fee'].hist(bins=np.arange(10,500,22),alpha=0.5)
full_merge[full_merge['plan'] == 'ultimate']['total_fee'].hist(bins=np.arange(10,500,22),alpha=0.7)
plt.xlabel('Ingresos')
plt.ylabel('Frecuencia')
plt.title('Distibución de los ingresos')
plt.legend(['surf','ultimate'])
plt.show()


# In[117]:


#Caluclo para ibtener intervalos
1 + 3.22*math.log1p(len(full_merge[full_merge['plan'] == 'ultimate']))


# 
# Ha ciendo una gráfica de barras de los ingresos, unpicamente hay dos planes; surf y ultimate, el cual van a estar cobrando la empresa a los usuarios mensualmente, según sea su plan. El plan básico cuesta unos 20 dólares, y por otro lado el plan premium cuesta 70; más de triple de segundo. Para contetar a la pregunta, ¿por qué más caro? es debido a que ofrece mejores caracterícticas ese plan.
# 
# Viendo la distribución de los ingresos por los dos planes, observamos que los ingresos están considerablemente sesgado hacia la derecha. La myoría de los usuarios ultimate no gastan má de lo que cuesta el plan.

# <div class="alert alert-block alert-success">
# <b>Comentario revisor</b> <a class="tocSkip"></a>
# 
#  Muy buena prática la de usar distintos tipos de gráficas identificar algunos hallazgos y llegar a conclusiones
# </div>

# ## Prueba las hipótesis estadísticas

# [Prueba la hipótesis de que son diferentes los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf.]

# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]

# In[118]:


# Prueba las hipótesis
data = pd.pivot_table(full_merge,values='total_fee',index='user_id',columns='plan')
print(data)
sample_surf = data['surf']
sample_ultimate = data['ultimate']
sample_surf = sample_surf.dropna()
sample_ultimate = sample_ultimate.dropna()

alpha = 0.05

results = st.ttest_ind(
sample_surf,
sample_ultimate)

print('valor p: ', results.pvalue) # extraer el valor p

if results.pvalue < alpha: # comparar el valor p con el umbral
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")


# Aplicando la prueba de hipótesis y teniendo la hipótesis.
# 
# Obtvimos que se rechaza la hipotesis nula. Esto quiere decir que son diferentes los ingresos promedio procedentes de los usuarios de los planes de llamada Ultimate y Surf.

# [Prueba la hipótesis de que el ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.]

# [Elabora las hipótesis nula y alternativa, escoge la prueba estadística, determina el valor alfa.]

# In[119]:


test = full_merge.copy()


# In[120]:


test['city'] = test['city'].where(test['city'].str.contains('NY-NJ'),'other regions')


# In[121]:


test['city'].unique()


# In[122]:


ny_nj_other_regions = pd.pivot_table(test,values='total_fee',index='user_id',columns='city')
ny_nj_other_regions = ny_nj_other_regions.rename(columns={"New York-Newark-Jersey City, NY-NJ-PA MSA":"ny_nj"})
ny_nj_other_regions.columns = ny_nj_other_regions.columns.str.replace(' ','_')


# In[123]:


ny_nj_other_regions


# In[124]:


# Prueba las hipótesis
sample_surf = ny_nj_other_regions['ny_nj']
sample_ultimate = ny_nj_other_regions['other_regions']
sample_surf = sample_surf.dropna()
sample_ultimate = sample_ultimate.dropna()

alpha = 0.05

results = st.ttest_ind(
sample_surf,
sample_ultimate)

print('valor p: ', results.pvalue) # extraer el valor p

if results.pvalue < alpha: # comparar el valor p con el umbral
    print("Rechazamos la hipótesis nula")
else:
    print("No podemos rechazar la hipótesis nula")


# En este caso no podemos rechazar la hipótesis nula de que el ingreso promedio de los usuarios del área NY-NJ es diferente al de los usuarios de otras regiones.

# ## Conclusión general
# 
# [En esta sección final, enumera tus conclusiones importantes. Asegúrate de que estas abarquen todas las decisiones (suposiciones) importantes que adoptaste y que determinaron la forma elegida para procesar y analizar los datos.]
# En este proyecto me dí cuenta de lo que mucho he aprendido y he usado muchos métodos y teoría que me han ayudado a resolver cada uno de los pasos. Hacen que estén más claro cuando lo pones en práctica y lo mucho que puedes analizar con estos datos, de los cuales eran tablas muy pequeñas, y las conclusiones/decisiones que podemos tomar al respecto. He tenido que ver el material nuevamente porque aún hay conceptos que son un tanto complicados/nuevos para mí, pero con el buen hábito de seguir aprendiendo y prácticando saldrá mucho mejor. También me he percatado lo importante qeu es la estadítica al momento de analizar y compredner los datos para tomar decisiones más precisas que nos ayuden a mejorar un proyecto. Estoy al pendiente de cualquier retroaliemntación con la que pueda mejorar este proyecto.

# In[ ]:




