def map(x, in_min, in_max, out_min,out_max):

	return float((x-in_min)*(out_max-out_min)/(in_max-in_min)+out_min)

def angle2cycle(angulo):

	tiempo = map(angulo,0,180,0.1e-3,2.5e-3)
	ciclo = tiempo*100/20e-3

	return(ciclo)
