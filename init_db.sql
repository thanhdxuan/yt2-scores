CREATE TABLE scores(Name TEXT, ID TEXT, Van REAL, Anh REAL, Toan REAL, Tong REAL, Rank INTEGER);
INSERT INTO
    scores
SELECT
    json_extract (value, '$.Name'),
    json_extract (value, '$.ID'),
    json_extract (value, '$.Van'),
    json_extract (value, '$.Anh'),
    json_extract (value, '$.Toan'),
    json_extract (value, '$.Tong'),
    json_extract (value, '$.Rank')
FROM json_each(
        readfile ('yt2-sorted-2.json')
    );