# Decision Tree Algorithm class inherits from Algorithm class

from model.algorithms.Algorithm import Algorithm

class DecisionTree(Algorithm):
    def __init__(self, name):
        super().__init__(name)
        self.hyperparameters = []


    def __str__(self):
        return "Decision Tree: " + self.name + " " + str(self.hyperparameters)

    def __repr__(self):
        return self.__str__()

    def set_hyperparameter(self, hyperparameter):
        self.hyperparameters.append(hyperparameter)

    def set_hyperparameters(self, hyperparameters):
        self.hyperparameters = hyperparameters

    def clone(self):
        return DecisionTree(self.name)

    
    def get_hyperparameters_names(self):
        return [
            "criterion",
            "splitter",
            "max_depth",
            "min_samples_split",
            "min_samples_leaf",
            "min_weight_fraction_leaf",
            "max_features",
            "random_state",
            "max_leaf_nodes",
            "min_impurity_decrease",
            "min_impurity_split",
            "class_weight",
            "presort"
        ]

    