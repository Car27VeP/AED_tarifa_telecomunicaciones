# Análisis exploratorio de las tarifas de una empresa de telecomunicaciones.

Trabajas como analista para el operador de telecomunicaciones Megaline. La empresa ofrece a sus clientes dos tarifas de prepago, Surf y Ultimate. El departamento comercial quiere saber cuál de los planes genera más ingresos para poder ajustar el presupuesto de publicidad.

Vas a realizar un análisis preliminar de las tarifas basado en una selección de clientes relativamente pequeña. Tendrás los datos de 500 clientes de Megaline: quiénes son los clientes, de dónde son, qué tarifa usan, así como la cantidad de llamadas que hicieron y los mensajes de texto que enviaron en 2018. Tu trabajo es analizar el comportamiento de los clientes y determinar qué tarifa de prepago genera más ingresos. Más adelante, encontrarás en las instrucciones del proyecto cuáles son exactamente los aspectos del comportamiento de los clientes que debes analizar. Determinar qué plan, en promedio, aporta más ingresos es una cuestión que se abordará mediante pruebas estadísticas. Más adelante encontrarás más información al respecto en la sección de instrucciones del proyecto.

Descripción de las tarifas
Nota: Megaline redondea los segundos a minutos y los megabytes a gigabytes. Para llamadas, cada llamada individual se redondea: incluso si la llamada duró solo un segundo, se contará como un minuto. Para tráfico web, las sesiones web individuales no se redondean. En vez de esto, el total del mes se redondea hacia arriba. Si alguien usa 1025 megabytes este mes, se le cobrarán 2 gigabytes.

A continuación puedes ver una descripción de las tarifas:

Surf

Pago mensual: 20$.
500 minutos al mes, 50 SMS y 15 GB de datos.
Si se exceden los límites del paquete:
1 minuto: 3 centavos.
1 SMS: 3 centavos.
1 GB de datos: 10$.
Ultimate

Pago mensual: 70$.
3000 minutos al mes, 1000 SMS y 30 GB de datos.
Si se exceden los límites del paquete:
1 minuto: 1 centavo.
1 SMS: 1 centavo.
1 GB de datos: 7$.
Diccionario de datos
En este proyecto, trabajarás con cinco tablas diferentes.

La tabla users (datos sobre los usuarios):
 
user_id: identificador único del usuario.
first_name: nombre del usuario.
last_name: apellido del usuario.
age: edad del usuario (en años).
reg_date: fecha de suscripción (dd, mm, aa).
churn_date: la fecha en la que el usuario dejó de usar el servicio (si el valor es ausente, la tarifa se estaba usando cuando fue extraída esta base de datos).
city: ciudad de residencia del usuario.
plan: nombre de la tarifa.

La tabla calls (datos sobre las llamadas):
 
id: identificador único de la llamada.
call_date: fecha de la llamada.
duration: duración de la llamada (en minutos).
user_id: el identificador del usuario que realiza la llamada.

La tabla messages (datos sobre los SMS):
 
id: identificador único del SMS.
message_date: fecha del SMS.
user_id: el identificador del usuario que manda el SMS.

La tabla internet (datos sobre las sesiones web):
 
id: identificador único de la sesión.
mb_used: el volumen de datos gastados durante la sesión (en megabytes).
session_date: fecha de la sesión web.
user_id: identificador del usuario.

La tabla plans (datos sobre las tarifas):
 
plan_name: nombre de la tarifa.
usd_monthly_fee: pago mensual en dólares estadounidenses.
minutes_included: minutos incluidos al mes.
messages_included: SMS incluidos al mes.
mb_per_month_included: datos incluidos al mes (en megabytes).
usd_per_minute: precio por minuto tras exceder los límites del paquete (por ejemplo, si el paquete incluye 100 minutos, el operador cobrará el minuto 101).
usd_per_message: precio por SMS tras exceder los límites del paquete.
usd_per_gb: precio por gigabyte de los datos extra tras exceder los límites del paquete (1 GB = 1024 megabytes).