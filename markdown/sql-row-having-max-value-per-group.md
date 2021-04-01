---
created: 2021-03-10
tag: sql
title: Rows having the max value per group
---
Apparently the "rows with max value per group" SQL question is so common that it turns
up as an interview question, and it has an entire StackOverflow tag dedicated to it:
<https://stackoverflow.com/questions/tagged/greatest-n-per-group>

This Stack Overflow answer is quite nice in its breadth of options:
<https://stackoverflow.com/questions/7745609/sql-select-only-rows-with-max-value-on-a-column#7745635>

All my solutions to this tended to have self joins etc, but I’d forgotten about the
`row_number()` window function that, when coupled with `order by`, makes it very easy:

```sql
SELECT class, name, score
FROM (
  SELECT name, class, score,
    ROW_NUMBER() OVER (PARTITION BY class ORDER BY score DESC) rank
  FROM grades
) best_scores WHERE rank=1;
```

Note that this query isn't possible in Django's ORM. You can get pretty close:

```python
from myapp import Grade
from django.db.models import F, Window,
from django.db.models.functions import RowNumber

Grade.objects.annotate(
    rank=Window(
        expression=RowNumber(), partition_by=F("group"), order_by=F("score").desc()
    )
)
```

This will add the row number to the `Grade` objects. However, if you add
`.filter(rank=1)` on the end you'll get something like:

```
NotSupportedError: Window is disallowed in the filter clause.
```

Unfortunately this isn't currently possible in the ORM; see
[this bug in the Django bug tracker](https://code.djangoproject.com/ticket/28333#comment:description)
for more.
