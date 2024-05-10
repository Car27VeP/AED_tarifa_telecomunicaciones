# %%[markdown] [markdown]
#  Imprime una muestra de los datos para las tarifas

# %% [markdown] [markdown]
#  ¡Hola!
# 
#  Mi nombre es Tonatiuh Cruz. Me complace revisar tu proyecto hoy.
# 
#  Al identificar cualquier error inicialmente, simplemente los destacaré. Te animo a localizar y abordar los problemas de forma independiente como parte de tu preparación para un rol como data-scientist. En un entorno profesional, tu líder de equipo seguiría un enfoque similar. Si encuentras la tarea desafiante, proporcionaré una pista más específica en la próxima iteración.
# 
#  Encontrarás mis comentarios a continuación - **por favor no los muevas, modifiques o elimines**.
# 
#  Puedes encontrar mis comentarios en cajas verdes, amarillas o rojas como esta:
# 
#  <div class="alert alert-block alert-success">
#  <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
#  Éxito. Todo está hecho correctamente.
#  </div>
# 
#  <div class="alert alert-block alert-warning">
#  <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
#  Observaciones. Algunas recomendaciones.
#  </div>
# 
#  <div class="alert alert-block alert-danger">
#  <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
#  Necesita corrección. El bloque requiere algunas correcciones. El trabajo no puede ser aceptado con comentarios en rojo.
#  </div>
# 
#  Puedes responderme utilizando esto:
# 
#  <div class="alert alert-block alert-info">
#  <b>Respuesta del estudiante.</b> <a class="tocSkip"></a>
#  # ¿Cuál es la mejor tarifa?
# 
#  Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
#  Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.
#  ## Observaciones del proyecto.
#  - Trabajar con la tabla plans para calcular la tarifa que le corresponde a cada usuarios. Estaba haciendo los calculos sin la ayuda de la tabla.
#  - Redondear el consumo de gb hacia arriba; como lo hice con los minutos en llamadas
#  - Donde usé el método groupby, usar el método pivot_table. Con el fin de ponerlo en practica y no se me olvidey corroborar la que la información calculada sea la misma tanto con groupby como con pivot_table.
#  - Hacer la graficas con librerias seaborn (sns) y pandas (pd)
#  - Corroborar que SI una los 4 dataframes agrupados calculados con las tablas.
#  - Usar el método pivot_table. No usar gorupby ni agg, por ahora.
#  - Declarar la unión de las tablas como merged_part1, merged_part2 & full_merged
#  ## Inicialización

# %%[markdown] [markdown]
#  ## Inicialización

# %% [markdown] [markdown]
#  ¡Hola!
# 
#  Mi nombre es Tonatiuh Cruz. Me complace revisar tu proyecto hoy.
# 
#  Al identificar cualquier error inicialmente, simplemente los destacaré. Te animo a localizar y abordar los problemas de forma independiente como parte de tu preparación para un rol como data-scientist. En un entorno profesional, tu líder de equipo seguiría un enfoque similar. Si encuentras la tarea desafiante, proporcionaré una pista más específica en la próxima iteración.
# 
#  Encontrarás mis comentarios a continuación - **por favor no los muevas, modifiques o elimines**.
# 
#  Puedes encontrar mis comentarios en cajas verdes, amarillas o rojas como esta:
# 
#  <div class="alert alert-block alert-success">
#  <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
#  Éxito. Todo está hecho correctamente.
#  </div>
# 
#  <div class="alert alert-block alert-warning">
#  <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
#  Observaciones. Algunas recomendaciones.
#  </div>
# 
#  <div class="alert alert-block alert-danger">
#  <b>Comentario del revisor</b> <a class="tocSkip"></a>
# 
#  Necesita corrección. El bloque requiere algunas correcciones. El trabajo no puede ser aceptado con comentarios en rojo.
#  </div>
# 
#  Puedes responderme utilizando esto:
# 
#  <div class="alert alert-block alert-info">
#  <b>Respuesta del estudiante.</b> <a class="tocSkip"></a>
#  # ¿Cuál es la mejor tarifa?
# 
#  Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de las tarifas genera más ingresos para poder ajustar el presupuesto de publicidad.
# 
#  Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos.
#  ## Observaciones del proyecto.
#  - Trabajar con la tabla plans para calcular la tarifa que le corresponde a cada usuarios. Estaba haciendo los calculos sin la ayuda de la tabla.
#  - Redondear el consumo de gb hacia arriba; como lo hice con los minutos en llamadas
#  - Donde usé el método groupby, usar el método pivot_table. Con el fin de ponerlo en practica y no se me olvidey corroborar la que la información calculada sea la misma tanto con groupby como con pivot_table.
#  - Hacer la graficas con librerias seaborn (sns) y pandas (pd)
#  - Corroborar que SI una los 4 dataframes agrupados calculados con las tablas.
#  - Usar el método pivot_table. No usar gorupby ni agg, por ahora.
#  - Declarar la unión de las tablas como merged_part1, merged_part2 & full_merged

# %%[markdown] [markdown]
#  ## Inicialización

# In[2]:
# Carga las librerías
import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
from scipy import stats as st


# Las liberías necesarias y que podría considerar para este proyecto.

# ## Cargar datos

# %%[markdown] [markdown]
#  Carga las librerías

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
from scipy import stats as st


# Las liberías necesarias y que podría considerar para este proyecto.

# ## Cargar datos

# %%[markdown] [markdown]
#  Carga las librerías

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
from scipy import stats as st


# Las liberías necesarias y que podría considerar para este proyecto.

# ## Cargar datos

# %%[markdown] [markdown]
#  Carga las librerías

# %%
import pandas as pd
import numpy as np
import seaborn as sns
import math
import matplotlib.pyplot as plt
from scipy import stats as st
# Las liberías necesarias y que podría considerar para este proyecto.

# ## Cargar datos

# %%[markdown] [markdown]
#  ## Cargar datos

# %%[markdown] [markdown]
#  Carga los archivos de datos en diferentes DataFrames

# %%
calls = pd.read_csv('megaline_calls.csv')
internet = pd.read_csv('megaline_internet.csv')
messagges = pd.read_csv('megaline_messages.csv')
plans = pd.read_csv('megaline_plans.csv')
users = pd.read_csv('megaline_users.csv')


# Se cargaron las 5 tablas necesarias para llevar a acabo este proyecto.

# ## Preparar los datos

# [Los datos para este proyecto se dividen en varias tablas. Explora cada una para tener una comprensión inicial de los datos. Si es necesario, haz las correcciones requeridas en cada tabla.]

# ### Vizualación de los 5 tablas para asegurarnos que se cargaron correctamente y como están elaboradas.

# %%[markdown] [markdown]
#  Se cargaron las 5 tablas necesarias para llevar a acabo este proyecto.
#  ## Preparar los datos
#  [Los datos para este proyecto se dividen en varias tablas. Explora cada una para tener una comprensión inicial de los datos. Si es necesario, haz las correcciones requeridas en cada tabla.]
#  ### Vizualación de los 5 tablas para asegurarnos que se cargaron correctamente y como están elaboradas.

# %%[markdown] [markdown]
#  Carga los archivos de datos en diferentes DataFrames

# %%
calls = pd.read_csv('megaline_calls.csv')
internet = pd.read_csv('megaline_internet.csv')
messagges = pd.read_csv('megaline_messages.csv')
plans = pd.read_csv('megaline_plans.csv')
users = pd.read_csv('megaline_users.csv')

# %%[markdown] [markdown]
#  Se cargaron las 5 tablas necesarias para llevar a acabo este proyecto.
#  ## Preparar los datos
#  [Los datos para este proyecto se dividen en varias tablas. Explora cada una para tener una comprensión inicial de los datos. Si es necesario, haz las correcciones requeridas en cada tabla.]
#  ### Vizualación de los 5 tablas para asegurarnos que se cargaron correctamente y como están elaboradas.

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

# %%[markdown] [markdown]
#  ### Calculamos la dimensión de las 5 tablas.
#  Obervamos que no tiene valores nulos, por lo que no es necesario aplicar ningún método para tratar con valores nulos.

# %%
df = pd.read_csv('megaline_calls.csv')

# %%
df.head()

# %%
df.sample(10)

# %%
df.sample(10,random_state=6758)

# %%
df.sample(10,random_state=6758).index


