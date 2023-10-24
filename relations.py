def is_reflexive(defined_set: set, relation_on_set: list[tuple]) -> bool:
    # a reflexive relation is the one in which every element maps to itself
    # so, if (a, a) is not in the relation, the relation is not reflexive

    # we loop trough the elements of the defined set
    # and check if the tuple (element, element) is in the relation
    # (element, element) is the tuple that maps the element to itself
    # if it is not, the relation is not reflexive
    for element in defined_set:
        if (element, element) not in relation_on_set:
            return False
    return True


def is_symmetric(relation_on_set: list[tuple]) -> bool:
    # a symmetric relation is the one in which if (a, b) is in the relation,
    # then (b, a) is also in the relation

    # we loop trough the elements of the relation
    # and check if the tuple (second element of the tuple, first element of the tuple) is in the relation
    # if it is not, the relation is not symmetric
    for (a, b) in relation_on_set:
        if (b, a) not in relation_on_set:
            return False
    return True

def is_antisymmetric(relation_on_set: list[tuple]) -> bool:
    # first, check if the relation is symmetric
    # if it is, it cannot be antisymmetric
    if(is_symmetric(relation_on_set)):
        return False

    # a antisymmetric relation is the one in which if (a, b) is in the relation,
    # then (b, a) is not in the relation

    # we loop trough the elements of the relation
    # and check if the tuple (second element of the tuple, first element of the tuple) is in the relation
    # if it is, the relation is not antisymmetric
    # but we need to be careful in case a = b, because in that case we should not check
    # if (b, a) is in the relation, because (a, b) = (b, a)
    for (a, b) in relation_on_set:
        if a == b:
            continue
        if (b, a) in relation_on_set:
            return False
    return True

def is_transitive (relation_on_set: list[tuple]) -> bool:
    relation_set: set = set(relation_on_set)
    # a transitive relation is the one in which if (a, b) and (b, c) are in the relation,
    # then (a, c) is also in the relation
    for (a, b) in relation_set:
        for (c, d) in relation_set:
            # if the second element of the tuple of the first relation is equal to
            # the first element of the tuple of the second relation
            # and the tuple (first element of the tuple of the first relation,
            # second element of the tuple of the second relation) is not in the relation
            if b == c and (a, d) not in relation_set:
                return False
    return True

def is_equivalence_relation(defined_set: set, relation_on_set: list[tuple]) -> bool:
    # check if the relation is reflexive, symmetric and transitive
    # if it is, it is an equivalence relation
    if(is_reflexive(defined_set, relation_on_set) and is_symmetric(relation_on_set) and is_transitive(relation_on_set)):
        return True
    return False

def composite_relations(relation_R: list[tuple], relation_S: list[tuple]) -> list[tuple]:
  relation_set: set = set()
  # looping trough the elements of the relation R
  # and the elements of the relation S
  # if the second element of the tuple of R is equal to the first element of the tuple of S
  # then we add the tuple (first element of the tuple of R, second element of the tuple of S) to the relation set
  # we do this for every tuple in the relation R and S because we want to find the composite relation
  # composed of the tuples of R and S is the relation that have the same second and first element respectively
  for (a, b) in relation_R:
      for (c, d) in relation_S:
          if b == c:
            relation_set.add((a, d))

  # we convert set to a list so we can sort it
  relation_set = list(relation_set)
  relation_set.sort()
  return relation_set


# set A = {1, 2, 3, 4, . . . , n}
def aces_in_relation_a(A: list[int]) -> int:
  # we find the length of the list A
  n: int = len(A)
  aces: int = 0

  # we create a matrix of zeros with the same size of the list A (n x n)
  matrix: list[list[int]] = [[0] * n for _ in range(n)]

  # because the condition on the relation is set to be
  # R = {(a,b)∣ a = 0} we check if 0 is in the list A
  if 0 in A:
    # if it is, we find the index of 0 in A
    index_of_zero: int = A.index(0)

    # if such element exists, we set the first element of the matrix to 1
    for i in range(n):
        matrix[index_of_zero][i] = 1
        aces += 1

  return aces


def aces_in_relation_b(A: list[int]) -> int:
  # we find the length of the list A
  n:int  = len(A)
  aces:int  = 0

  # condition on the relation is set to be
  # R = {(a, b) | a = b + 1}
  # so, we check if the list A is empty
  if n == 0:
    return 0

  # in the previous function aces_in_relation_a, we prepared an emtpy matrix
  # and then we populated it with 1's if the condition was met
  # in this function we could do the same thing, but since we are not really
  # using the matrix, we can just count aces without generating a matrix
  # we just need to check if the element of the list A is equal to the element of the list A + 1
  for a in range(n):
    for b in range(n):
       if A[a] == A[b] + 1:
          aces += 1

  return aces

def aces_in_relation_c(A: list[int]) -> int:
  # we find the length of the list A
  n: int = len(A)
  aces: int = 0

  if n == 0:
    return 0

  for a in range(n):
    for b in range(n):
       if A[a] >= A[b]:
          aces += 1

  return aces

def aces_in_relation_d(A: list[int]) -> int:
  n: int = len(A)
  aces: int = 0

  if n == 0:
    return 0

  for a in range(n):
    for b in range(n):
       # {(a, b) | a + b = 1000} is a condition on a task
       if A[a] + A[b] == 1000:
          aces += 1

  return aces

def aces_in_relation_e(A: list[int]) -> int:
  n: int = len(A)
  aces: int = 0

  if n == 0:
    return 0

  for a in range(n):
    for b in range(n):
       # {(a, b) | a + b ≥ 1001} is a condition on a task
       if A[a] + A[b] >= 1001:
          aces += 1

  return aces
