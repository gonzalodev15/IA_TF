


from random import choice
from pyknow import *



class Juego(Fact): 
	""" Juegos que se pueden escoger"""
	pass

class Dinero(Fact):
	"""Dinero disponible que se tiene"""
	pass

class Procesador(Fact):
	"""Procesador disponible que se tiene"""
	pass

class Tarjeta(Fact):
	"""Tarjeta disponible que se tiene"""
	pass

class Ram(Fact):
	"""Tarjeta disponible que se tiene"""
	pass


ListaJuego =['Juego1','Juego2','Juego3','Juego4','Juego5']
ListaDinero =['Poco','Normal','Mucho']
ListaProcesador =['Poco','Normal','Mucho']
ListaTarjeta =['Poco','Normal','Mucho']
ListaRam =['Poco','Normal','Mucho']

def ObtenerElMayor(x):
	mayor = 0
	for valor in x:
		if mayor < valor:
			mayor = valor
	if mayor == 7000:
		return 'Juego1'
	if mayor == 3000:
		return 'Juego2'
	if mayor == 7500:
		return 'Juego3'
	if mayor == 4500:
		return 'Juego4'
	if mayor == 6000:
		return 'Juego5'

# In[102]:

class ConjuntoPCs(KnowledgeEngine):
	ListaPC=[]
	def ReturnLista(self):
		return self.ListaPC
    
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Mucho')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPPMMMN(self):
		self.ListaPC=['HP Omen 17, mejor opción','Legion Y520, normal opción','Serie X570UB, peor opción']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Normal')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPPMNMN(self):
		self.ListaPC=['Legion Y520, mejor opción','Serie X570UB, normal opción','Dell G5, peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Poco')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPPMPMN(self):
		self.ListaPC=['Serie X570UB, mejor opción','Dell G5, normal opcion','Serie X570UB peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Poco')),Procesador(VProcesador='Poco')))
	def JPPMPP(self):
		self.ListaPC=['Usted ha escogido mucha tarjeta de video, poca Ram y poco Procesador, esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Normal')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPPMPP(self):
		self.ListaPC=['IdealPad 330, mejor opcion','K555LB-XX131H, normal opcion', 'X540UV, peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Normal')),Procesador(VProcesador='Poco')))
	def JPPMPP(self):
		self.ListaPC=['Usted ha escogido normal tarjeta de video, normal Ram y poco Procesador, esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Poco'),Ram(VRam='Poco')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPPPMN(self):
		self.ListaPC=['Usted ha escogido poca tarjeta de video y poca Ram, esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Poco'),
              AND(Tarjeta(VTarjeta='Poco'),Ram(VRam='Poco')),Procesador(VProcesador='Poco')))
	def JPPPP(self):
		self.ListaPC=['Usted ha escogido poca tarjeta de video, poca Ram y poco procesador, esta configuración es invalida, se recomienda cambiar su configuración']


	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Mucho')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPNMMMN(self):
		self.ListaPC=['Alienware 15, mejor opción','MSI GT5 TITAN8RG, normal opción','HP Omen 17, peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Normal')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPNMNMN(self):
		self.ListaPC=['HP Omen 17, mejor opcion','Dell G5, normal opción','Asus FX504GD-DM328T, peor opción']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Poco')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPNMPMN(self):
		self.ListaPC=['Usted ha escogido mucha tarjeta de video y poca Ram, esta configuración es invalida, se recomienda cambiar su configuración']
        
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Poco')),Procesador(VProcesador='Poco')))
	def JPNMPP(self):
		self.ListaPC=['Usted ha escogido mucha tarjeta de video, poca Ram y poco procesador, esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Mucho')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPNNMMN(self):
		self.ListaPC=['Alienware 15, mejor opcion','Asus FX504GD-DM328T, normal opcion','HP Omen 17, peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Normal')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPNNNMN(self):
		self.ListaPC=['Asus FX504GD-DM328T, mejor opcion','HP Omen 17, normal opcion','Legion Y520, peor opción']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Poco')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPNNPMN(self):
		self.ListaPC=['Usted ha escogido normal tarjeta de video y poca Ram , esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Poco')),Procesador(VProcesador='Poco')))
	def JPNNPMN(self):
		self.ListaPC=['Usted ha escogido normal tarjeta de video, poca Ram y poco Procesador, esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Poco'),Ram(VRam='Poco')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPNPPMN(self):
		self.ListaPC=['Dell G5, mejor opcion','Serie X570UB, normal opcion', 'IdealPad 330, peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Normal'),
              AND(Tarjeta(VTarjeta='Poco'),Ram(VRam='Poco')),Procesador(VProcesador='Poco')))
	def JPNPPP(self):
		self.ListaPC=['Usted ha escogido poca tarjeta de video, poca Ram y poco Procesador, esta configuración es invalida, se recomienda cambiar su configuración']


        
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Mucho')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPMMMMN(self):
		self.ListaPC=['ROG Zephyrus M (GM501), mejor opción','Alienware 15, normal opción','MSI GT5 TITAN8RG, peor opción']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Normal')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPMMNMN(self):
		self.ListaPC=['Alienware 15, mejor opción','HP Omen 17, normal opcion','Dell G5, peor opcion']
        
	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Poco')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPMMPMN(self):
		self.ListaPC=['Usted ha escogido mucha tarjeta de video y poca Ram, esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Mucho'),Ram(VRam='Poco')),Procesador(VProcesador='Poco')))
	def JPMMPP(self):
		self.ListaPC=['Usted ha escogido mucha tarjeta de video, poca Ram y poco Procesador, esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Mucho')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPMNMMN(self):
		self.ListaPC=['Alienware 15, mejor opción','MSI GT5 TITAN8RG, normal opción','Asus FX504GD-DM328T, peor opción']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Normal')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPMNNMN(self):
		self.ListaPC=['Alienware 15, mejor opción','MSI GT5 TITAN8RG, normal opción','HP Omen 17, peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Poco')),OR(Procesador(VProcesador='Mucho'),Procesador(VProcesador='Normal'))))
	def JPMNPMN(self):
		self.ListaPC=['Usted ha escogido normal tarjeta de video, poca Ram , esta configuración es invalida, se recomienda cambiar su configuración']

	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Normal'),Ram(VRam='Poco')),Procesador(VProcesador='Poco')))
	def JPMNPP(self):
		self.ListaPC=['Usted ha escogido normal tarjeta de video, poca Ram y poco Procesador, esta configuración es invalida, se recomienda cambiar su configuración']


	@Rule(AND(OR(Juego(VJuego='Juego1'),Juego(VJuego='Juego3')),Dinero(VDinero='Mucho'),
              AND(Tarjeta(VTarjeta='Poco'),Ram(VRam='Poca')),Procesador(VProcesador='Poco')))
	def JPMPPP(self):
		self.ListaPC=['Usted ha escogido mucha poca de video, poca Ram y poco Procesador, esta configuración es invalida, se recomienda cambiar su configuración']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Poco')))
	def JNP_D(self):
		self.ListaPC=['IdealPad 330, mejor opcion','K555LB-XX131H, normal opcion', 'X540UV, peor opcion']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Normal')))
	def JNN_D(self):
		self.ListaPC=['Dell G5, mejor opcion','Legion Y520, normal opcion','Serie X570UB, peor opcion']
        
	@Rule(AND(Juego(VJuego='Juego5'),Dinero(VDinero='Mucho')))
	def JNM_D(self):
		self.ListaPC=['Alienware 15, mejor opcion','Asus FX504GD-DM328T, normal opcion','HP Omen 17, peor opcion']

	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Poco')))
	def JLP_D(self):
		self.ListaPC=['Hp AM15, mejor opcion','Dell PG, normal opcion', 'X440UV, peor opcion']
        
	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Normal')))
	def JLN_D(self):
		self.ListaPC=['K555LB-XX131H, mejor opcion','X540UV, normal opcion',' Asus DGR120, peor opcion']
        
	@Rule(AND(OR(Juego(VJuego='Juego2'),Juego(VJuego='Juego4')),Dinero(VDinero='Mucho')))
	def JLM_D(self):
		self.ListaPC = ['Dell G5, mejor opcion','Serie X570UB, normal opcion', 'IdealPad 330, peor opcion']



def LogicaProposicional(x,OPDinero,OPProcesador,OPTarjeta,OPRam):
	OPJuego = ObtenerElMayor(x)
	engine = ConjuntoPCs()
	engine.reset()
	engine.declare(Juego(VJuego = OPJuego))
	engine.declare(Dinero(VDinero = OPDinero))
	engine.declare(Procesador(VProcesador = OPProcesador))
	engine.declare(Tarjeta(VTarjeta = OPTarjeta))
	engine.declare(Ram(VRam = OPRam))
	engine.run()
	return engine.ReturnLista()
   

   