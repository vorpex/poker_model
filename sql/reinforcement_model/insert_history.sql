INSERT

INTO
  {database}.history

VALUES (
  {game_id},
  '{phase}',
  {nr},
  {step},
  '{uuid}',
  {position},
  {stack},
  '{stack_range}',
  {pot},
  '{pot_range}',
  '{flop1}',
  '{flop2}',
  '{flop3}',
  '{turn}',
  '{river}',
  '{action}',
  {amount},
  {new_stack},
  '{new_stack_range}',
  {new_pot},
  '{new_pot_range}',
  '{amount_potrate}'
)