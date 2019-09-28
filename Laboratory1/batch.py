

from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import BatchStatement, BatchType,SimpleStatement



cluster = Cluster()
session = cluster.connect('dbislabwork')
update_user = session.prepare('''update dbislabwork.user set NicName = 'dlfkgjkl' where email = 'emaildima.com';''')
update_repository = session.prepare('''update dbislabwork.reposytoty set Name = 'nkjsdfnk' where Id = 1;''')
batch = BatchStatement(consistency_level=ConsistencyLevel.ONE)

batch.add(update_user)
batch.add(update_repository)
    
session.execute(batch)


# In[ ]:




