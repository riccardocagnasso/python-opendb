python-opendb
=============

Python interface to http://opendb.netfluid.org

Usage
=============

```python
import opendb
odb = opendb.OpenDB()

#list collections
odb.collections()

#list items in "foo" collection
odb.items("foo")

#get item "bar" in "foo" collection
odb.item("foo", "bar")

#create item "bar" in "foo" collection with attribute "baz" = 2
odb.add("foo", "bar", {"baz": 2})

#update item "bar" in "foo" collection setting attribute "baz" = 2
odb.update("foo", "bar", {"baz": 2})

#delete item "bar" in "foo" collection
odb.delete("foo", "bar")
```
