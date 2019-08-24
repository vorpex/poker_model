UPDATE
  poker_version2.games g

SET
  g.flop1 = '{flop1}',
  g.flop2 = '{flop2}',
  g.flop3 = '{flop3}',
  g.turn = '{turn}',
  g.river = '{river}'

WHERE
  1 = 1
  AND g.id = {index}