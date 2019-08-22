SELECT
  NVL(MAX(d.id), -1) AS id

FROM
  poker_version2.decision_points d

WHERE
  1 = 1
  AND d.phase = '{phase}'
  AND d.nr = {nr}
  AND d.position = {position}
  AND d.hand_db_format = '{hand_db_format}'
  AND d.stack = {stack}
  AND d.pot = {pot}
  AND d.history in (

  SELECT
    s.*

  FROM (
  
    SELECT CONCAT('"phase":', json_array(GROUP_CONCAT(h.phase))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"nr":', json_array(GROUP_CONCAT(h.nr))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"position":', json_array(GROUP_CONCAT(h.position))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"stack":', json_array(GROUP_CONCAT(h.stack))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"pot":', json_array(GROUP_CONCAT(h.pot))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"flop1":', json_array(GROUP_CONCAT(CONCAT('"', h.flop1, '"')))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"flop2":', json_array(GROUP_CONCAT(CONCAT('"', h.flop2, '"')))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"flop3":', json_array(GROUP_CONCAT(CONCAT('"', h.flop3, '"')))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"turn":', json_array(GROUP_CONCAT(CONCAT('"', h.turn, '"')))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"river":', json_array(GROUP_CONCAT(CONCAT('"', h.river, '"')))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"move":', json_array(GROUP_CONCAT(CONCAT('"', h.action, '"')))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
    UNION
    SELECT CONCAT('"amount":', json_array(GROUP_CONCAT(h.amount))) AS jobj FROM poker_version2.history h WHERE 1 = 1 AND h.game_id = {game_id} AND h.nr < {nr}
  
  ) s

)
