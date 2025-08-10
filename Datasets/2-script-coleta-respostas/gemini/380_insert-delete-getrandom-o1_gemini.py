class Solution:
    def __init__(self):
        self.data_map = {} 
        self.data_list = [] 

    def insert(self, val):
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val):
        if val not in self.data_map:
            return False
        last_elem_in_list = self.data_list[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data_list[index_of_elem_to_remove] = last_elem_in_list
        self.data_list.pop()
        self.data_map.pop(val)
        return True
        
    def getRandom(self):
        return random.choice(self.data_list)