SELECT
  s.*

FROM (

  SELECT CONCAT('"phase":', json_array(GROUP_CONCAT(h.phase))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"nr":', json_array(GROUP_CONCAT(h.nr))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"position":', json_array(GROUP_CONCAT(h.position))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"stack_range":', json_array(GROUP_CONCAT('"', h.stack_range, '"'))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"pot_range":', json_array(GROUP_CONCAT('"', h.pot_range, '"'))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"flop1":', json_array(GROUP_CONCAT(CONCAT('"', h.flop1, '"')))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"flop2":', json_array(GROUP_CONCAT(CONCAT('"', h.flop2, '"')))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"flop3":', json_array(GROUP_CONCAT(CONCAT('"', h.flop3, '"')))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"turn":', json_array(GROUP_CONCAT(CONCAT('"', h.turn, '"')))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"river":', json_array(GROUP_CONCAT(CONCAT('"', h.river, '"')))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"move":', json_array(GROUP_CONCAT(CONCAT('"', h.action, '"')))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}
  UNION
  SELECT CONCAT('"amount_potrate":', json_array(GROUP_CONCAT('"', h.amount_potrate, '"'))) AS jobj FROM {database}.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.step < {step}

) s
