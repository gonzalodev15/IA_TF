from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel

balanitis_model = BayesianModel([('Erupciones', 'Balanitis Candidiasica'),
                                ('Dolor', 'Balanitis Candidiasica'),
                                ('Picor', 'Balanitis Candidiasica'),
                                ('Papulas', 'Balanitis Candidiasica'),
                                ('Maculas', 'Balanitis Candidiasica'),
                                ('Supuracion maloliente', 'Balanitis por Anaerobios'),
                                ('Edemas', 'Balanitis por Anaerobios'),
                                ('Adenitis', 'Balanitis por Anaerobios'),
                                ('Enrojecimiento', 'Balanitis por Aerobios'),
                                ('Fisuras', 'Balanitis por Aerobios'),
                                ('Eritema', 'Balanitis por Aerobios'),
                                ('Edemas', 'Balanitis por Aerobios'),
                                ('Papulas', 'Balanitis por Herpes'),
                                ('Ulceras Dolorosas', 'Balanitis por Herpes'),
                                ('Inflamacion de Ganglios', 'Balanitis por Herpes'),
                                ('Vesiculas', 'Balanitis por Herpes'),
                                ('Lesiones blanco-grisaceas', 'Balanitis Circinada'),
                                ('Artritis', 'Balanitis Circinada'),
                                ('Uretritis', 'Balanitis Circinada'),
                                ('Conjuntivitis', 'Balanitis Circinada')])
								

bcandidiasica_cpd = TabularCPD(
                variable = 'Balanitis Candidiasica',
                variable_card = 2,
                evidence = ['Erupciones', 'Dolor', 'Picor', 'Papulas', 'Maculas'],
                evidence_card = [2, 2, 2, 2, 2],
                values = [[0.15,0.85]])
banaerobios_cpd = TabularCPD(
                variable = 'Balanitis por Anaerobios',
                variable_card = 2,
                evidence = ['Supuracion Maloliente', 'Edemas', 'Adenitis'],
                evidence_card = [2, 2, 2],
                values = [[0.25,0.75]])
baerobios_cpd = TabularCPD(
                variable = 'Balanitis por Aerobios',
                variable_card = 2,
                evidence = ['Enrojecimiento', 'Fisuras', 'Eritema', 'Edemas'],
                evidence_card = [2, 2, 2, 2],
                values = [[0.20,0.80]])
bherpes_cpd = TabularCPD(
                variable = 'Balanitis por Herpes',
                variable_card = 2,
                evidence = ['Papulas', 'Ulceras Dolorosas', 'Inflamacion de Ganglios', 'Vesículas'],
                evidence_card = [2, 2, 2, 2],
                values = [[0.30,0.70]])
bcircinada_cpd = TabularCPD(
                variable = 'Balanitis Circinada',
                variable_card = 2,
                evidence = ['Lesiones blanco-grisaceas', 'Artritis', 'Uretritis', 'Conjuntivitis'],
                evidence_card = [2, 2, 2, 2],
                values = [[0.15,0.85]])