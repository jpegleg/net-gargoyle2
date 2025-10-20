'''net_set.py imports functions from net_gargoyle.py to create a new gargoyle.db and nethash table then insert current state.'''
import uuid
import net_gargoyle as netg
global TXID
TXID = uuid.uuid4()

netg.createtable(TXID)
netg.interact(TXID)
netg.insertstat(TXID)
