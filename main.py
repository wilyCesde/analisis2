from data.apartamentos import apartamento1, apartamento2
import pandas as pd
from helpers.crearTablasHTML import crearTabla

# 1.CREAR DATAFRAME

tabla1 = pd.DataFrame(apartamento1, columns=['edades'])
tabla2 = pd.DataFrame(apartamento2, columns=['edades'])
tabla3 = pd.read_csv('./data/empleados.csv')


# EFECTUANDO FILTROS CON PYTHON
# 1 .DEFINIR UNA CONDICION LOGICA


empleadosJovenes = tabla3.query('edad<28 and cargo=="analista1"')
empleadosSalarioBajo = tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosAdespedir = tabla3.query('edad>50')


crearTabla(empleadosJovenes, "tablaJovenes")
crearTabla(empleadosSalarioBajo, "tablaSalarioBajo")
crearTabla(empleadosAdespedir, "tablaAdespedir")


# #####################################################
# estadisticasAPTO1=tabla1.describe()
# estadisticasAPTO2=tabla2.describe()
# estadisticasEmpleados=tabla3.describe()
# #####################################################
# print(estadisticasAPTO1)
# print('\n')
# print(estadisticasAPTO2)
# print('\n')
# print(estadisticasEmpleados)
# #####################################################
