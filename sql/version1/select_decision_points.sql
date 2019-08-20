SELECT
  NVL(MAX(d.id), -1) AS id

FROM
  poker.decision_points d

WHERE
  1 = 1
  AND d.hand = '{HAND}'
  AND d.stack = {STACK}
  AND d.pot = {POT}
  AND d.position = {POSITION}
  AND d.phase = {PHASE}
  AND d.nr = {NR}
  AND d.history in (

  SELECT
    *

  FROM (
  
    SELECT CONCAT('"phase":', json_array(GROUP_CONCAT(h.phase))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"nr":', json_array(GROUP_CONCAT(h.nr))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"position":', json_array(GROUP_CONCAT(h.position))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"stack":', json_array(GROUP_CONCAT(h.stack))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"pot":', json_array(GROUP_CONCAT(h.pot))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"flop1":', json_array(GROUP_CONCAT(CONCAT('"', h.flop1, '"')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"flop2":', json_array(GROUP_CONCAT(CONCAT('"', h.flop2, '"')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"flop3":', json_array(GROUP_CONCAT(CONCAT('"', h.flop3, '"')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"turn":', json_array(GROUP_CONCAT(CONCAT('"', h.turn, '"')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"river":', json_array(GROUP_CONCAT(CONCAT('"', h.river, '"')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"move":', json_array(GROUP_CONCAT(CONCAT('"', h.move, '"')))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
    UNION
    SELECT CONCAT('"amount":', json_array(GROUP_CONCAT(h.amount))) AS jobj FROM poker.history h WHERE 1 = 1 AND h.game_id = {GAME_ID} AND h.nr < {NR}
  
  ) s

)
