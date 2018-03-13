
# coding: utf-8

# In[3]:


class RuleClass:
    attributes = []
    attributes_value = []
    attributes_cover = []
    decision_cover =[]
    false_cover =[]
    Decision = ''
    def __cmp__(self, other):
        if self.strength > other.strength:
            return 1
        elif self.strength < other.strength:
            return -1
        else:
            return 0
        
    def __init__(self,attributes,attributes_value,attributes_cover,decision,decision_cover,false_cover):
        self.strength = len(decision_cover)
        self.specificity=len(attributes)
        self.support = self.strength*self.specificity
        self.attributes=attributes
        self.attributes_value=attributes_value
        self.attributes_cover = attributes_cover
        self.Decision=decision
        self.decision_cover = decision_cover
        self.false_cover= false_cover
        self.conditionalProbablity=0
        if(len(attributes_cover)!=0):
            self.conditionalProbablity= self.strength/len(attributes_cover)
        
    
    
    def print_rule(self):
        print('Rule ')
        print(attributes, attributes_value , decision_cover)
        print('Strength ',self.strength)
        print('Specificity ',self.specificity)
        print('Support ',self.support)
        prine('-----------------------------------------')
        


# In[2]:




