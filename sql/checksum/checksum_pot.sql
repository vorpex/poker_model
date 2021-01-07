SELECT
  SUM(h.new_pot - (h.pot + h.amount)) as checksum_result

FROM
  {database}.history h