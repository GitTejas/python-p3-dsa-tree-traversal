class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    result = []
    nodes_to_visit = [self.root]

    while len(nodes_to_visit) > 0:
      # Pop 
      node = nodes_to_visit.pop(0)
      # append & return
      if node['id'] == id:
        result.append(node)
        return result[0]
      # Else
      nodes_to_visit = node['children'] + nodes_to_visit

    #  None
    return None


