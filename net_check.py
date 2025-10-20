'''net_check.py imports the functions from net_gargoyle.py to print the gargoyle.db contents'''
import net_gargoyle as netg

global TXID
TXID = uuid.uuid4()

netg.interact()
netg.printdb(TXID)
