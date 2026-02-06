--Fix string imports to datetime, ignore order for now
CREATE OR REPLACE TABLE myproject-476114.mydataset.crime_data AS
SELECT
  PARSE_DATETIME('%m/%d/%Y %H:%M', REPLACE(occ_date_time, '  ', ' ')) AS occ_date_time,
  PARSE_DATETIME('%m/%d/%Y %H:%M', REPLACE(rep_date_time, '  ', ' ')) AS rep_date_time,
  * EXCEPT(occ_date_time, rep_date_time)
FROM myproject-476114.mydataset.crime_data;