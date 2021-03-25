def make_car(manufacturer, model,**car_features):
	car_features['manufacturer'] = manufacturer
	car_features['model'] = model
	return car_features
car = make_car('Ford', 'Fiesta', color ='white', service_package=True)
print(car)