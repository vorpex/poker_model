SELECT
  SUM(t.stack - t.prev_new_stack) AS checksum_result

FROM (

  SELECT
    h.game_id,
    h.uuid,
    h.step,
    h.stack,
    h.new_stack,
    lag(h.game_id) over (ORDER BY h.game_id, h.uuid, h.step) AS prev_game_id,
    lag(h.uuid) over (ORDER BY h.game_id, h.uuid, h.step) AS prev_uuid,
    lag(h.new_stack) over (ORDER BY h.game_id, h.uuid, h.step) AS prev_new_stack

  FROM
    {database}.history h

  ORDER BY
    h.game_id,
    h.uuid,
    h.step

) t

WHERE
  t.game_id = t.prev_game_id
  AND t.uuid = t.prev_uuid