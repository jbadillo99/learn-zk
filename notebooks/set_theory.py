import numpy as np
import pandas as pd
import operator
from itertools import product

class SetTheory:
    
    def __init__(self, setA:list = None, setB:list = None, bold_pairs=None, setNameA:str='SetA', setNameB:str='SetB'):
        
        """
        Initialize a SetTheory Instance
        
        Args:
            setA (list): The first set to be computed for the cartesian product
            setB (list): The second set to be computed for the cartesian product
            bold_pairs (list): The list of tuples that represent the ordered pairs that are in the subset of a cartesian product
        """
        self.setA = setA if setA is not None else []
        self.setB = setB if setB is not None else []
        self.bold_pairs = bold_pairs if bold_pairs is not None else []
        
        self.setNameA = setNameA
        self.setNameB = setNameB
        
        self.df = None
        
    def create_dataframe(self):
        cartesian_product = product(self.setA, self.setB)
        
        # Check if the dataframe has already been created, if not create one
        if self.df == None:
            self.df = pd.DataFrame(cartesian_product, columns = [self.setNameA, self.setNameB])
        
        # Create the Ordered Pairs based one the values from the cartesian product
        self.df["Ordered Pair"] = self.df.apply(lambda row: (row[self.setNameA],row[self.setNameB]), axis=1)
        
        # Create the Cartesian Table of ordered pair with the values from SetA as the rows and Set B as columnss
        self.df = self.df.pivot(index=self.setNameA, columns=self.setNameB, values='Ordered Pair')
    
    def display_dataframe(self, color:str="black") -> pd.DataFrame:
        """
        Return the generated dataset to display in Jupyter Notebook
        """
        if self.df is not None:
            return self.df.style.applymap(self.highlight_ordered_pairs, color=color)
        else:
            print("Dataset not generated. Call generate_cartesian_product() first.")
        
        
    def perform_operation(self,operator_str, operand1, operand2):
        """
        Perform an arithmetic operation based on the provided operator.

        Args:
            operator_str (str): String representation of the operator ('+', '-', '*', '/', etc.).
            operand1: The first operand.
            operand2: The second operand.

        Returns:
            The result of the arithmetic operation.
        """
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '//': operator.floordiv,
            '**': operator.pow,
            '%': operator.mod
            # Add more operators as needed
        }

        # Check if the provided operator_str is in the dictionary
        if operator_str in operators:
            # Use the corresponding operator function from the operator module
            operation = operators[operator_str]
            return operation(operand1, operand2)
        else:
            # Handle the case when an unsupported operator is provided
            raise ValueError(f"Unsupported operator: {operator_str}")
            
    def highlight_ordered_pairs(self, pair, color:str="black") -> str:
        """
        Higlight the ordered pairs from the cartesian product if they are in the set 'bold_pairs'
        """
        return f'font-weight: bold; color: {color}' if pair in self.bold_pairs else ''
    
    def binary_operator(self, operator: str, mod:int) -> list:
        # Define a custom function for styling
        bold_pairs = []

        for i in range(len(df)):
            if self.perform_operation(operator,df['Ordered Pair'][i][0],df['Ordered Pair'][i][1])%mod == df[1][i]:
                bold_pairs += [(df[self.setNameB][i],df[self.setNameA][i])]

        return bold_pairs
        
    
    