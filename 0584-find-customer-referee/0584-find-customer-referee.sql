select name
from customer
WHERE COALESCE(referee_id, 0) <> 2