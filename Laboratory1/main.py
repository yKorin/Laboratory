#!/usr/bin/env python
# coding: utf-8

# In[9]:


#!/usr/bin/env python
# coding: utf-8

from cassandra.cluster import Cluster
from cassandra.query import BatchStatement, BatchType,SimpleStatement
from cassandra import ConsistencyLevel

cluster = Cluster()
session = cluster.connect('dbislabwork')


session.execute("create index if not exists on dbislabwork.reposytoty(email);")
session.execute("create index if not exists on dbislabwork.project(repositoryId);")
session.execute("create index if not exists on dbislabwork.file(projectId);")

repository = SimpleStatement(
    "select * from dbislabwork.reposytoty where email = 'emailjoseph.com';",
    consistency_level=ConsistencyLevel.ONE)
session.execute(repository)

project = SimpleStatement(
    "select * from dbislabwork.project where repositoryId = 1;",
    consistency_level=ConsistencyLevel.ONE)
session.execute(project)


file = SimpleStatement(
    "select * from dbislabwork.file where projectId = 1;",
    consistency_level=ConsistencyLevel.ONE)
session.execute(file)

name = SimpleStatement(
    "select CountOfFiles,Name from dbislabwork.project where repositoryId = 1;",
    consistency_level=ConsistencyLevel.ONE)
session.execute(name)






# In[ ]:




