-- Create a composite index on the first letter of a name and the score

CREATE INDEX idx_name_first_score ON names (name(1), score);