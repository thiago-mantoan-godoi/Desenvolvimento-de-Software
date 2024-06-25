def calculate_cost(params):
    return params[0] * 1.2 + params[1] * 0.8 + params[2] * 1.5

def calculate_quality(params):
    return 100 - (params[0] * 0.5 + params[1] * 0.3 + params[2] * 0.7)

def calculate_production_time(params):
    return params[0] * 0.7 + params[1] * 1.0 + params[2] * 0.5

def fitness_function(params):
    cost = calculate_cost(params)
    quality = calculate_quality(params)
    production_time = calculate_production_time(params)
    
    weight_cost = 0.4
    weight_quality = 0.3
    weight_production_time = 0.3
    
    fitness = (weight_cost * cost) + (weight_quality * (100 - quality)) + (weight_production_time * production_time)
    return fitness,
