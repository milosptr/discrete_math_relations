# Individual Assignment 5

## Submission and Grading Rules
- There is no limit to the number of submissions before the deadline.
- Your code will be run through an autograder. Half of the tests will provide feedback on your code, while the other half will only indicate if a test failed without revealing input and expected output details. Make use of the feedback you receive.
- Do not use any Python libraries or external packages.
- Solutions to all problems must be submitted in one Python file named `relations.py`. You will receive a template file to use as the basis for your solution.
- For each problem, correctness of your code counts for 50% of the points, and providing arguments through code comments accounts for the remaining 50%.
- There are 10 bonus points available, awarded for achieving a full score from the autograder.

## Deadline for East Iceland Students
*Students in the east of Iceland have a submission deadline on Wednesday, October 25th, at 23:59, adjusted accordingly.

## Assignment Problems
### Problem 1
#### Part a) Reflexive Relations
- Implement a function `is_reflexive(defined_set, relation_on_set)` that returns whether a relation is reflexive.
  - Input: `defined_set` is a list representing the set on which the relations exist, and `relation_on_set` is a list of tuples representing a relation on the set.
  - Output: Boolean value (True if the relation is reflexive, False otherwise).
  
#### Part b) Symmetric Relations
- Implement a function `is_symmetric(relation_on_set)` that returns whether a relation is symmetric.
  - Input: `relation_on_set` is a list of tuples representing a relation.
  - Output: Boolean value (True if the relation is symmetric, False otherwise).
  
#### Part c) Antisymmetric Relations
- Implement a function `is_antisymmetric(relation_on_set)` that returns whether a relation is antisymmetric.
  - Input: `relation_on_set` is a list of tuples representing a relation.
  - Output: Boolean value (True if the relation is antisymmetric, False otherwise).
  
#### Part d) Transitive Relations
- Implement a function `is_transitive(relation_on_set)` that returns whether a relation is transitive.
  - Input: `relation_on_set` is a list of tuples representing a relation.
  - Output: Boolean value (True if the relation is transitive, False otherwise).

### Problem 2
- Implement a function `is_equivalence_relation(defined_set, relation_on_set)` that returns whether a relation is an equivalence relation.
  - Input: `defined_set` is a list representing the set on which the relations exist, and `relation_on_set` is a list of tuples representing a relation on the set.
  - Output: Boolean value (True if the relation is an equivalence relation, False otherwise).

### Problem 3
- Implement a function `composite_relations(relation_R, relation_S)` that takes two relations, R and S, and returns the composite relations S ◦ R.
  - Input: `relation_R` is a list of tuples representing the relation R, and `relation_S` is a list of tuples representing the relation S.
  - Output: List of tuples representing the composite relations S ◦ R.

### Problem 4
#### Part a) to Part e)
Let R be the relation on the set A = {1, 2, 3, 4, ..., n}. Implement five functions that take A as input and count the number of 1s in the matrix MR under specific relations.

#### Part a) {(a, b) | a = 0}
- Implement a function `aces_in_relation_a(A)` to count the number of 1s in MR.
  - Input: `A` is a list representing the set A.
  - Output: Integer representing the count of 1s in MR.

#### Part b) {(a, b) | a = b + 1}
- Implement a function `aces_in_relation_b(A)` to count the number of 1s in MR.
  - Input: `A` is a list representing the set A.
  - Output: Integer representing the count of 1s in MR.

#### Part c) {(a, b) | a ≥ b}
- Implement a function `aces_in_relation_c(A)` to count the number of 1s in MR.
  - Input: `A` is a list representing the set A.
  - Output: Integer representing the count of 1s in MR.

#### Part d) {(a, b) | a + b = 1000}
- Implement a function `aces_in_relation_d(A)` to count the number of 1s in MR.
  - Input: `A` is a list representing the set A.
  - Output: Integer representing the count of 1s in MR.

#### Part e) {(a, b) | a + b ≥ 1001}
- Implement a function `aces_in_relation_e(A)` to count the number of 1s in MR.
  - Input: `A` is a list representing the set A.
  - Output: Integer representing the count of 1s in MR.

*Note: The expected outcomes for specific examples are not provided here, as the functions should return integer values.*
