example (A B : Prop) (a : A) (b : B) : A ∧ B := by
  constructor
  exact a
  exact b
