import LeanCopilot

example (A B : Prop) (a : A) (b : B) : A ∧ B := by
  simp_all only [and_self]

-- example {α : Type} {P: α → Prop}: (∀x, (A → P x)) → (A → ∀x, P x) :=
--   by
--     intro a a_1 --a : ∀ (x : α), A → P x, a_1 : A
--     intro x
--     apply a
--     exact a_1

example {α : Type} {P: α → Prop}: (∀x, (A → P x)) → (A → ∀x, P x) :=
  by
    intro a a_1 x
    apply a
    exact a_1
