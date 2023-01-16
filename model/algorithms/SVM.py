from algorithms.Algorithm import Algorithm

class SVM(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.hyperparameters = None


    def __str__(self):
        return "SVM: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()

    def set_hyperparameter(self, name, value):
        self.hyperparameters[name] = value

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters

    def get_hyperparameters_names(self):
        return [
            "C",
            "kernel",
            "degree",
            "gamma",
            "coef0",
            "shrinking",
            "probability",
            "tol",
            "cache_size",
            "class_weight",
            "verbose",
            "max_iter",
            "decision_function_shape",
            "break_ties",
            "random_state"
        ]