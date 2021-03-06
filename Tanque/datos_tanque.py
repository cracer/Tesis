"""Este script genera los datos de simulacion del tanque sin falla y con falla"""

import numpy as np

"""__________________________________________ Variables Generales ___________________________________________________"""

'''Caracteristicas del Tanque'''

q = 10                                                  # Caudal de entrada [m^3/h]
radio = 0.5                                             # Radio del tanque [m]
area = np.pi * radio**2                                 # Area transversal del tanque [m^2]
r = 0.2                                                 # Valor inicial de la resistencia hidraulica
nivel_inicial = 0                                       # Nivel inicial del tanque [m]

'''Datos de la Simulacion'''

tiempo = 12                                             # Tiempo de simulacion [h] (240h -> 1d)
paso = 0.01                                              # Paso de integracion [h]
decimal = str(paso)[::-1].find('.')                     # Numero de decimales del paso
t_i = 0                                                 # Tiempo inciial de la simulacion [h]
t_f = tiempo                                            # Tiempo final de la simulacion [h]
tss_2 = np.ceil(4*area*r/paso)                          # Posicion de Tiempo de establecimiento del nivel
t_sim = np.arange(t_i, t_f, paso)                       # Vector de rangos de tiempo de la simulacion
t_sim_ee = t_sim[int(tss_2):]                           # Vector de tiempo de simulacion en estado estacionario
q_sim = np.ones(tiempo/paso)*q                          # Vector de caudal para cada tiempo
r_sim = np.ones(tiempo/paso)*r                          # Vector de resistencia hidraulica para cada tiempo

'''Datos con tiempo de Simulacion extendido'''

tiempo_extend = 480                                    # Tiempo de simulacion [h] (240h -> 1d)
t_f_extend = tiempo_extend                              # Tiempo final de la simulacion [h]
t_sim_extend = np.arange(t_i, t_f_extend, paso)         # Vector de rangos de tiempo de la simulacion
t_sim_ee_extend = t_sim_extend[int(tss_2/paso):]        # Vector de tiempo de simulacion en estado estacionario
q_sim_extend = np.ones(tiempo_extend/paso)*q            # Vector de caudal para cada tiempo
r_sim_extend = np.ones(tiempo_extend/paso)*r            # Vector de resistencia hidraulica para cada tiempo

"""___________________________________________ Variables de las Fallas ______________________________________________"""

'''Diferencias a detectar'''

detect_delta_media = np.linspace(1e-2, 5e-2, 20)
detect_delta_var = np.linspace(1.434337e-7, 6.82516e-7, 20)

detect_delta_media_residuos = np.linspace(4.4385e-5, 2.21925e-4, 20)
detect_delta_var_residuos = np.linspace(1.92133e-5, 4.80333e-5, 20)

'''Falla de Deriva'''

t_i_falla_deriva = 4                                        # Tiempo de inicio de la falla [h]
t_f_falla_deriva = [4.2, 6.1, 8.1, 12]                    # Tiempos de finalizacion de la falla [h]
delta_h_porcentaje = [1, 1.75, 2.5]                            # Variacion total del nivel del tanque [%]
delta_h = [i*2/100 for i in delta_h_porcentaje]             # Variacion total del nivel del tanque [m]
                                                            # *2 porque la media es 2m
'''Falla de Pulso'''

t_i_falla_pulso = 4                                         # Tiempo de inicio de la falla [h]
t_f_falla_pulso = 12                                        # Tiempos de finalizacion de la falla [h]
N_pulsos = [100, 200, 300, 400]                                # Numero de muestras con pulso
amplitud_pulso = [0.01, 0.025, 0.05]                        # Desviacion estandar de los pulsos
random_seed = 0                                             # Valor semilla del generador de numeros aleatorios
modo = 'fixed'                                              # Amplitud de pulsos de distribucion normal aleatoria

'''Falla de Varianza'''

t_i_falla_var = 4                                        # Tiempo de inicio de la falla [h]
t_f_falla_var = [4.2, 6.1, 8.1, 12]                    # Tiempos de finalizacion de la falla [h]
amplitud_var = [0.01, 0.025, 0.05]                       # Desviacion estandar

"""____________________________________Variables de las Fallas con Tiempo Extendido _________________________________"""

'''Diferencias a detectar'''

detect_delta_media_residuos_extend = np.linspace(1e-5, 5e-5, 20)
detect_delta_var_residuos_extend = np.linspace(0.001, 0.005, 20)

'''Falla de Deriva'''

t_i_falla_deriva_extend = 160                                        # Tiempo de inicio de la falla [h]
t_f_falla_deriva_extend = [160.2, 240.0, 320.1, 360]               # Tiempos de finalizacion de la falla [h]

'''Falla de Pulso'''

t_i_falla_pulso_extend = 160                                         # Tiempo de inicio de la falla [h]
t_f_falla_pulso_extend = 480                                        # Tiempos de finalizacion de la falla [h]
N_pulsos_extend = [320, 800, 1600, 2000]                              # Numero de muestras con pulso

'''Falla de Varianza'''

t_i_falla_var_extend = 160                                        # Tiempo de inicio de la falla [h]
t_f_falla_var_extend = [160.2, 240.0, 320.1, 360]              # Tiempos de finalizacion de la falla [h]
