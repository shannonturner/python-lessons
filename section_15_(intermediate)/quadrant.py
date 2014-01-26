def quadrant(address):

	"Returns the DC quadrant for the address given"

	return [quadrant for quadrant in address.split(' ') if quadrant in ['NW', 'NE', 'SW', 'SE']] or None
