SELECT
  SUM(h.new_stack - (h.stack - h.amount)) as checksum_result

FROM
  {database}.history h