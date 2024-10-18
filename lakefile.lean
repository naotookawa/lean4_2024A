import Lake
open Lake DSL

package "myproject"

lean_lib «Myproject» where
  -- add library configuration options here

@[default_target]
lean_exe "myproject" where
  root := `Main

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "v4.11.0"

require LeanCopilot from git "https://github.com/lean-dojo/LeanCopilot.git" @ "main"
