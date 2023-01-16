from algorithms.Algorithm import Algorithm

class KNearestNeighbours(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.hyperparameters = None


    def __str__(self):
        return "KNearestNeighbours: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()

    def set_hyperparameter(self, name, value):
        self.hyperparameters[name] = value

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters


    def get_hyperparameters_names(self):
        return [
            "n_neighbors",
            "weights",
            "algorithm",
            "leaf_size",
            "p",
            "metric",
            "metric_params",
            "n_jobs"
        ]